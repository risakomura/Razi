"""Mengubah terjemahan Hüsn ü Aşk (MD) menjadi JSON untuk husn_build_docx.js.

    python3 alat/husn_md2json.py terjemahan-husn-u-ask.md OUT.json

Yang dimasukkan: halaman judul dan seluruh terjemahan (dari `# TERJEMAHAN`).
Status proyek, konvensi markup, dan keputusan kerja tidak ikut.

Unsur yang dikenali (satu unsur per baris, bait dipisah baris kosong):
  # Teks {.judul-kitab}          -> JudulKitab
  [Teks]{.basmalah}             -> Basmalah
  ## Teks {.judul-bagian}        -> JudulBagian
  [N] larik pertama\\            -> LarikAwal (nomor bait N)
  larik kedua                   -> LarikAkhir
  bait bertingkat: 5 larik, larik ganjil LarikAwal, genap LarikAkhir,
  larik ke-5 `*...*` LarikUlang; nomor [N] boleh jatuh di larik mana pun
  ***                           -> PemisahBait
Nomor bait dicetak pada bait kelipatan lima dan bait pertama tiap bagian.
"""
import re, json, sys

SRC, OUT = sys.argv[1], sys.argv[2]
t = open(SRC, encoding='utf-8').read()
body = t[t.index('\n# TERJEMAHAN\n') + len('\n# TERJEMAHAN\n'):]

TOK = re.compile(r'\*(.+?)\*')
def runs(s):
    out, pos = [], 0
    for m in TOK.finditer(s):
        if m.start() > pos: out.append({'t': s[pos:m.start()], 's': None})
        out.append({'t': m.group(1), 's': 'KutipanLarik'})
        pos = m.end()
    if pos < len(s): out.append({'t': s[pos:], 's': None})
    return out

blocks, errors = [], []
expect = None          # nomor bait yang diharapkan berikutnya
first_in_part = True
chunks = [c.strip('\n') for c in re.split(r'\n\s*\n', body) if c.strip()]
for c in chunks:
    lines = c.split('\n')
    head = lines[0]
    if m := re.fullmatch(r'# (.+?) \{\.judul-kitab\}', head):
        blocks.append({'p': 'JudulKitab', 'r': runs(m.group(1))}); continue
    if m := re.fullmatch(r'\[(.+)\]\{\.basmalah\}', head):
        blocks.append({'p': 'Basmalah', 'r': runs(m.group(1))}); continue
    if m := re.fullmatch(r'## (.+?) \{\.judul-bagian\}', head):
        blocks.append({'p': 'JudulBagian', 'r': runs(m.group(1))}); first_in_part = True; continue
    if head == '***':
        blocks.append({'p': 'PemisahBait', 'r': []}); continue
    if re.match(r'\[\d+\] ', head) or len(lines) == 5:
        # bait (2 larik) atau bait bertingkat (5 larik, larik ke-5 larik ulang);
        # tiap larik kecuali yang terakhir diakhiri '\\'; nomor [N] boleh ada di larik mana pun
        if any(not l.endswith('\\') for l in lines[:-1]) or lines[-1].endswith('\\'):
            errors.append('pemutus larik salah: ' + head[:60]); continue
        lines = [l[:-1] if l.endswith('\\') else l for l in lines]
        if len(lines) not in (2, 3, 5):
            errors.append(f'{len(lines)} larik: ' + head[:60]); continue
        for i, l in enumerate(lines):
            n = None
            if m := re.match(r'\[(\d+)\] (.*)', l):
                n, l = int(m.group(1)), m.group(2)
                if expect is not None and n != expect:
                    errors.append(f'nomor bait {n}, seharusnya {expect}')
                expect = n + 1
            if (u := re.fullmatch(r'\*([^*]+)\*', l)) and i == len(lines) - 1 and len(lines) > 2:
                st, r = 'LarikUlang', [{'t': u.group(1), 's': None}]
            else:
                st, r = ('LarikAwal' if i % 2 == 0 else 'LarikAkhir'), runs(l)
            b = {'p': st, 'r': r}
            if i == 0 and len(lines) == 5: b['stanza'] = True
            if n is not None:
                b['n'] = n; b['show'] = first_in_part or n % 5 == 0
                first_in_part = False
            blocks.append(b)
        continue
    errors.append('unsur tak dikenal: ' + head[:60])

if errors:
    sys.exit('\n'.join(errors))
meta = {
    'title': 'Jelita dan Asmara',
    'subtitle': ['Hüsn ü Aşk'],
    'author': 'Şeyh Galib',
    'author_note': '(1171–1213/1757–1799)',
    'desc': 'Diterjemahkan dari teks Turki Utsmani suntingan Abdülbâki Gölpınarlı, dengan rujukan terjemahan Inggris Victoria Rowe Holbrook',
    'doc_title': 'Hüsn ü Aşk: Terjemahan Indonesia',
}
json.dump({'meta': meta, 'blocks': blocks}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
print('ok', OUT, sum(1 for b in blocks if 'n' in b), 'bait')
