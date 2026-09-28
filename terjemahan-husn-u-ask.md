# Hüsn ü Aşk: Terjemahan Indonesia

**Judul Indonesia:** *Jelita dan Asmara*
**Karya:** Şeyh Galib, Mehmed Esad (w. 1213/1799), *Hüsn ü Aşk* (rampung 1197/1783)
**Naskah dasar (Turki):** Şeyh Galib, *Hüsn ü Aşk*, teks dan terjemahan prosa bahasa Turki masa kini oleh Abdülbâki Gölpınarlı, Istanbul: Türkiye İş Bankası Kültür Yayınları, 2006 (cetakan pertama 1968; berkas `a09ecf14-Husn___A_k…epub`). Teks Gölpınarlı berpijak pada naskah tulisan tangan Galib sendiri (Süleymaniye, Halet Efendi Ek, no. 171), dengan penomoran bait 1–2101.
**Naskah rujukan (Inggris):** Şeyh Galip, *Beauty and Love*, terj. Victoria Rowe Holbrook, New York: The Modern Language Association of America, 2005 (berkas `f23d6453-Beauty_and_Love.docx`, hasil OCR)

---

## 0. Status Proyek dan Penanda Posisi

| Butir | Keterangan |
|---|---|
| Tahap | Penerjemahan berjalan |
| Sudah diterjemahkan | Bait 1–100 |
| Posisi berikutnya | Bait 101 (Mikraj, langit keenam) |

---

## 1. Konvensi Markup (untuk Pembentukan DOCX)

Setiap baris hanya memuat satu unsur. Bait dipisah satu baris kosong.

| Markup MD | Unsur | Gaya DOCX |
|---|---|---|
| `# Teks {.judul-kitab}` | Judul karya di awal terjemahan | Judul Kitab |
| `[Teks]{.basmalah}` (satu paragraf) | Basmalah pembuka | Basmalah |
| `## Teks {.judul-bagian}` | Judul bagian mesnawi (bab kisah, sanjungan, pembahasan) | Judul Bagian |
| `[N] larik pertama\` lalu `larik kedua` pada baris berikutnya | Satu bait (beyit) bernomor N, dua larik | Larik Awal + Larik Akhir; nomor dengan gaya karakter Nomor Bait |
| Baris ketiga `*teks*` sesudah larik kedua | Larik ulang (nakarat) penutup bait pada bagian bertingkat (*tardiyye*) | Larik Ulang |
| `***` (satu baris) | Pemisah antarbait bertingkat | Pemisah Bait |
| `*kata*` di dalam larik | Kutipan Arab atau Persia dalam larik, dan penekanan | Kutipan Larik |

Ketentuan penomoran:

1. Nomor bait mengikuti edisi Gölpınarlı (1–2101) dan ditulis di setiap bait dalam MD.
2. Dalam DOCX, nomor bait dicetak pada bait kelipatan lima dan pada bait pertama tiap bagian, rata kanan di luar larik (gaya karakter **Nomor Bait**, tabulasi kanan). Bait lain tetap membawa nomor sebagai data tetapi tidak dicetak.
3. Larik ulang (nakarat) dan pemisah bait tidak diberi nomor.
4. Judul bagian tidak dinomori; urutannya dijaga oleh nomor bait.

Konversi: `python3 alat/husn_md2json.py terjemahan-husn-u-ask.md /tmp/husn.json` lalu `node alat/husn_build_docx.js /tmp/husn.json husn-u-ask.docx` (lihat `alat/README.md`). Yang masuk DOCX hanya halaman judul dan terjemahan (dari `# TERJEMAHAN`); bagian 0–2 tidak ikut.

---

## 2. Keputusan Kerja

