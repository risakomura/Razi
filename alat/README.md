# Alat pembuat DOCX

Membuat ulang `asas-al-taqdis.docx` dari `terjemahan-asas-al-taqdis.md`:

```bash
python3 alat/md2json.py terjemahan-asas-al-taqdis.md /tmp/buku.json
npm install docx   # sekali saja
node alat/build_docx.js /tmp/buku.json asas-al-taqdis.docx
```

Yang dimasukkan ke DOCX: halaman judul, seluruh terjemahan (dari `# TERJEMAHAN`), dan glosarium (bagian 2 MD) sebagai lampiran. Status proyek dan keputusan kerja tidak ikut.

Gaya paragraf: Judul Buku, Subjudul Buku, Pengarang Buku, Keterangan Buku, Bagian Ke, Judul Bagian, Pasal, Judul Pasal, Subpasal, Penanda Sumber, Teks Isi, Teks Isi Pertama, Syair, Penutup, Catatan Kaki, Lampiran Judul, Lampiran Subjudul, Teks Lampiran, Sel Tabel, Sel Tabel Kepala.

Gaya karakter: Kutipan Ayat, Rujukan Ayat, Kutipan Riwayat, Transliterasi, Aksara Arab, Aksara Arab Tabel, Label Argumen, Tebal.

## Karya al-Rāghib: *al-Dharīʿa*, *Tafṣīl*, *Rasāʾil*

Membuat ulang ketiga DOCX dari berkas MD-nya:

```bash
python3 alat/ragib_md2json.py dhariah /tmp/dhariah.json
node alat/ragib_build_docx.js /tmp/dhariah.json adh-dhariah.docx

python3 alat/ragib_md2json.py tafsil /tmp/tafsil.json
node alat/ragib_build_docx.js /tmp/tafsil.json tafsil-nashatayn.docx

python3 alat/ragib_md2json.py rasail /tmp/rasail.json
node alat/ragib_build_docx.js /tmp/rasail.json rasail-ragib.docx
```

Data halaman judul tiap kitab ada di `BOOKS` dalam `ragib_md2json.py`.

Yang dimasukkan: halaman judul, Keterangan Penerjemah (bagian 2 MD, Keputusan Kerja), seluruh terjemahan (dari `# TERJEMAHAN`), dan glosarium (bagian 3 MD) sebagai lampiran pada halaman melintang. Status proyek dan tabel konvensi markup tidak ikut.

Catatan kaki Markdown berkunci (`[^e1]`, `[^p13]`, `[^m-khalt]`, dst.) menjadi catatan kaki Word yang sebenarnya, dinomori urut menurut rujukan pertamanya. Urutan ini sama dengan nomor yang dipakai untuk merujuk antarkitab ("nota kaki *al-Dharīʿa* no. N", "catatan *Tafṣīl* no. N"). Rujukan silang antarcatatan dalam satu kitab ("lihat catatan d3") dan sel glosarium yang hanya berisi kunci catatan diganti dengan nomor catatan kaki itu. Tabel glosarium tanpa garis (semua garis tepi `none`, 0 pt); lebar kolom dihitung dari panjang rata-rata isinya.

Gaya paragraf: Judul Buku, Subjudul Buku, Pengarang Buku, Keterangan Buku, Judul Pengantar, Teks Pengantar, Kitab Ke, Judul Kitab, Basmalah, Judul Bab, Judul Pasal, Subpasal, Butir, Teks Isi, Teks Isi Pertama, Syair, Catatan Kaki, Lampiran Judul, Lampiran Subjudul, Lampiran Kelompok, Teks Lampiran, Sel Tabel, Sel Tabel Kepala.

Gaya karakter: Kutipan Ayat, Rujukan Ayat, Kutipan Riwayat, Transliterasi, Label Argumen, Tebal, Tebal Miring, Aksara Arab, Aksara Arab Tabel.

## Şeyh Galib: *Hüsn ü Aşk* (*Jelita dan Asmara*)

Membuat ulang `husn-u-ask.docx` dari `terjemahan-husn-u-ask.md`:

```bash
python3 alat/husn_md2json.py terjemahan-husn-u-ask.md /tmp/husn.json
node alat/husn_build_docx.js /tmp/husn.json husn-u-ask.docx
```

Yang dimasukkan: halaman judul dan seluruh terjemahan (dari `# TERJEMAHAN`). Status proyek, konvensi markup, dan keputusan kerja tidak ikut. Tidak ada catatan kaki, header, footer, atau nomor halaman (siap ditempatkan ke InDesign).

Parser memeriksa bahwa nomor bait berurutan 1 sampai 2101 tanpa lompatan, bahwa setiap larik kecuali yang terakhir dalam satu bait diakhiri `\`, dan bahwa setiap blok berisi 2 larik (bait) atau 5 larik (bait bertingkat dengan larik ulang). Nomor bait dicetak pada kelipatan lima dan pada bait pertama tiap bagian, rata kanan di tepi teks.

Gaya paragraf: Judul Buku, Subjudul Buku, Pengarang Buku, Keterangan Buku, Judul Kitab, Basmalah, Judul Bagian, Larik Awal, Larik Akhir, Larik Ulang, Pemisah Bait.

Gaya karakter: Nomor Bait, Kutipan Larik.
