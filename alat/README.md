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
