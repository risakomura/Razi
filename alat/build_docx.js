const fs = require('fs');
const path = require('path');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, FootnoteReferenceRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, Footer,
  PageNumber, VerticalAlign,
} = D;

const [, , IN, OUT] = process.argv;
const book = JSON.parse(fs.readFileSync(IN, 'utf8'));

const FONT = 'Times New Roman';
const FONT_AR = 'Traditional Arabic';
const pt = (n) => Math.round(n * 2);

// ---------- gaya paragraf (nama dipakai langsung oleh InDesign saat Place)
const P = (id, name, run, paragraph, extra = {}) => ({
  id, name, basedOn: extra.basedOn || 'Normal', next: extra.next || id, quickFormat: true,
  run: Object.assign({ font: FONT }, run), paragraph,
});
const paragraphStyles = [
  P('JudulBuku', 'Judul Buku', { size: pt(30), bold: true }, { alignment: AlignmentType.CENTER, spacing: { before: 2600, after: 240 } }),
  P('SubjudulBuku', 'Subjudul Buku', { size: pt(15), italics: true }, { alignment: AlignmentType.CENTER, spacing: { after: 960 } }),
  P('PengarangBuku', 'Pengarang Buku', { size: pt(13), smallCaps: true }, { alignment: AlignmentType.CENTER, spacing: { after: 240 } }),
  P('KeteranganBuku', 'Keterangan Buku', { size: pt(10), italics: true }, { alignment: AlignmentType.CENTER, spacing: { after: 120 } }),
  P('BagianKe', 'Bagian Ke', { size: pt(12), smallCaps: true, characterSpacing: 40 },
    { alignment: AlignmentType.CENTER, spacing: { before: 2000, after: 160 }, keepNext: true, pageBreakBefore: true, outlineLevel: 0 }),
  P('JudulBagian', 'Judul Bagian', { size: pt(16), bold: true },
    { alignment: AlignmentType.CENTER, spacing: { after: 360 }, keepNext: true, outlineLevel: 0 }),
  P('Pasal', 'Pasal', { size: pt(12), bold: true },
    { alignment: AlignmentType.CENTER, spacing: { before: 480, after: 60 }, keepNext: true, outlineLevel: 1 }),
  P('JudulPasal', 'Judul Pasal', { size: pt(12), italics: true },
    { alignment: AlignmentType.CENTER, spacing: { after: 240 }, keepNext: true }),
  P('Subpasal', 'Subpasal', { size: pt(11), bold: true, italics: true },
    { alignment: AlignmentType.LEFT, spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 2 }),
  P('PenandaSumber', 'Penanda Sumber', { size: pt(8.5), italics: true, color: '666666' },
    { alignment: AlignmentType.CENTER, spacing: { after: 240 }, keepNext: true }),
  P('TeksIsi', 'Teks Isi', { size: pt(11) },
    { alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 276 }, indent: { firstLine: 340 } }),
  P('TeksIsiPertama', 'Teks Isi Pertama', { size: pt(11) },
    { alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 276 }, indent: { firstLine: 0 } }, { basedOn: 'TeksIsi', next: 'TeksIsi' }),
  P('Syair', 'Syair', { size: pt(10.5), italics: true },
    { alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120, line: 276 }, indent: { left: 567, right: 567 } }, { next: 'TeksIsiPertama' }),
  P('Penutup', 'Penutup', { size: pt(11), smallCaps: true, characterSpacing: 40 },
    { alignment: AlignmentType.CENTER, spacing: { before: 480 } }),
  P('CatatanKaki', 'Catatan Kaki', { size: pt(8.5) },
    { alignment: AlignmentType.JUSTIFIED, spacing: { after: 40, line: 240 } }),
  P('LampiranJudul', 'Lampiran Judul', { size: pt(16), bold: true },
    { alignment: AlignmentType.CENTER, spacing: { before: 1200, after: 360 }, pageBreakBefore: true, keepNext: true, outlineLevel: 0 }),
  P('LampiranSubjudul', 'Lampiran Subjudul', { size: pt(11), bold: true },
    { alignment: AlignmentType.LEFT, spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 1 }),
  P('TeksLampiran', 'Teks Lampiran', { size: pt(10) },
    { alignment: AlignmentType.JUSTIFIED, spacing: { after: 120, line: 264 } }),
  P('SelTabel', 'Sel Tabel', { size: pt(8) }, { alignment: AlignmentType.LEFT, spacing: { after: 0, line: 240 } }),
  P('SelTabelKepala', 'Sel Tabel Kepala', { size: pt(8), bold: true }, { alignment: AlignmentType.LEFT, spacing: { after: 0, line: 240 } }, { basedOn: 'SelTabel' }),
];

// ---------- gaya karakter
const C = (id, name, run) => ({ id, name, basedOn: 'DefaultParagraphFont', quickFormat: true, run });
const characterStyles = [
  C('KutipanAyat', 'Kutipan Ayat', { italics: true }),
  C('RujukanAyat', 'Rujukan Ayat', { italics: false }),
  C('KutipanRiwayat', 'Kutipan Riwayat', { italics: true }),
  C('Transliterasi', 'Transliterasi', { italics: true }),
  C('AksaraArab', 'Aksara Arab', { font: { ascii: FONT_AR, hAnsi: FONT_AR, cs: FONT_AR, eastAsia: FONT_AR }, rightToLeft: true, sizeComplexScript: pt(13), language: { bidirectional: 'ar-SA' } }),
  C('AksaraArabTabel', 'Aksara Arab Tabel', { font: { ascii: FONT_AR, hAnsi: FONT_AR, cs: FONT_AR, eastAsia: FONT_AR }, rightToLeft: true, sizeComplexScript: pt(10), language: { bidirectional: 'ar-SA' } }),
  C('LabelArgumen', 'Label Argumen', { bold: true }),
  C('Tebal', 'Tebal', { bold: true }),
];

