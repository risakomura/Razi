// Membangun DOCX terjemahan karya al-Rāghib dari JSON keluaran ragib_md2json.py.
// Catatan kaki dibuat sebagai catatan kaki Word yang sebenarnya; tabel glosarium tanpa garis.
const fs = require('fs');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, FootnoteReferenceRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle,
  VerticalAlign, PageOrientation, TableLayoutType,
} = D;

const [, , IN, OUT] = process.argv;
const book = JSON.parse(fs.readFileSync(IN, 'utf8'));

const FONT = 'Times New Roman';
const FONT_AR = 'Traditional Arabic';
const pt = (n) => Math.round(n * 2);

// ---------- gaya paragraf (nama sesuai tabel konvensi markup dalam MD)
const P = (id, name, run, paragraph, extra = {}) => ({
  id, name, basedOn: extra.basedOn || 'Normal', next: extra.next || id, quickFormat: true,
  run: Object.assign({ font: FONT }, run), paragraph,
});
const C_ = AlignmentType.CENTER, J = AlignmentType.JUSTIFIED, L = AlignmentType.LEFT;
const paragraphStyles = [
  P('JudulBuku', 'Judul Buku', { size: pt(26), bold: true }, { alignment: C_, spacing: { before: 2400, after: 240 } }),
  P('SubjudulBuku', 'Subjudul Buku', { size: pt(13), italics: true }, { alignment: C_, spacing: { after: 120 } }),
  P('PengarangBuku', 'Pengarang Buku', { size: pt(13), smallCaps: true }, { alignment: C_, spacing: { before: 720, after: 120 } }),
  P('KeteranganBuku', 'Keterangan Buku', { size: pt(10), italics: true }, { alignment: C_, spacing: { after: 120 } }),
  P('JudulPengantar', 'Judul Pengantar', { size: pt(14), bold: true },
    { alignment: C_, spacing: { before: 720, after: 360 }, pageBreakBefore: true, keepNext: true, outlineLevel: 0 }),
  P('TeksPengantar', 'Teks Pengantar', { size: pt(10) }, { alignment: J, spacing: { after: 120, line: 264 } }),
  P('KitabKe', 'Kitab Ke', { size: pt(12), smallCaps: true, characterSpacing: 40 },
    { alignment: C_, spacing: { before: 1800, after: 160 }, keepNext: true, pageBreakBefore: true, outlineLevel: 0 }),
  P('JudulKitab', 'Judul Kitab', { size: pt(16), bold: true },
    { alignment: C_, spacing: { after: 360 }, keepNext: true, outlineLevel: 0 }),
  P('Basmalah', 'Basmalah', { size: pt(11), italics: true }, { alignment: C_, spacing: { before: 120, after: 240 }, keepNext: true }, { next: 'TeksIsiPertama' }),
  P('JudulBab', 'Judul Bab', { size: pt(12), bold: true },
    { alignment: C_, spacing: { before: 480, after: 240 }, keepNext: true, outlineLevel: 1 }),
  P('JudulPasal', 'Judul Pasal', { size: pt(11), bold: true, italics: true },
    { alignment: L, spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 2 }),
  P('Subpasal', 'Subpasal', { size: pt(10.5), italics: true },
    { alignment: L, spacing: { before: 200, after: 80 }, keepNext: true, outlineLevel: 3 }),
  P('Butir', 'Butir', { size: pt(11) },
    { alignment: J, spacing: { before: 60, after: 60, line: 276 }, indent: { left: 400, hanging: 400 }, tabStops: [{ type: 'left', position: 400 }] }),
  P('TeksIsi', 'Teks Isi', { size: pt(11) },
    { alignment: J, spacing: { after: 0, line: 276 }, indent: { firstLine: 340 } }),
  P('TeksIsiPertama', 'Teks Isi Pertama', { size: pt(11) },
    { alignment: J, spacing: { after: 0, line: 276 }, indent: { firstLine: 0 } }, { basedOn: 'TeksIsi', next: 'TeksIsi' }),
  P('Syair', 'Syair', { size: pt(10.5) },
    { alignment: C_, spacing: { before: 0, after: 0, line: 264 }, indent: { left: 567, right: 567 } }, { next: 'TeksIsiPertama' }),
  P('CatatanKaki', 'Catatan Kaki', { size: pt(8.5) }, { alignment: J, spacing: { after: 40, line: 240 } }),
  P('LampiranJudul', 'Lampiran Judul', { size: pt(16), bold: true },
    { alignment: C_, spacing: { before: 480, after: 360 }, keepNext: true, outlineLevel: 0 }),
  P('LampiranSubjudul', 'Lampiran Subjudul', { size: pt(11), bold: true },
    { alignment: L, spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 1 }),
  P('LampiranKelompok', 'Lampiran Kelompok', { size: pt(9.5) }, { alignment: L, spacing: { before: 200, after: 80 }, keepNext: true }),
  P('TeksLampiran', 'Teks Lampiran', { size: pt(10) }, { alignment: J, spacing: { after: 120, line: 264 } }),
  P('SelTabel', 'Sel Tabel', { size: pt(8) }, { alignment: L, spacing: { after: 0, line: 220 } }),
  P('SelTabelKepala', 'Sel Tabel Kepala', { size: pt(8), bold: true }, { alignment: L, spacing: { after: 0, line: 240 } }, { basedOn: 'SelTabel' }),
];

