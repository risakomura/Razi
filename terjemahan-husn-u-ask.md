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
| Sudah diterjemahkan | Bait 1–399 |
| Posisi berikutnya | Bait 400 (Keadaan Cinta Keduanya) |

---

## 1. Konvensi Markup (untuk Pembentukan DOCX)

Setiap baris hanya memuat satu unsur. Bait dipisah satu baris kosong.

| Markup MD | Unsur | Gaya DOCX |
|---|---|---|
| `# Teks {.judul-kitab}` | Judul karya di awal terjemahan | Judul Kitab |
| `[Teks]{.basmalah}` (satu paragraf) | Basmalah pembuka | Basmalah |
| `## Teks {.judul-bagian}` | Judul bagian mesnawi (bab kisah, sanjungan, pembahasan) | Judul Bagian |
| `[N] larik pertama\` lalu `larik kedua` pada baris berikutnya | Satu bait (beyit) bernomor N, dua larik | Larik Awal + Larik Akhir; nomor dengan gaya karakter Nomor Bait |
| Lima baris berturut-turut, empat pertama diakhiri `\`, baris kelima `*teks*` | Bait bertingkat (*tardiyye*): empat larik dan satu larik ulang (nakarat) | Larik Awal, Larik Akhir, Larik Awal, Larik Akhir, Larik Ulang |
| `*kata*` di dalam larik | Kutipan Arab atau Persia dalam larik, judul karya, dan penekanan | Kutipan Larik |

Ketentuan penomoran:

1. Nomor bait mengikuti edisi Gölpınarlı (1–2101) dan ditulis di setiap bait dalam MD, di awal larik tempat bait itu bermula.
2. Pada bait bertingkat, Gölpınarlı menghitung tiap dua larik sebagai satu bait secara bersambung melintasi bait bertingkat, sehingga nomor dapat jatuh pada larik ketiga, kelima (larik ulang), atau larik lain. Penempatan ini dipertahankan.
3. Dalam DOCX, nomor bait dicetak pada nomor kelipatan lima dan pada nomor pertama tiap bagian, rata kanan di tepi teks (gaya karakter **Nomor Bait**, tabulasi kanan). Nomor lain tetap ada sebagai data tetapi tidak dicetak.
4. Judul bagian tidak dinomori; urutannya dijaga oleh nomor bait. Parser memeriksa bahwa nomor bait berurutan tanpa lompatan.

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

[101] Titah dari hadirat Al-Haqq pun disampaikan,\
hukum-hukum yang lampau dilarang tegas.

[102] Tenung dan nujum ditolak,\
yang tampak dan tempat penampakan ditata rapi.

[103] Ketika sampai di langit ketujuh,\
bahagia dianugerahkan bagi seisi alam.

[104] Kaiwan menjadikan Bilal pemberi syafaat,\
lalu mengusapkan muka ke tanah seraya berkata:

[105] "Cukuplah malam ini aku memohon maaf;\
jadikan hitam warna yang paling tinggi."

[106] Ketika Raja *Lawlaka*\
telah tuntas menjelajah segala falak,

[107] anugerah Ilahi belum juga\
menemukan mikraj yang sempurna.

[108] Begitu kaki yang melangkah menjejak Kursi,\
rindu membuat bintang-bintang tetap jadi pengembara.

[109] Sebab, demikian sabda sang Nabi, langit gugus bintang\
tercipta demi dimuliakan kedatangan ini.

[110] Oleh jejak kaki zat yang suci,\
Lembu penyangga bumi terangkat naik ke falak.

[111] Raja yang esa itu bermurah hati,\
si Kembar diangkat menjadi kepala pengawal istana.

[112] Ketika Timbangan menadahkan tangan meminta-minta,\
bukan dirham, mutiara yang ditaburkan.

[113] Ikan bergegas menuju debu telapak kaki,\
Kepiting menyelam ke pusaran persembunyian.

[114] Singa teringat akan putra paman sang Nabi,\
dan dari sanalah datang pertolongan yang membebaskan.

[115] Sebab Domba telah datang mengadu,\
seraya mengisahkan keperkasaan itu.

[116] Timba pun kalang kabut, meratap,\
"Setetes saja, demi sumur Zamzam!"

[117] Oleh satu limpahan, riang dan bangga,\
Timba berputar menjadi Kincir Muhammadi.

[118] Ketika Kambing dihiasi gugus Kartika,\
dijadikan hadiah bagi kedua cucunda.

[119] Sayap agung malaikat di malam rahasia itu\
terbang selalu dari Mayang.

[120] Karena jam langit butuh jarum, sang Kalajengking\
tepat pada waktunya ikut mengajukan hajat.

[121] Kemuliaan diterima pun menjadi mungkin,\
tak semenit pun karunia terlewat.

[122] Menatap busur kakek tua bernama Zaman,\
tampaklah betapa ringkih keadaan dunia.

[123] Sang Raja penunggang *Qaba Qawsain*\
melanjutkan perjalanan ke balik dua alam.

[124] Seiring langkah dengan Jibril al-Amin,\
hingga Arasy Tuhan dijadikan tempat singgah.

[125] Lauh dan Kalam dan seribu rahasia,\
juga para karubiyan, tampak di mata.

[126] Arasy begitu terpana oleh rindu\
sampai lupa tempat berdiri.

[127] Arasy ditinggal di belakang laksana bayang,\
sang empunya martabat Arasy berseru, "Dzul-Arsy!"

[128] Dalam perjalanan itu tampak alam di sebaliknya,\
hingga Sidratul Muntaha terlihat pula.

[129] Terbukalah pintu haribaan pertemuan;\
kedekatan tertinggal, datanglah kesatuan.

[130] Pada Jibril tampak ketidakberdayaan,\
di sana makna meninggalkan kata-kata.

[131] Mula-mula apa, lalu jadi apa, entahlah;\
sudah penuh sebibir, lalu apa lagi yang tertuang, embuh.

[132] Wahai yang rahmatnya tercurah cuma-cuma, wahai Rahman,\
dengan kasih, riangkanlah hamba ini,

[133] yang mendamba bahagia abadi,\
yakni si fakir, Galib Esad.

[134] Berdosa memang, tetapi umatmu jua,\
harapan satu-satunya hanyalah syafaatmu.

[135] Tanpa karunia syafaatmu,\
banyak ahli zuhud berakhir dengan tangan hampa.

[136] Karena aku pelaku dosa besar, hitam catatan,\
bagi setiap hajatku tersedia kabar gembira.

## Sanjungan bagi Hazrat Maulana {.judul-bagian}

[137] Setelah Allah menutup barisan para nabi,\
datanglah kepada kita para wali yang arif.

[138] Raja kaum itu, Mulla Hunkar;\
cukup satu penguasa bagi jagat ini.

[139] Sultan di takhta negeri makrifat,\
duduk di sajadah Singa Tuhan.

[140] Pikirannya penunjuk jalan hakikat,\
laksana wakil Ash-Shiddiq.

[141] Mentari di langit keturunan Haidar,\
pejalan di jalan Sang Singa, berantai emas.

[142] Seruas buluh penanya memperdengarkan diri,\
barulah kita tahu, seruling suara Daud itu apa.

[143] Melampaui ulama agama,\
pantas disebut "Nabi negeri Rum".

[144] Makna ucapannya ruh Isa,\
laksana Mahdi, syariat dihidupkan kembali.

[145] Hingga kini tak satu kitab pun bergelar\
"inti Al-Qur'an"; lihatlah kemuliaan kitab sang Maulana.

[146] Negeri tuturnya kota raya,\
sepetak kecilnya singgasana Ibnu Adham.

[147] Lelaki seperti Ibrahim Gulsyani\
menjadi bulbul tunggal di taman itu.

[148] Para abdal falak binasa oleh cinta sang Maulana,\
surya dan bulan pun koyak dada karena cinta.

[149] Bait-bait yang mulia itu, ayat demi ayat,\
adalah rahasia syariat dan hakikat.

[150] Tutur yang terang itu pelita makna,\
tiap titiknya permata malam bagi makna.

[151] Mahkota kaum para wali,\
raja dan tuan bagi insan-insan suci.

[152] Ombak samudra tenggelam dan berpisah\
telah meliputi barat dan timur.

[153] Titahnya berlaku di segala penjuru,\
limpahannya mengalir di setiap bagian waktu.

[154] Alam sudah penuh dengan limpahan himmah,\
tak usah lagi bicara soal karamah.

## Mengenang Pembimbingku {.judul-bagian}

[155] Agar perbincangan ini sampai ke ujung,\
seorang yang terpuji menjadi pendorong,

[156] yang tersungkur di jalan kemuliaan,\
yakni ayahandaku, Reşid Efendi,

[157] yang menyepi di zawiyah hati,\
pencinta Maulawi yang rela menyabung kepala.

[158] Sungguh, dulu aku tercenung dan bisu,\
tak kuasa berkata-kata.

[159] Lidah pena terdiam kelu,\
seribu ombak duka bergolak.

[160] Jemu sudah pada bual dan bicara,\
khayal pun melampaui warna dan aroma.

[161] Kisah Mikraj tertinggal tak terucap,\
kisah Jelita dan Asmara ini pun tak bermahkota.

[162] "Bicaralah!" kata ayahanda, mendorongku bertutur;\
oleh limpahan napas beliau, rampunglah karya.

[163] Si sesat ini dituntun,\
diajari gaya sang Pir dalam bertutur.

[164] Jawara gelanggang itu mengisi\
relung batinku dengan air hayat melalui himmah.

[165] Karena menjadi pemandu di jagat cinta,\
bukankah keayahannya berlipat dua?

[166] Setiap sanjungan yang kuucapkan\
bersih dari bencana riya.

[167] Laksana seruling, aku dihidupkan\
oleh limpahan napas sosok yang luhur itu.

[168] Beliau menjadi sebab dan mencurahkan himmah,\
maka aku sempat berkhidmat kepada banyak ahli hal.

[169] Sungguh, oleh jejak kemurahan beliau\
aku hidup kembali; mengingkarinya adalah kufur.

[170] Beliau sendiri tak menyebutnya pertolongan,\
dan aku pun tak pernah merasa cukup berterima kasih.

[171] Samudra kemurahan tiada berseberang,\
di dalamnya mutiara limpahan melimpah ruah.

[172] Insya Allah, Yang Maha Pengasih lagi Maha Penyayang,\
rahasia penyaksian akan tampak terang.

## Sebab Penulisan Kitab {.judul-bagian}

[173] Aku menjadi orang dalam sebuah majelis keakraban,\
di dalam surga itu, akulah Adam.

[174] Majelis, namun sejatinya taman mawar kasih,\
bulbul-bulbulnya para karib yang saling mengasihi.

[175] Masing-masing penyair penimbang kata,\
semuanya belia, semuanya berbekal harta.

[176] Yang diobrolkan: syair, keutamaan, makrifat;\
yang mengakrabkan: nazam, prosa, dan paham yang cermat.

[177] Aku mabuk anggur pagi kejenakaan,\
waktu itu pagi masa muda yang ranum.

[178] Sesekali dibacakan *Khairabad*,\
Nabi dikenang dengan kebaikan.

[179] Memang karya itu ajaib,\
dihargai di kalangan ahlinya.

[180] Digubah di hari tua,\
kala sang penyair sudah beruban.

[181] Seorang ahli makna, dalam memuji nazam itu,\
menyanjung berlebih-lebihan.

[182] Seisi majelis pun mengiyakan,\
mengulang-ulang pendapat itu dengan sepakat.

[183] Sampai-sampai kesimpulannya:\
mustahil ada yang sanggup menandingi.

[184] Cawan itu terasa berat bagiku,\
tampak laksana ujian.

[185] Dengan sindiran kualamatkan bicara,\
kepada rombongan itu kujawab begini:

[186] "Pantaskah Nabi\
menempelkan kata pada tutur sang Syaikh?

[187] Hai yang buta akan kisah itu,\
kurangkah yang ditinggalkan Syaikh Attar?

[188] Kisah itu cuma segitu,\
selebihnya dusta tanpa ujung.

[189] Bait-baitnya bergaya nazam Persia,\
semua rangkaian idafah beruntun.

[190] Dalam prosa indah memang jadi hiasan,\
tapi dalam tutur Turki, beratnya bukan kepalang.

[191] Kalau sedikit, tak apa-apa,\
barangkali malah kami sebut seni.

[192] Satu lagi: si penggubah kata itu,\
dalam berlebih-lebihan, burung yang terbang rendah.

[193] Pujian bagi Buraq Kebanggaan Alam?\
*Rahsyiyah* Nef'i sudah lebih dulu ada.

[194] Perlukah Buraq dipuji dan dilukis?\
Siapa yang menyuruh mengerjakan itu?

[195] Mari kita maafkan, mungkin saja tak paham;\
kuda yang sekali tersandung tak dipenggal kepalanya.

[196] Satu lagi: orang tua yang renta itu\
telah meraih nama dan tenar bermacam-macam.

[197] Lima maharaja keturunan malaikat\
dengan murah hati menyokong bakatnya.

[198] Di pasar dunia hajatnya terpenuhi,\
di gelanggang tutur namanya harum.

[199] Meski begitu, tetap saja bermalas-malas,\
banyak makna dilalaikan.

[200] Dengan menemukan satu dua ungkapan manis,\
lelakikah namanya, melukis soal kawin-mawin?

[201] Kalau kau bilang, Nizami yang mulia\
juga menempuh cara itu,

[202] itu gaya Persia, tak usah heran;\
para rind Persia memang tak peduli adab.

[203] Untuk apa meniru segala tingkah itu?\
Boleh saja, tapi buat apa nekat berlebihan?

[204] Satu lagi: si penimbang kata itu\
membebani pena dengan jerih tanpa harta.

[205] Seorang maling bertelanjang kaki\
hendak disejajarkan dengan Mansur.

[206] Mikraj khayal disusun-susun,\
maunya si maling jadi sekutu Al-Masih.

[207] Tiang pancang *Khairabad*, si Kampung Kebajikan,\
tak lain kisah kesempurnaan seorang tak berkebajikan.

[208] Sungguh, itu kisah hasil curian;\
bagi para maling, banyak pelajaran.

[209] Orang tua itu cuma bersusah payah,\
malah memberi kilau pada kerja maling.

[210] Kalau memberi nasihat, begini seleranya:\
'Dunia fana, akhirat baka.'

[211] Serusak apa pun, sepikun apa pun,\
tak ada telinga yang belum pernah mendengar itu.

[212] Lelaki sejati ialah yang membuka jalan baru,\
menyadarkan para ahli yang arif.

[213] Tuturnya bukan asal ceplos,\
tapi maju setelah berkali-kali menguji.

[214] Tapi kepada siapa rahasia ini kubuka?\
Andai aku pun tahu sebanyak itu!

[215] Andai tuturku seirama dengan mulut orang banyak,\
perlukah aku terbang di angkasa?

[216] Duh, duh, rahasia apa yang kubeberkan ini!\
Seratus tobat, seratus ribu kali kusangkal!

[217] Satu bait berwarna yang dipuji seorang ahli tutur\
sebanding dengan satu langit.

[218] Pena di tanganku selalu berkata:\
'Bencana bagiku, pujian orang banyak.'

[219] Karena kerja orang semacam itu hanya mengayomi\
dan menyesuaikan diri dengan pemahaman orang,

[220] tentu hatinya jadi beku,\
lidahnya tak sampai menjangkau makna.

[221] Namun bakat tetap saja kentara,\
titipan yang diterima tampak di gelanggang.

[222] Orang yang tangkas batinnya dan waspada\
tak akan menyamakan maling dengan raja.

[223] Betapapun patah sayapnya,\
elang raja tak akan menyerupai burung hantu dan angsa.

[224] Tak tersisakah lagi mabuk kasih?\
Sudah tamatkah kisah itu?

[225] Adakah selain cinta yang layak\
dibelanjai permata kata?

[226] Kalau kau bilang, sudah seribu kali diulang,\
jangan muak pada anggur keabadian.

[227] Seluruh alam hanyalah derita cinta dan keakraban,\
selebihnya duka, pedih, dan kesialan.

[228] Bila kau paham jalan ini,\
tak akan ada maling sesat menghadang di jalanmu.

[229] Inilah derita tutur, tak bisa dibeberkan;\
masih banyak lagi yang tak sanggup kuungkapkan.

[230] Bendahara permata seni itu\
tak punya seni yang sampai ke rasa."

[231] Sampai seorang yang bernapas Al-Masih menyindir:\
"Bikin sendiri tak mampu, karya orang pun tak suka."

[232] Macam-macam keberatan telah kuajukan,\
dan tiap-tiapnya kubuktikan.

[233] Lagu yang mulai kulantunkan ini\
mula-mula membuatku merintih dan sesak hati.

[234] Kawan-kawan memegang kata-kataku:\
"Ayo, klaim butuh bukti, sekarang tunjukkan!

[235] Apa yang digapai Nabi dengan susah payah,\
Allah berikan kepadamu di masa muda."

[236] Dengan gairah itu kuangkat pena,\
kugubah nazam ini, patah-patah terjalin.

[237] Kekuranganku kuakui,\
namun omonganku bukan omong kosong.

[238] Walau kain Evren buruk warnanya,\
tak kalah dari kain Aleppo.

[239] Siapa yang datang dari kota keakraban\
tahu dari mana barang dagangan kami berasal.

## Awal Kisah {.judul-bagian}

[240] Pena, seruas buluh yang menaburkan gula,\
yang hatinya hidup oleh limpahan Syams Tabriz,

[241] menuangkan uraian cinta dalam rupa ini,\
menuturkan kepadaku hikayat cinta:

[242] Konon di tanah Arab ada satu kabilah,\
menghimpun segala perangai indah.

[243] Kepala halaman kitab kesatriaan,\
pemuka kaum Arab: Bani Mahabbah.

[244] Tapi kabilah macam apa! Kiblat derita,\
hitam nasib, pucat pasi muka semua.

[245] Pakaian: terik surya bulan Juli;\
minuman: nyala api pembakar dunia.

[246] Lembahnya pasir dan beling duka,\
sedih dan ratap sebanyak butir pasir.

[247] Kemahnya asap desah kehampaan,\
obrolannya rintih melulu, laksana seruling.

[248] Masing-masing gandrung pada seorang jelita,\
mulut berlumur darah bagai mata pedang.

[249] Rezeki: bala yang datang tiba-tiba;\
api menghujani kepala setiap saat.

[250] Yang ditanam: benih bunga api;\
yang dituai: hati koyak berkeping.

[251] Para penghidup kata berkata:\
Majnun pun berasal dari kabilah itu.

[252] Siapa saja yang sengaja mencari bala,\
pasti keturunan tungku yang sama.

[253] Yang dijual selalu barang bernama nyawa,\
yang dibeli bara tersembunyi.

## Tentang Perjamuan {.judul-bagian}

[254] Kalau kaum itu hendak bersuka dan minum,\
topan bala pun bergolak.

[255] Piala: gada sebesar gunung;\
anggur: maut yang menggentarkan.

[256] Majelis: medan laga yang rusuh;\
biduan: hiruk pikuk penggebuk hati.

[257] Belati disangka cawan,\
cabikan kain disangka sutra mahal.

[258] Izrail saki pribadi kaum itu,\
Mirrikh penari di perjamuan.

[259] Kecapi dan genderang: suara ratapan;\
penabuh rebana: demam menggigil peluluh nyawa.

[260] Kudapan dan badam di sela minum:\
mata jahat orang dan racun kepedihan.

[261] Sumbat kapas pada botol: kapas pembalut luka selar,\
dan di dalam luka selar, anggur nyala mengalir laksana sungai.

[262] Jerit, siksa, putus asa, dan dendam rindu:\
itulah perkakas bersuka; perlu apa lagi?

## Tentang Perburuan {.judul-bagian}

[263] Bila kaum itu berangkat berburu,\
tak pernah menuju negeri yang ada jalan pulang.

[264] Puyuh buruan: selalu kadal;\
ayam hutan: kalajengking terbang.

[265] Elang pemburu: tatap kerinduan;\
tangkapan: burung hantu dan celepuk kengerian.

[266] Bila naga melingkar hendak melompat,\
"Selamat datang, barisan bangau!" seru kaum itu.

[267] Kijang buruan: asap desah yang membubung,\
tubuh hitam legam, tanduk menyala api.

[268] Pemburu gandrung pada buruan;\
kelinci, bagi kaum itu, peluru yang melesat.

[269] Agar anak panah tak melenceng ke mana-mana,\
diri sendiri yang ditarik ke tali busur.

[270] Yang dipanah: ular berbelang;\
anak panah: ular-panah, tabung panah: wajah sendiri.

## Tentang Musim Semi {.judul-bagian}

[271] Bila musim semi tiba di kawasan itu,\
semua berlarian ke padang.

[272] Menyambung desah luka selar hingga ke gunung-gunung,\
secepat kilat menuju kebun.

[273] Yang dicari hanya air yang mengalir,\
sama saja bibir luka dan bibir kali.

[274] Ada yang melihat bunga sedap malam lalu menyangka malam,\
ada pula yang menyebut sunbul kalajengking.

[275] Selar duka disangka taman bertabur mawar,\
sungai darah disangka bunga arguwan.

[276] Masing-masing menyusuri tepi kebun,\
tulip yang dipetik: luka selar sendiri.

[277] Tak seorang tahu nikmatnya taman,\
derita karena si pencuri hati telah merampas semuanya.

[278] Tak tahu apa itu pohon delima berbunga:\
api yang menumbuhkan, ataukah taman mawar?

[279] Mawar tertawakah, arguwan menangiskah?\
Anak-anak pohon itu menangis darahkah?

[280] Rintih ini dari bulbul atau dari mawar?\
Sunbulkah yang membuat hati kusut?

[281] Kenapa anak sungai dirantai?\
Tak juga diam; oleh siapa hatinya disakiti?

[282] Siapa yang menjerumuskan cemara ke dalam hasrat?\
Kenapa kuau tak dinaungi di bawah sayap?

[283] Apa gerangan derita narsis hingga jatuh sakit?\
Tak sudikah sang kekasih menatap wajahnya?

[284] Api yang turun karena hasrat,\
atau mawar yang tumbuh karena keluh kesah?

[285] Tak seorang bisa membedakan tanah dan langit,\
mata tak dapat memilah bintang dan taman mawar.

[286] Laksana Majnun, ke mana-mana mengembara,\
tapi mengembara serampangan belaka.

[287] Kiaskan setiap musim dengan musim semi itu;\
jangan suruh aku menuturkan musim gugurnya, takutlah!

## Peristiwa Ganjil {.judul-bagian}

[288] Suatu malam di tengah kaum itu\
tampak kejadian yang sangat ganjil.

[289] Malam itu lahir seribu takdir,\
udara dan benda-benda langit penuh kengerian.

[290] Falak-falak saling bertubrukan,\
malaikat ada yang menangis, ada yang tertawa.

[291] Seribu rindu dan riang, seribu takut,\
lonceng gereja, genderang, dan seruan "Ya Hu!"

[292] Gemuruh di atap langit,\
gempa di permukaan bumi.

[293] Kadang gelap berlapis-lapis,\
kadang cahaya tercurah di segala penjuru.

[294] Daun dan pohon semua bersujud,\
sungai-sungai lebur oleh takjub lalu mengalir.

[295] Kadang muncul seribu ancaman,\
kadang takut dan harap berdebur berombak.

[296] Bintang-bintang bertemu dalam konjungsi,\
hujan sukacita, lalu hujan es bencana.

[297] Dalam gelap banyak suara menyeramkan,\
seruan lantang orang-orang yang dikenal.

[298] Gelisah itu menular pada semua orang,\
riang hati hanya perkara anggapan.

[299] Langit bergemuruh, dum, dum, oleh suara,\
bumi raib linglung oleh peristiwa.

## Lahirnya Jelita dan Asmara {.judul-bagian}

[300] Malam itu dua anak bangsawan\
menjejakkan kaki di istana dunia.

[301] Seketika merekahlah fajar harapan,\
terbit bulan, terbit pula mentari.

[302] Rupanya penyebab semua itu dua raja kecil ini,\
masing-masing menunggang surya dan bulan.

[303] Yang satu anak perempuan berdada melati,\
yang satu anak lelaki berparas Al-Masih.

[304] Kabilah pun paham duduk perkara,\
semua mendengar kabar dua jiwa yang ditimpa cobaan.

[305] Anak perempuan itu dinamai Jelita,\
anak lelaki pilihan itu, Asmara yang tak bahagia.

[306] Kemudian ada yang memanggil Jelita, Laila,\
ada yang Syirin, ada yang Adzra.

[307] Ada yang menamai Asmara, Majnun,\
ada yang Wamiq, ada yang Farhad.

[308] Lalu kamus itu berubah rupa:\
Asmara dipanggil Laila, Jelita dipanggil Majnun.

[309] Setiap saat takdir membongkar jimat,\
menukar nama dengan nama lain.

[310] Selagi keduanya masih bayi tanpa riwayat,\
langit berputar hendak menghapus nama.

[311] Agar termasyhur justru karena tanpa nama,\
dan kelak hilang diri menjadi kebiasaan.

## Pertunangan {.judul-bagian}

[312] Sebuah perjamuan indah digelar,\
para pemuka kabilah datang semua.

[313] Diputuskan: dua bulan ini,\
mau tak mau, menjadi milik satu sama lain.

[314] Ayah keduanya akan dibujuk rela,\
dan begitulah doa-doa dipanjatkan.

[315] Takdirlah yang meletakkan dasar keputusan itu,\
majelis pun bubar tanpa kericuhan.

## Masa Kecil Asmara, atau Cara Asmara Dibesarkan {.judul-bagian}

[316] Asmara mulai menggeliat dan meronta,\
terbelit bedong kegelisahan.

[317] Langit yang sarat bencana\
membuatkan buaian istirahat dari keranda.

[318] Agar mata si bayi terbiasa lelap,\
sang pengasuh melantunkan syair ini:

[319] Bulanku, tidurlah, tidurlah, agar malam ini\
seruan "Ya Rabb" bersarang di telingamu.\
[320] Walau belum terang apa yang dituju,\
begitulah agaknya putusan bintang:\
*di tusuk sate kezaliman, kau kelak jadi kebab.*

[321] Kuncupku, tidurlah, hanya sebentar waktumu,\
niat langit terhadapmu sungguh jahat;\
[322] sebab langit bengis tak kenal ampun,\
kalaupun bermurah, cuma sangkaan belaka.\
[323] *Aku takut kelak kau hancur luluh.*

Narsis Asmara, lelaplah dengan manja,\
[324] bersimpuhlah di ujung jubah takdir, memohonlah;\
bukalah mata jiwa dengan seribu cemas,\
[325] berjaga-jagalah dari ujung bala:\
*kau kelak jadi mainan pusaran nasib.*

[326] Mari, rehatlah di buaian yang damai,\
beberapa malam saja, bersantailah;\
[327] pikirkan akhir, kasihanilah diri,\
biasakan minum darah sebagai ganti susu:\
[328] *kau kelak jadi peneguk cawan celaan.*

Tidurlah dalam buaian, wahai berdada melati,\
[329] langit yang berputar tak akan tetap begini;\
bintang tak beredar dengan satu keadaan,\
[330] lihatlah, sebentar lagi apa yang diperbuat kepadamu:\
*kau kelak jadi kincir di banjir duka.*

[331] Jangan biasakan diri berjaga,\
kalau ada pertolongan, datangnya dari tidur;\
[332] algojo langit ini menyodorkan racun,\
hingga kerjamu meraung seperti Galib:\
[333] *kau kelak jadi rebab di perjamuan pedih.*

[334] Dalam buaian, si molek berdada melati itu\
laksana mentari terang di dalam bulan sabit.

[335] Setiap kali buaian diayun,\
bergetar laksana air raksa.

[336] Bintang harapan itu gemetar,\
seperti surya di dalam cermin,

[337] laksana bulan Nakhsyab di dasar sumur,\
atau surya yang singgah di gugus Kalajengking.

[338] Bila di buaian hatinya kesal,\
bagai pedang bergetar dalam sarung.

[339] Selagi si molek terlelap di buaian,\
ruh di dalam tubuh beroleh tenaga.

[340] Kijang kecil itu serupa cahaya mata,\
tempat bersemayamnya sudut alis.

[341] Atau bocah itu Isa rupanya,\
buaian mulia itu mihrab baginya.

[342] Namun tetap saja muak oleh duka,\
seperti si sakit di atas kasur empuk.

[343] Tak pernah tenang dalam satu keadaan,\
tubuh bergetar laksana nyala api.

[344] Sesekali, bila lunglai benar,\
orang bilang: sedang mabuk kantuk.

[345] Pendek kata, api bertubuh mawar itu\
melewatkan hari-hari dengan guncangan begitu.

## Masa Kecil Jelita {.judul-bagian}

[346] Takdir yang semrawut\
mengayun buaian Jelita pula.

[347] Langit yang lalim\
membiasakan Jelita pada ayunan terbalik:

[348] di tengah sedih, nikmat gembira;\
di tengah riang, hajat tak tercapai.

[349] Pada lahirnya penuh hormat,\
padahal tidur diharamkan bagi mata.

[350] Karena raja kecil yang tega itu tak lain fitnah,\
takdir ingin fitnah itu terjaga.

[351] Mari tinggalkan rincian,\
agar tak menimbulkan jemu.

[352] Tak elok bila kawan-kawan\
sejak pandangan pertama sudah tercengang melongo.

## Permulaan Segala Perkara {.judul-bagian}

[353] Bulan dan tahun berlalu begitu,\
tibalah waktu duka tak lagi lalai.

[354] Para pemuka kabilah berkumpul,\
menyalakan lilin bagi keputusan yang bernas:

[355] bahwa dua jenaka yang cerdas ini\
harus menjadi purnama sempurna dengan menuntut ilmu.

[356] Modal segala cita-cita adalah kepandaian;\
tunduk kepala, itulah mahkota di kepala.

[357] Karena bersahabat dengan bulan,\
setiap orang mendengar dan mengenal bintang Suha.

## Teman Seperguruan {.judul-bagian}

[358] Dua biji badam masuk ke dalam satu kulit,\
berangkat ke pesantren bernama Adab.

[359] Dua bocah laksana dua larik menjadi satu bait,\
menjadi pembuka bagi makna yang lembut.

[360] Dua mata penyihir merapal mantra,\
di hadapan tatapan, alis menjadi rehal.

[361] Seperti pena: dua lidah, satu hati,\
keduanya menuturkan satu bahasan.

[362] Dua lilin kapur barus menjadi satu cahaya,\
menjadikan tempat itu istana kristal.

[363] Pesantren menjadi hayula di antara keduanya,\
dua makna masuk ke dalam satu rupa.

[364] Dua kuntum mawar pada satu dahan\
saling menjadi bulbul.

[365] Keduanya bertaut satu sama lain,\
di dalam kuntum itu mengikat sumpah darah.

[366] Sesekali, dalam membuat perumpamaan,\
surya dan bulan dijadikan cermin.

[367] Keduanya duduk di satu tempat,\
bayangan dan yang berbayang masuk ke satu cermin.

[368] Pesantren itu keputren kesatuan,\
di sana perpisahan dan pertemuan berkumpul.

[369] Saling menatap dengan mata dahaga,\
bidadari dan pelayan muda di dalam Firdaus.

[370] Biarlah bulan dan surya di langit berkarib,\
laron dan nyala api di rongga lentera.

[371] Di antara keduanya, lungsin dan pakan pertemuan:\
tatap cermat yang terpukau, terpukau.

[372] Pelajarannya melulu rida dan pasrah,\
Mulla Gila guru pembimbingnya.

## Tentang Mulla Gila {.judul-bagian}

[373] Tapi Gila macam apa! Syaikh yang sempurna,\
mufti bagi para perancang yang berakal.

[374] Pengembara sepi di lembah kemustahilan,\
lepas dari belenggu kemungkinan.

[375] Malam kebodohan dijadikan pagi,\
semua larangan dijadikan halal.

[376] Masa bodoh! Tak pernah memanjat dahan pikir,\
jalannya tak pernah tersesat ke padang batu pikiran.

[377] Perbuatannya jauh dari "mengapa" dan "bagaimana",\
dimaafkan dalam agama, dimaafkan dalam kufur.

[378] Di hadapannya raja dan pengemis sama saja,\
omongan akal cuma ocehan dan aib.

[379] Seorang diri, raja yang perkasa,\
atas titahnya segala indra berlalu.

[380] Tak ada urusan dengan sangka dan ragu,\
tak tersisa satu syak pun tentang falak.

[381] Kepada Allah pun kalau membangkang,\
tak gentar, api pun tak membakar.

[382] Sultan lain, berdiri sendiri,\
prajuritnya bertelanjang semua.

[383] Ada usul yang cocok dengan hujahnya,\
perkara remeh-temeh menempel pada kiasnya.

[384] Kalau berdebat, seisi jagat dibungkam,\
dengan satu kata, orang pintar pun dibuat paham.

[385] Ibnu Malik dibenamkan ke tanah,\
seribu cela ditemukan pada Fakhruddin.

[386] Melihat imamah Imad,\
dijulukinya "Kiai Lobak".

[387] Di perjamuannya Mirza Jan pemetik kobuz,\
Fakhr-i Jurjan cuma tukang jamu.

[388] Syaikhul Islam di negeri bala,\
atas ucapannya tak berlaku hukum apa pun.

[389] Iblis pengemis buta yang menadah sedekahnya,\
Aristoteles kepala badut istananya.

## Jelita Jatuh Cinta kepada Asmara {.judul-bagian}

[390] Atas putusan takdir yang tak berpihak,\
Jelita kasmaran pada rupa Asmara.

[391] Jelita penghias alam, dengan seribu nyawa,\
menjadi Zulaikha bagi Yusuf itu.

[392] Seharusnya dicintai, malah mencintai;\
seharusnya Adzra, malah jadi Wamiq.

[393] Pipi Asmara, dan cinta pada pipi itu,\
menjadikan pipi Jelita taman mawar liar.

[394] Kalau membaca *alif*, teringat perawakan Asmara,\
desah dan jeritnya naik hingga ke Arasy.

[395] Kalau membaca *jim*, huruf itu jadi *dal*, penunjuk ke ikal rambut;\
dari satu titik saja, seribu hal terbaca.

[396] Huruf *ra* ditakuti seperti belati,\
huruf *mim* tak mau tinggal di bibir.

[397] Gerigi huruf *sin* yang berwajah gergaji\
menebang pohon muda umurnya.

[398] Juz Al-Qur'an di tangan bak purnama bercahaya,\
tulisan berhamburan laksana bintik di pipi.

[399] Anak-anak lain tekun pada pelajaran,\
keduanya tekun berkasih-kasihan.

## Keadaan Cinta Keduanya {.judul-bagian}

[400] Ayo, bayangkan taman mawar itu:\
laronnya mawar, pelitanya bulbul.

[401] Bibir delima yang manis menghangatkan darah Asmara,\
Syirin memberi nyawa kepada Farhad.

[402] Si bibir gula tampak seperti burung nuri,\
yang dicintai, tapi berperangai pencinta.

[403] Laila-nya majnun pada bayangan Qais,\
lilinnya merintih, hati berdarah, demi laron.

[404] Sesekali sang kekasih mengurai kuncir,\
pipi itu menyelar dada kecupan semerah mawar.

[405] Sesekali bibir delima terbuka memulai bincang,\
kelopak mawar pun robek oleh rindu.

[406] Suci tak membiarkan mulut terbuka,\
namun permata rahasia tetap saja kentara.

[407] Tutur Jelita: keakraban dan kasih;\
kerja Asmara: takjub di dalam takjub.

[408] Pada lahirnya Asmara yang mulia diam,\
namun laksana pusaran, sekeliling dihirup habis.

[409] Cinta atau tidak, tak seorang tahu;\
tapi tak bisa juga disebut tak tahu apa-apa.

[410] Diam: tak mendesah, tak meratap;\
terpana: tak kenal jalan, tak kenal aturan.

[411] Si molek itu serupa cermin belaka,\
tanpa nyawa, tanpa lidah, rupa yang lain dari yang lain.

[412] Makin menatap, makin diserap Jelita yang mulia,\
mentari Jelita itu ditarik ke dalam diri.

[413] Bulan Nakhsyab itu, laksana surya,\
seluruhnya tatapan: tanpa telinga, tanpa bibir.

[414] Jelita menyala-nyala bagai api;\
Allah yang tahu, siapa bakal terbakar.

[415] Jelita lunglai seperti air mata sendiri,\
tiap desah melingkar di leher bagai kalung pusaran.

[416] Laksana botol kaca, menunduk kepada Asmara;\
yang ini seolah dalam botol kaca, yang itu dalam kendi tanah.

[417] Hati yang ini berdarah, kentara nyata;\
yang itu, pada lahirnya, sebongkah batu.

[418] Dambaan Jelita di balik batas mungkin,\
maksud hati Asmara tersembunyi.

[419] Seperti kijang: elok jalannya, liar perangainya,\
tak sudi mengejar-ngejar siapa pun.

[420] Di hadapan si penyihir hati itu,\
Jelita koyak berkeping laksana jaring.

[421] Sesekali Asmara melirik sayu,\
si jenaka ini pun resah oleh takjub.

[422] Di tangan tatapan tergenggam pedang cemburu,\
takjub membuka jalan bagi prasangka.

[423] Kata Jelita, "Masa, si biang onar langit ini\
tak sudi pada aku yang jadi debu di kakinya?

[424] Pasti ada kekasih lain yang dirindu;\
buruan macam apa yang diincar?

[425] Kalau dambaannya purnama, biar aku jadi malam;\
kalau cintanya langit, biar aku jadi bintang.

[426] Berhala mana yang dikhayalkan?\
Tak bisakah kuncirku jadi zunnar baginya?

[427] Biar aku jadi brahmana di depan berhala itu,\
melayani sang kekasih pujaannya."

[428] Lalu bulan itu merenung dan berkata,\
"Naudzubillah, omongan apa ini!

[429] Adakah di falak bintang semacam itu,\
sampai surya mengadukan hajat kepada bulan?

[430] Aku ini bulan; kalau aku saja tak dipedulikan,\
apalagi Suha, bintang kecil itu?"

[431] Namun Jelita penghias alam\
tak pernah membeberkan kisah itu.

[432] Bisik-bisik batin itu dipendam,\
tak sampai menyakiti si wajah rembulan.

[433] Namanya memang Jelita tanpa cela,\
tapi apa gerangan yang tak ternilai itu, apa?

## Lukisan Jelita {.judul-bagian}

[434] Pipi tulip, kuncir hitam,\
kuntum mawar di tengah rumpun sunbul.

[435] Cermin dada: samudra air raksa,\
untaian mutiara di sana menjadi pusaran.

[436] Gigi dan mulut, tak syak lagi,\
perbendaharaan gaib penuh mutiara dan permata.

[437] Mukjizat hanya milik mulut itu:\
satu titik, sekaligus tafsir ayat Nur.

[438] Dagu, bagi yang haus akan takjub,\
cawan perak berisi air hayat.

[439] Mata elang raja itu menakjubkan jiwa,\
kijang pesona, merpati manja.

[440] Lengan yang halus: dahan perak,\
seakan diuleni dari kelopak nesrin.

[441] Jari yang putih: lilin kapur barus,\
inai merah bak kelopak mawar, kuntum cahaya.

[442] Tubuh semampai membangkitkan mahsyar,\
bala langit riang karena perawakan itu.

[443] Gerak-gerik: fitnah hari kiamat,\
gerai rambut: pertanda fitnah itu.

[444] Delima dan mutiara haus akan sepatah kata,\
padahal bibir yakut itu sendiri pandai bertutur.

[445] Alis menghunus pedang ke arah rambut,\
rantai pun terbelah ke dua sisi.

[446] Tatap sayu: musuh nyawa;\
gerai hitam: lawan iman.

[447] Dada yang bening, bercahaya, putih bersih,\
tanpa bual, serupa tiang fajar.

[448] Leher: cemara perak di bibir kali,\
seakan cahaya bulan di Selat Bosporus.

[449] Cuping telinga laksana cahaya pagi,\
mentari menjadi anting permata malam.

[450] Dengan cincin panah bertatah permata, tangan itu\
mematahkan cengkeram surya.

[451] Pipi: pagi hari raya harapan;\
pemerah pipi: darah mata surya.

[452] Lengan: Kautsar yang abadi;\
cincin: permata murni.

[453] Kartika di falak dan bintang-bintang lain\
menjadi kalung mutiara di leher.

[454] Gerai rambut: perbendaharaan ambar mentah;\
tahi lalat di pipi: budak Hindu penjaga atap.

[455] Buah dada: jeruk taman surga,\
mata mabuk rindu pada jeruk itu.

[456] Ketika peri itu menginai tumit,\
cawan anggur pun bersimpuh di kaki.

[457] Delima bibir: permata penabur gula;\
lilin wajah: cahaya bulan penabur mawar.

[458] Alis membuat pemahaman silau,\
bulu mata tombak yang memburu waham.

[459] Warna pipi: yakut dalam kapas;\
makna mulut: huruf yang tak terucap.

[460] Ruh bibir: permata tutur;\
pipi mawar: surga senyuman.

[461] Mata penyihir itu, pedang di tangan,\
menjaga perbendaharaan negeri manja.

[462] Tahi lalat di sudut mulut\
seolah orang Maghribi pemburu harta karun.

[463] Kalau bulu mata membayang di pipi,\
gemetarlah dari ujung rambut sampai ujung kaki.

[464] Seakan Nizami yang tua, dengan bait ini,\
melukiskan bulu mata dan rambut itu:

[465] *"Rambutnya menyapu jalan si pemburu kecup,*\
*bulu matanya berkata, 'Allah yang memberi.'"*

[466] Bibir delima: nyala api peminum gula;\
pipi mawar: musim semi berselimut mawar.

[467] Dada bening dan leher bercahaya itu:\
lilin kapur barus di hadapan cermin.

[468] Perbendaharaan dada: harta berjimat,\
lukisan Arzhang di dalam cermin.

[469] Bibir manis bak kuntum cahaya,\
laronnya berdengung seperti lebah.

[470] Anak panah tatapan: meteor yang menembus;\
panah kezaliman: takdir yang tepat sasaran.

[471] Yang disegarkan khayal: limpahan ilham;\
yang lunglai oleh tutur: rahasia yang samar.

[472] Jubah semerah mawar: darah merak;\
dalam manjanya, seribu warna terasa.

[473] Kekejamannya membuat negeri Afghan muak,\
tingkah lakunya taman di negeri tebu.

[474] Kerut kening zalimnya: bala bagi harapan;\
sayang kemurahannya: suka ria abadi.

[475] Andai Khidir beroleh obat dari mata itu,\
kegelapan akan tampak sebagai air hayat.

[476] Rambut menjanjikan hati akan bertaut,\
tatapan bersumpah akan perpisahan.

[477] Anak rambut yang kusut di dahi itu\
menorehkan tugra titah membunuh orang-orang yang menderita.

[478] Memungut upeti dari raja negeri manja,\
negeri permohonan dijarah habis.

[479] Gerai rambut menyamun kafilah kesturi,\
di tiap helai dirangkai cakram emas dan perhiasan.

[480] Kuncir: bencana bagi hati dan agama;\
Cina dan Macin tunduk pada titahnya.

[481] Mata hitam dan tarikan alis:\
"Ya Hu" kembar di dalam mihrab.

[482] Tahi lalat hitam: bala bagi harta dan ketenangan,\
pengacau Zanzibar dan Sudan.

[483] Seribu Laila laksana kawanan kijang\
menjadi pengekor bagi bayangan Majnun-nya.

[484] Di rambut itu terikat seribu tali nyawa,\
tersambung pada lungsin dan pakan kelupaan.

[485] Di hadapan wajah mawar itu, banyak jiwa yang arif\
berseru lantang, "Barakallah!"

[486] Sepenuhnya halus dan lembut,\
senantiasa manis dan elok.

[487] Wahai pena, seribu kali barakallah,\
engkau telah mengenal daya pikat Jelita.

[488] Telah kau kenang puji-pujian si wajah rembulan,\
kau lukiskan seluruh gayanya.

[489] Karena tujuanmu bernazam ialah karya,\
menuturkan Asmara pun sebuah kepandaian.

## Lukisan Asmara {.judul-bagian}

[490] Wajah rembulan, kulit sawo matang,\
laksana air keabadian di balik tirai.

[491] Bulu halus di pipi: kilap hijau pada bilah pedang,\
cahaya bulan kelam di musim semi Kashmir.

[492] Di taman duka Asmara, Khidir makna\
meneguk air beracun kehidupan dunia.

[493] Bagi tatapan yang angkuh itu, Jibril pun\
tak layak jadi burung yang setengah tersembelih.

[494] Kerling maut serupa Izrail, bencana nyawa;\
fitnah pun korban bermata tertutup baginya.

[495] Bulu halus di pipi: asap api Namrud;\
bibir delima: Kautsar bercampur anggur.

[496] Seisi jagat tentu binasa\
andai bulu halus itu bukan penawar bagi ular rambut.

[497] Di mata tersimpan tutur Isa,\
sepatah kata saja menghidupkan takdir.

[498] Tatapan mabuk: pedang yang tajam;\
anggurnya: air mata bidadari.

[499] Jambul di bawah kopiah\
ibarat Ismul A'zam tertulis di bulan.

[500] Di tangan pedang, surya penitik darah\
menenggelamkan para syahid dalam cahaya.

[501] Rambut membuat sihir sadar diri,\
kerling berseru, "Kami berlindung kepada Allah!"

[502] Bila tatapan mulai berlaku lalim,\
Isa pun dijadikan mempelai bagi pengantin maut.

[503] Bulu halus di sekitar bibir: cahaya wahyu,\
seakan Injil turun seperti kepada Isa.

[504] Si mata sakit ini, naudzubillah,\
Izrail pun di hadapannya minta ampun.

[505] Tontonlah algojo tatapan itu,\
lihatlah Izrail yang menghadiahkan nyawa.

[506] Bibir yang, bila mengucap kata kasih,\
seperti senja, sudah biasa minum darah.

[507] Bulu mata, sekali bergetar sedikit,\
memamerkan seribu bala tentara.

[508] Ruh tutur yang menambah nyawa itu\
bagi para pencinta bala tak berasal-usul.

[509] Cahaya keelokan tak tertangkap nalar,\
di sisinya matahari cuma segenggam tanah.

[510] Makna mulut: rahasia Lahut;\
tiap janji: fatamorgana Nasut.

[511] Tajalli manja begitu tinggi derajatnya,\
telinga tak mau berkarib dengan seruan "Perlihatkanlah diri-Mu".

[512] Para pencinta memusuhi tampak dan tak tampak,\
bulu mata beradu cakar dengan surya.

[513] Bagi si tak kenal duka itu, darah air mata Yakub\
jadi pemerah pipi pengantin baru dambaan.

[514] Para pendamba senada rintih seruling,\
lagu di majelisnya: *"Lan tarani."*

[515] Burung iman terikat di pelana,\
tali nyawa putus bagai zunnar yang koyak.

[516] Bibir yang merah berfatwa menumpahkan darah akal,\
jiwa takwa dikorbankan bagi tatapan.

[517] Tutur bibir guru bagi bibir pedang manja;\
menepati janji pun, seperti janji, sama zalimnya.

[518] Pedang: merak surga darah;\
gada berbilah enam: lonceng bagi gereja agama.

[519] Bagi kuda hitam langit, kasih Asmara laksana Khusraw;\
bulan sabit menjadi rumah pelana.

[520] Hati-hati tercerai-berai seperti janji Asmara,\
rapuh bagai gelembung air.

[521] Dengan bait ini Nasy'at sang penggubah\
meringkas rincian keelokan Asmara:

[522] *"Langit menjadi lentera bagi lilin wajahnya,*\
*laronnya malaikat, tetapi putus asa."*

[523] Andai langit ini seluruhnya mentari,\
bulan sabit tetap meniru alisnya.

[524] Andai surya cemerlang terbit di dalam gelap,\
barulah serupa wajah dan bulu halusnya.

[525] Andai Zuhrah sehaluan di dalam purnama,\
barulah menyamai tahi lalat di pipinya.

[526] Walau cahaya hitam hancur berkeping,\
tak akan kupakai sebagai kiasan bagi rambut itu.

[527] Sekalipun Isa meneguk air Khidir,\
bulu halus bibir Asmara tetap makna yang lain.

[528] Andai Maryam mengandung Yusuf,\
barulah kembar dengan keelokan Asmara.

[529] Andai kuntum cahaya bernyawa,\
tentu jadi lebah demi mengecup bibirnya.

[530] Andai kufur dan iman menjelma rupa,\
bulu halus itu dijadikan titah yang dipatuhi.

[531] Andai Hulagu beroleh limpahan dari Al-Masih,\
tentu jadi pendoa bagi kerling itu.

[532] Bulu halus beraroma ambar di pipi:\
kafir di dalam Firdaus yang tinggi.

[533] Bukan, bukan! Kuncir di pipi yang suci itu:\
sunbul di tengah lumbung api.

[534] Penyihir kerling itu tanpa tedeng aling-aling;\
Jibril siapa, Isa siapa?

[535] Duka Asmara tak mendamba kelaliman;\
kalau mau, apalah tujuh bangunan langit ini?

[536] Tak diizinkan tatapan menjarah;\
kalau diizinkan, sudah lama agama dan dunia runtuh.

[537] Bila berniat membangkitkan topan duka,\
kasihan pada bocah-bocah air mata.

[538] Andai Nuh duka Asmara berseru, *"La tadzar,"*\
Firaun pun ditenggelamkan ke dalam iman.

[539] Andai Harut tatapan itu memberi isyarat,\
Zulaikha terjerumus ke dalam sumur.

[540] Andai kekafiran ditugasi meruntuhkan agama,\
mata hitam itulah yang memberi izin.

[541] Di hati mana pun lilin dambaan menyala,\
ulat Ayub menjadi laron di sana.

[542] Di pasar kasih Asmara, Yusuf\
berlumur darah seratus penyesalan.

[543] Para peminta-minta, dari ujung kepala sampai kaki,\
menghiasi "tangan putih" dengan mohor Jamsyid.

[544] Pipi: mentari yang membakar,\
surya berkilau di tengah api.

## Jelita Sesekali Datang ke Tempat Menyepi Asmara {.judul-bagian}

[545] Saki, bermurahlah, pikiranku melayang,\
kakiku terikat tali ketakpedulian.

[546] Beri anggur, derita ini tak ada obatnya,\
samudra tutur tak bertepi.

[547] Haruskah samudra jernih ini diam tak berombak?\
Haruskah aku tak berkata? Coba insaflah.

[548] Kalau cahaya anggur kau tahan,\
bulan hati kau sembunyikan di balik awan.

[549] Takutlah pada hati kami yang berkeping,\
jaga sutramu dari percik bara kami.

[550] Di kepalaku samudra hasrat bergolak;\
apa gunanya kata, sekadar sehela napas?

[551] Saki, tolonglah, aku layak dikasihani,\
di pasar bala aku doyan duka.

[552] Aku perlu banyak uang kata-kata\
untuk memborong segala jenis duka.

[553] Kata-kata, tapi tentang mabuk,\
tentang terkapar dan remuk.

[554] Beri anggur, sebab tutur sudah sampai ujung,\
modal duka sudah habis.

[555] Susahnya, baru saja mulai,\
mukadimah rahasia pun belum tertata.

[556] Beri aku anggur, wahai mawar kelembutan,\
dan tanyakan, kisah apa yang kututurkan.

[557] Saki pembawa anggur di majelis makna\
dengan kegembiraan ini mulai menghadiahkan nyawa:

[558] rindu Jelita kian bertambah,\
hari demi hari hati si wajah rembulan makin berdarah.

[559] Derita hati kian menjadi-jadi oleh Asmara,\
seribu pikir dan khayal menjadi kebiasaan.

[560] Keelokan Asmara menambah gelisah,\
kilau dan cahaya Jelita berganti corak.

[561] Keadaan itu membuat tubuh gemetar,\
cermin memang, tapi cermin dari air raksa.

[562] Cawan anggur nyala api direguk sampai puas,\
pipi membara berkilau-kilau.

[563] Pemerah pipi: darah air mata kehampaan;\
bedak putih: putih mata yang menangis.

[564] Nasib hitam karena ikal rambut yang berpilin,\
tidur kusut karena jambul.

[565] Kadang rambut dihamparkan di jalan,\
kadang datang dan pergi laksana angin pagi.

[566] Diam dan tenang itu sulit,\
memilih mengembara pun sulit.

[567] Dipasangnya permainan manja,\
di papan catur duka ditemukannya jebakan.

[568] Seperti Zuhrah, bernyanyi sepanjang malam,\
hingga pagi rintih kecapi pun tak bersisa.

[569] Setiap malam jalan umur digulung,\
muka diusapkan ke tempat menyepi Asmara.

[570] Setiap malam, laksana kunang-kunang,\
menemukan jalan ke taman harapan.

[571] Melihat mata kekasih terlelap,\
belajar menangis dari laron.

[572] Yakni bulbul yang merdu suaranya itu\
merintih dalam diam, diam-diam.

[573] Langkahnya begitu lembut,\
duri pun tak menusuk telapak.

[574] Berjalan seperti bintang tetap,\
seolah beredar bersama falak.

[575] Tak bernapas karena duka, si tanpa nyawa itu\
gemetar bagai gelembung air.

[576] Burung huma keberuntungan itu, seperti kelelawar,\
terbiasa berjalan di malam hari.

[577] Tanpa sungkan berkeliaran di kegelapan,\
seolah makna yang tersembunyi di dalam huruf.

[578] Membentangkan bayang di atas cahaya bulan,\
agar cahaya tak jadi beban bagi sang kekasih.

[579] Tak berjalan di atas kaki:\
"Jangan-jangan bayanganku jatuh dan membangunkan kekasih."

[580] Setelah menghiasi cahaya bulan dengan bayang,\
awan desah dinaikkan tinggi-tinggi.

[581] Nasib sendiri pun tak diinginkan terjaga,\
siapa tahu mengusik tidur kekasih.

[582] Datang dan pergi tanpa suara, tanpa bunyi,\
seolah melancong di dalam hati.

[583] Hati yang luka digulung,\
Zanzibar tampak di dalam cermin.

[584] Dengan sekali desah tersingkap cadar,\
di dalam gelap tampak mentarinya.

[585] Maksudnya menatap wajah\
tanpa sang kekasih sadar ditatap.

[586] Bila sang pembelai hati didapati terjaga,\
lembar permohonan tak dibuka.

[587] Menghibur diri dengan bara duka,\
tampak tersenyum laksana nyala.

[588] Menuturkan dongeng manis-manis,\
berdalih agar kekasih tidur manis.

[589] Ingin kekasih lekas lelap,\
diceritakannya dongeng istana si tupai.

[590] Air mata disembunyikan dengan rambut,\
bercerita tentang kali dan padang rumput.

[591] Bersenandung lagu kegilaan,\
kisah Laila dan Majnun.

[592] Akhirnya, bila si wajah melati tertidur,\
mata Jelita menjadi kijang di taman itu.

[593] Sang bijak itu, laksana Majnun,\
puas dengan sekadar memandang.

[594] Ada makna yang terang di sini:\
Jelita memang kasmaran pada Asmara, tetapi

[595] gemar datang memandang di malam hari;\
manja sudah berganti menjadi permohonan.

## Lukisan Musim Semi {.judul-bagian}

[596] Ridwan surga penciptaan,\
biji mata para ahli penglihatan,

[597] yakni pena berjubah hitam,\
memulai tutur dengan cara begini:

[598] Suatu ketika musim semi penerang alam\
menghadiahkan cawan Nauruz kepada dunia.

[599] Zaman mabuk oleh anggur itu,\
jimat tipu dayanya pun pecah.

[600] Dunia penuh riang gembira,\
mahsyar lukisan serba ajaib.

[601] Tetumbuhan bergolak laksana surga,\
mawar dan tulip meneguk seteguk demi seteguk.

[602] Di tiap lorong musim semi pirus,\
di tiap kuntum jubah Nauruz.

[603] Entah anggur apa yang diminumkan surya,\
bocah-bocah padang rumput jadi Jamsyid semua.

[604] Ganti hujan, tercurah anggur bening,\
di kepala padang rumput berputar pusaran.

[605] Awan yang baru mengembang, laksana kijang,\
menyusu pada udara semerbak sunbul.

[606] Udara sedemikian lembap\
hingga angin sepoi seiring langkah dengan banjir.

[607] Anyelir beroleh limpahan dari awan,\
sunbul disiram harum mawar.

[608] Mata air zamrud bergolak,\
kubah langit peridot terpantul di dalamnya.

[609] Kilat tertawa semanis itu\
hingga bulan bersumpah atas namanya.

[610] Cahaya bulan mengalirkan sungai susu,\
air raksa berkocak dengan air perak.

[611] Lembap membuat orang sayu mengantuk,\
bulu mata jadi lebah bagi madu tidur.

[612] Udara penabur mawar memberi limpahan,\
buah labu pahit pun meneteskan gulali mawar.

[613] Musim semi yang riuh memberi riang,\
urat awan dijadikan senar tanbur.

[614] Setelah udara menyetel kelembapan,\
burung nyala api tak lagi terbang.

[615] Di udara lembap bercat narsis ini,\
mana bisa warna mawar pudar?

[616] Udara membusungkan dada seperti elang,\
siapa sanggup menerbangkan burung tidur?

[617] Anggur kegilaan merampas akal,\
kaki kebun pun terikat pada kali.

[618] Ketika Nauruz membasahi udara,\
rumput di tanah jadi bulu nuri.

[619] Rajawali langit turun ke sarang,\
kuntum mawar menjadi sarang bagi huma.

[620] Daya tumbuh begitu perkasa\
hingga ruh-ruh iri pada anak pohon.

[621] Tiap sulur anggur yang berbaring di buaian para-para\
mengulurkan tangan ke susu awan.

[622] Tiap mutiara yang tercurah dari awan\
membuat bocah-bocah rumput girang tertawa.

[623] Awan menjadikan kebun bendahara manisan,\
burung nuri beterbangan seperti lebah di atas gula.

[624] Angin taman laksana kesturi,\
mimisan pohon arguwan tak henti-henti.

[625] Rantai kegilaan bersambung-sambung,\
ombak mawar bercampur dengan anak sungai.

[626] Banjir bulan April bergolak sedemikian rupa\
hingga batu dan beling jadi mutiara yang bergulir.

[627] Dunia berlubang-lubang seperti pedupaan,\
tiap mata air jadi kendi air mawar yang indah.

[628] Langit mengharumkan hidung,\
kilat bersin berulang-ulang.

[629] Bumi ditimpa tumbuh dan subur\
hingga menjangkau langit keempat.

[630] Tiap gundukan tanah menjadi Badakhsyan,\
sungai delima meluap ke kebun.

[631] Oleh limpahan itu batu dan cadas\
berkilau serupa sutra semerah mawar.

[632] Tiap kuntum yang muncul dari taman mawar\
membuka rahasia bumi dan langit.

[633] Tanduk kijang berubah menjadi dahan mawar,\
cemara pemikat hati menghasilkan kantong kesturi.

[634] Taman mawar membawa kabar surga,\
duri di pagar menandingi pohon Tuba.

[635] Angin yang elok menjadi Israfil,\
menghidupkan kebangkitan bumi.

[636] Kuntum girang laksana bulbul,\
membuka omong dan celoteh kepada mawar.

[637] Bunga pansi si plin-plan bergolak,\
pena dan surat pun terdiam.

[638] Narsis membuka cerita tentang anggur dan seruling,\
menabur mutiara kabar mahkota Kay.

[639] Pohon cinar yang congkak mengangkat tangan,\
mengucap sepatah kata yang berisi api.

[640] Tulip menyelar hati oleh kabar itu,\
pelita mawar pun kalut.

[641] Bumi dan langit penuh ratap dan rintih,\
namun perbincangan itu tak juga terungkap.

[642] Iris diwarnai oleh melati,\
darah menetes dari pipi melati.

[643] Mawar dan anyelir diam-diam berciuman,\
sunbul menjamah narsis.

[644] Di taman mawar terdengar bisik-bisik,\
semua dibocorkan kepada angin sepoi.

## Lukisan Pagi {.judul-bagian}

[645] Suatu dini hari, jejak pagi yang menghadiahkan nyawa\
menghidupkan kebun.

[646] Fajar menjadi pohon kurma Maryam,\
rupanya telah lahir Al-Masih yang bernapas harum.

[647] Surya bertajalli sedemikian rupa\
hingga disangka Musa naik ke Tur.

[648] Mentari memenuhi pagi dengan cahaya,\
Gunung Kristal menjadi tempat bagi Ali.

[649] Kunci sumur dan penjara terbuka,\
Yusuf kembali menjadi sultan Mesir.

[650] Purnama meletakkan pondasi pagi,\
singgasana Balqis terpandang oleh Jam.

[651] Haidar menghunus lagi Zulfikar,\
Khaibar ditaklukkan dengan pedang.

[652] Pagi yang riang menjadi tempat surya,\
Adam masuk surga sekali lagi.

[653] Khidir makna membuka jalan gaib,\
dunia menjadi cermin Iskandar.

[654] Surya memuliakan Ismail,\
sumur Zamzam mencium kakinya.

[655] Pagi yang memikat menjadi tempat mentari,\
api menjadi taman mawar bagi Ibrahim.

[656] Mentari menjadikan pagi kapas yang dihambur,\
setiap bagian zaman berpakaian mawar.

[657] Syirin menatap sungai susu,\
menyodorkan cawan delima kepada para pencinta.

[658] Sang Aziz yang didamba menampakkan wajah,\
tapi mata Yakub sudah telanjur putih.

## Jelita dan Asmara Keluar Bertamasya ke Taman Makna {.judul-bagian}

[659] Oleh pengaruh udara, pada Asmara yang mulia\
mata air rindu bergolak.

[660] Jelita pun dirasuk keadaan lain,\
keduanya berniat bertamasya.

[661] Dua pelita terang itu\
singgah di Taman Makna.

[662] Taman Makna, tempat yang\
airnya ungu violet, tanahnya ambar.

[663] Kebun surga itu, tanah yang riang itu,\
tanah memang, tapi tanah Adam.

[664] Pohon-pohon di kebun itu Sidrah semua,\
sebutir prem mentah di sana: langit hijau.

[665] Rerumputan yang hijau: umur abadi;\
embun: bintang; kuntum: mentari.

[666] Taman mawarnya samudra cahaya merah,\
mutiara jernihnya delima layak raja.

[667] Tiap gundukan tanahnya Tur seratus tajalli,\
di sana tak ada ucapan *"Lan tarani."*

[668] Pelitanya yang benderang: cahaya wahyu;\
hamparan rumputnya: sayap Jibril.

[669] Bunga sedap malam: pelita iman di malam hari;\
kelopak mawar musim gugur: permata nyawa.

[670] Kembang emasnya memberi harga pada laut dan tambang,\
narsisnya kenang-kenangan dari surga.

[671] Mentari sebatang pohon, cahayanya pagi,\
burung-burung ruh bersarang di sana.

[672] Daun pepohonan: sayap agung malaikat,\
serupa bunga delima yang merekah.

[673] Menyebut padang mawar itu "selendang Kashmir hijau berbunga",\
alangkah rendahnya ungkapan itu.

[674] Mirrikh penjaga taman,\
bunga matahari di sana purnama benderang.

[675] Pohon dan buah, apel dan jeruk,\
merjan dan akik bertimbun-timbun.

[676] Pelataran padang dihampar bintang,\
intan lebih banyak dari kerikil.

[677] Tiap pecahan batu yang kering\
bintang penunjuk jalan bagi kawan-kawan.

[678] Senantiasa berkhidmat pada taman itu,\
dupa Maryam adalah bunga Isa.

[679] Pansi si plin-plan di padang dan gurun:\
tempat bernaung banyak pemuda pemikat yang baru berjanggut tipis.

[680] Seperti taman mawar khayal,\
kuntum-kuntum mawar: bulbul bersayap merah.

[681] Khidir padang rumput: laut zamrud;\
petak di tengahnya: sampan peridot.

[682] Banyak yang elok laksana pohon pistachio\
menjadikan bulu mata sapu di sana.

[683] Ketika pelita mawar menyala terang,\
anggur menjadi minyak yang benderang.

[684] Ketika dedalu Majnun mengurai rambut,\
Laila pun terikat pada padang.

[685] Ketika cemara memamerkan perawakan,\
kiamat datang bersimpuh di kaki.

[686] Bunga anemon mabuk kegilaan,\
mengejek cawan yang berkilau.

[687] Pohon arguwan yang baru tumbuh\
berbuah api masa muda.

[688] Sulur anggur menghiasi tongkat polo dengan permata,\
di sana menjadi komandan, dahi mencium tanah.

[689] Anggur hitam: budak Hindu penjaga atap,\
namun tempatnya empat kubah benda langit.

[690] Persik semerah mawar putih sudah terkenal,\
dijuluki "pipi kekasih".

[691] Pir yang sedap berair\
mengangkut air ke kebun dengan tangan sendiri.

[692] Tulip di kebun itu seluruhnya\
penjaga kebun khusus bermahkota merah.

[693] Pohon prem, hijau segar oleh riang,\
tiap buahnya burung nuri bertutur gula.

[694] Aprikot: warna delima bibir Laila;\
cawan anggur jadi majnun karena membayangkannya.

[695] Tiap ceri: anting yakut,\
santapan bagi mata pencinta yang menonton.

[696] Tiap rerumputan: musim semi Kashmir,\
tanpa musim panas dan dingin, seperti lukisan.

[697] Mata penyihir tak terhingga banyaknya\
menjadi kijang di hamparan violet itu.

[698] Prem hitam: air hayat,\
atau permata Sailan yang tiada banding.

[699] Sunbul: kuncir di pipi mawar liar,\
anyelir menjadi sisirnya.

[700] Elang raja tak terbiasa berburu;\
kalaupun berburu, merak yang menangkap kuau.

[701] Burung hudhud bermahkota di kepala seperti Jam,\
tentara perinya ayam hutan dan puyuh.

[702] Kebun nyala itu menjadi padang\
yang tak butuh surya dan bulan langit.

[703] Yang hatinya terbakar: kembang api cahaya bulan;\
yang permatanya bercahaya: kunang-kunang.

## Kolam Limpahan {.judul-bagian}

[704] Sebuah kolam yang berberkah mengairi tempat itu,\
namanya Limpahan.

[705] Rupanya Tuhan menyirami taman itu\
dengan air perak seluruhnya.

[706] Tak syak lagi, kolam yang terang itu\
cermin keelokan sang saksi gaib.

[707] Di dalamnya tersembunyi keadaan beraneka:\
samudra sifat dan permata zat.

[708] Tiap kerang di sana perbendaharaan cahaya,\
laksana kelopak mata bidadari yang benderang.

[709] Pada cermin perak kolam itu tiap saat\
terlukis alam yang lain.

[710] Air Khidir membanjiri tempat suci itu,\
tanah yang mulia itu jadi hijau.

[711] Anggur murni datang ke air itu,\
lalu karena iri menjadi api belaka.

[712] Langit tenggelam dan tercengang di kolam itu,\
surya dan bulan laksana Yunus dan ikan.

[713] Andai Tasnim melihat airnya,\
air muka Tasnim tertumpah, mengemis-ngemis.

[714] Walhasil, taman mawar yang melapangkan dada itu\
serupa tabiat penyair yang suci.

## Tentang Sabda, Penjamu Taman Makna {.judul-bagian}

[715] Seorang tua berjiwa muda dan cerdik\
menjadi penjamu di tempat itu.

[716] Namanya Sabda, mulia pribadinya,\
umurnya lebih tua dari falak.

[717] Paham hakikat Jelita dan Asmara,\
tahu watak panas dan dingin.

[718] Pikirannya permata malam makrifat,\
teman rahasia batin kekasih dan yang dikasihi.

[719] Masalah sekaligus kitab yang diturunkan,\
mukjizat sekaligus nabi yang diutus.

[720] Dalam menyesatkan dan menunjuki, jarang tandingannya,\
dengan segala cara mampu menyempitkan dan melapangkan.

[721] Bila berkehendak, tanpa senjata dan baju zirah,\
damai dijadikannya penyamun perang.

[722] Bila bermurah dan memberi,\
maut dan hidup dijadikannya nyawa dan kekasih.

[723] Kadang menjadi raksasa, kadang peri,\
kadang makhluk laut, kadang makhluk darat.

[724] Bagi yang tersesat menjadi Khidir penunjuk jalan,\
bagi yang sebatang kara menjadi raja.

[725] Kadang alim, kadang penyair,\
kadang zahid, kadang tukang sihir.

[726] Putus asa dan rindu tunduk pada titahnya,\
harap dan pinta teraniaya di sisinya.

[727] Atas perintahnya mengalir tiada henti\
kadang air mata suka, kadang air mata duka.

[728] Yang berkabung dibuat riang,\
yang sadar dibuat mabuk sayu.

[729] Kecerdasannya tak terlukiskan,\
maknanya tak seorang pun tahu.

[730] Seluruh isi alam butuh kepada Sabda,\
oleh Sabda manusia mendapat hidup.

[731] Penerang keelokan wajah-wajah rembulan,\
debu di mata para pemburu hajat.

[732] Bagi yang riang, kawan akrab yang harum napasnya;\
bagi yang sakit, pakaian berkabung.

[733] Menghibur sesuai pikiran,\
bertajalli sesuai cermin.

[734] Bila berkehendak, tanpa berutang budi,\
seketika lawan dijadikan sebab bagi lawannya.

[735] Kadang tertawan di sumur derita,\
kadang menjadi Aziz di Mesir kejayaan.

[736] Bagi martabat Sabda, pangkat ini terlalu rendah,\
sifat-sifatnya melampaui dusta.

## Pembahasan Lain {.judul-bagian}

[737] Wahai pencari permata malam makna,\
dengarkan tuturku dengan insaf.

[738] Satu dua pembahasan tentang makna ini\
membuat tutur jadi panjang.

[739] Beberapa orang gila berkedok akal\
berkata: tak ada lagi tema baru;

[740] seakan para penutur terdahulu\
sudah mengucapkan semua di zaman dulu,

[741] tak seorang pun tersisa kecakapan,\
kerja penyair tinggal mencuri.

[742] "Memangnya masih ada kata yang belum terucap?\
Masih ada omongan yang belum dibilang?"

[743] Ini sebenarnya tak layak dijawab,\
tak layak dibelanjai permata tutur,

[744] tapi sebagian tukang omong kosong,\
sisa-sisa kaum setan anak setan,

[745] menurut sangkaan sendiri penyair zaman ini,\
duduk di sajadah kedai kopi,

[746] pecandu yang mengigau dalam tidur sial,\
di tengah api laksana feniks,

[747] saling menjilat satu sama lain,\
berkata, "Memang begitu, Juragan.

[748] Di mana kini penutur negeri Rum,\
Nermi, si Odabaşı tua almarhum?

[749] Atau Mihneti yang ditimpa bala,\
Ayni Çelebi, si cahaya mata?

[750] Sayang, syair-syair pun dibawa pergi,\
tinggal kami ini, sisa-sisa pedang.

[751] Hargailah kami, kawan-kawan,\
ahli bakat sudah langka."

[752] Demi saling menjual syair,\
tema baru pun diingkari.

[753] Buku kumpulan kecil di tangan, tempat tinta di pinggang,\
di toko, di jalan, di setiap kampung,

[754] menggeleng-geleng keheranan,\
berkata, "Si Sabit tua itu, tiada duanya!"

[755] Karena tak sanggup sendiri,\
pagi nazam hendak dijadikan malam gulita.

## Pelengkap Tutur {.judul-bagian}

[756] Para penyair gadungan dari kalangan juru tulis,\
yang kebanyakan tuan-tuan kantor,

[757] berjubah wol, sarat kebanggaan,\
pembuat ombak di samudra istilah,

[758] yang memandang cita-cita teragung:\
menghafal *Munsyaat* Ragıb.

[759] Lalu satu dua bocah laki-laki yang elok,\
tanbur, anggur, dan beberapa diwan.

[760] Bila jemu bekerja,\
katanya, inilah sumber tenaga.

[761] Jangan sebut doyan bocah; bukankah maksudnya begitu?\
Bukankah kepenyairan semacam itu hambar tanpa garam?

[762] Kaum santri softa jangan harap jadi penyair;\
golongan itu tak perlu kubahas.

[763] Mulla yang berbekal contoh-contoh *Talkhis*\
mengaku-ngaku bernazam: klaim palsu.

[764] Di antara orang kota kita, sebagian kawan\
bergegas menuju arah kepandaian:

[765] belajar dari Işık dan Torani,\
mengutip dari Revani.

[766] Seperti lalat, dengan sedikit omong kosong\
hendak meremehkan madu nazam.

[767] Maksudnya, tutur bertema segar\
sudah langka, seperti bakat yang berirama.

## Pembahasan Pertama: Tentang Wujud Tutur {.judul-bagian}

[768] Wahai pemahami kehalusan makna yang suci,\
dengarlah apa kata pena yang gesit ini.

[769] Bila diandaikan dan dihitung di alam luar,\
tempat-tempat penampakan dan nama-nama laksana kembar.

[770] Sebelum menghidupkan dan mematikan,\
Tuhan Yang Mahamulia sudah Al-Muhyi.

[771] Namun satu menyusul yang lain:\
penciptaan dengan makhluk, dan nama Sang Pencipta.

[772] Nama-nama setiap saat saling berhadapan,\
maka perputaran falak berganti-ganti.

[773] Jangan kira pertentangan itu dari Zat,\
semua jejak berasal dari sifat.

[774] Mustahil tata dan ubah itu sia-sia,\
setiap sifat Tuhan punya daya.

[775] Al-Haqq qadim tanpa kurang dan fana,\
Al-Haqq berbicara tanpa lahjah dan suara.

[776] Yang ditakdirkan butuh penakdir,\
untuk berkata butuh yang membuat berkata.

[777] Pelimpah tutur adalah Al-Haqq,\
manusia berhak atas anugerah ini.

[778] Bila kau kenal Yang Berbicara tanpa sirna,\
tinggalkan kesesatan Muktazilah.

[779] Sifat Tuhan tak berujung,\
limpahan tutur tak berkesudahan.

[780] Telitilah dengan cermat dan insaf:\
sudahkah para pendahulu menghabiskan limpahan itu?

[781] Tanpa batas, tanpa kira dan taksiran,\
tema-tema baru terus dituturkan.

[782] Kau raihlah daya paham,\
biar aku bertutur dan kau mendengar.

[783] Terlebih, bukankah peristiwa yang terus baru\
menjadi sebab lahirnya tema baru?

## Pembahasan Kedua: Tentang Perlunya Tutur {.judul-bagian}

[784] Di zaman jahiliah,\
seisi alam sibuk mengaku-ngaku fasih.

[785] Pasar Ukaz digelar,\
orang-orang menyajikan syair.

[786] Lidah berlaga dengan pedang,\
pertikaian seiring dengan syair spontan.

[787] Ketika Tuhan Yang Mahahidup lagi Mahaagung\
menganugerahkan Al-Qur'an kepada dunia,

[788] kefasihan terhimpun bersama mukjizat,\
para fasih di kaum itu gentar.

[789] Agar kaum sesat itu tak berdaya,\
Allah menantang untuk membuat tandingan.

[790] Hingga kini tetap tegak di tempatnya\
kemukjizatan kalam Yang Mahahidup dan Mahakuasa.

[791] Andai kini tak ada lagi daya beda dan pilah,\
sia-sialah perintah dan tantangan itu.

[792] Andai syair dan kefasihan lenyap,\
keutamaan Al-Qur'an ini pun hilang.

[793] Andai tak tersisa penyair yang paham tutur,\
bukti Tuhan berkurang.

[794] Memang, tantangan itu untuk melemahkan,\
tapi dapatkah daya dikerahkan bila tak ada daya?

[795] Dengan bukti kubungkam lawanku,\
dengan Al-Qur'an kubuktikan bakatku.

## Pembahasan Ketiga: Tentang Keumuman Perlunya Tutur {.judul-bagian}

[796] Panglima para imam yang paling paham\
tak mewajibkan nazam Arab dalam salat.

[797] Keumuman mukjizat dibenarkan,\
perlunya makna pun dibenarkan.

[798] Dalam menerangkan hal ini bahkan berkata,\
walau riwayat bahwa pendapat itu ditarik kembali lebih kuat:

[799] orang bukan Arab boleh\
mengungkapkan dengan bahasa sendiri.

[800] Di setiap zaman satu dua penggubah\
tentu menunjukkan kemukjizatan,

[801] dengan mengerahkan khayal yang jernih\
menyatakan pengakuan.

## Tentang Hakikat Kepenyairan {.judul-bagian}

[802] Penyair artinya ahli hati,\
artinya berperangai manis dan bersahaja.

[803] Kalau tidak, segerombol rakyat jelata,\
pemakan sisa rezeki si penggoda,

[804] mana bisa meneguk piala gaya?\
Mana bisa akrab dengan wahyu hati?

[805] Kepenyairan butuh bara derita,\
duka dan bala setia menyertai.

[806] Tak sudi turun derajat ke wajah dan bibir,\
biar padang rumput mekar mawar yang belum pernah terlihat.

[807] Berlari-lari di setiap jalan,\
biar elang khayal menangkap kijang.

[808] Bila masuk ke lorong berliku khayal,\
jangan sampai kesambet jin desas-desus.

[809] Bila dibuka pembahasan pengetahuan,\
pena harus paham keadaan.

[810] Biar pikiran menyelam ke samudra anggur,\
ingin kulihat permata terbawa pulang.

[811] Permata yang kumaksud bukan kata\
yang asal cocok, alis dengan mata.

[812] Seperti ayam betina yang congkak:\
satu telur, seribu kokok dan ribut.

[813] Kebanyakan kata Arab dan asing,\
semuanya kasar, berat, kasar sekali.

[814] Lihat, lihat, manis nian gayanya:\
"delima bibir yang manis di samping kecup mawar".

[815] Perhatikan keserasian dalam kata ini:\
"rambut hitam dan senja di rantau".

[816] "Belati" di sini, aduh halusnya!\
Isyarat kepada alis.

[817] Memang ini pun kepandaian yang lumayan,\
namun tutur tetaplah lain.

[818] Seorang penyair rind yang bersih perangainya\
mengucap kata ini, paling pas di tempatnya:

[819] *"Jangan ulurkan tangan pada gaya yang sudah dikunyah,*\
*sudah ada yang mengucapkannya dulu.*

[820] *Karena kami condong pada lenggok manja,*\
*kami hanya menerima gaya yang segar."*

[821] Kalau tidak, halus kata dan tema\
tak lebih dari klaim keutamaan yang penuh sesak.

[822] Pantaskah dalam nazam membual soal ilmu?\
Atau haruskah aku diam? Insaflah.

## Pelengkap Tutur {.judul-bagian}

[823] Tutur yang termasyhur diraih\
Firdausi, Khusraw, dan Nizami.

[824] Dalam gaya Nawai, Fuzuli\
menemukan jalan sampai bagi tutur.

[825] Di Istanbul kita, Nev'izade\
sudah berlari-lari, namun berjalan kaki.

[826] Masakan disamakan dengan Nizami?\
Cocokkah lagu kecapi dengan Al-Qur'an?

[827] Memang, kehalusan bakatnya tak bisa diingkari,\
dan masih banyak lagi yang seperti itu.

[828] Seribu pujian bagi masing-masing,\
seribu kutuk bagi para pendengkinya.

[829] Sampai kapan kurebut kata dari kata?\
Mari kita kembali ke kisah sendiri.

## Sabda Menjadi Perantara bagi Keduanya {.judul-bagian}

[830] Melihat dua bala muda ini,\
Sabda paham duduk perkara.

[831] Sesekali memperhatikan wajah Jelita,\
sesekali mencurahkan himmah pada Asmara.

[832] Seperti apel, keduanya satu,\
rupa merah, wajah kuning pucat.

[833] Keadaan itu tampak ruwet,\
tampak seperti permainan terbalik.

[834] Iba pada dua anak muda itu,\
Sabda menjadi perantara di tengah.

[835] Sama sekali tak percaya\
bahwa Jelita jadi hamba Asmara.

[836] Mungkinkah diharapkan dari cahaya bulan\
kain linan dijadikan pagi abadi?

[837] Jalan pikir pun macet:\
masa obor menyala demi laron?

[838] Tanda-tanda cinta nyata terang,\
buat apa istikharah bagi yang sudah ada?

[839] Tapi tak diteliti,\
dari siapa kepada siapa bara dan dorongan ini.

[840] Adat di kabilah itu:\
pemudalah yang meminati si jelita.

[841] Begitulah tata cara negeri itu,\
perkara semacam ini belum pernah terjadi.

[842] Keduanya memang sama-sama melirik,\
tapi yang satu ayam hutan, yang satu elang raja.

[843] Hati Jelita terinjak-injak seperti rambutnya,\
Asmara tak menoleh sedikit pun.

[844] Sabda melihat dua si tega ini\
telah merintis jalan lain.

[845] Kasihan pada Jelita, dilindunginya,\
dipanggil ke tempat sepi dan diajak bicara.

[846] Katanya, "Jadilah sehaluan denganku,\
jangan persulit perkara yang gampang ini.

[847] Sejak diwan ini didirikan,\
Sulaiman sudah butuh burung hudhud.

[848] Jadikan kawan pengikut bagi taufik,\
carilah Syapur, jadilah Khusraw di alam itu.

[849] Kekasih dicapai lewat kawan;\
jangan sangka kawan musuh bagi kawan.

[850] Para penempuh jalan mengakui rahasia ini:\
teman seperjalanan dan jalan, keduanya satu.

[851] Orang arif yang bergegas di jalan ini,\
begitu menemukan teman, menemukan jalan.

[852] Yang berjalan sendiri, sekalipun mentari,\
selamanya bersemayam di dalam darah.

[853] Lewat kawan sampai kepada kekasih;\
kalau kau paham, yang dicari pun kawan jua."

[854] Sang Pir benar-benar mencurahkan himmah,\
keakraban kian segar hari demi hari.

[855] Manja dan pinta berulang-ulang,\
dalam bincang keduanya jadi susu dan gula.

[856] Setiap saat, sesuai kehendak hati,\
dua bulan itu saling menjadi pembeli.

[857] Tapi mau apa, pasar ini tak lama;\
langit yang tega iri pada nikmat ini.

[858] Entah angin apa yang berembus,\
mawar layu, suara bulbul terputus.

## Seruan kepada Saki {.judul-bagian}

[859] Saki, inikah saatnya berhenti?\
Berhenti itu apa, ujiankah ini?

[860] Saki, bermurahlah, hujankan anggur,\
jadilah awan, tapi hujankan delima murni.

[861] Ini jual beli, jangan menyesal:\
beri sekuntum, ambil seribu neraka.

[862] Taruh sepercik bara di luka hati,\
beri setitik embun, ambil seribu taman mawar.

[863] Saki, tak adakah seteguk anggur?\
Aku menangis darah, tak adakah kebab?

[864] Saki, bawakan air arguwan,\
api masa muda telah membakarku.

[865] Aku pesakit duka, tawanan perpisahan,\
berilah syarbat sesuai denyut nadi.

[866] Kekalkah langit yang lalim ini?\
Putarlah piala, jangan terbiasa berlambat.

[867] Karena umur bersemangat bergegas,\
dahuluilah dengan satu dua piala.

[868] Panaskan udara kerinduan,\
biar kututurkan duka perpisahan.

## Takjub Muncul dan Melarang Keduanya Berbincang {.judul-bagian}

[869] Majnun berjubah hitam kehampaan,\
yakni pena yang telah kehilangan segala,

[870] menyingkap rahasia kepada Laila khayal,\
memulai tutur dengan cara begini:

[871] Di kabilah ada seorang lelaki,\
bernama Takjub, singa yang tak kenal derita.

[872] Seluruh negeri itu dikuasai,\
mengaku jadi polisi atas dua kekasih ini.

[873] Dari mata-mata takdir tahulah Takjub\
bahwa Jelita dan Asmara saling mendamba.

[874] Seperti langit, bertekad berbuat aniaya,\
di tengah-tengah dipasang tembok perpisahan.

[875] Diperintahkan agar dua jiwa nekat ini\
tak saling melirik.

[876] Melanggar perintah itu perkara sulit,\
dua bulan itu terpaksa berpisah.

[877] Lihatlah langit yang tak setia:\
dua sahabat tak dibiarkan tenang.

[878] Keelokan Jelita tertutup tirai,\
bulan itu menyusup ke balik ufuk.

[879] Dan Asmara yang mulia, mentari berkilau itu,\
berguling-guling dalam air darah senja.

## Jelita Menyusun Siasat {.judul-bagian}

[880] Jelita membayangkan seolah\
seorang diri bertarung melawan Takjub,

[881] yakni dengan satu desah pembakar nyawa\
membakar rumah tangga musuh itu.

## Nasihat Sabda {.judul-bagian}

[882] Seketika Sabda datang menyusul,\
tapi datang dengan tergopoh-gopoh.

[883] Kepada Jelita diberinya banyak nasihat:\
"Jangan lepaskan anak panah kepada Takjub.

[884] Tak pantas kau sakit hati pada lelaki itu,\
lelaki itu cermin keelokan sang kekasih.

[885] Jangan jadikan desah hati orang Zanggi yang mabuk,\
jangan pecahkan cermin Asmara."

[886] Semua dalil dibentangkan,\
intisari tuturnya begini:

[887] "Tak patut meruntuhkan bangunan ini,\
satu sisinya menghadap kekasih.

[888] Tulislah surat, biar aku yang mengantar;\
untuk sementara, lewatkan waktu dengan senang begini.

[889] Jangan bertarung dengan Takjub; yang lalu biarlah berlalu,\
supaya Asmara senang padamu."

[890] Tanpa daya, si molek itu\
merasa cukup dengan surat.

[891] Walau pena sarat kata,\
hampir-hampir menangis darah dalam surat.

[892] Setelah menuruti nasihat itu,\
begini keadaan dipaparkan:

## Surat Jelita kepada Asmara {.judul-bagian}

[893] Kepala surat: nama Tuhan,\
Yang Maha Berdiri Sendiri, Qadim, Hidup, Pengasih;

[894] Yang meninggikan langit dari bumi,\
menurunkan rahmat dari langit ke bumi;

[895] Yang meruntuhkan istana dambaan,\
mematahkan kaki harapan;

[896] Yang meluluskan hajat para perindu,\
mengharumkan nama para penutur;

[897] Yang mengadakan baik dan buruk dari ketiadaan,\
pembuka siasat bagi rind dan zahid.

[898] Kemudian, salam penghormatan dicurahkan\
kepada pribadi pemberi syafaat umat,

[899] kepada para sahabat pilihan, keluarga, dan keturunan;\
semoga salam atas semuanya.

[900] Surat ini, pergilah kepada kekasih jiwa;\
sebuah desah, naiklah ke langit.

[901] Duka hati memang tak terlukiskan,\
namun seperti api, tak bisa disembunyikan.

[902] Surat dari seorang fakir ini\
kertasnya remuk seperti hati.

[903] Untuk si zalim yang raja,\
di matanya suratku debu jalanan.

[904] Wahai raja yang dulu karib bagi hambanya,\
kini kenapa kau benci?

[905] Hamba remuk yang kau pandangi dulu, akulah;\
kini kepada siapa kau terikat, Tuan?

[906] Memang aku tahu kau tak berpisah dariku,\
tak sampai setega itu tak setia.

[907] Tapi perpisahan menghabiskan semua yang kutahu;\
bukankah si sakit suka mengigau?

[908] Malapetaka yang datang tiba-tiba ini,\
semoga Allah akhiri dengan pertemuan.

[909] Kalau aku jatuh memohon, sayangku,\
apa daya, aku dikurung dalam sangkar.

[910] Perempuan, setajam apa pun pedangnya,\
seruling harapannya sumbang.

[911] Saat aku senapas denganmu,\
aku mabuk oleh piala hasrat.

[912] Sudah tahu apa jadinya keadaan;\
kalau kau lelaki, jangan kau lalaikan juga.

[913] Keadaan itu hilang, aku tak berdaya,\
pengembara yang patah sayap.

[914] Ke kota ini datang duka perpisahan,\
pertemuan pergi, kerinduan tiba.

[915] Takjub menghalangiku bertemu;\
jangan kau pun puas dengan sepucuk surat.

[916] Syariat himmah, apakah merestui\
orang berdaya berbuat seperti yang tak berdaya?

[917] Anggaplah aku terkapar di tanah;\
tak syak, aku debu di telapak kaki kekasih.

[918] Mentari, raja langit,\
kalau tak menghiraukan zarah, alangkah jahatnya.

[919] Wahai kekasih yang tak iba pada keadaanku,\
ingatlah, ada hari akhirat.

[920] Bertahun-tahun aku jadi mawar musim semimu,\
akhirnya musim gugur tiba, aku layu.

[921] Kepadamu aku rindu dengan nyawa dan kepala,\
berkhidmat sekuat dayaku.

[922] Kini keadaanku genting,\
jangan tinggalkan yang merintih ini, kasihanilah.

[923] Dariku tak akan datang lagi langkah ke arahmu;\
jangan lalai pada pertemuan atau ajalku.

[924] Entah lewat pertemuan kuraih hajat darimu,\
entah lewat maut kuhidupkan nama.

[925] Takjub membuatku merintih tak berdaya;\
wahai perwira, kini ghirah jadi bagianmu.

[926] Kalau kau ada minat padaku,\
pergilah, biasakan desah dan ratap.

[927] Pasti orang kabilah mendengar,\
lalu membungkammu dengan mempertemukan kita.

[928] Kalau kau tersinggung oleh perkara ini,\
jangan berlaku kejam, takutlah kepada Tuhan.

[929] Bukan aku yang mengadakan derita ini,\
darimulah datang segala aniaya.

[930] Wahai bulan yang menghitamkan bintangku,\
takutlah, Allah Maha Membalas.

[931] Kau pun akan ditimpa bencana,\
kau pun berselimut nyala seperti desahku.

[932] Jangan biarkan si debu ini dalam rindu,\
hiburlah, walau dengan sepatah kata.

[933] Bersyukurlah kepada Tuhan, wahai bertubuh melati;\
ah, andai kau jadi aku, aku jadi kau!

[934] Kalau kau jijik pada aibku,\
tunjukkan jalan yang lurus.

[935] Adakah malu menetap pada pencinta?\
Adakah sesuatu melampaui takarannya?

[936] Aku tahu, derita ini tak ada padamu,\
tapi hari-hari langit masih panjang.

[937] Tak diketahui apa di balik tirai;\
banyak yang tak tahu-menahu terjerembap ke derita ini.

[938] Jelas adat di kabilah:\
minat harus darimu kepadaku.

[939] Kalau lelaki enggan pada tunangan,\
si gadis mau tak mau jadi perawan tua di rumah.

[940] Desah dan rintih tak memberi jalan keluar,\
topan duka tak kunjung sampai ke tepi.

[941] Dariku duka, derita, bara, dan pengaduan;\
di tanganmulah perkara tuntas, aturlah siasat.

[942] Tutur sudah sampai ujung, wahai bulan;\
semoga Allah jadikan baik akhirnya.

## Sabda Mengantar Surat kepada Asmara {.judul-bagian}

[943] Ketika tutur sampai ke ujung,\
surat diserahkan ke tangan Sabda.

[944] Sabda menerima dan berangkat,\
seperti hudhud menuju sang raja.

[945] Didapatinya Asmara bisu dan diam,\
terpana seperti biasa.

[946] Tak ada neraka duka, tak ada nikmat bertemu,\
seolah tak ada kekasih, tak ada orang lain.

[947] Kata Sabda, "Cukup sudah begini;\
buka surat ini, lihat apa tenungnya.

[948] Lihat juga, Jelita yang tiada dua\
betapa menjauh darimu.

[949] Dengan seribu putus asa mengadu,\
menuturkan kata perpisahan."

[950] Asmara mendengar kata itu lalu siuman,\
lalu jatuh lagi dan pingsan.

[951] Sekian lama tak sadarkan diri,\
kembali bicara dengan darah bercucuran dari mata.

[952] Tanyanya, "Surat macam apa itu?\
Tunjukkan, jubah hitam macam apa itu."

[953] Setelah diterima dan dibaca dari ujung ke ujung,\
paham apa inti gugatan.

[954] Saat itu pula pena diangkat,\
ditulisnya pula surat balasan.

## Salinan Surat Asmara {.judul-bagian}

[955] Kepala surat: nama Yang Mahasuci,\
Pengada akal, Pencipta ruh;

[956] Yang memakmurkan alam bala,\
Yang menceraikan dua sahabat;

[957] Yang menjadikan Jelita mentari berkilau,\
Yang memanggang Asmara di dalam api;

[958] Yang memberi harapan bertemu kepada yang putus asa,\
Yang menjadikan si karib tawanan rindu.

[959] Salawat yang banyak kepada Rasul,\
maharaja agung, ayah Al-Batul,

[960] dan salam yang banyak dialamatkan\
kepada keturunan mulia dan seluruh keluarga.

[961] Surat ini sepercik bara hitam,\
abu nyala hati yang terbakar.

[962] Untuk bidadari surga yang di jalannya\
mawar dan musim semi adalah neraka.

[963] Tutur memang keadaan orang hidup,\
namun kadang, kata orang, membuat mayat bicara.

[964] Wahai raja pembunuh hamba sendiri,\
siasat apa? Apa yang kupunya di tangan?

[965] Suratmu sampai ke hati yang merintih,\
panah mengenai, luka pun terjadi.

[966] Entah mantra apa dongeng itu,\
membawa kabar neraka ke dalam jiwa.

[967] Neraka kusebut, tapi nyawa rela pada neraka;\
di dalamnya ada kata bernama perpisahan.

[968] Sekian lama aku bisu,\
sarat gundah karena takut itu.

[969] Tak melihatku terjaga, kau sangka\
akulah yang dicintai, dan kaulah pencinta.

[970] Sedangkan aku, mengenang masa itu,\
hati terbiasa terpana.

[971] Aku ini tak berdaya, paksaan apa ini?\
Demi Allah, betapa cepat habis sabarmu.

[972] Wahai raja yang menganggap diri hamba,\
Yusuflah yang jatuh ke sumur.

[973] Melihat inai di tangan, jangan sangka itu darah:\
Zulaikha tak punya bagian dari cinta.

[974] Wahai mawar, jangan bilang, "Darahku berkeping-keping,"\
jangan sangka aku bulbul yang lemah.

[975] Itu cuma pemerah pipi, bukan darah;\
kata bulbul bukan mantra bagi mawar.

[976] Jangan kira kaulah yang diremukkan duka,\
kaulah mentari hari yang terang.

[977] Yang kusut akulah, dengan seribu duka,\
dan di setiap duka, ada lagi satu alam.

[978] Melihat keadaanku yang tabah,\
kau sangka sayapku lapang dan santai.

[979] Aduhai, melihat ratap pada bulbul,\
tuduhan kau buktikan atas laron.

[980] Di jalan ini memang banyak kerja,\
samudra duka tak bertepi.

[981] Namun kawan-kawan menetapkan:\
derita harus disembunyikan, disembunyikan.

[982] Karena kau ingin semua terbuka,\
ratapan tampaknya gampang dicari.

[983] Kalau yang dimaui huru-hara cinta,\
ini langit, ini desah berasap.

[984] Mulai kini aku dan penyembahan berhala;\
aduhai, aduhai, zuhud dan mabuk!

[985] Karena kau berkata, "Merataplah,"\
mata yang menangis pedulikah pada topan?

[986] Karena kau ingin siasat dariku,\
mulai kini jangan muak pada ratapan.

[987] Buku duka belum sampai ke tanda terima,\
aku tak berharap hajat darimu.

[988] Maksud itu dulu dikesampingkan,\
kini perkara ini yang jadi hasil.

[989] Titah milikmu, tercapainya pun darimu;\
menyerahkan nyawa bagianku, menerimanya bagianmu.

[990] Lihatlah jadinya ratap dan rintih ini,\
keputusan apa yang lahir dari gugatan.

[991] Aku tak mengira diriku ingkar janji;\
walau kiamat datang, aku tak menarik kata.

[992] Siasat, akulah yang mengatur;\
wahai bermata sayu, senangkanlah hatimu.

[993] Para pemuka kabilah, siapa pun,\
biar lepas tangan, ini perkara kepala dan nyawa.

[994] Di jalan ini siapa bisa menghadang?\
Nyawa bekal perjalananku, Tuhan saksiku.

[995] Bersabarlah sebentar, jangan meratap;\
mari kita lihat apa yang diperbuat Tuhan Yang Agung.

[996] Simpan suratku ini, jadikan jimat nyawa;\
janji yang telah kau buat, peganglah, awas!

## Tentang Suci, Inang Pengasuh Jelita {.judul-bagian}

[997] Setelah jauh dari rupa Asmara,\
Jelita sakit oleh pikiran itu.

[998] Lilin itu telah dijadikan perhiasan pangkuan\
oleh seorang berperangai api bernama Suci.

[999] Dulu disusui,\
mawar itu diberi embun dari keringat.

[1000] Di musim kanak-kanak,\
diairi dari anak sungai rasa malu.

[1001] Mendengar ratapan di kala sendiri,\
tahulah Suci duka Jelita, hilang akal.

[1002] Ketika gamelan perpisahan melampaui tirai,\
Suci mendengar lengkap dengan iramanya.

[1003] Terasa bahwa si penggalan bulan\
ingin menjadi bintang bagi sebuah mentari.

[1004] Tak tahu apa dan bagaimana deritanya,\
untuk mawar yang mana desah dinginnya.

[1005] Setiap malam, memandangi si pembelai hati,\
luka selar baru menyala di hati.

[1006] Bila yang satu menyelar dengan rindu,\
yang ini menjadikan rambut sendiri sumbu.

[1007] Bila si cemara semampai itu mendesah,\
di kepala inang ini kiamat pecah.

[1008] Bila air mata itu jadi banjir samudra,\
si malang berlari tak tentu arah ke padang.

[1009] Jelita mendesah setiap saat;\
yang tahu hanya Asmara, dan Allah.

[1010] Suci bertanya tentang bara derita,\
jawabnya sehela desah dingin.

[1011] Jelita menuturkan duduk perkara,\
mimpinya ditakwilkan begini:

[1012] "Tak ada obatnya, aku tertimpa bala,\
seorang diri aku jatuh ke Karbala.

[1013] Nyawa jadi penjual permata rindu,\
mata jadi peminum piala rindu.

[1014] Cermin hati remuk,\
cahaya bulan hilang, tinggal gelisah.

[1015] Aku di laut yang tak bertepi,\
di perang yang tak berbenteng.

[1016] Nasib sial jadi musuh hati;\
lihatlah, reruntuhan memusuhi burung hantu.

[1017] Malam menyembunyikan wajah kekasih,\
cermin pun berkabung.

[1018] Langit merusak tata hidupku,\
cawan hidup berubah jadi luka selar di hati.

[1019] Kilat datang meluluhlantakkan,\
pondok sukacitaku roboh.

[1020] Aku tinggal tertawan derita pisah,\
kekasih bersama orang lain jadi nyawa dan tambatan.

[1021] Mulut kuntum bisu oleh takjub,\
embun jatuh di atas mawar nyala.

[1022] Aku sebatang kara, perkaranya sulit;\
Allah Maha Kaya, Maha Penyayang, Maha Penutup aib.

[1023] Lekuk rambut membuatku gila,\
rupanya suratan di dahiku yang tiba.

[1024] Aku sakit perpisahan, kekasih tak kenal derita;\
sulitnya, penghibur duka tak kenal derita.

[1025] Meratap pun tak diizinkan,\
walau duka menanti begitu banyak.

[1026] Kalau mendesah, desahku jadi buaya api,\
akhirnya si congkak itu mengincarku.

[1027] Mataku jadi lembap air mata kuntum,\
piala penantian penuh.

[1028] Aku tak berdaya di perahu derita,\
di tepi pantai, penolong dan kekasih meratap.

[1029] Aku tak butuh siapa pun sezarah;\
obatku bukan dalam takdir penyembuhan.

[1030] Di jalan rayaku muncul genderuwo rindu,\
akal dan hikmah berbalik pulang.

[1031] Aku tinggal sendiri, di kepala sarat cinta buta;\
ah, kepada siapa mengadukan siapa?

[1032] Aku jatuh ke padang sesat duka, aduh, tolong!\
Tak ada seorang pun yang bisa kutuduh zalim.

[1033] Yang paling dekat pun di arah hidayah;\
andai aku yang lenyap dari tengah-tengah.

[1034] Andai hati ini menemukan cara menghilang,\
jalan raya keselamatan tentu didapat.

[1035] Kalau Khidir taufik tahu jalan, pasti datang;\
kalau ada, tentu sudah hilang.

[1036] Aku jatuh sakit di tangan musuh,\
aku piala, kini pecah.

[1037] Taman mawar keelokanku dijarah,\
aku butuh musim semi lagi.

[1038] Rambut dan kuncirku menyengatku,\
kalajengking datang menyiksaku di kubur.

[1039] Seakan desahku panjang tak berhenti,\
naga tatapanku sendiri menelanku.

[1040] Perawakanku yang disebut pohon yakut\
kini jadi pohon keranda.

[1041] Seperti mataku, bibir delimaku pun sakit,\
manis tutur jadi racun ajal.

[1042] Api pipiku membakarku,\
musim semiku jadi darah di mata.

[1043] Kutancapkan mata di jalan penantian,\
bulu mata jadi peri di mata air itu.

[1044] Kuntum permohonanku tak mekar,\
tidur manjaku terbang seperti bulbul.

[1045] Aku jatuh ke dalam takjub hingga\
alam seolah penuh darah, racun, dan huru-hara.

[1046] Aku di dalam kilat yang membuat terpana,\
neraka di mataku bayi dalam gendongan.

[1047] Jiwaku memusuhi riang;\
kalau kau bilang bergembiralah, aku makin sesak.

[1048] Api di mataku mentari yang berkilau,\
surga di mataku duri akasia."

[1049] Mentari yang penuh kilau itu\
telah tenggelam di samudra gelisah.

[1050] Membuat laut resah bergolak,\
air mata dicurahkan berlaut-laut.

[1051] Kadang masuk ke tanah seperti air mata,\
kadang naik ke langit seperti desah.

[1052] "Jangan tanya derita si sakit cinta,\
jangan usik perang si sebatang kara.

[1053] Ini takdir yang menimpaku,\
Allah yang tahu kisah apa ini.

[1054] Bisakah derita dituturkan kepada yang tak berderita,\
apalagi yang berada di luar siasat?

[1055] Jangan tanya laron tentang dambaannya,\
pahami cintanya dari bara yang membakar.

[1056] Andai tahu apa bara dan huru-hara ini,\
takkan kujarah pondasi sabar.

[1057] Kasihanilah, api duka yang jatuh ke jiwa\
jangan sampai jatuh ke lidah.

[1058] Langit menjadikanku tawanan perpisahan,\
si haus ini dikenyangkan dengan hijran.

[1059] Selagi aku mendesah dan meratap seorang diri,\
setelah mendengar, jangan kau pun berbuat aniaya.

[1060] Sayang, kau bisa binasa,\
kena panah desah.

[1061] Dengan mendengarkan panjangnya desah,\
jalan kehinaan sudah tampak.

[1062] Mulai kini aku tersohor di negeri,\
hari demi hari gelisah oleh duka.

[1063] Tungku api dadaku hancur,\
terbakar aku oleh hasrat ini, tolong!

[1064] Beginilah hawa Kakbah duka,\
ratapan adalah doa di kuil itu.

[1065] Harapan dari tabib: penyakit;\
dambaan: bertambahnya duka.

[1066] Siapa pun yang meminati jalan ini,\
keselamatan adalah penyamun bagi pejalan itu.

[1067] Temani aku di perjalanan, jangan jijik;\
kau tahu jalan menuju kehinaan?

[1068] Bila kekasih ditinggal kekasih,\
mau tak mau hina, jangan harap tertutup.

[1069] Bila sang kekasih merelakan nyawa ini,\
tak cukupkah bala kehidupan?"

## Suci Mengetahui Kekusutan Jelita {.judul-bagian}

[1070] Mendengar jawaban itu,\
gelisah Suci melampaui pikiran.

[1071] Menyesal telah membuat Jelita bicara,\
tinju kerugian dipukulkan ke telinga dan bibir.

[1072] Katanya, "Aduh, derita apa yang menimpaku!\
Aku sendiri yang mencari, lalu tahu.

[1073] Dengan bara ini kubakar rumah tangga;\
andai tak kudengar kata itu!

[1074] Andai mata dan telingaku buta dan tuli,\
hidup dan makan minumku tak jadi racun.

[1075] Kini bala ini sulit obatnya,\
si sakit lemah, deritanya maut.

[1076] Jelas ini derita cinta,\
si bocah pengembara di jalan cinta.

[1077] Begitu menyebut kekasih, langsung diam,\
nama Asmara pun dilupakan.

[1078] Adakah sesuatu yang bisa tetap samar?\
Tanpa cinta, mungkinkah duka ini?

[1079] Namun perlu ada penghiburan,\
kuntum ini perlu diasuh."

[1080] Menurut akalnya, sambil merangkai dongeng,\
dimulailah kepala naskah nasihat.

## Perdebatan Suci dengan Jelita {.judul-bagian}

[1081] Katanya, "Wahai mawar dambaanku,\
tunas baru di taman hatiku,

[1082] setiap derita ada obatnya,\
setiap yang sakit ada sembuhnya.

[1083] Jangan biasakan dongeng putus asa;\
walau jatuh cinta, jangan meratap.

[1084] Hati-hati sekali, wahai bertubuh mawar,\
jangan sampai bibir dan langit-langit mulut mendengar tuturmu ini.

[1085] Jangan perbanyak ratapan,\
jangan buang kehormatan dan malu ke angin.

[1086] Satu huruf yang terbang dari bibir\
tak mau bersarang, walau di seribu telinga.

[1087] Rahasia yang tak kau jaga baik-baik\
tak akan menetap di dada mana pun.

[1088] Rahasia itu raja, perhatikanlah;\
jangan usir dari rumah, hormatilah.

[1089] Sebab kelak, bila bala tentara tahu,\
kau dan rumahmu jungkir balik.

[1090] Dengar kata, bermurahlah, bermurahlah;\
jangan ucapkan rahasia, lindungilah.

[1091] Bercelup warna apa saja, tapi jangan kasih warna;\
jangan biarkan cermin kejernihan berkarat.

[1092] Kata itu kilat bagi lumbung hati dan jiwa,\
jangan sampai lepas dari sarungnya.

[1093] Sekali lepas, diri sendiri jadi sasaran angin,\
dan tempat jatuhnya pun musnah.

[1094] Karena melepas huruf ke seantero dunia,\
busur tak pernah selamat dari meregang.

[1095] Kalau rahasiamu kau beberkan kepada orang,\
aku takut kau kelak kelabakan."

## Jawaban Jelita kepada Suci {.judul-bagian}

[1096] Mendengar kata itu, Jelita sedih,\
menangis racun, tertawa getir.

[1097] Katanya, "Aneh benar jalanmu,\
banjir kau suruh diam.

[1098] Mungkinkah aku mengingkari Asmara?\
Rahasia ini bukan yang kau pahami.

[1099] Kau tak tahu obatnya, sudah, jangan tanya,\
jangan capekkan si sakit dengan celoteh.

[1100] Kukira mau bicara soal Asmara,\
membawa kabar Asmara kepada si perintih ini.

[1101] Kau malah meninggalkan bahasan itu,\
kadang menyebut cermin, kadang rahasia.

[1102] Kubilang langit terasa sempit di kepalaku;\
sekarang buat apa tempayan Plato?

[1103] Kehormatan itu apa? Malu itu kata apa?\
Buat apa balsam penyambung tulang bagi laron?

[1104] Aku merayu-rayu api,\
kau bilang di jalan ada bahaya.

[1105] Kadang kau bicara soal raja dan tentara,\
kadang kau bilang jangan biarkan kejernihan berkarat.

[1106] Anggur apa yang membuatku mabuk ini?\
Apa pula yang kau larang itu?

[1107] Kalau kau butuh dongeng,\
dengarlah, biar aku bernyanyi."

[1108] Seperti laut, tiba-tiba bergolak,\
berseru, "Wahai Asmara!", lalu diam.

## Suci Mencari Dalih Lain {.judul-bagian}

[1109] Melihat keadaan itu, Suci yang tiada dua\
menemukan lagi dalih lain.

[1110] Katanya, "Asmara yang mulia, tiada tara,\
lelaki yang tak kenal sungkan.

[1111] Di pesantren seperguruan denganmu,\
dalam hal ini kabilah sepakat.

[1112] Tentu kau tunangannya,\
kau yang akan meraih pertemuan abadi.

[1113] Tak elok pula baginya perkara ini:\
kau yang mendamba, lalu dia yang didamba.

[1114] Sekali kabar ini tersebar,\
masih dimaafkankah kehinaannya?

[1115] Sekalipun mendamba, bisulah;\
kau perempuan, bermurahlah, jual mahal sedikit.

[1116] Aku takut, kalau Asmara mendengar,\
kau dijadikan latihan pedang rindu."

## Jelita Memikirkan Hal Lain {.judul-bagian}

[1117] Jelita tercekat pada ucapan itu,\
sebab Asmara disebut, huruf demi huruf.

[1118] Katanya, "Maut itu apa, wahai jiwa,\
asal rida sang kekasih tak luput?

[1119] Aku takut kekasih bermuram hati,\
kau takut dia menyakiti."

[1120] Si sakit ini sudah terpana,\
rasa malu itu terlupakan.

[1121] "Tanpa sadar kau menyadarkanku:\
kau berkata 'ah', kudengar 'bulan'.

[1122] Biar sesak hatiku, bibir kusegel,\
asal si berperangai kuntum itu tak merajuk.

[1123] Biar kutelan darah, tak kubeberkan,\
asal orang tak menaburkan garam di lukaku.

[1124] Biar jiwa nekat ini terbakar oleh duka,\
asal kerlingnya tak jadi beracun.

[1125] Mulai kini aku biasakan diam;\
mati pun, namanya tak kusebut.

[1126] Hei, siksaan apa ini, Allah, Allah!\
Terbakar di api, tapi tak boleh bilang aduh!"

## Suci Menutup Jalan Ratapan {.judul-bagian}

[1127] Kata Suci, "Perkara ini tak ada obatnya,\
semoga Tuhan memberi insaf kepada kekasih itu.

[1128] Bulan itu murka mendengar ratapan,\
matanya gelap bila kau mendesah.

[1129] Katanya, 'Ratapan itu hakku;\
bagi sang kekasih cukup setia saja.'"

## Jelita Menjadi Tenang {.judul-bagian}

[1130] Mendengar kata itu, mau tak mau,\
bulan itu berniat jual mahal.

[1131] Seperti tungku, tempatnya di pojok,\
pada lahirnya kembali bersuka dan minum.

## Sabda Mengabari Asmara {.judul-bagian}

[1132] Untuk memahami perkara ini,\
Sabda pun bersembunyi di sana.

[1133] Didengarnya seluruh kisah,\
rupanya menyimak gugatan itu.

[1134] Setelah Sabda tahu rahasia ini,\
didatanginya Asmara dan dikabari:

[1135] "Jelita hangus hatinya karenamu;\
insaflah kini, wahai penerang hati.

[1136] Pantaskah Jelita meratap,\
sedang kau tak merelakan nyawa ini?

[1137] Demi Allah, beginikah adat main cinta:\
sang kekasih yang harus merayu-rayu?

[1138] Mulai kini tambahkan dambaanmu,\
biasakan diri pada pedihnya perpisahan."

## Perkara Berbalik: Asmara Tergila-gila karena Jelita {.judul-bagian}

[1139] Sampailah kita di sisi ini: Asmara yang tak sampai hajat,\
berjiwa singa, bertubuh sakit,

[1140] seorang diri menyalakan desah pembakar dada,\
beberapa malam melewatkan hari dengan senang.

[1141] Kapur barus dijaga dari percik bara,\
beroleh cahaya dari sumbu dini hari.

[1142] Yakni khayal wajah kekasih\
menjamu malam hingga pagi.

[1143] Bila pikiran duka bersambung-sambung,\
yang terbayang selalu gerai rambut kekasih.

[1144] Makin mabuk oleh anggur rindu,\
makin bungkam bibir delima yang asin.

[1145] Bila hilang nama di samudra duka,\
menyebut nama Jelita, lalu tenang.

[1146] Tipu daya janji kosong si jintan\
menjadikan kebun harapan kebun jeruk nipis.

[1147] Walhasil, Asmara yang gesit\
bergembira dengan harapan bertemu.

[1148] Tapi begitu kabar perpisahan terdengar,\
duri perpisahan patah di dalam hati.

[1149] Tubuh halus berparas cahaya itu\
kurus kering seperti biji mata.

[1150] Tak tahu bahwa langit si perusak kerja\
dalam perpisahan menetap pada nada sumbang.

[1151] Di hari pertemuan hidup dinikmati,\
senja hari itu tak dipikirkan.

[1152] Melihat sang kekasih jadi kawan,\
dikira langit bakal kekal begitu.

[1153] Tidakkah pantas, tidakkah layak\
manja si pencinta seharga nikmat dua alam?

[1154] Bila yang dicintai terbiasa merayu,\
pencinta pun berbahagia walau di neraka.

[1155] Mungkinkah mencerna kejayaan itu?\
Sesaatnya seharga kerajaan dunia.

[1156] Di atas semua itu, perpisahan adalah bala;\
jarang pencinta sanggup menanggung manja itu.

[1157] Bukan sembarang pemain cinta\
yang mampu membalikkan manja jadi rayuan.

[1158] Siapa yang ditimpa duka pedih ini?\
Dari Firdaus dilempar ke neraka jahim.

[1159] Kekasih sudah berhasrat kepada Asmara,\
bagi si malang, penawar jadi naga.

[1160] Si pemburu yang merapal seribu mantra,\
seribu *Tabbat* terbalik,

[1161] begitu kijang tertangkap,\
tanpa ragu menghunus pedang siksa.

[1162] Uraian duka tak bisa ringkas,\
diperinci pun tak berkesimpulan.

[1163] Sanggupkah desah-desah itu dituturkan?\
Satu tombaknya pun tak muat di langit.

[1164] Hati yang berbara itu alam derita,\
tabel falak tak mampu memuat bintang-bintangnya.

[1165] Mana ada kata bagi samudra bala ini?\
Falak pun terbakar oleh kisah ini.

[1166] Ketika Asmara putus asa akan Jelita,\
tangan penyesalan membangkitkan jeritan.

[1167] Berkabung dengan seribu permata air mata,\
menanam intan di luka hati.

[1168] Tak bisa bicara karena takjub,\
tak bisa diam karena ngeri.

[1169] Bala kekasih merampas lidah,\
di matanya tak ada neraka, tak ada topan.

[1170] Pecahan hati ditumpahkan dari mata,\
api tercurah dari setiap kata.

[1171] Bila menghela napas di laut bala,\
seperti gelembung, langit pun tak muat.

[1172] Bila mendesah dingin di dalam neraka,\
musim beku pun jadi cemburu.

[1173] Bila menangis dan mendesah karena rindu,\
Juli yang panas dijadikan bulan Desember.

[1174] Kadang menggerutu kepada mentari,\
menaruh api di hadapan gelembung.

[1175] Kadang menatap bintang-bintang,\
kilat desah membakar ladang itu.

[1176] Seperti Majnun, tapi tak menetap di padang,\
tiap kota yang dipandang jadi gurun.

[1177] Air mata berkilau dicurahkan sedemikian\
hingga dunia jadi fatamorgana dan pusaran.

[1178] Lemah seperti benang bunga api,\
membuka jalan ketiadaan ke setiap negeri.

[1179] Seperti nyamuk, lemah tak sampai hajat,\
Namrud langit pun dibuat pening.

[1180] Bulan itu begitu kurus\
hingga kadang ikut terbang bersama desah.

[1181] Namun oleh sempurna wibawanya,\
Arasy pun gemetar karena segan.

[1182] Asal Asmara mendesah demi Jelita,\
dunia runtuh? Biar saja runtuh.

[1183] Dada yang porak-poranda oleh duka,\
pedulikah pada reruntuhan alam?

[1184] Biar saja langit pengacau itu runtuh,\
asal sang kekasih yang mulia senang.

[1185] Asmara yang gesit sudah keluar dari tengah;\
kalau bumi dan falak terbakar, apa urusannya?

[1186] Karena tak seorang pun tenang di sana,\
bahtera falak memang layak celaka.

[1187] Sesekali, bila hancur oleh duka,\
tembang bertingkat ini dilantunkan:

[1188] Hati tertawan oleh seorang raja\
yang tiap hambanya pahlawan pembunuh;\
[1189] kerling dan bibir delima dalam tutur sehati,\
tatapan yang asing condong pada darah:\
[1190] *panah dukanya karib dengan nyawa.*

Diwan takdirnya dibangun di atas aniaya,\
[1191] algojo pun gemetar takut nyawa;\
di setiap pojok jerit "tolong, aniaya!",\
[1192] huru-hara kiamat, desah dan ratap:\
*mahsyarkah ini, atau Karbala?*

[1193] Bibir delima: umur Nuh makna;\
di mata tersembunyi ruh makna;\
[1194] darah yang ditumpahkan: anggur pagi makna;\
limpahan tutur: pembukaan makna:\
[1195] *tiap tutur hidup, tiap tutur abadi.*

Bila rambut diurai dan dijarah,\
[1196] bala tentara iman berlindung pada kufur;\
karena takut itu kuncir kusut masai,\
[1197] pedang pembunuh jadi bukti gugatan:\
*aduh, gugatan ganjil macam apa ini!*

[1198] Biar hati si malang terbakar oleh duka,\
asal berhala berapi itu percaya;\
[1199] biar nyawa bercelup darah hijran,\
asal mata sayu itu puas minum anggur:\
[1200] *seribu kemurahan tebusan bagi setiap murkanya.*

Seperti Galib, seratus ribu yang tergila-gila\
[1201] menjadi Majnun di padang cintanya;\
tak seorang pun merintih dan berdarah hati,\
[1202] ahli derita rela pada tiap kekejamannya:\
*tapi apa daya, tak setia.*

## Tentang Ghirah {.judul-bagian}

[1203] Di sisi Asmara ada seorang penanggung bala,\
bernama Ghirah, setiap pesannya api.

[1204] Pengasuh si tak berdaya itu,\
awan bagi permata khayal itu.

[1205] Lilin pembakar dada itu dijadikannya\
penerang keputren majelis pedih.

[1206] Si hati luka itu dipelihara seperti bocah bara,\
agar membakar setiap negeri.

[1207] Seperti biji mata para pencinta,\
setiap saat dipakaikan hitam.

[1208] Tahun demi tahun, seperti benih tulip,\
disimpan agar luka selar muncul.

[1209] Lama disembunyikan dalam kapas,\
agar seperti luka selar penuh darah.

[1210] Si pembelai hati itu, seperti bocah air mata,\
dibuat bermain tanah di debu duka,

[1211] agar kelak, bila dewasa, bulan itu\
menghadapkan wajah ke jalan seperti batu nisan.

## Ghirah Berbantah dengan Asmara {.judul-bagian}

[1212] Melihat derita rindu pada Asmara,\
Ghirah mendapat kesempatan dan bertanya:

[1213] "Wahai kuntum di taman nyala neraka,\
kenapa kau mengaduh begitu?

[1214] Apa sebab desah sedingin ini?\
Kurangkah derita yang sampai?

[1215] Apa deritamu? Jangan-jangan kau dapat obat?\
Rintih apa ini, kau dapat kesembuhan?

[1216] Kalau kau meratap karena derita,\
sayang, seribu kali aniaya atasku!

[1217] Lelaki yang menyepelekan derita bukan lelaki;\
derita mesti jadi panji lelaki."

## Jawaban Asmara {.judul-bagian}

[1218] Asmara menatap lelaki itu dengan getir,\
tatapannya menanam racun di luka selar derita.

[1219] Katanya, "Kau tahu soal ini?\
Pernah kau dengar nama Jelita?

[1220] Pergi sana, kataku bukan untukmu;\
diam, diam, ini bukan kisah itu.

[1221] Berusahalah menyusul kawan-kawan;\
pulanglah, sabar dan tenang sudah tertinggal.

[1222] Biar zaman ini penuh oleh desahku;\
kau pergi saja, terjadilah apa yang mesti terjadi.

[1223] Di zaman hatiku riang, ke mana saja kau?\
Sekarang kau dapat waktu untuk bicara?

[1224] Aku sudah tak di sini; jangan berhenti,\
siapa lagi yang mau berdebat dan membantahmu?"

## Jawaban Ghirah {.judul-bagian}

[1225] Kata Ghirah, "Ini tanda setia kawan,\
maksudku berbagi duka denganmu.

[1226] Jauh dari itu, kata-kata ini bukan celaan;\
jangan sakiti kawan lama.

[1227] Tapi duka dan desah tak memberi obat,\
samudra darah ini tak memberi tepi.

[1228] Tinggalkan hiruk pikuk sebanyak ini,\
suara bergaung sia-sia seperti gunung.

[1229] Jangan hilangkan diri karena satu luka,\
tinggalkan ratapan, malu, malu!

[1230] Atau kau kira perkara ini gampang?\
Kau kira bala tentara duka cuma pawai?"

## Jawaban Asmara {.judul-bagian}

[1231] Asmara menatap dan berkata, "Apa pendapatmu?\
Ya Rabb, bala apa yang menimpa kami, aduh!

[1232] Ghirah sudah tak paham kata-kata,\
atau lidahku yang kelu?

[1233] Haruskah setiap desah itu desah rindu,\
setiap tangis langsung pengaduan?

[1234] Maafkan, kawan, maafkan:\
Asmara ditugasi mendesah, ditugasi."

## Jawaban Ghirah {.judul-bagian}

[1235] Kata Ghirah, "Desah memang indah,\
tapi apa gunanya bila tak pada tempatnya?

[1236] Ketahuilah, padang-padang ini tak berseberang,\
dan Jelita pun tak rela pada ini."

## Jawaban Asmara {.judul-bagian}

[1237] Kata Asmara, "Kau tak berakal,\
tak mampu memahami baik dan buruk.

[1238] Andai Jelita tak berkenan pada desah ini,\
seketika langit lenyap.

[1239] Kau kira desah itu uap kepala?\
Kau kira ratapku tak berbekas?

[1240] Semuanya dongeng pengantar tidur kekasih,\
semuanya tembang di majelisnya.

[1241] Walhasil, bagi Laila jadi bahan tertawa:\
putus asa Qais dan jerih Naufal."

## Ghirah Mencari Dalih Lain {.judul-bagian}

[1242] Ghirah menghela desah pembakar dada,\
siang pun jadi malam.

[1243] Katanya, "Seribu kali barakallah,\
rupanya Asmara tahu; kini aku tahu.

[1244] Tapi kau perlu satu tekad,\
kekasih harus kau tuntut.

[1245] Pergilah, pinang kekasihmu di tengah kabilah;\
kau elang raja, sambar buruanmu.

[1246] Tinggalkan ratap, tuju sang kekasih;\
seribu pendapat, hasilnya satu kerja.

[1247] Aku pun menunggang kuda bersamamu,\
di pegunungan bala aku teman gua.

[1248] Dengan syarat kau bertekad\
agar Suci mati oleh murkamu,

[1249] atau beri aku izin dalam hal itu,\
biar murkaku menumpas Suci.

[1250] Pegang kataku ini, baik ini, baik;\
Ghirah tak mau ada orang lain di tengah.

[1251] Suci jadi sebab, Takjub pun jadi\
penunjuk jalan perpisahan bagi yang sehati.

[1252] Peristiwa ini kau pun tahu;\
entah khayal apa yang merasukimu.

[1253] Kalau kerang tak dibelah, mana mungkin\
didapat permata dambaan?"

## Asmara Tersinggung {.judul-bagian}

[1254] Asmara berkata sambil menangis, "Diam!\
Sekali ini dengarlah kata Sabda.

[1255] Masa panah dilepas lurus ke arah kekasih?\
Jangan kau melurus ke negeri itu.

[1256] Kalau kau punya sedikit budi,\
temani aku, berkhidmatlah padaku.

[1257] Jangan takut kepala, jangan pikirkan nyawa,\
ikuti pasarku, tanggunglah satu kerugian.

[1258] Masa orang gila diberi petunjuk jalan?\
Usul mentah ini justru yang paling matang.

[1259] Masa wajah dihadapkan pada pedang?\
Apakah setiap yang berkilau itu cermin?

[1260] Kalau sanggup begini, mari ke sisiku;\
kalau tidak, katakan apa yang kau anggap baik.

[1261] Datang-datang bicara soal syarat dan janji,\
seperti perempuan menembangkan lagu buaian:

[1262] 'Kalau begini, biar begitu;\
kalau begitu, biar begini.'

[1263] Membuka bahasan ala madrasah,\
hendak menghabiskan semua padaku."

## Ghirah Menyanggupi Berkhidmat kepada Asmara {.judul-bagian}

[1264] Kata Ghirah, "Aku berjanji, kawan:\
tanpa pikir kepala, aku sehaluan denganmu.

[1265] Sekali lagi pun takkan kubuka mulut,\
biar nuri rahasia tinggal dalam sangkar ini.

[1266] Kalau langit sepakat,\
sehelai rambutmu hilang, kuserahkan kepalaku.

[1267] Jangan sangka aku mencari jalan senang,\
aku cuma menguji rindumu.

[1268] Jangan sangka si sarat duka ini mengelak,\
jangan tersinggung oleh omonganku."

[1269] Ketika Ghirah melompati pedang begitu,\
Asmara memberi isyarat dengan alis:

[1270] "Mari ke sisiku, kita berangkat;\
yang lalu biarlah berlalu, jangan cari dalih."

[1271] Membaca Fatihah untuk niat ini,\
Asmara memulai latihan pertama menuju pertemuan.

## Asmara Meminang Jelita kepada Kabilah {.judul-bagian}

[1272] Ghirah dan Asmara yang gesit\
berhasrat mencapai tujuan.

[1273] Mulla Gila memberi fatwa:\
demi Jelita, berperang jadi fardu.

[1274] Asmara, si penelan duka, bermaksud\
mengetahui keadaan kabilah.

[1275] Setiap orang mencari jalan bertemu,\
mengaku jadi pencinta si jelita.

[1276] Begini memang semestinya bala yang sulit:\
Asmara seorang diri, seisi alam saingan.

[1277] Seluruh kabilah dikumpulkan,\
di sana Asmara mengajukan hajat:

[1278] "Akulah peminang permata Jelita,\
dalam perang pinangan aku yang unggul.

[1279] Kalau Jelita mutiara, hatiku kerangnya;\
kekasih dan jiwa saling menggantikan.

[1280] Kalau Jelita mentari yang terang,\
akulah langit bagi cahaya itu.

[1281] Kalau gugatan ini sampai perlu siasat,\
ini pena, ini pedang dan belati.

[1282] Setiap lawan yang dibinasakan pedangku,\
ratapan kematiannya aku yang menggubah."

## Kabilah Mengejek: Alangkah Enaknya Harta Tanpa Jerih {.judul-bagian}

[1283] Para pemuka kabilah Mahabbah\
saling memberi isyarat:

[1284] "Si tak berhati ini mulai ngelantur;\
apa obat akal bagi orang majnun?"

[1285] Masing-masing menggoda sebisa-bisanya,\
si malang dijadikan bahan olok-olok.

[1286] Ada yang bilang, "Jangan asah pedangmu,\
pantanglah candu sepantang-pantangnya."

[1287] Ada yang bilang, "Khayal itu bala;\
aduh, derita ini tak ada obatnya."

[1288] Ada yang bilang, "Jangan gemar syair,\
sebab syair menguatkan khayal."

[1289] Ada yang bilang, "Selamat atas takhta Tuan;\
rajaku, semoga mujur nasib Tuan."

[1290] Ada yang bilang, "Majzub yang ajaib benar;\
cari hiburan, bukan, maunya?"

[1291] Ada yang bilang, "Ini demam panas;\
kalau tak dibekam, ya begini jadinya."

[1292] Ada yang bilang, "Di tangannya ada pedang;\
obat orang gila: rantai."

[1293] Ada yang bilang, "Wajar kalau dibilang begitu,\
sebab hartanya habis banyak."

[1294] Dari segala penjuru pintu terbuka,\
para tukang bual mengumbar omongan.

[1295] Satu dua tukang oceh menemukan ujung benang,\
mengulang-ulang pelajaran salah ucap.

[1296] "Maaf, kawan-kawan, kalau bikin pusing;\
air mawar ini ampuh buat pilek.

[1297] Suatu waktu aku pergi ke pemandian,\
entah apa yang kulakukan, apa yang kuperbuat.

[1298] Kalian bilang pemandian, jadi teringat\
satu kejadian yang lebih penting dari semua.

[1299] Biar kuceritakan itu dulu:\
dulu aku berbaiat pada seorang syaikh..."

[1300] Kalau semua omongan itu dicatat,\
risalah kita tak akan sampai tamat.

[1301] Walhasil, orang-orang kecil yang juling pikirnya itu\
memulai seribu campur aduk kata.

[1302] Diuraikan hadis yang bercabang-cabang,\
dituturkan sebab-sebab kegilaan.

[1303] Asmara dan Ghirah terjepit di tengah,\
seluruh Bani Mahabbah bersenang-senang.

[1304] Tercengang, lelaki gesit itu\
menghadapkan dada yang koyak kepada Jelita.

[1305] Jelita mengirim pesan begini:\
"Dengarlah kata kabilah.

[1306] Apa pun pendapat yang dinyatakan kabilah,\
itulah pendapatku; jangan jemu."

## Asmara Merendah kepada Kabilah {.judul-bagian}

[1307] Tanpa daya, lelaki yang bingung itu\
menjadi budak titah para musuh.

[1308] Bertanya, "Apa sebab aniaya ini,\
yang diada-adakan kabilah?

[1309] Kenapa keadaanku dijadikan ejekan,\
kataku dianggap aib?

[1310] Apa yang menghalangi kalian menasihati?\
Bukankah aku masuk akal dan mau menerima?

[1311] Kalau peminang Jelita disebut gila,\
langit ini jadi rumah sakit jiwa.

[1312] Terangkan sebab hardikan ini;\
kalau aku bersalah, jelaskanlah."

## Kabilah Sepakat: Maskawin Adalah Menanggung Bala, Begitulah Adat Kami {.judul-bagian}

[1313] Seluruh pemuka kabilah\
menerangkan maksud kepada Asmara:

[1314] "Wahai orang bijak peminang Jelita,\
bila permata nasihat masih bertahan di telingamu,

[1315] pikirkanlah, kami semua saling kenal,\
semua ditimpa gelora dan hasrat.

[1316] Siapa yang sampai kepada kekasih dengan sepatah kata,\
sampai ke musim semi dengan sekuntum bunga?

[1317] Mungkinkah harta tanpa jerih?\
Banyak orang yang dapat jerih tanpa harta.

[1318] Bukankah lebih pantas kami bersenang-senang\
melihat klaim bertemu Jelita sekonyong-konyong?

[1319] Mana bisa bertemu kekasih dengan kata?\
Kasihanilah, jangan ulang kata itu.

[1320] Jangan kira gugatan kami ini tipu daya;\
tanya saja Qais dari kabilah kami.

[1321] Tanpa derita dan duka bertemu kekasih,\
kepada siapa itu pernah pantas?

[1322] Tak seorang pun menempuh jalan itu,\
tak seorang pun pernah mendengarnya.

[1323] Di gelanggang, mahkota itu untuk kepala;\
serahkan kepala, supaya jadi kepala di jalan ini."

## Asmara Menyanggupi Segala Bala {.judul-bagian}

[1324] Asmara paham apa ujung perkara,\
huru-hara omongan pun didiamkan.

[1325] Katanya, "Silakan, khidmat apa?\
Mulai kini aku dan bala dan derita."

[1326] Para pemuka kabilah mengatur siasat:\
"Siapkan uang tunai untuk mahar.

[1327] Akad Jelita butuh harga mahal,\
pertama-tama kau butuh Kimia.

[1328] Jangan diam, berangkatlah ke negeri Kalbu,\
taruh nyawa dan kepala di jalan menuju Kalbu.

[1329] Di kota itu konon ada Kimia,\
di jalannya konon banyak bala.

[1330] Naga berbelang berkepala seribu,\
kapal lilin, di bawahnya laut api.

[1331] Seribu tahun perjalanan: Reruntuhan Duka,\
di seberangnya Istana Ratapan.

[1332] Di awal jalan itu ada penyihir termasyhur,\
tiap helai rambutnya ular, ini bukan bohong.

[1333] Di sebuah padang ada raksasa dan peri,\
singa, harimau, binatang buas darat,

[1334] jin berupa-rupa, seribu muka buruk,\
naga-naga berkedok penyihir.

[1335] Di malam-malam gelap, genderuwo liar,\
suaranya menggelegar melebihi guruh.

[1336] Dengan sihir api dihujankan ke padang itu,\
kadang ular berbelang.

[1337] Kalau Allah menolong dan kau lolos,\
kalau air kota Kalbu kau minum,

[1338] dapatkan Kimia yang ada di sana,\
lalu datanglah ke sini, sampailah kepada Jelita."

## Asmara Berangkat ke Negeri Kalbu, dan Apa yang Menimpanya {.judul-bagian}

[1339] Asmara girang oleh kabar ini,\
dengan seribu rindu dikoyaknya baju.

[1340] Seketika bertanya di mana negeri Kalbu,\
lalu menempuh jalan menuju Kalbu.

[1341] Ghirah pun menjadi kawan seiring,\
dua sahabat menuju kekasih.

[1342] Begitu lelaki jalan itu masuk ke jalan,\
pada langkah pertama jatuh ke sumur.

[1343] Tapi sumur macam apa! Sumur pusaran,\
seperti keabadian, tak terlihat dasarnya.

[1344] Kata Ghirah, "Wahai yang rela berkorban,\
sekarang tanyalah Kimia kepada Karun."

[1345] Sumur ini kota raya,\
perbendaharaan harta karun putus asa dan ratapan.

[1346] Bukan jalan ketiadaan, bukan negeri kegelapan;\
sumur yang isinya rintih dan jerit.

[1347] Pertanda gulita perpisahan,\
laut kegelapan tak bertepi.

[1348] Andai Khidir tersesat dan jatuh ke sini,\
umurnya putus di tengah jalan.

[1349] Andai surya melemparkan laso bulan dan tahun,\
mustahil menemukan dasarnya.

[1350] Karena bulan Nakhsyab jatuh ke sumur itu,\
pantas dinamai Sumur Nakhsyab.

[1351] Jangan sesali kejatuhannya;\
Yusuf pun menemukan mikraj di sumur.

[1352] Seakan lesung dagu menjadi tempat rambut,\
bulan Kanaan bertemu Harut.

[1353] Walhasil, mentari penghias alam itu\
terbalik, sumur dijadikan kediaman.

[1354] Hendak menuju kubah Simak,\
tapi perjalanan lain tampak bagi bumi.

[1355] Berlalu bertahun, berbulan, berhari,\
akhirnya dasar ditemukan, lalu berhenti.

[1356] Rupanya sumur derita itu\
tempat tidur dan istirahat seorang raksasa.

[1357] Raksasa yang punya banyak bala tentara,\
masing-masing tambang kehitaman.

[1358] Bermuka buruk seperti malam perpisahan,\
haus darah, bau busuk bagai bangkai gajah.

[1359] Kedua insan malang itu ditangkap,\
kaki keduanya dijerat laso.

[1360] Dihadapkan kepada raksasa yang mabuk:\
"Inilah buruan, remuk dan terikat."

[1361] Raksasa mengerikan itu memanggil ke hadapan,\
seakan mentari berhadapan dengan Zuhal.

[1362] Katanya, "Hendak ke mana kau\
sampai jatuh ke dasar sumur begini tanpa hati-hati?

[1363] Kudengar kau menaburkan nyawa demi duka Jelita;\
kau pencari emas, tawanan tambang.

[1364] Tapi pikiran bengkok macam apa ini?\
Ini bukan nalar, ini bala di kepala.

[1365] Kau di mana, mentari itu di mana?\
Laut di mana, fatamorgana di mana?

[1366] Rupanya tubuhmu rezeki nomplok bagi kami;\
mata hati dan penglihatanmu tertutup.

[1367] Siapa yang pernah sampai ke negeri Kimia?\
Siapa yang pernah menggapai Anqa atau huma?

[1368] Tanpa pikir dan tanya kau berangkat,\
pada langkah pertama jatuh ke sumur.

[1369] Allah, Allah, alangkah dungunya!\
Kalau lalai, ya lalai sampai begini.

[1370] Sayang, kasihan aku, kau masih muda;\
tapi betapa ganjil buruk sangkamu."

## Asmara Mengamuk {.judul-bagian}

[1371] Asmara panas oleh api dendam,\
berkata, "Untuk apa kata-kata lembut ini?

[1372] Bukankah maumu membunuh?\
Kini aniaya dan keadilan ada di tanganmu.

[1373] Seakan dengan kata-kata ini khayal kekasih\
bisa tersembunyi sezarah pun dari hatiku!

[1374] Jangan coba menakut-nakuti, tak pada tempatnya;\
yang kusebut pertemuan tak lain ajalku.

[1375] Khayal kekasih ini bukan milikku saja;\
sekalipun aku mati, rumput pun meratap.

[1376] Di sumur ini seruling tumbuh di mana-mana,\
menuturkan duka perpisahan kepada para pencinta.

[1377] Hasrat ini tak pergi dari kepala kami,\
asap ini tetap mengepul dari tungku kami.

[1378] Ini obor duka, tak bisa padam;\
menyerahkan nyawa bisa, berbalik tidak."

## Raksasa Memenjarakan Keduanya {.judul-bagian}

[1379] Raksasa terkutuk berakhlak busuk itu\
memerintahkan agar keduanya dipenjara,

[1380] agar lemak dan daging bertambah,\
lalu si terkutuk menjadikannya santapan.

[1381] Sekian lama Asmara dan Ghirah\
tinggal di sana, tawanan derita.

[1382] Saling menghibur,\
saling menguatkan untuk bertahan.

## Kedatangan Sabda {.judul-bagian}

[1383] Suatu pagi Sabda, sang Pir, datang menyusul,\
sampai di bibir sumur dan bertutur:

[1384] "Wahai anak-anak muda yang terikat di sumur,\
yang tetap penyayang di masa bala,

[1385] berusahalah lepas, jangan diam;\
jalan penuh bahaya; singkatnya, jangan diam.

[1386] Dari sumur ini tak ada jalan lepas,\
tak ada tempat berlindung bagi yang terjatuh,

[1387] kecuali di dasar sumur ada seutas tali,\
para jin tak tahu-menahu.

[1388] Seorang pir menuliskan rajah padanya,\
menuliskan banyak nama untuk penjagaan.

[1389] Siapa yang berpegang erat pada tali itu\
dijaga oleh Ismul A'zam.

[1390] Jin tak mampu mencelakai,\
makin memanjat, makin selamat dan tenteram.

[1391] Ini kukatakan dengan mantra;\
jangan kau bocorkan kepada para jin."

## Asmara dan Ghirah Terbebas {.judul-bagian}

[1392] Dua penyabung nyawa itu menuruti perintah,\
seperti Mansur di tali gantungan, kepala terangkat tinggi.

[1393] Asmara, si penakluk langit, membuka mata,\
melihat bahwa pir itu Sabda.

[1394] Tahulah Sabda datang dari negeri kekasih,\
pagi itu dari musim semi itu.

[1395] Dengan rindu dan derita Asmara mendesah:\
"Demi Allah, ceritakan Jelita kepadaku.

[1396] Menyebut-nyebutkah? Apa yang dikhayalkan?\
Sesekali ingatkah pada si tak berdaya ini?

[1397] Tahukah akan kepedihan kami?\
Pernahkah menanyakan keadaan kami?

[1398] Teringatkah pada sahabat?\
Diterimakah bala-bala ini?

[1399] Aku jatuh ke dasar sumur dengan hasrat itu:\
supaya berdekatan dengan bulan di sumur.

[1400] Kemudian kudengar itu cuma sangka;\
tempat bulan di puncak langit.

[1401] Kini aku masih malu atas pinta itu,\
aku sudah masuk ke tanah, tapi tak tenang.

[1402] Pantas aku tetap di bala itu,\
kau datang menyusul seperti Khidir di tengahnya.

[1403] Kini beri aku kabar dari kekasih;\
yang lalu sudah lalu, kabarkan yang ini."

[1404] Sabda tak menghiraukan desah dan rintih itu,\
menjadi burung, terbang ke kebun kekasih.

[1405] Kata Ghirah kepada Asmara, "Saudaraku,\
mari, lelaki jalan mesti di jalan."

[1406] Dua huma ketinggian itu mengepakkan sayap,\
turun ke jalan seperti burung hantu perantauan.

[1407] Panjang tatapan dijadikan tongkat,\
dua insan penanggung bala itu berjalan.

[1408] Duka menyusul kejatuhan,\
di jalan muncul Reruntuhan Duka,

[1409] jalan yang dulu telah disebut,\
setiap langkahnya lubang putus asa.

## Lukisan Malam dan Dahsyatnya Musim Dingin {.judul-bagian}

[1410] Di padang hitam keduanya tersesat:\
malam terpanjang musim dingin, bala mendadak.

[1411] Padang macam apa ini, naudzubillah,\
jin-jin bermain lembing di sana setiap saat.

[1412] Putus asa dan takut susul-menyusul,\
kadang salju turun, kadang gelap.

[1413] Ketika gulita dan salju berkarib,\
cahaya dan gelap masuk satu cetakan.

[1414] Oleh dingin cahaya bulan membeku,\
ganti embun, air raksa yang tercurah.

[1415] Gulita berubah jadi kijang putih,\
padang penuh kapur barus di dalam kesturi.

[1416] Dari satu sisi, gulita di tengah salju\
terkepung seperti hitam biji mata.

[1417] Langit kaca retak oleh es,\
seakan jatuh ke tanah berkeping-keping.

[1418] Lihat, lihat falak si pembuat onar:\
membawakan cermin kepada Zanzibar!

[1419] Ketika dingin dan salju tercurah,\
si hitam malam menyeringai memperlihatkan gigi.

[1420] Ladam bulan berpaku seribu, yaitu bintang-bintang,\
hilang di gulita musim dingin.

[1421] Jalan dan lapangan menjadi gugus Singa,\
di tiap pojok seekor singa dari kapas.

[1422] Seakan lidah nyala api kelu,\
ratap nyala bergetar.

[1423] Bunga api yang congkak membeku,\
api tertinggal di tengah permata.

[1424] Kaca pemandian pecah,\
kubah dan atapnya jadi intan.

[1425] Air jernih pegunungan jadi terbang,\
turun lagi dengan nama salju.

[1426] Kali Perak hendak lari dari padang,\
tertahan di Sütlüce.

[1427] Saudara saling menumpahkan darah,\
jari dan tangan jadi dahan merjan.

[1428] Dunia jadi bayang hitam oleh ngeri,\
pegunungan seiring langkah dengan badai.

[1429] Tak tersisa burung congkak di udara,\
sesekali hanya warna api yang terbang.

[1430] Gelembung anggur seperti yakut\
tak lagi gentar pada nyala.

[1431] Di dalam api terbentuk air bening,\
asap berlindung pada badai.

[1432] Untuk memancing ikan,\
di semua kail diikatkan bara.

[1433] Kubah hijau akan turun ke bumi kelabu\
andai dingin tak menopang dengan tiang es.

[1434] Sultan musim dingin menghias kota,\
seruling perak berjatuhan di bibir atap.

[1435] Lidah yang bertutur jadi bongkah es,\
huruf keluhan sampai ke bibir atap.

[1436] Tungku api mentari akan hancur\
andai pagi tak memancangkan pasak es.

[1437] Bila laut kadang jadi padang,\
ikan jadi santapan kijang.

[1438] Andai mulut anjing pemburu hangat,\
kelinci menyangkanya pelukan ayah.

[1439] Karena takut tergelincir,\
peri pun tak datang ke tepi kolam.

[1440] Kalau bara cemre tak tergelincir,\
takkan jatuh ke bumi sampai bulan Juni.

[1441] Watak orang semua tampak nyata,\
bibir orang tak kalah dari bibir atap.

[1442] Bincang orang dengan napas gemetar:\
rantai kegilaan, tapi dari intan.

[1443] Lilin berkilau di dalam lentera\
serupa dahan merjan tersembunyi di laut.

[1444] Melihat rajawali falak di kandang ayam,\
burung tekukur di sangkar pun terdiam.

[1445] Agar tak memunguti biji kehampaan,\
anak-anak menaburkan bunga api bagi burung pipit.

[1446] Tangan Mirrikh membeku oleh dingin,\
belati jatuh dari langit ke tanah.

[1447] Singa falak jadi singa salju,\
gigi diganti bintang Kartika.

[1448] Seperti bintang penerang malam,\
sesekali tampak hari yang cerah.

[1449] Bila mata yang menangis membeku,\
orang mencari maut dengan kacamata.

[1450] Demi mencari sebab bara hati,\
lawan dan kawan hangat berkarib.

[1451] Kijang bergegas menuju mesiu,\
ayam hutan datang ke sumbu senapan.

[1452] Mabuk anggur setara dengan zuhud,\
api basah jadi air kering.

[1453] Paling ajaib: jalan pikiran membeku,\
syair datang ke tabiat dengan tersendat.

[1454] Semua penutur bungkam,\
gudang anggur makna tak bergolak.

[1455] Galib, para penyair tak bisa menyamaiku;\
aku bermanja-manja pada nyala pikiran.

## Pelengkap Tutur {.judul-bagian}

[1456] Karena takut dan bahaya itu, Asmara yang sadar\
tersesat dalam ngeri dan duka.

[1457] Tahu bahwa ini bukan kota, melainkan padang,\
entah sihir, entah kimia.

[1458] Sebab-sebab binasa berulang-ulang:\
gelegar guruh, kilat, dan badai.

[1459] Laut kegelapan berombak demi ombak,\
genderuwo khayal bergerombol demi gerombol.

[1460] Di satu sisi bala waham dan liar,\
di sisi lain udara salju dan gelap.

[1461] Belum pernah melihat negeri duka,\
anak manja zaman itu.

[1462] Melihat gelap melampaui daratan,\
pemuda itu tenggelam dalam ngeri.

[1463] Lama berlari tak tentu arah,\
seperti puting beliung ke segala penjuru.

[1464] Di padang itu tak tampak satu jejak pun,\
tak terlihat satu jalan selamat pun.

[1465] Tiba-tiba si elok bagai peri itu melihat\
api menyeramkan laksana tumpukan panen.

[1466] Pertanda ter jahanam,\
di atasnya lidah api demi lidah api.

[1467] Asap nyala menjangkau falak,\
sihir belaka, tapi berwujud nyala.

## Lukisan si Penyihir {.judul-bagian}

[1468] Seorang nenek bersarang di sana,\
penyihir mengerikan bermuka raksasa.

[1469] Seakan setan bermukim di neraka,\
empat penjurunya air mendidih, ter, dan aspal.

[1470] Kepala: contoh Gunung Hitam;\
mulut dan gigi: kubur kafir yang tua.

[1471] Hidung: padang Tanjung Moda,\
sarang dubuk, liang kadal.

[1472] Bibir bawah menjuntai sampai lutut,\
seperti bangkai gajah yang busuk.

[1473] Dua mata berwarna buruk: kura-kura;\
bulu mata seperti kaki kepiting.

[1474] Dua kelabang hitam dijadikan alis,\
dua gulung ular dijadikan rambut.

[1475] Dua buah dada seperti dua babi\
yang dibalik kepala ke bawah untuk suatu kerja.

[1476] Dua telinga: lubang ladang,\
sarang landak, tempat tidur tikus.

[1477] Dari mulut mengalir air busuk,\
bau busuk seperti selokan.

[1478] Di hidung kelabang, tikus, kalajengking,\
di mulut ular berbisa dan biawak.

[1479] Lidah bercakap dengan api,\
seakan zabaniyah neraka.

[1480] Perkakas sihir siap di sisi:\
seribu belanga tua dan minyak berlimpah.

[1481] Minyak yang dituang ke belanga\
menimbulkan beribu-ribu khayal.

[1482] Kadang menunggang awan seperti angin,\
kadang membuat api menjerit.

[1483] Anak-anak lahir dari satu sisi tubuh,\
dari darah bocah-bocah yang ditelan,

[1484] lalu dimakan lagi\
oleh si busuk jahat itu anak-anak yang dilahirkan.

## Si Penyihir Menginginkan Asmara {.judul-bagian}

[1485] Dengan sihir dipanggilnya Asmara,\
dipamerkan segala hiasan dan perhiasan:

[1486] seribu macam kain, barang, dan kemegahan,\
intan dan delima, permata dan emas.

[1487] Semua itu dikenakan seketika,\
berkata kepada Asmara, "Mari, Nak, kawinilah aku.

[1488] Nikahilah, aduh, si malang ini;\
hatiku terpikat padamu, tak ada daya.

[1489] Menjadikanmu sultan langit ini\
tampak gampang bagi si fakir ini, gampang.

[1490] Kalau kau enggan pada perkara ini,\
dengan satu sihir keadaanmu kubuat merana."

[1491] Asmara mendengar dan memahami kata itu,\
kadang menangis, kadang heran.

[1492] Kepala diangkat ke langit,\
kepada Yang Mengetahui rahasia manusia dan jin.

[1493] Langit dijadikan perisai bagi desah,\
dikenangnya Jelita yang berwajah mentari:

[1494] "Wahai Jelita, wahai mentari cemerlang,\
wahai yang menjadikan Asmara tawanan bara,

[1495] inikah harapanku darimu, wahai bulan:\
penyihir yang mendamba pertemuan denganku?

[1496] Aku lunglai dalam derita perantauan,\
kau riang dalam nikmat dan suka.

[1497] Aku tersesat di salju dan gulita,\
semoga falak ini menurut maumu.

[1498] Tapi beginikah gaya cinta?\
Insaflah, wahai bulan kemurahan.

[1499] Yang kekasihnya tawanan bara,\
air Kautsar pun tak lewat di tenggorokannya."

[1500] Kadang nasib, kadang langit, kadang kekasih\
membuat pasar air mata ramai.

## Si Penyihir Menyalib Asmara {.judul-bagian}

[1501] Melihat Asmara dalam bala ini,\
si penyihir makin murka.

[1502] Dengan sihir disalibnya,\
dijadikan sasaran pedang dan tusuk sate.

[1503] Di hadapan api itu Asmara dan Ghirah\
disalib, agar dunia mengambil pelajaran.

[1504] Berlagak Namrud sejadi-jadinya,\
si tukang sihir menyalib sang raja.

[1505] Karena sumur yang dalam sudah dilihat,\
di jalan ini katapel pun ditonton.

[1506] Laksana pelita, kuntum segar itu\
menaikkan kilau tiang gantungan.

[1507] Karena si penyihir mencintai Asmara,\
maksudnya cuma menakut-nakuti.

[1508] Waham mencekik leher,\
tapi jiwa yang suci tak terluka sedikit pun.

[1509] Di tiang itu, seperti khatib di mimbar,\
si bertubuh melati tinggal berminggu-minggu.

[1510] Meratap seribu macam ratap,\
yang melihat mengira bulbul merintih.

[1511] Kadang mengadukan aniaya kepada langit,\
kadang mendesah dan menjerit kepada Jelita.

[1512] Kadang menyapa nasib,\
menajamkan anak panah celaan:

[1513] "Wahai nasib, apa pula ketidaksetiaan ini?\
Tak adakah persahabatan denganmu?

[1514] Anggaplah sang kekasih tak setia,\
itu memang adat, dan pantas pula.

[1515] Pencinta memang harus berduka dan ditimpa bala,\
kekasih memang harus tak setia.

[1516] Tapi kau, janganlah ikut-ikutan si genit itu,\
jangan ikut-ikutan lenggok zaman."

[1517] Tak di sana, tak di sini ada pengaruhnya,\
paham bahwa semua kerja takdir.

[1518] Kesadaran kembali ke kepala,\
teringat rahmat Yang Maha Pengampun:

[1519] "Wahai Pencipta manusia dan jin, rahmat!\
Aku tak berdaya, ampun, kasihanilah.

[1520] Kalau tak ditakdirkan bertemu kekasih,\
ambil nyawaku, berikan kepada si genit itu."

[1521] Dengan seribu pikiran, bergumam kusut,\
merintih dan mendesah kepada Sesembahan.

[1522] Saat itu Sabda datang menghadap,\
muncul laksana perintah "Kun".

[1523] Seketika terbuka malam gulita,\
takut dan cemas berganti rindu.

[1524] Al-Haqq tampak, waham bubar,\
sihir musnah seperti mimpi.

[1525] Melihat sang Pir, Asmara yang gesit\
menangis, mengoyak dada.

[1526] Menyebut Jelita, mendesah dan menjerit,\
lalu melantunkan syair suci ini:

[1527] Selamat datang, wahai utusan kekasih,\
hadiahkan kepada kami sepotong kabar kekasih;\
[1528] biar nyawa jadi tebusan hari raya kekasih,\
sia-siakah harapan akan kekasih?\
[1529] *Tak adakah salam kekasih untuk kami?*

[1530] Wahai Khidir bagi yang terjatuh, katakanlah,\
singkapkan rahasia ini, katakanlah;\
[1531] jadilah juru bahasaku, katakanlah,\
jangan sembunyikan, satu per satu katakanlah:\
[1532] *tak adakah ujung bagi buku duka?*

[1533] Ya Rabb, penantian macam apa ini,\
masa apa ini yang tak juga berlalu?\
[1534] Melulu sesak dan duri demi duri;\
andai kutahu, si genit macam apa ini:\
*tak adakah dambaan semacam pertemuan?*

[1535] Aku naik ke puncak tiang gantungan seperti Mansur,\
suaraku azan tiupan sangkakala;\
[1536] duka menjadikan leherku seruling Mansur,\
aku terkepung bala tentara bala:\
[1537] *tak adakah pesan dari raja itu?*

[1538] Para pengemis meraih hajat dari langit ini,\
sahabat-sahabat tertunda ke hari esok;\
[1539] tak bertahankah janji-janji dan kesetiaan itu?\
Tak terkabulkah doa-doa yang kupanjatkan?\
*Tak adakah tata bagi keadaan hati?*

[1540] Hati bisu oleh takjub duka,\
tak berdaya seperti Galib;\
[1541] surat pengaduan yang kukirim tak berbalas,\
kini tinggal satu kemungkinan:\
*tak adakah nama insaf di tempat itu?*

## Sabda Membawa Kabar Gembira {.judul-bagian}

[1542] Sabda membuka pintu tutur,\
menjawab dengan cara begini:

[1543] "Kau kira kekasihmu tak tahu apa-apa?\
Atau kau kira akan meninggalkanmu?

[1544] Raja negeri keelokan dan pesona itu\
penolong bagi yang terjatuh.

[1545] Jelita itulah pencinta, jangan kau kira yang dicinta;\
dengar, inilah kata yang terpercaya.

[1546] Lihatlah kuasa Jelita yang tiada banding:\
bagaimana nasib si penyihir itu!

[1547] Kini buka mata dan perhatikan;\
lihat si penyihir, ambil pelajaran dari rahasia ini."

[1548] Asmara penghias alam sekali menoleh,\
memandang si penyihir, tapi

[1549] apa yang terlihat? Sudah berubah rupa:\
bangkai anjing masuk ke dalam karung.

[1550] Tak ada hiasan, tak ada perhiasan:\
bangkai babi, kafir yang membeku.

[1551] Sekali tebas pedang terbelah dua;\
berbuat jahat, jahat pula bintangnya.

[1552] Di sisinya tak ada api, tak ada gelap,\
tak ada salju, tak ada salib, tak ada ngeri.

[1553] Sabda melukiskan khayal itu,\
menerangkan sebabnya begini:

[1554] "Kau lupa nama Jelita,\
maka penyihir membuatmu terpana begitu.

[1555] Nama Jelita itulah jimat sihir ini,\
penghapusnya ialah nama itu.

[1556] Ketika kau sampaikan hajat,\
terjadilah yang terjadi, himmah dicurahkan.

[1557] Jelita yang tiada dua menyambut jeritmu,\
menghadiahkan sebilah pedang bertatah permata.

## Lukisan Pedang {.judul-bagian}

[1558] Tapi pedang macam apa! Pedang intan,\
algojo musuh, meteor bagi bisikan setan.

[1559] Satu larik dari Zulfikar Haidar,\
satu ayat dari kancah perang Haidar.

[1560] Cermin pertolongan Ilahi,\
Khidir bagi jalan dan adat raja-raja.

[1561] Membuat iri pedang mata dan alis,\
membungkam penyair tukang hujat.

[1562] Sungai darah, kali api,\
racun ajal, naga berbelang.

[1563] Bulan sabit sarungnya yang indah,\
pamornya dari ujung ke ujung bintang Tsurayya.

[1564] Seperti ombak air hayat,\
intan, tapi batu asahnya merjan.

[1565] Pedang yang di laut tak bertepi\
mengalirkan nyawa, bukan air.

[1566] Cengkeram mentari yang terang\
mencabutnya dari telur bulan.

[1567] Seperti kerling kekasih yang genit,\
melontarkan huruf kepada huru-hara takdir.

[1568] Bulan di langit laga dan perang,\
ikan pedang di pusaran bala.

[1569] Buah dan hasilnya nyala, dahan api,\
tubuh penuh api, bersepuh emas.

[1570] Air mancur dari air yang kenyang delima,\
kali zamrud yang berkilau kehitaman.

[1571] Nuri hijau bercucur darah,\
elang raja, namun berwajah kuau.

[1572] Tunduk pada isyarat Izrail,\
sayap ombaknya membangkitkan mahsyar.

[1573] Pemurah tambang mengeluarkannya\
dari telur burung Malakut.

[1574] Dalam kerasnya ada jernih penjagaan,\
ombak permatanya baju zirah Daud.

[1575] Burung hijau pembawa kabar hitam,\
di sayapnya tersembunyi maut merah.

[1576] Peminum darah, tapi penolak kezaliman,\
jawaban pamungkas bagi bantahan bengkok.

[1577] "Pedang ini saksi gugatanmu;\
jangan pandang sebelah mata, ini pedang desah.

[1578] Segala yang menghadang di jalan ini,\
serahkan kepada pedang desah.

## Lukisan Kuda {.judul-bagian}

[1579] Si bagai peri itu juga menghadiahkan kepadamu\
seekor kuda yang memikat hati:

[1580] kuda semerah mawar, laksana kuau,\
taman mawar surga dan laut darah,

[1581] pengombak air delima dan yakut,\
laksana Rafraf, penempuh jalan Lahut,

[1582] dari kepala sampai kaki musim semi berbaju mawar,\
seperti anggur, merah delima dan bergolak,

[1583] air raksa, tapi bertubuh nyala,\
seperti mentari, api yang berwujud,

[1584] tubuh diuleni dari kehalusan,\
tiap geraknya lenggok kiamat,

[1585] Tuba surga, pohon nyala,\
istana Adn, singgasana nyala,

[1586] serupa darah hati pencinta,\
air Khidir, tapi mirip darah,

[1587] merak surga dan singa gemilang,\
pengantin cantik berbaju merah.

[1588] Bila lenggok langkahnya dipercepat,\
membawa kabar keabadian kepada azali.

[1589] Bila langkahnya dilonggarkan,\
satu saat pun tak sampai ke debunya.

[1590] Sebegitu cepat larinya\
hingga butir-butir udara tak terusik.

[1591] Bila bertekad melipat tempat,\
mendahului bagian-bagian waktu.

[1592] Membuat iri kuda belang bertubuh mawar,\
gerak manis seperti Syirin, tenang seperti Rustam.

[1593] Bila sesekali menancapkan kaki untuk diam,\
Laut Hitam dijadikan batu hitam.

[1594] Si bertubuh nyala berdiri seperti gunung,\
laksana kubah merah Bahram.

[1595] Dua telinga: jambul elang raja;\
leher: kendi yang tegak congkak.

[1596] Hewan, tapi air hayat;\
seperti pagi musim semi, pohon merjan.

[1597] Tiap helai bulunya dawai tanbur dalam riang,\
ringkiknya tiupan sangkakala.

[1598] Kuku: tempurung otak raksasa putih;\
ekor: benang sinar cahaya mentari.

[1599] Mengalir seperti air di bumi dan tambang,\
melompat seperti api ke langit.

[1600] Mata kijang, dada singa,\
surai sunbul, napas seperti naga.

[1601] Anqa yang harum napasnya dan paham tutur,\
nyala berjimat dalam terbang.

[1602] Sewarna pemerah darah air mata,\
seirama dengan kanun cinta.

[1603] Seperti nuri, walau berbaju merah,\
membungkam kuda hitam pena.

[1604] Kekasih dan pemberani dan lapang,\
seperti riang anggur penakluk singa.

[1605] Walhasil, kuda ringan sayap itu\
akan mengantarmu ke kota Kalbu.

[1606] Ini kenang-kenangan Jelita untukmu;\
bersungguh-sungguhlah, ini negeri duka."

[1607] Ghirah pun diberi bulu dan sayap,\
diberi daya untuk menemanimu.

[1608] Kau lihat, raja macam apa itu,\
yang menjadi penunjuk jalan bagi Asmara?

[1609] Kalau kau tanya, dari mana Jelita yang tiada dua\
memperoleh kuasa ini,

[1610] aku ini hamba yang malu di hadapannya;\
pahamilah, aku debu di kakinya.

[1611] Bila sang hakim itu memerintah,\
semua ini bagiku seperti bukan apa-apa."

[1612] Begitu Asmara yang mulia menunggang kuda itu,\
dipacunya menempuh jalan.

[1613] Ghirah pun mengembangkan bulu dan sayap,\
keduanya mengenang pertemuan dengan sang raja.

## Asmara Jemu {.judul-bagian}

[1614] Terasa amat berat bagi Asmara,\
sesekali merenung, lalu jemu:

[1615] meninggalkan kekasih untuk berjalan,\
meninggalkan bulan untuk ke sumur.

[1616] Hari demi hari makin putus asa,\
bermil-mil makin jauh.

[1617] Kata Ghirah, "Harapan tak boleh putus;\
mungkinkah kemurahan Yang Maha Berdiri Sendiri menjauh?

[1618] Yang terus berjalan sampai ke tujuan,\
yang mengembara tak tentu arah pun menemukan permata.

[1619] Sudah jelas, bagi Al-Haqq tak ada depan dan belakang,\
tak ada arah, tak ada penjuru.

[1620] Siang malam mari bergegas,\
suatu hari kita lihat mentari itu."

[1621] Purnama sempurna itu berjalan,\
setiap malam menempuh seribu tahun.

[1622] Mentari cemerlang itu melipat,\
setiap hari, jarak sembilan falak.

[1623] Menunggang mentari seperti Isa,\
tak ambil peduli akan perjalanan.

[1624] Sesekali, bila takut akan nyawa,\
Ghirah berkata kepada si tak kenal ampun itu:

[1625] "Maut tak sepanjang umur seperti perpisahan;\
apa yang Allah beri yang tak sanggup dipikul hamba?"

## Benteng Rupa-Rupa {.judul-bagian}

[1626] Saki, bawakan api anggur pagi,\
terangi ruh dengan api itu.

[1627] Biar gelora mata yang menangis jatuh ke hati,\
topan berombak di dalam tungku.

[1628] Biar dada ini jadi bekas kebakaran,\
tapi anggur menenggelamkannya dalam nyala.

[1629] Hati kami terikat pada dawai organ,\
sekaligus dirantai ombak darah.

[1630] Rantai kami tak bisa dibuka\
kecuali oleh pedang ombak anggur.

[1631] Berikan anggur itu dengan murka,\
biar Mirrikh bala jadi gelembungnya.

[1632] Biar cawan semerah mawar itu mengeluarkan kami dari kepala,\
menyelaraskan kami dengan Mansur.

[1633] Mari lupakan baik dan buruk,\
biar binasa berpelukan dengan nyawa.

[1634] Rupanya Reruntuhan Duka itu tempat jagal;\
mana garis cawan, mana hizib agung?

[1635] Karena jalan tertutup duri dan sampah,\
biarlah banjir bunga api itu menyapu bersih.

[1636] Aku bergegas menuju padang duka;\
siapa kini yang berani menghadangku?

[1637] Kemarilah, para penghadang jalan,\
yang merindukan pedang desah!

## Asmara Melintasi Reruntuhan Duka {.judul-bagian}

[1638] Ketika Asmara yang mulia, tanpa gentar,\
dengan penuh damba jatuh ke padang duka,

[1639] dengan pedang itu Asmara yang melesat secepat kilat\
menjadikan padang duka pasir gelanggang.

[1640] Setiap genderuwo bala yang muncul di jalan\
dijadikan santapan pedang desah.

[1641] Bumi dibalik jadi langit,\
naga-naga diberi warna bima sakti.

[1642] Kepala raksasa dan genderuwo digelar bak dagangan,\
bala tentara itu dibayar tunai dengan maut.

[1643] Darah singa dijadikan lautan,\
padang berubah jadi kulit harimau.

[1644] Dengan sebilah pedang, anak keturunan malaikat itu\
menjadikan gulita jahim taman surga.

[1645] Sebentar saja reruntuhan duka dilintasi,\
sihirnya dilihat, fatamorgananya pula.

[1646] Jalan itu dilalui sebelum ajal,\
Istana Ratapan tertinggal di belakang.

[1647] Kisah itu sudah didengar:\
kapal lilin di atas laut api.

[1648] Kini tiba-tiba muncul di jalan\
samudra api pembakar hati itu.

[1649] Memperlihatkan kapal-kapal dari lilin,\
banyak raksasa bermukim di laut itu.

[1650] Sebab api tak menyakiti kaum itu;\
masa api tersakiti oleh api?

[1651] Kapal-kapal ditahan di udara,\
banyak orang dungu tak berbekal tertangkap.

[1652] Siapa pun yang maju ke kapal,\
raksasa-raksasa itu membinasakannya.

[1653] Sampan, tapi serupa pohon hias pesta kawin,\
lambungnya merah dan berwujud nyala.

[1654] Seakan pulau malapetaka,\
penuh bara, bala, kiamat merah.

[1655] Masing-masing seperti Gunung Surkhab,\
penuh raksasa berayah tiri gunung.

[1656] Kapal lilin itu seakan keranda,\
tapi kuburnya tak diketahui.

[1657] Bahtera dan api yang sarat celaka itu\
tak lain lilin-lilin kuburan.

[1658] Api itu tempat sihir berkuasa,\
tapi tak sanggup menyakiti pantai.

[1659] Ketika para raksasa memanggil Asmara:\
"Mari naik kapal, kau akan selamat,"

[1660] Asmara paham duduk perkara,\
bersabar, tak tergesa-gesa.

[1661] Tapi apa daya, jalan tertutup,\
tak satu jalan pun terlihat.

## Mengadukan Keadaan Diri {.judul-bagian}

[1662] "Wahai Pencipta dan Pengatur, sampai kapan\
derita dan duri demi duri ini?

[1663] Pantaskah ada penyamun, padahal jalan milik-Mu?\
Bila Kau mencari dambaan, dambaan pun milik-Mu.

[1664] Haruskah setiap ahli derita yang bergelora\
naik ke tiang gantungan seperti Mansur?

[1665] Jangan jadikan aku sasaran perpisahan;\
buat apa menguji yang ingkar janji?

[1666] Karena Kau jadikan aku tempat sezarah cinta,\
Kau sejajarkan kepalaku dengan mentari,

[1667] jangan ikat aku di tangan para penyihir;\
bunuhlah aku, jangan biarkan sakit begini.

[1668] Maut itu hidup abadi;\
bila diminta demi nafsu, itulah rugi.

[1669] Yang dimaksud hanyalah rida,\
dan untuk maksud itu pun perlu karunia.

[1670] Di jalan mencari, kakiku terikat;\
Engkaulah yang membuka, aku tak punya apa-apa.

[1671] Berilah perlindungan yang layak diterima,\
terimalah, dan berilah doa.

[1672] Anugerahkan pencarian di hatiku,\
anugerahkan adab dalam meminta.

[1673] Biar pinta ini bergandeng dengan satu kemurahan,\
biar kelancanganku seluruhnya jadi kesempurnaan.

[1674] Kalau tiang gantungan, itulah pojok majelisku;\
kalau api, api itulah persinggahanku.

[1675] Bila samudra pertolongan bergolak,\
mustahil hamba-hamba dilupakan.

[1676] Aku tahu duka ini tak seharga desah,\
demi Allah, tak seharga satu tatapan.

[1677] Tapi harapanku rahmat-Mu,\
yang kami akrabi pertolongan-Mu.

[1678] Di padang ketiadaan Kau bermurah,\
Kau beri pakaian wujud ketika kami tiada.

[1679] Kini pun kami di ketiadaan, tiada kami,\
pendamba nikmat-Mu yang merata."

***

[1680] Tinggallah Asmara di sana, tawanan rindu,\
tak kuat menyeberang, tak terpikir kembali.

[1681] Kuda kemerahan bertubuh mawar itu bicara:\
"Kenapa kau berhenti?"

[1682] Asmara menaburkan mutiara air mata,\
bertutur laksana mutiara yang bergulir:

[1683] "Aku tak bersayap dan berbulu seperti Ghirah;\
dengan api ini, bagaimana nasibku?

[1684] Aku bukan rajawali yang bersiap\
terbang ribuan farsakh."

[1685] Kuda merah itu menjelma seperti Anqa,\
menerjang api tanpa sungkan.

[1686] Api yang asapnya asap Namrud,\
genderuwo hitam penampakan Namrud.

[1687] Api duka menguasai dunia,\
pusaran-pusarannya sumur jahanam.

[1688] Neraka, tapi taman nyala dari air raksa;\
setiap bara meneguk teguk pusaran.

[1689] Semerah mawar seperti air darah hati,\
laut bunga api, samudra darah.

[1690] Setiap selamnya samudra api,\
setiap kedalamannya jahim api.

[1691] Kata Ghirah kepada Asmara, "Jangan bakar nyawamu;\
inilah api Kimia itu.

[1692] Terbanglah laksana rajawali,\
jadilah unggul di kowi ujian itu.

[1693] Jangan kira kau datang dari pintu ini;\
kau pergi lewat api, pulang lewat air.

[1694] Jangan lari dari api kefanaan ini,\
jangan masuk lagi ke perut kuda."

[1695] Api menguatkan kesempurnaan Asmara,\
laksana mentari dalam air darah senja.

[1696] Topan bunga api berombak demi ombak,\
kuda merah terbang, puncak demi puncak.

[1697] Samudra api penuh gelora bala,\
kuda pemikat itu bagai nyalanya.

[1698] Desah dingin, seperti ayat *"Jadilah dingin,"*\
melintasi api itu bagai asap.

[1699] Di sisinya Ghirah mengembangkan sayap,\
laron, tapi berupa singa.

[1700] Mentari terang itu tertinggal di dalam asap,\
seakan fitnah gerhana bulan.

[1701] Setiap saat para genderuwo,\
dengan sebilah pedang, dikirim nyawanya ke jahanam.

[1702] Kuda di bawahnya laksana salamander,\
Ghirah pun bersama-sama di sisinya.

[1703] Walhasil, jalan api itu\
dilalui laksana angin sepoi dini hari.

[1704] Sampai ke pantai yang jalannya\
musim semi taman-taman Firdaus.

[1705] Bulbulnya nuri pandai bertutur,\
nurinya karib dengan bara dan gamelan.

[1706] Rumput bergelombang seperti laut,\
tiap pohon penabur mawar seperti Tuba.

[1707] Topan padang rumput, laut zamrud,\
bumi langit hijau, alam zamrud.

[1708] Di setiap arah bunga-bunga tampak,\
penuh senyum seperti wajah-wajah rembulan.

[1709] Tiap kuntum musim semi yang riang,\
tiap embun awan yang basah.

[1710] Seperti langit, kebun yang bercahaya itu;\
bunga mataharinya serupa mentari.

[1711] Padang penuh narsis dan anyelir,\
rumput liar dan debunya sunbul.

[1712] Udaranya begitu jernih dan memikat\
hingga bulbulnya harum seperti kuntum.

[1713] Butir-butir debu dalam cahaya surya merekah,\
masing-masing bunga jam, seperti biasa.

[1714] Duri-duri berbunga lebat di padang rumput,\
tertawa ke arah putaran falak.

[1715] Memandang kebun dan padang itu,\
luka selar Asmara segar kembali oleh satu desah.

[1716] Mengenang Taman Makna,\
dilantunkannya syair baru ini:

[1717] Duhai, masa ketika hati riang,\
negeri jiwa kota sukacita;\
[1718] kukenang lagi lagu-lagu itu;\
demi Allah, wahai falak, berilah keadilan:\
[1719] *dulu akulah hiasan zaman.*

[1720] Sebuah kebun tempat jiwa ini bersarang,\
tiap kuntumnya seolah surga;\
[1721] kesempatan datang dan menjarah semua,\
di hatiku riang itu masih tinggal:\
[1722] *dulu aku mabuk anggur kehormatan.*

[1723] Tak pernah aku memohon kepada langit,\
bersuka dan minum dan gamelanku tersedia;\
[1724] cemara manjaku berjalan di sisiku,\
rahasiaku belum terbuka begini:\
*dulu aku membuat iri musim semi.*

[1725] Kini aku jatuh ke duka penantian,\
seperti bulbul jatuh ke musim semi baru;\
[1726] banyak api kulintasi lalu jatuh ke pantai,\
seperti cawan, jatuh berkeping-keping:\
*dulu aku peminum anggur rajukan kekasih.*

[1727] Aduh, masa itu telah lewat,\
mawar lewat, duri demi duri lewat;\
[1728] wajah hilang, kampung pun lewat,\
jiwa kehausan, mabuk sayu pun lewat:\
[1729] *dulu aku peminum anggur bersama sang kekasih.*

[1730] Bersama kekasih aku bersuka dan minum,\
bergolak seperti pusaran;\
[1731] majelis anggur kuselimuti nyala,\
bulbul-bulbulnya kubungkam:\
*dulu aku bertuah seperti Galib.*

## Sabda Memberi Kabar dalam Rupa Burung Nuri {.judul-bagian}

[1732] Selagi bulan itu membaca syair segar ini,\
tiba-tiba terdengar suara ganjil.

[1733] Seekor nuri hijau berparuh merah\
di sebuah dahan mengulang-ulang:

[1734] "Putri Raja Cina, si penumpah darah itu,\
datang ke kebun ini laksana pagi penabur mawar.

[1735] Sayang kau, anak muda, sayang,\
kau kelak kasmaran pada si genit itu.

[1736] Pasti kau sampai ke Benteng Rupa-Rupa,\
di sana kau dijerumuskan ke dalam derita."

[1737] Asmara memandang nuri itu dengan angkuh,\
rahasia tersembunyi pun terbuka.

[1738] Menyebut nama Jelita, berkata, "Mustahil!\
Masa aku membuktikan cinta kepada orang lain?"

[1739] Nuri hijau itu, setelah membeberkan ini,\
terbang menemani Khidir jalan gaib.

[1740] Tiba saatnya, apa yang dilihat Asmara yang bergelora?\
Serombongan bidadari tiba di kebun itu.

[1741] Satu bulan dan serombongan jelita,\
mentari cemerlang di tengah planet-planet.

[1742] Seperti bala tentara malaikat, semua suci,\
seperti tentara akal yang tajam.

[1743] Bulan yang menjadi raja rombongan itu\
ratu bagi tentara peri.

[1744] Bermata bidadari, berparas ruh,\
persis serupa Jelita yang mulia.

[1745] Taman mawar pipi: surga;\
pedang tatapan: pencipta perpisahan.

[1746] Alis: basmalah kitab rahmat;\
bibir: isyarat kepada surah Al-Kautsar.

[1747] Pipi merah: cawan berkilau,\
menuang titik-titik ke pipi mentari.

[1748] Tubuh perak, berhala bak melati,\
tapi pada rupanya diam.

[1749] Setiap saat bercakap dengan isyarat;\
tak punya mulut, apa daya si bulan?

[1750] Si kafir tak pernah berkata sepatah pun,\
juru bahasanya melulu kerling.

[1751] Walhasil, mentari penghias alam itu\
seluruhnya Jelita yang elok,

[1752] hanya saja Jelita pandai bertutur,\
mawar harum melati ini diam.

[1753] Dengan seribu manja wajah diperlihatkan,\
Asmara seketika jadi lukisan di dinding:

[1754] "Jelitakah si wajah rembulan ini,\
yang menjadikan dadaku harta karun api?

[1755] Atau ini peri tempat ini,\
di sisinya bala tentara peri?"

[1756] Selagi Asmara mengulang-ulang pikiran itu,\
belum sempat mengungkapkan ujung benang,

[1757] dibawakan singgasana bertatah permata,\
diletakkan rombongan bertubuh cahaya itu.

[1758] Si wajah rembulan duduk di sana,\
atau mentari terpantul di kolam cahaya.

[1759] Menatap sekeliling dengan cermat,\
memerintah, dan memanggil Asmara.

[1760] Seketika dibawa menghadap,\
cahaya pun tenggelam dalam cahaya.

[1761] Perjamuan riang disiapkan,\
seribu macam sukacita hidup kembali.

[1762] Asmara dihormati berulang-ulang,\
diberi tempat di sisinya.

## Perjamuan Bersuka {.judul-bagian}

[1763] Seketika dibawakan anggur pagi,\
bulan itu mencampur ruh dengan anggur.

[1764] Nampan emas: mentari berkilau;\
piala: bintang-bintang berkilat.

[1765] Di pelukan singgasana, sang raja\
memeluk Asmara seperti bulan.

[1766] Anggur dan piala bergolak demi gelora,\
bulan dan lingkaran cahayanya meneguk demi teguk.

[1767] Anggur berapi itu berombak,\
sampan-sampan berlayar seperti di laut.

[1768] Anggur sewarna merah fajar,\
cawan semerah mawar mengejek bulan.

[1769] Cair, tapi bertabiat delima,\
tinta delima bagi bab-bab *Fusus al-Hikam*.

[1770] Tabiat yang lahir dari nyala penuh nikmat,\
tiap tegukan membangkitkan seribu ketulusan.

[1771] Anggur, tapi darah merak yang murni,\
dalam mabuknya seribu warna terasa.

[1772] Irama lagu dan gamelan dimulai,\
biduannya mabuk, suaranya nyala.

[1773] Di tangan saki piala cahaya,\
dahan kristal menumbuhkan mawar.

[1774] Saki itu si bagai peri sendiri,\
bidadari yang anggurnya api.

[1775] Nampan anggur murni sebuah kolam,\
narsis di bibir kolam cawan berkilau emas.

[1776] Kendi dan piala bibir bertemu bibir,\
bagi si rind tanah dan permata sama.

[1777] Pasar itu ramai kilau,\
sampan pergi kosong, pulang penuh.

[1778] Melihat itu kendi bersyukur,\
tak henti-henti bersujud.

[1779] Bulan dalam cahaya bulan, cahaya bulan dalam bulan,\
anggur tenggelam di botol, botol di anggur.

[1780] Setelah samudra api jadi tamasya,\
topan anggur tampak bergolak.

[1781] Anggur buah anggur seperti yakut,\
piala cahaya seperti intan.

[1782] Bila saki mulai menyindir,\
anggur menjadi sewarna arak putih.

[1783] Warna anggur terbang pudar,\
seolah menjadi bulbul bagi piala.

[1784] Bila si bertubuh melati itu tersipu,\
arak menjadi anggur merah.

[1785] Sekejap peri itu menjadikan\
cawan susu darah Farhad.

[1786] Cawan berkilau di tangan tatapan:\
permata nyawa di tangan Izrail.

[1787] Setiap tatapan meminumkan seribu cawan,\
pedang desah ditimang-timang mata.

[1788] Dalam mabuk itu Asmara melepas pedang,\
berkata, "Pedang itu ada di depan mata."

## Nasib Asmara {.judul-bagian}

[1789] Pagi semerah mawar itu mengambil pedang,\
pergi meninggalkan Asmara merintih, berdarah hati.

[1790] Asmara yang bergelora memandang kebun itu:\
tak tampak tentara peri, tak tampak bidadari.

[1791] Tak ada bulan, tak ada rombongan bintang,\
tak ada raja, tak ada kursi bertatah permata.

[1792] Hati baru mulai menggeliat,\
ditimpa seribu gelisah.

[1793] "Rupanya pertemuan itu perpisahan, sayang;\
bagi pencinta, bersuka itu mustahil, sayang."

[1794] Permulaan diberi akhir,\
pagi malam itu jadi senja.

[1795] Karena Asmara menyangka si genit itu Jelita,\
tertipu rupa, lalu percaya.

[1796] Jalan menakutkan, pedang desah hilang,\
si kekasih yang dikenal itu telah meninggalkan.

[1797] Tak kuat berjalan, tak kuat bertahan,\
Asmara dan Ghirah tertinggal dalam bala.

[1798] Setiap memandang kebun penuh keburukan itu,\
bala jarak menyelar hati.

[1799] Terpana dan tercengang pada rupa itu,\
disangkanya Jelita, lalu meratap.

## Sabda Memberi Kabar dalam Rupa Burung Kuau {.judul-bagian}

[1800] Terdengar seekor kuau yang congkak\
menyampaikan pesan berapi begini:

[1801] "Itu putri Raja Cina;\
jangan kira Jelita, itu lukisan dendam.

[1802] Nama gadis itu Pencuri Akal,\
pembunuh manusia berparas peri.

[1803] Kalau besok bulan itu datang ke kebun ini,\
aduh, kau dibawa ke Benteng Rupa-Rupa."

[1804] Asmara mengumpulkan akal ke kepala,\
tapi percuma, sudah terbakar seperti lilin.

[1805] Mawar haribaan pertemuan itu tinggal\
di kebun itu seperti burung hantu perantauan.

[1806] Benarlah, gadis bertubuh melati itu\
kembali menjadikan kebun itu kediaman.

[1807] Kembali menatap sekeliling,\
memandang Asmara seperti semula.

[1808] Meneguk anggur yang jernih itu,\
samudra kasih bergolak.

[1809] Dengan satu isyarat kepada Asmara,\
dibawanya berjalan beriringan.

[1810] Menuju Benteng Rupa-Rupa,\
raja yang tiada dua itu turun ke jalan.

[1811] Ketika si petaka itu menunggang kuda merah\
dan hendak berangkat, Ghirah pun tahu.

[1812] Katanya kepada Asmara, "Aduh,\
jangan ikut, kau akan tersesat.

[1813] Kau dengar apa kata kuau si nuri;\
aku tak bisa diam sebegini."

[1814] Kata Asmara, "Saudaraku,\
kau lihat raja itu? Mirip Jelita.

[1815] Karena dari satu sisi berkerabat dengan kekasih,\
andai membunuhku pun, pantas.

[1816] Bukankah rida yang pertama dituju?\
Tak senangkah kau pada perkara ini?"

[1817] Ghirah, setia pada janji,\
mau tak mau mengikuti si sesat itu.

[1818] Asmara dan Ghirah bersama si bertubuh melati\
tiba di benteng itu bersama-sama.

[1819] Apa yang terlihat? Benteng yang ganjil,\
di setiap sisinya rupa-rupa, benteng yang ajaib.

[1820] Begitu masuk dari sebuah pintu,\
seketika pintu tertutup dan lenyap.

[1821] Si petaka itu pun menghilang,\
Asmara dan Ghirah terkurung di sana.

## Lukisan Benteng Rupa-Rupa {.judul-bagian}

[1822] Benteng yang serupa Somnath,\
tiap batu hitamnya serupa Lata.

[1823] Pasarnya sewarna gereja,\
kota raya tanpa pintu.

[1824] Setiap lorong dan jalannya pasar Yusuf,\
di dinding-dindingnya lukisan orang elok.

[1825] Lukisannya menyamai langit gugus bintang,\
serupa kamar Zulaikha.

[1826] Seakan pahatan Bisutun,\
Syirin-Syirinnya bulan semerah tulip.

[1827] Tiap kubahnya buatan tangan Farhad,\
tapi tiap batunya kubur Farhad.

[1828] Tak lain jimat khayal,\
tiap rupa upeti negeri rupa.

[1829] Marmernya tatahan halus tanpa warna,\
dindingnya memamerkan rupa-rupa Arzhang.

[1830] Setiap menara lentera khayal,\
hadiah baru bagi zaman.

[1831] Rupa-rupa halus di sana semua\
setipis khayal Syaukat.

[1832] Hayula terpisah dari rupa,\
masa depan tunggal bersama setengah nyawa.

[1833] Rupanya yang melukis semua itu\
putri Raja Cina si penipu.

[1834] Seperti bayangan si pencinta,\
tipu dayanya tak cocok dengan kenyataan.

[1835] Si penuntut kezaliman melukis rupa-rupa ini\
dengan kuas bulu mata peri.

[1836] Bila membuat Mani malu,\
gincu sendawanya jadi otak Bihzad.

[1837] Walhasil, mentari timur Cina itu\
telah menghias benteng ini.

[1838] Setiap rupa diperhatikan Asmara,\
menyebut Jelita, mendesah perpisahan.

[1839] Kata Ghirah, "Naiklah ke kuda merah,\
jangan tinggal di benteng ini, jadilah penempuh."

[1840] Begitu Asmara yang tiada dua menunggang kuda,\
debu jalan dibuatnya menjulang ke langit.

[1841] Mulai melipat jalan itu,\
seketika menempuh jalan seribu bulan.

[1842] Ketika mentari sampai ke barat,\
ternyata dua langkah pun belum ditempuh.

[1843] Masih terkurung di Benteng Rupa-Rupa,\
melihat keadaan diri, putus asa.

[1844] Segala yang dulu pernah terjadi\
di benteng ini terjadi lagi secara rinci:

[1845] jatuh lagi ke sumur seperti dulu,\
ditangkap bala tentara genderuwo;

[1846] menempuh padang salju yang ngeri,\
melihat musibah yang membinasakan;

[1847] bergulat dengan si penyihir,\
di jalan muncul laut api;

[1848] masih banyak lagi rupa ngeri pengiris nyawa,\
bertahun-tahun rintih, tangis, dan desah.

[1849] Dengan seribu takut Asmara menempuh jalan itu,\
sebab pedang desah tak lagi di tangan.

[1850] Tiba-tiba jalan makna terbuka,\
Asmara yang tiada dua menoleh dan melihat:

[1851] persinggahan itu masih persinggahan yang dulu,\
rupa-rupa itu, benteng berjimat itu.

[1852] Mengadu kepada Sesembahan,\
menuturkan keadaan hati:

[1853] "Ya Rabb, berilah si genit itu belas kasih;\
aku sakit, berilah si genit itu sehat.

[1854] Dengan setetes embun ini senangkanlah bulan itu,\
sebab tercapainya maksud dari-Mu.

[1855] Tak lagi ditanyakannya keadaanku,\
sebab kami telah menyembah rupa.

[1856] Aku tak berdaya; Engkau Maha Tahu;\
saat itu aku tiada; Engkau Qadim.

[1857] Mengakui dosa itu perkara sulit,\
tapi mana mungkin menuduh kekasih zalim?

[1858] Mari, jangan hukum cinta kiasanku,\
bila tuturku mengandung isti'arah.

[1859] Mustahil ada yang menyamai-Mu;\
mustahil Engkau lain dan bulan itu lain.

[1860] Karena aku tawanan langit yang berganti-ganti warna,\
mungkinkah tuturku mantap?

[1861] Pasanglah rantai pada si penyembah berhala ini,\
tarik ke kehambaan dalam keadaan remuk.

[1862] Penuhi segala maksudku,\
sampaikan aku ke maksud yang azali.

[1863] Biar si jelita itu menarikku ke dada,\
nikmat dan dukanya menyatu denganku seperti susu dan gula.

[1864] Luruskan; tapi mustahil ini,\
aduhai, ini khayal belaka.

[1865] Meminta yang mustahil dari-Mu itu benar,\
setiap dambaan mungkin terjadi, itu benar.

[1866] Mustahil kukatakan, biar rindu pergi;\
biar kesenangan bertambah, perpisahan pergi.

[1867] Bagi yang riang hatinya, rindu itu bala,\
bagi ahli bala, sebuah kesenangan.

[1868] Biar cawan abadi itu memabukkanku,\
biar pertemuan menambah rindu.

[1869] Aku pesakit duka, penagih derita,\
sudah lama akrab dengan derita.

[1870] Samakan warna obatku dengan deritaku,\
selaraskan tembangku dengan ratapku."

## Sabda Memberi Kabar dalam Rupa Bulbul {.judul-bagian}

[1871] Selagi bulan itu berkeliling sambil meratap,\
tiba-tiba tampak seekor bulbul mabuk.

[1872] Bulbul itu, menyapa Asmara,\
menyambung-nyambung rantai duka:

[1873] "Di benteng ini ada perbendaharaan,\
jangan kira kosong, ada harta karun.

[1874] Bakarlah, biar naik ke langit,\
jadilah pemilik harta cuma-cuma itu.

[1875] Kalau istana indah ini tak kau bakar,\
takkan kau temukan selamanya si pencuri hati.

[1876] Dan putri Raja Cina yang congkak itu\
akan menjadikan hatimu kebab api.

[1877] Selama kubah tinggi ini belum terbakar,\
tak ada kemungkinan kau keluar.

[1878] Jangan bersusah payah sia-sia,\
pintu ini terkunci dengan mantra.

[1879] Ibu gadis itu peri,\
si gadis membelimu dengan nyawa.

[1880] Di antara keduanya banyak tarik-menarik,\
sebab api tak akrab dengan tanah.

[1881] Akhirnya para peri mengincarmu,\
darah hatimu dijadikan anggur.

[1882] Anggur yang diminum di kebun itu\
seluruhnya darah raja-raja.

[1883] Kalau tak mendapat kesempatan mengambil pedangmu,\
tak akan berani memenjarakanmu."

[1884] Begitu Asmara paham perkara ini,\
bangunan itu dibakar.

[1885] Ketika gereja itu tersulut,\
banyak salib berkumpul dengan Isa.

[1886] Rupa-rupanya naik ke langit,\
tujuh sarang ini pun terhias.

[1887] Desah dingin diterbangkan lagi,\
si penyabung nyawa itu aman dari api.

[1888] Benteng terbakar, tanah itu terbakar,\
putri Raja Cina pun terbakar.

[1889] Terbukalah sebuah perbendaharaan berjimat,\
di sana seluruh alam terlukis.

[1890] Tapi di dalamnya tak ada Jelita yang tiada dua;\
Asmara tak menontonnya.

[1891] Di tanah itu ditemukan pedang desah,\
juga anak panah doa dini hari.

[1892] Si bagai peri itu kembali ke jalan,\
membakar diri laksana api.

[1893] Tapi jalan macam apa! Tiap langkah sumur,\
tiap helai rumputnya ular pencabut nyawa.

[1894] Bila teringat pada kekasih,\
diulang-ulangnya kata ini:

[1895] "Wahai bulan, cukup, cukup aniaya ini;\
tolonglah jeritku, sebab jerit pun sudah habis."

## Lukisan Lemahnya Asmara {.judul-bagian}

[1896] Kelemahan kian bertambah\
hingga tak sanggup lagi mendesah dan menjerit.

[1897] Seperti bayang, jatuh dari kuda merah,\
bunga api terpisah dari bara.

[1898] Bulan dunia itu menjadi bulan sabit,\
mentari kemuliaan tergelincir.

[1899] Anggur keelokan berkurang,\
tinggal seteguk di dasar piala kosong.

[1900] Kelemahan yang ujung dari kelemahan,\
bahkan di balik ketiadaan.

[1901] Menjadi gelembung di laut duka,\
tiap menghela napas, hancur.

[1902] Rupa tanpa hayula,\
makna lain tanpa beban huruf.

[1903] Tak kuat lagi tubuh memikul pakaian,\
sutra cahaya bulan pun jadi beban.

[1904] Andai warna pipi mengembangkan sayap,\
terbang ke negeri ketiadaan.

[1905] Nyala seperti kunang-kunang,\
kadang tampak, kadang lenyap.

[1906] Tatapan jadi laut bagi mata,\
cahaya tatapan menutup jalan.

[1907] Tenggelam dalam lemah, si malang itu\
menyangka warnanya sendiri samudra darah.

[1908] Benang pikiran jadi rantai,\
tak sanggup menjelajah negeri pikir.

[1909] Seakan urat sinar tatapannya\
menangkapnya seperti jala ikan.

[1910] Kelemahan membuatnya begitu layu:\
nyala, tapi nyala yang mati.

[1911] Kalau bergerak, berubah jadi udara;\
kalau bergumam, berubah jadi suara.

[1912] Tersakiti oleh gelembung anggur,\
layu oleh harum mawar.

[1913] Tak sanggup menempuh bulan dan tahun,\
tak tersisa kemungkinan hidup.

[1914] Setiap saat umur berlalu,\
bagian-bagian tubuh tercerai-berai.

[1915] Bagian? Jangan sebut bagian: atom yang tak terbagi,\
membaginya pun tak termuat khayal.

[1916] Tiap helai rambut di tubuh seolah rantai,\
tapi rantai itu terlukis pada bayangannya.

[1917] Kalau wajahnya tampak dan kau pandang cermat,\
ketiadaan dan kemungkinan berhimpun di sana.

[1918] Siapa pun yang melihat akan mengakui\
bahwa baka nyata di dalam fana.
