import re, json, sys
SRC = sys.argv[1]
OUT = sys.argv[2]
t = open(SRC).read()

# nama surah yang dipakai dalam rujukan ayat di badan teks
SURAH = ["Ali 'Imran", 'Fathir', 'Fushshilat', 'Gafir', 'Hud', 'Ibrahim', 'Luqman', 'Maryam', 'Muhammad', 'Muḥammad', 'Qaf', "Saba'", 'Shad', 'Taha', 'Yasin', 'Yunus', 'Yusuf', 'adz-Dzariyat', "al-'Alaq", "al-'Ankabut", "al-A'la", "al-A'raf", 'al-Ahzab', "al-An'am", "al-Anbiya'", 'al-Baqarah', 'al-Fajr', 'al-Fath', 'al-Furqan', 'al-Hadid', 'al-Hajj', 'al-Haqqah', 'al-Hasyr', 'al-Hijr', 'al-Ikhlas', 'al-Insan', "al-Isra'", 'al-Jasiyah', 'al-Kahf', 'al-Lail', "al-Ma'arij", "al-Ma'idah", "al-Mu'minun", 'al-Mujadalah', 'al-Mulk', 'al-Muthaffifin', 'al-Qalam', 'al-Qamar', 'al-Qashash', 'al-Qiyamah', "al-Waqi'ah", 'an-Nahl', 'an-Najm', 'an-Naml', "an-Nazi'at", "an-Nisa'", 'an-Nur', "ar-Ra'd", 'ar-Rahman', 'ar-Rum', 'as-Sajdah', 'ash-Shaffat', "asy-Syu'ara'", 'asy-Syura', 'at-Tahrim', 'at-Takwir', 'at-Taubah', 'ath-Thur', 'az-Zariyat', 'az-Zukhruf', 'az-Zumar', 'aṣ-Ṣaff', 'Āl ʿImrān']
_SN = '|'.join(re.escape(s) for s in sorted(SURAH, key=len, reverse=True))
SREF = re.compile(r"\((?:%s): [\d, \-]+(?:; (?:%s): [\d, \-]+)*\)" % (_SN, _SN))
AR = re.compile(r'[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+(?:[ ،]+[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]+)*')

SMALL = set('yang dan dari bahwa di ke pada dalam dengan atau untuk tentang oleh bagi atas serta sebagai'.split())
def title_case(s):
    out = []
    for i, w in enumerate(s.lower().split(' ')):
        parts = w.split('-')
        if i > 0 and w in SMALL:
            out.append(w)
        else:
            out.append('-'.join(p[:1].upper() + p[1:] for p in parts))
    s = ' '.join(out)
    return s.replace("Ta'ala", "Ta'ala")

def split_arabic(text, st):
    runs = []
    pos = 0
    for m in AR.finditer(text):
        if m.start() > pos: runs.append({'t': text[pos:m.start()], 's': st})
        runs.append({'t': m.group(), 's': 'AksaraArab'})
        pos = m.end()
    if pos < len(text): runs.append({'t': text[pos:], 's': st})
    return runs

def split_refs(text, st):
    runs = []
    pos = 0
    for m in SREF.finditer(text):
        if m.start() > pos: runs += split_arabic(text[pos:m.start()], st)
        runs.append({'t': m.group(), 's': 'RujukanAyat'})
        pos = m.end()
    if pos < len(text): runs += split_arabic(text[pos:], st)
    return runs

TOK = re.compile(r'\[\^(\d+)\]|\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*')
def inline(s, label_ok=False):
    runs = []
    pos = 0
    first = True
    for m in TOK.finditer(s):
        if m.start() > pos:
            runs += split_refs(s[pos:m.start()], None)
        if m.group(1):
            runs.append({'fn': int(m.group(1))})
        elif m.group(2):
            runs += split_arabic(m.group(2), 'Tebal')
        elif m.group(3):
            st = 'LabelArgumen' if (label_ok and m.start() == 0) else 'Tebal'
            runs += split_arabic(m.group(3), st)
        else:
            it = m.group(4)
            if it.startswith('"') or it.startswith('“') or it.startswith("'"):
                after = s[m.end():m.end() + 80]
                st = 'KutipanAyat' if SREF.match(after.lstrip(' ')) else 'KutipanRiwayat'
            else:
                st = 'Transliterasi'
            runs += split_refs(it, st)
        pos = m.end()
    if pos < len(s):
        runs += split_refs(s[pos:], None)
    # gabungkan run bersebelahan yang gayanya sama
    out = []
    for r in runs:
        if out and 't' in r and 't' in out[-1] and out[-1]['s'] == r['s']:
            out[-1]['t'] += r['t']
        else:
            out.append(r)
    return out

