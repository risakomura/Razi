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

## Karya al-Rāghib (*al-Dharīʿa*, *Tafṣīl*, *Rasāʾil*), *Miftāḥ al-Ghayb* al-Qūnawī, dan *Nuzhat al-Arwāḥ* al-Shahrazūrī

Membuat ulang ketiga DOCX dari berkas MD-nya:

```bash
python3 alat/ragib_md2json.py dhariah /tmp/dhariah.json
node alat/ragib_build_docx.js /tmp/dhariah.json adh-dhariah.docx

python3 alat/ragib_md2json.py tafsil /tmp/tafsil.json
node alat/ragib_build_docx.js /tmp/tafsil.json tafsil-nashatayn.docx

python3 alat/ragib_md2json.py rasail /tmp/rasail.json
node alat/ragib_build_docx.js /tmp/rasail.json rasail-ragib.docx

python3 alat/ragib_md2json.py miftah /tmp/miftah.json
node alat/ragib_build_docx.js /tmp/miftah.json miftah-al-ghayb.docx

python3 alat/ragib_md2json.py nuzhat /tmp/nuzhat.json
node alat/ragib_build_docx.js /tmp/nuzhat.json nuzhat-al-arwah.docx
```

*Nuzhat al-Arwāḥ* al-Shahrazūrī memakai alat yang sama. Dalam blok syair, larik-larik dipisah baris `>` kosong agar tidak bergabung saat MD dibaca biasa; baris pemisah itu dilewati oleh `ragib_md2json.py`. Nama surah dalam rujukan ayat boleh memuat huruf bertanda IJMES (mis. `(al-ʿAnkabūt: 2)`).

Data halaman judul tiap kitab ada di `BOOKS` dalam `ragib_md2json.py` (termasuk `author` dan `author_dates`; bila kosong, dipakai nama al-Rāghib).

Yang dimasukkan: halaman judul, Keterangan Penerjemah (bagian 2 MD, Keputusan Kerja), seluruh terjemahan (dari `# TERJEMAHAN`), dan glosarium (bagian 3 MD) sebagai lampiran pada halaman melintang. Status proyek dan tabel konvensi markup tidak ikut.

Catatan kaki Markdown berkunci (`[^e1]`, `[^p13]`, `[^m-khalt]`, dst.) menjadi catatan kaki Word yang sebenarnya, dinomori urut menurut rujukan pertamanya. Urutan ini sama dengan nomor yang dipakai untuk merujuk antarkitab ("nota kaki *al-Dharīʿa* no. N", "catatan *Tafṣīl* no. N"). Rujukan silang antarcatatan dalam satu kitab ("lihat catatan d3") dan sel glosarium yang hanya berisi kunci catatan diganti dengan nomor catatan kaki itu. Tabel glosarium tanpa garis (semua garis tepi `none`, 0 pt); lebar kolom dihitung dari panjang rata-rata isinya.

Gaya paragraf: Judul Buku, Subjudul Buku, Pengarang Buku, Keterangan Buku, Judul Pengantar, Teks Pengantar, Kitab Ke, Judul Kitab, Basmalah, Judul Bab, Judul Pasal, Subpasal, Butir, Teks Isi, Teks Isi Pertama, Syair, Catatan Kaki, Lampiran Judul, Lampiran Subjudul, Lampiran Kelompok, Teks Lampiran, Sel Tabel, Sel Tabel Kepala.

Gaya karakter: Kutipan Ayat, Rujukan Ayat, Kutipan Riwayat, Transliterasi, Label Argumen, Tebal, Tebal Miring, Aksara Arab, Aksara Arab Tabel.
