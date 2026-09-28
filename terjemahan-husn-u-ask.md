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