// ---------- gaya karakter
const C = (id, name, run) => ({ id, name, basedOn: 'DefaultParagraphFont', quickFormat: true, run });
const arFont = { ascii: FONT_AR, hAnsi: FONT_AR, cs: FONT_AR, eastAsia: FONT_AR };
const characterStyles = [
  C('KutipanAyat', 'Kutipan Ayat', { italics: true }),
  C('RujukanAyat', 'Rujukan Ayat', { italics: false }),
  C('KutipanRiwayat', 'Kutipan Riwayat', { italics: true }),
  C('Transliterasi', 'Transliterasi', { italics: true }),
  C('LabelArgumen', 'Label Argumen', { bold: true }),
  C('Tebal', 'Tebal', { bold: true }),
  C('TebalMiring', 'Tebal Miring', { bold: true, italics: true }),
  C('AksaraArab', 'Aksara Arab', { font: arFont, rightToLeft: true, sizeComplexScript: pt(13), language: { bidirectional: 'ar-SA' } }),
  C('AksaraArabTabel', 'Aksara Arab Tabel', { font: arFont, rightToLeft: true, sizeComplexScript: pt(11), language: { bidirectional: 'ar-SA' } }),
];

function runs(rs) {
  const out = [];
  rs.forEach((r, i) => {
    if (r.fn !== undefined) {
      // dua rujukan catatan yang berdampingan dipisah koma superskrip
      if (i > 0 && rs[i - 1].fn !== undefined) out.push(new TextRun({ text: ',', superScript: true }));
      out.push(new FootnoteReferenceRun(r.fn)); return;
    }
    const o = { text: r.t };
    if (r.s) o.style = r.s;
    if (r.s === 'AksaraArab' || r.s === 'AksaraArabTabel') o.rightToLeft = true;
    out.push(new TextRun(o));
  });
  return out;
}

// ---------- catatan kaki
const footnotes = {};
for (const [id, rs] of Object.entries(book.foot)) {
  footnotes[id] = { children: [new Paragraph({ style: 'CatatanKaki', children: runs([{ t: ' ', s: null }, ...rs]) })] };
}

// ---------- halaman judul
const M = book.meta;
const title = [
  new Paragraph({ style: 'JudulBuku', children: [new TextRun(M.title)] }),
  ...M.subtitle.map((x) => new Paragraph({ style: 'SubjudulBuku', children: [new TextRun(x)] })),
  new Paragraph({ style: 'PengarangBuku', children: [new TextRun(M.author || 'al-Rāghib al-Iṣfahānī')] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun(M.author_dates || '(w. 502/1108)')] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun(M.desc)] }),
];

// ---------- keterangan penerjemah
const front = [new Paragraph({ style: 'JudulPengantar', children: [new TextRun('Keterangan Penerjemah')] })];
for (const r of book.front) front.push(new Paragraph({ style: 'TeksPengantar', children: runs(r) }));

// ---------- badan teks
const body = book.blocks.map((b) => {
  const o = { style: b.p, children: runs(b.r) };
  if (b.pb) o.pageBreakBefore = true;
  if (b.p === 'Syair') o.spacing = { before: b.first ? 160 : 0, after: b.last ? 160 : 0, line: 264 };
  return new Paragraph(o);
});