// ---------- run
function runs(rs) {
  const out = [];
  for (const r of rs) {
    if (r.fn !== undefined) { out.push(new FootnoteReferenceRun(r.fn)); continue; }
    const o = { text: r.t };
    if (r.s) o.style = r.s;
    if (r.s === 'AksaraArab' || r.s === 'AksaraArabTabel') o.rightToLeft = true;
    out.push(new TextRun(o));
  }
  return out;
}

// ---------- catatan kaki
const footnotes = {};
for (const [id, rs] of Object.entries(book.foot)) {
  footnotes[id] = { children: [new Paragraph({ style: 'CatatanKaki', children: runs([{ t: ' ', s: null }, ...rs]) })] };
}

// ---------- halaman judul
const title = [
  new Paragraph({ style: 'JudulBuku', children: [new TextRun('Asās al-Taqdīs')] }),
  new Paragraph({ style: 'SubjudulBuku', children: [new TextRun('Landasan Penyucian Allah')] }),
  new Paragraph({ style: 'PengarangBuku', children: [new TextRun('Fakhr al-Dīn al-Rāzī')] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun('(w. 606/1210)')] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun('Diterjemahkan dari teks Arab, dengan perbandingan terjemahan Turki İbrahim Coşkun')] }),
];

// ---------- badan teks
const body = book.blocks.map((b) => new Paragraph({ style: b.p, pageBreakBefore: b.pb ? true : undefined, children: runs(b.r) }));

// ---------- lampiran glosarium
const PAGE_W = 8391, MARG = 1021, TW = PAGE_W - 2 * MARG; // A5
const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
const borders = { top: border, bottom: border, left: border, right: border };
function table(head, rows) {
  const n = head.length;
  const W = n === 5 ? [1180, 1100, 1250, 1300, TW - 1180 - 1100 - 1250 - 1300] : [Math.round(TW / 2), TW - Math.round(TW / 2)];
  const cell = (children, w, headRow) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.TOP,
    margins: { top: 40, bottom: 40, left: 70, right: 70 },
    shading: headRow ? { fill: 'E8E8E8', type: ShadingType.CLEAR, color: 'auto' } : undefined,
    children,
  });
  const hr = new TableRow({ tableHeader: true, children: head.map((h, i) => cell([new Paragraph({ style: 'SelTabelKepala', children: runs([{ t: h.replace(/\*/g, ''), s: null }]) })], W[i], true)) });
  const br = rows.map((row) => new TableRow({ children: row.map((c, i) => cell([new Paragraph({ style: 'SelTabel', children: runs(c.map((r) => (r.s === 'AksaraArab' ? { ...r, s: 'AksaraArabTabel' } : r))) })], W[i], false)) }));
  return new Table({ width: { size: TW, type: WidthType.DXA }, columnWidths: W, rows: [hr, ...br] });
}
const gloss = [new Paragraph({ style: 'LampiranJudul', children: [new TextRun('Lampiran: Glosarium Istilah')] })];
gloss.push(new Paragraph({ style: 'TeksLampiran', children: runs([
  { t: 'Glosarium ini memuat istilah kunci yang dipakai secara baku dalam terjemahan. Padanan Inggris diambil dari kepala entri ', s: null },
  { t: 'Kashshāf Iṣṭilāḥāt al-Funūn wa-l-ʿUlūm', s: 'Transliterasi' },
  { t: ' karya Muḥammad ʿAlī al-Tahānawī, ed. Rafīq al-ʿAjam dan ʿAlī Daḥrūj (Beirut: Maktabat Lubnān Nāshirūn, 1996). Tanda † menandai istilah yang diberi catatan kaki berdasarkan ', s: null },
  { t: 'Kashshāf', s: 'Transliterasi' },
  { t: ' pada kemunculan pertamanya. Tanda "-" berarti entri tidak ditemukan atau kepala entrinya tidak terbaca dalam berkas yang dipakai.', s: null },
]) }));
for (const g of book.gloss) {
  if (g.k === 'sub') gloss.push(new Paragraph({ style: 'LampiranSubjudul', children: runs(g.r) }));
  else if (g.k === 'table') { gloss.push(table(g.head, g.rows)); gloss.push(new Paragraph({ style: 'SelTabel', children: [] })); }
  else if (g.k === 'para' && !/^Transliterasi mengikuti IJMES/.test(g.r.map((r) => r.t || '').join(''))) gloss.push(new Paragraph({ style: 'TeksLampiran', children: runs(g.r) }));
}

const page = { size: { width: PAGE_W, height: 11906 }, margin: { top: 1134, bottom: 1134, left: MARG, right: MARG, footer: 567 } };
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: pt(9) })] })] });

const doc = new Document({
  creator: 'Penerjemah', title: 'Asās al-Taqdīs: Terjemahan Indonesia',
  styles: { default: { document: { run: { font: FONT, size: pt(11) } } }, paragraphStyles, characterStyles },
  footnotes,
  sections: [
    { properties: { page }, children: title },
    { properties: { page }, footers: { default: footer }, children: [...body, ...gloss] },
  ],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log('ok', OUT, buf.length); });
