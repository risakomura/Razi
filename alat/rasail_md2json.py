"""Mengubah terjemahan-rasail-ragib.md menjadi JSON untuk rasail_build_docx.js.

Yang dimasukkan: keputusan kerja (sebagai Keterangan Penerjemah), seluruh
terjemahan (dari `# TERJEMAHAN`), dan glosarium (bagian 3) sebagai lampiran.
Catatan kaki Markdown berkunci (`[^s1]`, `[^m-khalt]`, dst.) dinomori ulang
menurut urutan rujukan pertamanya, dan rujukan silang antarcatatan
("lihat catatan d3") serta kolom kunci glosarium diganti dengan nomor itu.
"""
import re, json, sys

SRC, OUT = sys.argv[1], sys.argv[2]
t = open(SRC).read()
bstart = t.index('# TERJEMAHAN')
body = t[bstart:]

AR = re.compile(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+(?:[ ،/]+[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+)*')
SREF = re.compile(r" \((?:[A-Za-z][A-Za-z'\-]*|Ali 'Imran): [\d][\d, \-]*(?:; (?:[A-Za-z][A-Za-z'\-]*|Ali 'Imran): [\d][\d, \-]*)*\)")

# ---------- nomor catatan kaki menurut urutan rujukan pertama
defs = {}
for m in re.finditer(r'^\[\^([^\]]+)\]: (.*)$', body, re.M):
    defs[m.group(1)] = m.group(2)
num = {}
for m in re.finditer(r'\[\^([^\]]+)\](?!:)', body):
    num.setdefault(m.group(1), len(num) + 1)
assert set(num) == set(defs), (set(num) ^ set(defs))

KEY = r'(?:[spdt]\d+|[mkr]-[a-z0-9]+)'
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

TOK = re.compile(r'\[\^([^\]]+)\]|\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*|`([^`]+)`')
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
            for i, part in enumerate(re.split(r'\*', g)):
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

HEAD = re.compile(r'^(#{1,3}) (.+?) \{\.(kitab-ke|judul-kitab|judul-bab|judul-pasal)\}$')
STY = {'kitab-ke': 'KitabKe', 'judul-kitab': 'JudulKitab', 'judul-bab': 'JudulBab', 'judul-pasal': 'JudulPasal'}

# ---------- badan teks
blocks = []
after_head = True
lines = body.split('\n')[1:]
for i, l in enumerate(lines):
    if not l.strip() or l.startswith('[^') or l.strip() == '---':
        continue
    m = HEAD.match(l)
    if m:
        blocks.append({'p': STY[m.group(3)], 'r': inline(m.group(2))})
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
    assert not l.startswith('#'), l
    blocks.append({'p': 'TeksIsiPertama' if after_head else 'TeksIsi', 'r': inline(l, label_ok=True)})
    after_head = False

foot = {str(num[k]): inline(v) for k, v in defs.items()}

# ---------- keterangan penerjemah (bagian 2 MD)
ks = t.index('## 2. Keputusan Kerja'); ke = t.index('## 3. Glosarium')
front = []
for l in t[ks:ke].split('\n')[1:]:
    if not l.strip() or l.strip() == '---': continue
    front.append(inline(l))

# ---------- glosarium (bagian 3 MD)
ge = t.index('\n---', ke)
gloss = []
sub = None
for l in t[ke:ge].split('\n')[1:]:
    if not l.strip(): continue
    if l.startswith('### '):
        sub = l[4:5] + l[5:8]
        gloss.append({'k': 'sub', 'r': inline(l[4:].strip())}); continue
    if l.startswith('|'):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if all(re.fullmatch(r'-+', c) for c in cells): continue
        own = sub and sub.startswith(('3.2', '3.3'))
        if gloss and gloss[-1]['k'] == 'table':
            row = []
            for j, c in enumerate(cells):
                h = gloss[-1]['head'][j]
                if own and h in ('Catatan', 'Kunci'):
                    ks_ = re.findall(r'`([^`]+)`', c)
                    if ks_ and all(k in num for k in ks_):
                        c = ', '.join(str(num[k]) for k in ks_)
                row.append(inline(c, ar='AksaraArabTabel'))
            gloss[-1]['rows'].append(row)
        else:
            head = ['No. catatan' if (own and c == 'Kunci') else c for c in cells]
            gloss.append({'k': 'table', 'head': head, 'rows': []})
        continue
    if re.match(r'^\*\*[^*].*\*\* \(', l) or re.match(r'^\*\*[^*]+\*[^*]+\*[^*]*\*\*$', l):
        gloss.append({'k': 'group', 'r': inline(l)}); continue
    # sebutan kunci Markdown (`m-…`) tidak bermakna dalam DOCX
    l = re.sub(r' \(`[mkr]-…`\)', '', l)
    gloss.append({'k': 'para', 'r': inline(l)})

json.dump({'front': front, 'blocks': blocks, 'foot': foot, 'gloss': gloss}, open(OUT, 'w'), ensure_ascii=False)
from collections import Counter
print(Counter(b['p'] for b in blocks), 'catatan', len(foot), 'glosarium', Counter(g['k'] for g in gloss))
print('kutipan ayat', sum(1 for b in blocks for r in b['r'] if r.get('s') == 'KutipanAyat'),
      'rujukan ayat', sum(1 for b in blocks for r in b['r'] if r.get('s') == 'RujukanAyat'))