1. **Titik tolak:** teks Turki Utsmani suntingan Gölpınarlı, dibaca bait demi bait bersama terjemahan prosa Gölpınarlı ke bahasa Turki masa kini. Terjemahan Inggris Holbrook dipakai sebagai rujukan untuk diksi dan pembacaan, tidak sebagai sumber dasar. Bila Holbrook menyimpang dari teks Turki, teks Turki yang diikuti.
2. **Bentuk:** mesnawi diterjemahkan bait demi bait, satu bait dua larik, tanpa memaksakan rima. Rima dan asonansi dipakai bila datang dengan wajar dan tidak menggeser maksud.
3. **Bahasa:** indah tanpa keluar dari maksud; kosakata kaya, tidak akademis; ragam tak baku dan kata Jawa atau Sunda dipakai secukupnya, terutama pada tuturan yang di dalam teks Galib memang bernada akrab atau jenaka. Kata ganti (*-nya*, *ia*, *dia*, *mereka*) dihemat: subjek dilesapkan, nama diulang, atau kalimat disusun ulang.
4. **Tanpa penjelasan:** tidak ada catatan kaki, catatan penerjemah, atau glosarium di dalam terjemahan. Kiasan, nama, dan istilah dibiarkan bekerja di dalam larik.
5. **Nama tokoh alegoris** diterjemahkan agar alegorinya terbaca: Hüsn = **Jelita**, Aşk = **Asmara**, Suhan = **Sabda**, Gayret = **Ghirah**, İsmet = **Suci**, Hayret = **Takjub**, Molla Cünûn = **Mulla Gila**; Benî Mahabbet = **Bani Mahabbah**; Kalb = **Kalbu**; Mekteb-i Edeb = **Pesantren Adab**; Kal'a-i Zâtü's-Suver = **Benteng Rupa-Rupa**; Kimyâ = **Kimia**. Nama nabi, tokoh, tempat, dan istilah keagamaan ditulis dalam bentuk lazim Indonesia.
6. **Judul bagian** (dalam naskah berbahasa Persia) diterjemahkan ke bahasa Indonesia.
7. Tanpa aksara Arab, tanpa tanda pisah panjang dan menengah, tanpa penanda halaman.

---

# TERJEMAHAN

# Jelita dan Asmara {.judul-kitab}

[Dengan nama Allah Yang Maha Pengasih, Maha Penyayang]{.basmalah}

## Pujian bagi Allah {.judul-bagian}

[1] Segala puji bagi Yang merahmati sekalian insan,\
Yang memberi rukhsah bagi lemah dalam pujian.

[2] Tanpa rukhsah bagi lemah, pelik segala keadaan,\
kaki pena yang pincang tentu terbenam di kubangan.

[3] Bila puja bagi-Nya tak bertepi, tak terbilang,\
syukurlah, lidah kelemahan masih fasih berbilang.

[4] Pujilah, sebab syariat makna telah berfatwa:\
lemah dalam memuji Tuhan itu sah adanya.

[5] Kaum yang lemah beroleh pengertian\
dari sabda mulia, *"Tak kami kenal Engkau sebenar pengenalan."*

[6] Tanpa itu pun, ujungnya lemah jua yang didapat,\
tetapi tiada satu jiwa bakal sampai mendekat.

[7] Kekurangan kita dipayungi dengan pembelaan,\
bukan dipersulit, malah dilimpahi pertolongan.

[8] Tak wajib atas Tuhan memilih yang paling maslahat,\
tak ada pula yang memaksa kemurahan turun berlipat.

[9] Semata dari kemurahan, dilukis segala rupa,\
di atas keadilan ditakar tata semesta.

[10] Tanpa rukhsah bagi lemah, papa kita jadinya,\
bisu belaka, gagap pula tutur kata.

[11] Sukar nian menunaikan syukur dan puja:\
di mana bibir zarah, di mana surya?

[12] Namun lidah kelemahan masih kita punya,\
dalam menyanjung, lemah itu pula yang kita nyatakan terbuka.

[13] Jika ditimbang dengan insaf dan cermat,\
bukankah rukhsah bagi lemah itu nikmat?

[14] Tiap nikmat layak disanjung puja,\
dalam hal ini pun syukur mesti menyerta.

[15] Di sini pula lemah kita tersingkap nyata,\
dan sekali lagi Tuan Yang Mulia mengampuni kita.

[16] Kalau khayal dibiarkan lepas tanpa tepi,\
rantai kata bersambung-sambung tiada henti.

[17] Samudra pikir berdebur berombak,\
takjub di dalam takjub bergolak.

[18] Maka hati pun mabuk dan terpana,\
akal membungkam gelombang bicara.

## Sanjungan bagi Junjungan Semesta {.judul-bagian}

[19] Ruh-ruh, anugerah dari Ilahi,\
hanyalah debu di jalan Raja para Nabi.

[20] Raja yang bersinggasana di alam tanpa tempat,\
penyapu halamannya para malaikat terdekat.

[21] Raja yang, demi mengecup telapak kaki sang Nabi,\
bulan pun pecah berkeping laksana bintang-bintang.

[22] Jibril pembawa kabar anugerah,\
Mikail bendahara yang membagi berkah.