// ---------- lampiran glosarium (halaman melintang, tabel tanpa garis)
const A5W = 8391, A5H = 11906, MARG = 1021;
const TW = A5H - 2 * MARG; // lebar teks halaman melintang
// lebar kolom: minimal selebar kata terpanjangnya, sisanya dibagi menurut panjang isi
const plain = (rs) => rs.map((r) => r.t || '').join('');
const CH = 68, PAD = 150; // perkiraan lebar satu huruf 8 pt dan margin sel (dxa)
function widths(head, rows) {
  const cols = head.map((h, i) => [h, ...rows.map((r) => plain(r[i] || []))]);
  const minW = cols.map((c, i) => (head[i] === 'Arab' ? 950 : 0) || Math.min(Math.max(...c.flatMap((x) => x.split(/\s+/)).map((w) => w.length)) * CH + PAD, 1150));
  const want = cols.map((c) => (c.slice(1).reduce((a, x) => a + x.length, 0) / Math.max(c.length - 1, 1)) * CH + PAD);
  let W;
  const sumMin = minW.reduce((a, b) => a + b, 0);
  if (sumMin >= TW) W = minW.map((x) => (x * TW) / sumMin);
  else {
    const extra = want.map((x, i) => Math.max(x - minW[i], 0));
    const sumX = extra.reduce((a, b) => a + b, 0) || 1;
    W = minW.map((x, i) => x + ((TW - sumMin) * extra[i]) / sumX);
  }
  W = W.map(Math.round);
  W[W.length - 1] += TW - W.reduce((a, b) => a + b, 0);
  return W;
}
const NB = { style: BorderStyle.NONE, size: 0, color: 'auto' };
const noCell = { top: NB, bottom: NB, left: NB, right: NB };
const noTable = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };
// tabel dengan kepala yang sama memakai lebar kolom yang sama
const byHead = {};
for (const g of book.gloss) if (g.k === 'table') (byHead[g.head.join('|')] ||= []).push(...g.rows);
function table(head, rows) {
  const W = widths(head, byHead[head.join('|')]);
  const cell = (children, w) => new TableCell({
    borders: noCell, width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.TOP,
    margins: { top: 50, bottom: 50, left: 70, right: 70 }, children,
  });
  const hr = new TableRow({ tableHeader: true, children: head.map((h, i) => cell([new Paragraph({ style: 'SelTabelKepala', children: runs([{ t: h.replace(/\*/g, ''), s: null }]) })], W[i])) });
  const br = rows.map((row) => new TableRow({ cantSplit: true, children: row.map((c, i) => cell([new Paragraph({ style: 'SelTabel', children: runs(c) })], W[i])) }));
  return new Table({ width: { size: TW, type: WidthType.DXA }, columnWidths: W, layout: TableLayoutType.FIXED, borders: noTable, rows: [hr, ...br] });
}
const gloss = [new Paragraph({ style: 'LampiranJudul', children: [new TextRun(M.gloss_title)] })];
for (const g of book.gloss) {
  if (g.k === 'sub') gloss.push(new Paragraph({ style: 'LampiranSubjudul', children: runs(g.r) }));
  else if (g.k === 'group') gloss.push(new Paragraph({ style: 'LampiranKelompok', children: runs(g.r) }));
  else if (g.k === 'table') { gloss.push(table(g.head, g.rows)); gloss.push(new Paragraph({ style: 'SelTabel', children: [] })); }
  else gloss.push(new Paragraph({ style: 'TeksLampiran', children: runs(g.r) }));
}

const margin = { top: 1134, bottom: 1134, left: MARG, right: MARG };
const page = { size: { width: A5W, height: A5H }, margin };
const pageLand = { size: { width: A5W, height: A5H, orientation: PageOrientation.LANDSCAPE }, margin };

const doc = new Document({
  creator: 'Penerjemah', title: M.doc_title,
  styles: { default: { document: { run: { font: FONT, size: pt(11) } } }, paragraphStyles, characterStyles },
  footnotes,
  sections: [
    { properties: { page }, children: title },
    { properties: { page }, children: [...front, ...body] },
    { properties: { page: pageLand }, children: gloss },
  ],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log('ok', OUT, buf.length); });
