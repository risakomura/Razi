"""Mengubah terjemahan karya al-Rāghib (MD) menjadi JSON untuk ragib_build_docx.js.

    python3 alat/ragib_md2json.py dhariah|tafsil|rasail|miftah OUT.json

Yang dimasukkan: halaman judul, keputusan kerja (sebagai Keterangan
Penerjemah), seluruh terjemahan (dari `# TERJEMAHAN`), dan glosarium
(bagian 3) sebagai lampiran. Catatan kaki Markdown berkunci (`[^s1]`,
`[^m-khalt]`, dst.) dinomori ulang menurut urutan rujukan pertamanya; urutan
ini sama dengan nomor "nota kaki no. N" dan "catatan no. N" yang dipakai
untuk merujuk antarkitab. Rujukan silang antarcatatan ("lihat catatan d3")
dan kolom kunci glosarium diganti dengan nomor itu.
"""
import re, json, sys, os

BOOKS = {
    'dhariah': {
        'src': 'terjemahan-adh-dhariah.md',
        'title': 'al-Dharīʿa ilā Makārim al-Sharīʿa',
        'subtitle': [],
        'desc': 'Diterjemahkan dari terjemahan Turki Erdemli Yol (terj. Muharrem Tan), dengan pencocokan pada teks Arab edisi Abū al-Yazīd al-ʿAjamī',
        'doc_title': 'al-Dharīʿa ilā Makārim al-Sharīʿa: Terjemahan Indonesia',
    },
    'tafsil': {
        'src': 'terjemahan-tafsil-nashatayn.md',
        'title': 'Kejadian dan Kebahagiaan',
        'subtitle': ['Tafṣīl al-Nashʾatayn wa Taḥṣīl al-Saʿādatayn', 'Edisi Kedua'],
        'desc': 'Diterjemahkan dari teks Arab edisi Dār Maktabat al-Ḥayāh (Beirut, 1983), dengan perbandingan terjemahan Turki Lütfi Doğan',
        'doc_title': 'Tafṣīl al-Nashʾatayn wa Taḥṣīl al-Saʿādatayn: Terjemahan Indonesia',
    },
    'miftah': {
        'src': 'terjemahan-miftah-al-ghayb.md',
        'title': 'Kunci Gaib Penghimpunan dan Wujud',
        'subtitle': ['Miftāḥ Ghayb al-Jamʿ wa-l-Wujūd', 'Metafisika Keesaan Wujud dan Manusia Sempurna'],
        'author': 'Ṣadr al-Dīn al-Qūnawī',
        'author_dates': '(w. 673/1274)',
        'desc': 'Diterjemahkan dari terjemahan Turki Ekrem Demirli, dengan pencocokan pada teks Arab edisi ʿĀṣim al-Kayyālī dan terjemahan Inggris Özgür Koca, disertai kutipan syarah Miṣbāḥ al-Uns karya Shams al-Dīn al-Fanārī',
        'doc_title': 'Miftāḥ Ghayb al-Jamʿ wa-l-Wujūd: Terjemahan Indonesia',
    },
    'rasail': {
        'src': 'terjemahan-rasail-ragib.md',
        'title': 'Risalah-Risalah al-Rāghib al-Iṣfahānī',
        'subtitle': ['Adab Bergaul dengan Manusia', 'Keutamaan Manusia dengan Ilmu-Ilmu',
                     'Tingkatan Ilmu-Ilmu dan Amal-Amal', 'Uraian tentang Lafal al-Wāḥid dan al-Aḥad'],
        'desc': 'Diterjemahkan dari teks Arab edisi tahkik ʿUmar ʿAbd al-Raḥmān al-Sārīsī, dengan perbandingan terjemahan Turki',
        'doc_title': 'Risalah-Risalah al-Rāghib al-Iṣfahānī: Terjemahan Indonesia',
    },
}

BOOK, OUT = sys.argv[1], sys.argv[2]
cfg = BOOKS[BOOK]
t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', cfg['src'])).read()
bstart = t.index('\n# TERJEMAHAN\n') + 1
body = t[bstart:]