[23] Dengan *"Lawlaka"* zat yang suci disanjung,\
sifatnya dan Al-Qur'an saling wadah, saling kandung.

[24] Gerbang kubahnya, *Qaba Qawsain*;\
permadani di bawah telapaknya, ilmu kedua alam.

[25] Raja Malakut, martabatnya setinggi Arasy;\
bulan Jabarut, bayangnya terhampar di bumi.

[26] Kata orang yang akrab dengan Keesaan: satu belaka\
ombak Ahadiyah dan Ahmadiyah.

[27] Cahaya itu *"yang mula-mula dicipta"*;\
kalau kusebut "kedua sesudah Tuhan", dimaafkan jua.

[28] Adam, bapak segala manusia,\
hanyalah sebatang pohon di taman kenabian.

[29] Nuh sang peratap, berurai air mata,\
menjadi pelaut di samudra pesona sang Nabi.

[30] Saat Nil kegundahan Musa meluap bergelora,\
limpahan sang Nabi menjelma Khidir yang datang menyapa.

[31] Ketika syariatnya mulai mengayun pedang,\
bagian Ibrahim: berhala-berhala ditumbang.

[32] Mikraj kesempurnaan zat yang mulia\
diajarkan Idris kepada penghuni angkasa.

[33] Begitu tinggi keelokan yang tak ternilai harganya,\
Yusuf pun hanya budak yang dibeli sahaja.

[34] Demi mewartakan kedatangan sang Nabi, Isa\
naik hingga ke mimbar langit, fasih bersuara.

[35] Kejadiannya menjadi sebab maujudnya alam,\
umatnya pewaris rahasia ilmu yang terpendam.

[36] Cermin keesaan Ilahi\
adalah cermin wujudnya, persis tanpa selisih.

[37] Sadarlah akan iman yang sejati:\
cukup bagimu satu Allah, satu Nabi.

[38] Yang dahaga dipuaskan tanpa bayaran,\
mukjizatnya ditunjuk dengan ujung jari tangan.

[39] Hitam kesturi malam Isra\
menjadi cap mohor pada piagam kenabian.

[40] Walau tutur menjadi mata air karamah,\
mustahil menandingi Kitab Allah.

[41] Al-Qur'an sendiri melukiskan sang Rasul,\
memaparkan akhlaknya yang agung dan luhur.

[42] Wahai pena, pendekkanlah lidahmu:\
dengan Kalam di atas Lauh, Allah telah menulis semua itu.

## Kisah Mikraj {.judul-bagian}

[43] Suatu malam, rumah Ummu Hani\
menjadi langit bagi rembulan itu.

[44] Tapi malam macam apa! Penjaga rahmat,\
syaikh tanah haram di haribaan Hadirat.

[45] Serupa Bilal yang arif,\
cahaya iman di dalam cahaya hitam.

[46] Malam yang penuh jejak kemuliaan itu\
seolah Uwais al-Qarani, terang cahayanya tanpa ragu.

[47] Malam datang mengusapkan muka pada debu telapak kaki,\
sebab undangan menuju ketinggian telah tiba.

[48] Demi malam itu, langit yang berputar\
mengorbankan beribu-ribu fajar.

[49] Malam bercahaya itu laksana air hayat:\
hitam warnanya, hijau gelombangnya.

[50] Musim semi Nasut mendatangkan awan,\
padang hijau Lahut bergolak girang.

[51] Mata air Khidir tampak nyata,\
ruh-ruh keabadian terpuaskan dahaga.

[52] Kegelapan turun menyelubungi tirai gaib,\
tak syak lagi, surya berbisik rahasia kepada bulan.

[53] Agar surya dapat memperlihatkan wajah kepada bulan,\
cahaya-cahaya masuk ke dalam gelap persembunyian.

[54] Seakan Nil ketakjuban meluap,\
agar Mesir pertemuan hidup kembali.

[55] Titik hitam di lubuk hati mengembang,\
di dalamnya malam Isra menjadi rahasia.

[56] Semesta raya penuh cahaya,\
malam itu juga, pagi pun tiba.

[57] Kerinduan mencabik surya berkeping-keping,\
obor bintang-gemintang bersorak nyaring.

[58] Sembilan falak menjadi lumbung cahaya,\
kilau tanah menudungi surya.

[59] Limpahan tiba di bumi ini\
hingga bumi menjelma istana kaca.

[60] Andai surya dan bulan tak lebih dulu turun,\
bintang-bintanglah yang gugur sebagai ganti embun.

