// Membangun DOCX terjemahan Hüsn ü Aşk dari JSON keluaran husn_md2json.py.
// Satu bait = dua paragraf (Larik Awal, Larik Akhir); nomor bait dicetak rata kanan
// pada tabulasi kanan larik yang membawa nomor, hanya untuk nomor yang ditandai `show`.
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Footer, PageNumber, TabStopType,
} = require('docx');

const [, , IN, OUT] = process.argv;
const book = JSON.parse(fs.readFileSync(IN, 'utf8'));

const FONT = 'Times New Roman';
const pt = (n) => Math.round(n * 2);
const A5W = 8391, A5H = 11906, MARG = 1134;
const TW = A5W - 2 * MARG; // lebar teks

const P = (id, name, run, paragraph, extra = {}) => ({
  id, name, basedOn: extra.basedOn || 'Normal', next: extra.next || id, quickFormat: true,
  run: Object.assign({ font: FONT }, run), paragraph,
});
const C_ = AlignmentType.CENTER, L = AlignmentType.LEFT;
const paragraphStyles = [
  P('JudulBuku', 'Judul Buku', { size: pt(26), bold: true }, { alignment: C_, spacing: { before: 2400, after: 240 } }),
  P('SubjudulBuku', 'Subjudul Buku', { size: pt(13), italics: true }, { alignment: C_, spacing: { after: 120 } }),
  P('PengarangBuku', 'Pengarang Buku', { size: pt(13), smallCaps: true }, { alignment: C_, spacing: { before: 720, after: 120 } }),
  P('KeteranganBuku', 'Keterangan Buku', { size: pt(10), italics: true }, { alignment: C_, spacing: { after: 120 } }),
  P('JudulKitab', 'Judul Kitab', { size: pt(18), bold: true },
    { alignment: C_, spacing: { before: 1440, after: 360 }, keepNext: true, pageBreakBefore: true, outlineLevel: 0 }),
  P('Basmalah', 'Basmalah', { size: pt(11), italics: true }, { alignment: C_, spacing: { before: 120, after: 360 }, keepNext: true }),
  P('JudulBagian', 'Judul Bagian', { size: pt(12), bold: true },
    { alignment: C_, spacing: { before: 480, after: 240 }, keepNext: true, keepLines: true, outlineLevel: 1 }),
  // larik awal: menjorok sedikit; larik akhir: menjorok lebih dalam, seperti tata letak mesnawi
  P('LarikAwal', 'Larik Awal', { size: pt(11) },
    { alignment: L, spacing: { before: 100, after: 0, line: 264 }, indent: { left: 0, hanging: 0 }, keepNext: true, keepLines: true,
      tabStops: [{ type: TabStopType.RIGHT, position: TW }] }),
  P('LarikAkhir', 'Larik Akhir', { size: pt(11) },
    { alignment: L, spacing: { before: 0, after: 0, line: 264 }, indent: { left: 850 }, keepLines: true }, { next: 'LarikAwal' }),
  P('LarikUlang', 'Larik Ulang', { size: pt(11), italics: true },
    { alignment: L, spacing: { before: 60, after: 60, line: 264 }, indent: { left: 1700 }, keepLines: true }, { next: 'LarikAwal' }),
  P('PemisahBait', 'Pemisah Bait', { size: pt(10) }, { alignment: C_, spacing: { before: 160, after: 60 } }, { next: 'LarikAwal' }),
];
const characterStyles = [
  { id: 'NomorBait', name: 'Nomor Bait', basedOn: 'DefaultParagraphFont', quickFormat: true, run: { size: pt(8), color: '666666' } },
  { id: 'KutipanLarik', name: 'Kutipan Larik', basedOn: 'DefaultParagraphFont', quickFormat: true, run: { italics: true } },
];

const runs = (rs) => rs.map((r) => new TextRun(r.s ? { text: r.t, style: r.s } : { text: r.t }));

const M = book.meta;
const title = [
  new Paragraph({ style: 'JudulBuku', children: [new TextRun(M.title)] }),
  ...M.subtitle.map((x) => new Paragraph({ style: 'SubjudulBuku', children: [new TextRun(x)] })),
  new Paragraph({ style: 'PengarangBuku', children: [new TextRun(M.author)] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun(M.author_note)] }),
  new Paragraph({ style: 'KeteranganBuku', children: [new TextRun(M.desc)] }),
];

const body = book.blocks.map((b) => {
  if (b.p === 'PemisahBait') return new Paragraph({ style: b.p, children: [new TextRun('*')] });
  const children = runs(b.r);
  const o = { style: b.p, children };
  if (b.show) {
    // nomor bait rata kanan pada tabulasi kanan tepi teks
    children.push(new TextRun({ text: '\t' + b.n, style: 'NomorBait' }));
    o.tabStops = [{ type: TabStopType.RIGHT, position: TW }];
  }
  if (b.stanza) o.spacing = { before: 240, after: 0, line: 264 };
  return new Paragraph(o);
});

const page = { size: { width: A5W, height: A5H }, margin: { top: 1134, bottom: 1134, left: MARG, right: MARG, footer: 567 } };
const footer = () => new Footer({ children: [new Paragraph({ alignment: C_, children: [new TextRun({ children: [PageNumber.CURRENT], size: pt(9) })] })] });

const doc = new Document({
  creator: 'Penerjemah', title: M.doc_title,
  styles: { default: { document: { run: { font: FONT, size: pt(11) } } }, paragraphStyles, characterStyles },
  sections: [
    { properties: { page }, children: title },
    { properties: { page }, footers: { default: footer() }, children: body },
  ],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log('ok', OUT, buf.length); });