AR = re.compile(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+(?:[ ،/]+[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+)*')
SNAME = r"(?:Ali 'Imran|'?[A-Za-z][A-Za-z'\-]*)"
SREF = re.compile(r" \(%s: [\d][\d, \-]*(?:; %s: [\d][\d, \-]*)*\)" % (SNAME, SNAME))

# ---------- nomor catatan kaki menurut urutan rujukan pertama
defs = {}
for m in re.finditer(r'^\[\^([^\]]+)\]: (.*)$', body, re.M):
    assert m.group(1) not in defs, m.group(1)
    defs[m.group(1)] = m.group(2)
num = {}
for m in re.finditer(r'\[\^([^\]]+)\](?!:)', body):
    num.setdefault(m.group(1), len(num) + 1)
assert set(num) == set(defs), (set(num) ^ set(defs))

KEY = r'(?:[a-z]\d+|[mkr]-[a-z0-9]+)'
def xref(s):
    """'catatan d3', 'catatan p36 dan k-murid' -> 'catatan no. N'."""
    def rep(m):
        ks = re.split(r' dan |, ', m.group(1))
        if not all(k in num for k in ks):
            return m.group(0)
        ns = [str(num[k]) for k in ks]
        return 'catatan no. ' + (' dan '.join(ns) if len(ns) == 2 else ', '.join(ns))
    return re.sub(r'\bcatatan (%s(?:(?: dan |, )%s)*)\b' % (KEY, KEY), rep, s)

def split_arabic(text, st, ar='AksaraArab'):
    runs, pos = [], 0
    for m in AR.finditer(text):
        if m.start() > pos: runs.append({'t': text[pos:m.start()], 's': st})
        runs.append({'t': m.group(), 's': ar})
        pos = m.end()
    if pos < len(text): runs.append({'t': text[pos:], 's': st})
    return runs

TOK = re.compile(r'\[\^([^\]]+)\]|\*\*\*(.+?)\*\*\*|\*\*((?:[^*]|\*[^*]+\*)+)\*\*|\*(.+?)\*|`([^`]+)`')
def inline(s, label_ok=False, ar='AksaraArab'):
    s = xref(s)
    runs, pos = [], 0
    for m in TOK.finditer(s):
        if m.start() > pos:
            runs += split_arabic(s[pos:m.start()], None, ar)
        if m.group(1):
            runs.append({'fn': num[m.group(1)]})
            pos = m.end(); continue
        if m.group(2):
            runs += split_arabic(m.group(2), 'TebalMiring', ar)
        elif m.group(3):
            g = m.group(3)
            st = 'LabelArgumen' if (label_ok and m.start() == 0 and s[m.end():m.end() + 1] == ':') else 'Tebal'
            # teks miring di dalam teks tebal
            for i, part in enumerate(g.split('*')):
                if part: runs += split_arabic(part, ('TebalMiring' if i % 2 else st), ar)
        elif m.group(4):
            it = m.group(4)
            if it[:1] in '"“\'':
                ref = SREF.match(s, m.end())
                if ref:
                    runs.append({'t': it, 's': 'KutipanAyat'})
                    runs.append({'t': ' ', 's': None})
                    runs.append({'t': ref.group()[1:], 's': 'RujukanAyat'})
                    pos = ref.end(); continue
                runs.append({'t': it, 's': 'KutipanRiwayat'})
            else:
                runs += split_arabic(it, 'Transliterasi', ar)
        else:
            runs.append({'t': m.group(5), 's': None})
        pos = m.end()
    if pos < len(s):
        runs += split_arabic(s[pos:], None, ar)
    out = []
    for r in runs:
        if out and 't' in r and 't' in out[-1] and out[-1]['s'] == r['s']:
            out[-1]['t'] += r['t']
        else:
            out.append(r)
    return out

HEAD = re.compile(r'^(#{1,4}) (.+?) \{\.(kitab-ke|judul-kitab|judul-bab|judul-pasal|subpasal)\}$')
STY = {'kitab-ke': 'KitabKe', 'judul-kitab': 'JudulKitab', 'judul-bab': 'JudulBab',
       'judul-pasal': 'JudulPasal', 'subpasal': 'Subpasal'}

# ---------- badan teks
blocks = []
after_head = True
lines = body.split('\n')[1:]
for i, l in enumerate(lines):
    if not l.strip() or l.startswith('[^') or l.strip() == '---':
        continue
    m = HEAD.match(l)
    if m:
        st = STY[m.group(3)]
        b = {'p': st, 'r': inline(m.group(2))}
        # judul kitab tanpa nomor (Mukadimah) dimulai di halaman baru
        if st == 'JudulKitab' and not (blocks and blocks[-1]['p'] == 'KitabKe'):
            b['pb'] = True
        blocks.append(b)
        after_head = True; continue
    m = re.match(r'^\[(.+)\]\{\.basmalah\}$', l)
    if m:
        blocks.append({'p': 'Basmalah', 'r': inline(m.group(1))})
        after_head = True; continue
    if l.startswith('> '):
        prev = lines[i - 1] if i else ''
        nxt = lines[i + 1] if i + 1 < len(lines) else ''
        blocks.append({'p': 'Syair', 'r': inline(l[2:].strip()),
                       'first': not prev.startswith('> '), 'last': not nxt.startswith('> ')})
        after_head = True; continue
    m = re.match(r'^(\d+\.|- \([a-z]\)) (.*)$', l)
    if m:
        blocks.append({'p': 'Butir', 'r': [{'t': m.group(1).lstrip('- ') + '\t', 's': None}] + inline(m.group(2), label_ok=True)})
        after_head = True; continue
    assert not l.startswith(('#', '|', '[')), l
    blocks.append({'p': 'TeksIsiPertama' if after_head else 'TeksIsi', 'r': inline(l, label_ok=True)})
    after_head = False
blocks[0]['pb'] = True

foot = {str(num[k]): inline(v) for k, v in defs.items()}

# ---------- keterangan penerjemah (bagian 2 MD)
ks = t.index('\n## 2. Keputusan Kerja'); ke = t.index('\n## 3. Glosarium')
def nokey(l):
    # sebutan kunci Markdown (`m-…`, `[^m-…]`) tidak bermakna dalam DOCX
    l = re.sub(r' \((?:`[mkr]-…`(?:\)? dan \(?)?)+\)', '', l)
    return re.sub(r' \(`\[\^[mk]-…\]`\)', '', l)
front = [inline(nokey(l)) for l in t[ks:ke].split('\n')[2:] if l.strip() and l.strip() != '---']

# ---------- glosarium (bagian 3 MD)
ge = t.rindex('\n---', 0, bstart)
gtitle = re.sub(r'^## 3\. ', '', t[ke + 1:t.index('\n', ke + 1)])
gloss = []
for l in t[ke:ge].split('\n')[2:]:
    if not l.strip(): continue
    if l.startswith('### '):
        gloss.append({'k': 'sub', 'r': inline(l[4:].strip())}); continue
    if l.startswith('|'):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?', c) for c in cells): continue
        if gloss and gloss[-1]['k'] == 'table':
            row = []
            for c in cells:
                # sel yang hanya berisi kunci catatan kitab ini diganti nomor catatannya
                if re.fullmatch(r'`[^`]+`(?:, `[^`]+`)*', c):
                    ks_ = re.findall(r'`([^`]+)`', c)
                    if all(k in num for k in ks_):
                        c = ', '.join(str(num[k]) for k in ks_)
                row.append(inline(c, ar='AksaraArabTabel'))
            gloss[-1]['rows'].append(row)
        else:
            gloss.append({'k': 'table', 'head': ['No. catatan' if c == 'Kunci' else c for c in cells], 'rows': []})
        continue
    if re.match(r'^\*\*[^*].*\*\* \([^)]*\)$', l) or re.match(r'^\*\*[^*]+\*[^*]+\*[^*]*\*\*$', l):
        gloss.append({'k': 'group', 'r': inline(l)}); continue
    gloss.append({'k': 'para', 'r': inline(nokey(l))})

meta = {k: cfg[k] for k in ('title', 'subtitle', 'desc', 'doc_title', 'author', 'author_dates') if k in cfg}
meta['gloss_title'] = 'Lampiran: ' + gtitle
json.dump({'meta': meta, 'front': front, 'blocks': blocks, 'foot': foot, 'gloss': gloss},
          open(OUT, 'w'), ensure_ascii=False)
from collections import Counter
print(BOOK, Counter(b['p'] for b in blocks), 'catatan', len(foot), 'glosarium', Counter(g['k'] for g in gloss))
print('kutipan ayat', sum(1 for b in blocks for r in b['r'] if r.get('s') == 'KutipanAyat'),
      'rujukan ayat', sum(1 for b in blocks for r in b['r'] if r.get('s') == 'RujukanAyat'))
