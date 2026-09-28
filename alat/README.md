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

## Rasāʾil al-Rāghib

Membuat ulang `rasail-ragib.docx` dari `terjemahan-rasail-ragib.md`:

```bash
python3 alat/rasail_md2json.py terjemahan-rasail-ragib.md /tmp/rasail.json
node alat/rasail_build_docx.js /tmp/rasail.json rasail-ragib.docx
```

Yang dimasukkan: halaman judul, Keterangan Penerjemah (bagian 2 MD), seluruh terjemahan (dari `# TERJEMAHAN`), dan glosarium (bagian 3 MD) sebagai lampiran pada halaman melintang. Status proyek dan tabel konvensi markup tidak ikut.

Catatan kaki Markdown berkunci (`[^s1]`, `[^p13]`, `[^m-khalt]`, dst.) menjadi catatan kaki Word yang sebenarnya, dinomori urut menurut rujukan pertamanya. Rujukan silang antarcatatan ("lihat catatan d3") dan kolom kunci glosarium 3.2 dan 3.3 diganti dengan nomor catatan kaki itu. Tabel glosarium tanpa garis (semua garis tepi `none`, 0 pt).

Gaya paragraf: Judul Buku, Subjudul Buku, Pengarang Buku, Keterangan Buku, Judul Pengantar, Teks Pengantar, Kitab Ke, Judul Kitab, Basmalah, Judul Bab, Judul Pasal, Teks Isi, Teks Isi Pertama, Syair, Catatan Kaki, Lampiran Judul, Lampiran Subjudul, Lampiran Kelompok, Teks Lampiran, Sel Tabel, Sel Tabel Kepala.

Gaya karakter: Kutipan Ayat, Rujukan Ayat, Kutipan Riwayat, Transliterasi, Label Argumen, Tebal, Tebal Miring, Aksara Arab, Aksara Arab Tabel.