[61] Cahaya membungkus sekalian alam,\
hidup pun tampak terang, tiada kelam.

[62] Malam itu pelita yang langka memancarkan kilat,\
lenyaplah terik surya dan sinar bulan.

[63] Bintang-gemintang yang benderang bertumpuk laksana panen,\
surya dan bulan di sana hanya kunang-kunang.

[64] Malam kelam menjadi cermin cahaya,\
kekasih menampakkan wajah kepada kekasih.

[65] Tuhan berkehendak, lalu mengutus\
Jibril al-Amin sebagai bentara undangan.

[66] Setiap kali Jibril turun dari langit,\
seakan naik dari bumi ke Arasy.

[67] Malaikat teragung membawa kabar gembira:\
"Wahai Rasul yang paling mulia,

[68] Buraq yang tiada tara, itulah namanya,\
Arasy yang tertinggi datang ke kakimu.

[69] Lintasilah Arasy dan langit,\
jangan biarkan alam tanpa tempat bermuram durja."

[70] Tujuan dari *kun fayakun* penciptaan\
tunduk pada titah Tuhan.

[71] Segala sesuatu bergegas kembali ke asal,\
maka Al-Qur'an pun naik lagi ke langit.

[72] Ketika kaki keberuntungan menjejak sanggurdi,\
pelana itu rumah Keesaan.

[73] Tak tersisa bumi, tak tersisa zaman,\
lenyap sarang ganjil yang bernama dunia.

[74] Ketika samudra Keesaan bergelora,\
rupa berganti menjadi makna.

[75] Rahasia Keesaan pun masuk ke dalam rupa,\
makna yang azali mendapat rupa.

[76] Tiba-tiba tampak haribaan Aqsa,\
rahasia kehambaan pun tersingkap.

[77] Sang Nabi bersujud, Al-Haqq pun disujudi;\
maqam ini dinamai gaib yang tersaksikan.

[78] Arwah para rasul berjamaah,\
Allah yang tahu apa yang terjadi.

[79] Wahai pena, jangan terlalu gesit berlari;\
rahasia kenabian tak tergapai budi.

[80] Pantaskah embun bicara soal samudra?\
Pantaskah urusan Tuhan bagi manusia?

[81] Mari, tempuhlah adat para penyair,\
tinggalkan dulu omongan kaum sufi.

[82] Begitu kaki menjejak langit pertama,\
purnama yang jelita terbelah dua.

[83] Agar nyata bagi makhluk tanpa selubung\
bahwa zaman Ahmad itulah daur Rembulan.

[84] Karena dalam Mikraj tiada zaman,\
tak ada daya menyebut "yang lebih dulu".

[85] Terbelahnya bulan oleh mukjizat itu\
sungguh menjadi bukti dada yang dibelah.

[86] Hati yang luka itu dipulihkan,\
dihibur, lalu berjalan melenggang.

[87] Para malaikat jadi pengawal di depan,\
berseru riuh, "Allah besertamu!", dengan hati bergelora.

[88] Mengikuti wahyu yang turun,\
sang Nabi tiba di langit Utarid.

[89] Datanglah penyair yang martabatnya setinggi falak,\
memohon ampun kepada sang Raja.

[90] Buku hitam penyair itu dimaafkan,\
dosanya diampuni demi Hassan.

[91] Sang Pengutus menjadi penunjuk jalan bagi utusan-Nya,\
pintu langit ketiga pun terbuka.

[92] Zahra, sang putri, dijadikan syafaat bagi Zuhrah,\
bintang itu pun beroleh bagian dari ampunan sang Raja.

[93] Ketika langit keempat dijelajah,\
empat unsur berbangga dua kali lipat.

[94] Al-Masih beroleh limpahan dari Sang Rupawan,\
seolah dihidupkan kembali.

[95] Malam itu pelita abadi berkilat,\
surya malu, lalu masuk ke dalam tanah.

[96] Ketika kubah kelima menjadi persinggahan,\
Mirrikh diguncang gundah di hati.

[97] Menangis darah, bersiap memohon maaf,\
hingga kaki langit semerah mawar.

[98] Raja yang tunggangannya langit memberi maaf,\
dosa Mirrikh diampuni demi Izrail.

[99] Karena enam penjuru mendambakan sang Nabi,\
jalan pun sampai ke langit keenam.

[100] Agar Raja tujuh iklim itu\
mengajarkan syariat kepada kadi langit.