lines = t.split('\n')
bstart = lines.index('# TERJEMAHAN')

# ---------- catatan kaki
foot = {}
for l in lines:
    m = re.match(r'^\[\^(\d+)\]: (.*)$', l)
    if m: foot[int(m.group(1))] = inline(m.group(2))

# ---------- badan teks
blocks = []
after_head = True
i = bstart + 1
pending_bagian = False
while i < len(lines):
    l = lines[i]; i += 1
    if not l.strip() or l.startswith('[^') or l.startswith('---'):
        continue
    if l.startswith('## '):
        txt = l[3:].strip()
        if re.match(r'^BAGIAN ', txt):
            blocks.append({'p': 'BagianKe', 'r': [{'t': title_case(txt), 's': None}]})
            pending_bagian = True
        elif pending_bagian:
            blocks.append({'p': 'JudulBagian', 'r': inline(title_case(txt))})
            pending_bagian = False
        else:
            blocks.append({'p': 'JudulBagian', 'r': inline(title_case(txt)), 'pb': True})
        after_head = True
        continue
    if l.startswith('### '):
        txt = l[4:].strip()
        m = re.match(r'^(Pasal [^:]+|Mukadimah): (.*)$', txt)
        if m:
            blocks.append({'p': 'Pasal', 'r': inline(m.group(1))})
            blocks.append({'p': 'JudulPasal', 'r': inline(m.group(2))})
        else:
            blocks.append({'p': 'Pasal', 'r': inline(txt)})
        after_head = True
        continue
    if l.startswith('#### '):
        blocks.append({'p': 'Subpasal', 'r': inline(l[5:].strip())})
        after_head = True
        continue
    if l.startswith('*(') and l.endswith(')*'):
        blocks.append({'p': 'PenandaSumber', 'r': inline(l[1:-1])})
        after_head = True
        continue
    if l.startswith('> '):
        s = l[2:].strip()
        if s.startswith('*') and s.endswith('*'): s = s[1:-1]
        blocks.append({'p': 'Syair', 'r': inline(s)})
        after_head = True
        continue
    if l.strip() == '*Tamat.*':
        blocks.append({'p': 'Penutup', 'r': [{'t': 'Tamat', 's': None}]})
        continue
    blocks.append({'p': 'TeksIsiPertama' if after_head else 'TeksIsi', 'r': inline(l, label_ok=True)})
    after_head = False

# ---------- glosarium (lampiran)
gs = t.index('## 2. Glosarium'); ge = t.index('## 3. Riwayat')
gl = t[gs:ge].split('\n')
gloss = []
for l in gl[1:]:
    if not l.strip() or l.startswith('---'): continue
    if l.startswith('### '):
        h = re.sub(r'^\d+\.\d+ ', '', l[4:].strip())
        h = h.replace(' (Bagian II sampai IV)', '')
        gloss.append({'k': 'sub', 'r': inline(h)}); continue
    if l.startswith('|'):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if all(re.fullmatch(r'-+', c) for c in cells): continue
        if gloss and gloss[-1]['k'] == 'table':
            gloss[-1]['rows'].append([inline(c) for c in cells])
        else:
            gloss.append({'k': 'table', 'head': cells, 'rows': []})
        continue
    gloss.append({'k': 'para', 'r': inline(l)})

json.dump({'blocks': blocks, 'foot': foot, 'gloss': gloss}, open(OUT, 'w'), ensure_ascii=False)
from collections import Counter
print(Counter(b['p'] for b in blocks), len(foot), len(gloss))
refs = sum(1 for b in blocks for r in b['r'] if r.get('s') == 'RujukanAyat')
print('rujukan ayat', refs, 'kutipan ayat', sum(1 for b in blocks for r in b['r'] if r.get('s') == 'KutipanAyat'))
