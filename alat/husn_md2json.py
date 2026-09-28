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
  *larik ulang*                 -> LarikUlang (baris ketiga bait, opsional)
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
    if m := re.fullmatch(r'\[(\d+)\] (.+)\\', head):
        n = int(m.group(1))
        if expect is not None and n != expect:
            errors.append(f'nomor bait {n}, seharusnya {expect}')
        expect = n + 1
        if len(lines) not in (2, 3):
            errors.append(f'bait {n}: {len(lines)} baris'); continue
        show = first_in_part or n % 5 == 0
        blocks.append({'p': 'LarikAwal', 'n': n, 'show': show, 'r': runs(m.group(2))})
        blocks.append({'p': 'LarikAkhir', 'r': runs(lines[1])})
        if len(lines) == 3:
            u = re.fullmatch(r'\*(.+)\*', lines[2])
            if not u: errors.append(f'bait {n}: baris ketiga bukan larik ulang')
            else: blocks.append({'p': 'LarikUlang', 'r': [{'t': u.group(1), 's': None}]})
        first_in_part = False
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
print('ok', OUT, sum(1 for b in blocks if b['p'] == 'LarikAwal'), 'bait')
