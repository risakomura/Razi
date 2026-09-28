# Rasāʾil al-Rāghib al-Iṣfahānī: Terjemahan Indonesia

**Judul Indonesia:** *Risalah-Risalah al-Rāghib al-Iṣfahānī*
**Karya:** al-Rāghib al-Iṣfahānī, Abū al-Qāsim al-Ḥusain bin Muḥammad bin al-Mufaḍḍal (w. 502/1108), empat risalah: (1) *Risāla fī Ādāb Mukhālaṭat al-Nās*; (2) *Risāla fī Faḍīlat al-Insān bi-l-ʿUlūm*; (3) *Risāla fī Marātib al-ʿUlūm wa-l-Aʿmāl*; (4) *Risāla fī Dhikr al-Wāḥid wa-l-Aḥad*
**Naskah dasar (Arab):** *Rasāʾil al-Rāghib al-Iṣfahānī*, tahkik ʿUmar ʿAbd al-Raḥmān al-Sārīsī (berkas `0af95d4d-RASAIL_RAGIB.docx`, hasil OCR; data terbitan tidak termuat dalam berkas)
**Naskah pembanding (Turki):** terjemahan Turki keempat risalah yang termuat dalam berkas yang sama (judul terbitan dan nama penerjemah tidak termuat), yang berdasarkan edisi tahkik di atas dan sering membetulkan bacaannya
**Karya pendamping:** terjemahan *al-Dharīʿa ilā Makārim al-Sharīʿa* (`terjemahan-adh-dhariah.md`) dan terjemahan *Tafṣīl al-Nashʾatayn wa Taḥṣīl al-Saʿādatayn* (`terjemahan-tafsil-nashatayn.md`) dalam repositori yang sama, selanjutnya disebut "terjemahan *al-Dharīʿa*" dan "terjemahan *Tafṣīl*"
**Rujukan istilah:** al-Rāghib al-Iṣfahānī, *al-Mufradāt fī Gharīb al-Qurʾān*, ed. Ṣafwān ʿAdnān al-Dāwūdī, 1412/1992 (primer); Muḥammad ʿAlī al-Tahānawī, *Kashshāf Iṣṭilāḥāt al-Funūn wa-l-ʿUlūm*, ed. Rafīq al-ʿAjam dan ʿAlī Daḥrūj, 1996 (pembanding); glosarium terjemahan *al-Dharīʿa* dan *Tafṣīl* (acuan padanan)

---

## 0. Status Proyek dan Penanda Posisi

| Butir | Keterangan |
|---|---|
| Tahap | Selesai |
| Sudah diterjemahkan | Risalah Pertama s.d. Keempat (lengkap) |
| Posisi berikutnya | - |
| Nomor catatan terakhir | CM s13 · CP p113 · CD d55 · CT t4 |
| Catatan istilah | lihat 3.3 |

---

## 1. Konvensi Markup (untuk Pembentukan DOCX)

Markup sama dengan terjemahan *al-Dharīʿa* dan *Tafṣīl*. Setiap baris hanya memuat satu unsur.

| Markup MD | Unsur | Gaya DOCX |
|---|---|---|
| `# Teks {.kitab-ke}` | Nomor risalah: Risalah Pertama, dst. | Kitab Ke |
| `# Teks {.judul-kitab}` | Judul risalah | Judul Kitab |
| `## Teks {.judul-bab}` | Bab di dalam risalah ("Bab" dalam Risalah Pertama, "Pasal" dalam Risalah Kedua) | Judul Bab |
| `### Teks {.judul-pasal}` | Subjudul di dalam bab, atau bagian di dalam Risalah Ketiga dan Keempat | Judul Pasal |
| `[Teks]{.basmalah}` (satu paragraf) | Basmalah pembuka | Basmalah |
| Paragraf biasa | Teks isi | Teks Isi / Teks Isi Pertama |
| `> teks` (satu larik per baris) | Syair | Syair |
| `**Label**:` di awal paragraf | Label pembagian (Pertama, Kedua, dst.) | Label Argumen |
| `*"kutipan"* (Surah: ayat)` | Kutipan ayat beserta rujukannya | Kutipan Ayat + Rujukan Ayat |
| `*"kutipan"*` tanpa rujukan ayat | Kutipan hadis, atsar, atau ucapan | Kutipan Riwayat |
| `*kata*` lainnya | Transliterasi dan judul karya | Transliterasi |
| `[^sN]` | Catatan penjelasan penyunting edisi Arab, ʿUmar al-Sārīsī (awalan **CM:**), diambil secara selektif | Catatan Kaki |
| `[^pN]` | Catatan penerjemah Indonesia (awalan **CP:**), termasuk koreksi bacaan berdasarkan terjemahan Turki | Catatan Kaki |
| `[^dN]` | Catatan rujukan silang ke *al-Dharīʿa* (awalan **CD:**) | Catatan Kaki |
| `[^tN]` | Catatan rujukan silang ke *Tafṣīl* (awalan **CT:**) | Catatan Kaki |
| `[^m-…]` / `[^k-…]` | Catatan istilah *al-Mufradāt* / *Kashshāf* untuk istilah yang belum diberi catatan dalam terjemahan *al-Dharīʿa* dan *Tafṣīl* | Catatan Kaki |
| `[^r-…]` | Rujukan ke catatan istilah yang sudah ada dalam terjemahan *al-Dharīʿa* atau *Tafṣīl* | Catatan Kaki |

Definisi catatan kaki diletakkan tepat sesudah paragraf yang merujuknya. Penanda halaman sumber tidak dipakai.

---

## 2. Keputusan Kerja

1. **Teks dasar:** teks Arab edisi tahkik al-Sārīsī. Teks ini rusak di banyak tempat, baik karena OCR maupun karena kekeliruan tahkik (salah baca huruf bertitik, kata yang tertukar, baris yang berpindah, dan kalimat yang terpotong oleh pergantian halaman). Terjemahan Turki dipakai sebagai saksi kedua; bila ia memberikan bacaan yang lebih masuk akal atau menunjuk sumber lain, bacaan itu diikuti. Pembetulan bacaan yang mengubah makna dicatat singkat dalam catatan **CP**; pembetulan kecil yang jelas (salah cetak, kata terulang) dilakukan tanpa catatan.
2. **Susunan teks:** hasil OCR mencampur teks inti dengan catatan kaki dan kadang memindahkan kalimat ke halaman sesudahnya. Urutan teks inti disusun ulang menurut alur kalimat dan dicocokkan dengan terjemahan Turki.
3. **Catatan penyunting (CM):** diambil secara selektif, yaitu yang menjelaskan teks inti secara berarti (identifikasi orang dan kitab, keterkaitan dengan karya al-Rāghib yang lain, penafsiran). Yang tidak diambil: (a) aparatus tahkik (bacaan naskah, koreksi huruf), (b) takhrij hadis dan rujukan diwan, (c) glos kosakata yang maknanya sudah tertuang dalam terjemahan, (d) biografi yang tidak diperlukan. Catatan penyunting yang keliru dibetulkan dan pembetulannya disebut.
4. **Catatan penerjemah Turki** tidak diterjemahkan tersendiri; pembetulan bacaan dan identifikasinya yang berguna dimasukkan ke dalam catatan **CP** dengan menyebut sumbernya.
5. **Redaksi yang sama dengan *al-Dharīʿa* atau *Tafṣīl*:** bila al-Rāghib memakai redaksi yang sama (ayat, hadis, syair, atau kalimatnya sendiri), terjemahannya mengikuti terjemahan kitab tersebut. Kesamaan gagasan, perbedaan, dan pertentangan dicatat dalam **CD** atau **CT**.
6. **Catatan istilah:** istilah yang sudah diberi catatan dalam terjemahan *al-Dharīʿa* dirujuk dengan nomor nota kakinya ("nota kaki no. N"); istilah yang sudah diberi catatan dalam terjemahan *Tafṣīl* dirujuk dengan nomor catatannya dalam berkas itu. Istilah baru diberi catatan *al-Mufradāt* atau *Kashshāf*.
7. **Padanan istilah** mengikuti glosarium terjemahan *al-Dharīʿa* dan *Tafṣīl*, termasuk: *idrāk* = menangkap, menginsafi, mengidrak (pengidrakan); *taʿaqqul* = menginteleksi; *maʿqūl* = inteligibel; *maḥsūs* = terindra; *ʿaqlī* = akliah; *wahm* = sangkaan; *jawhar* = substansi.
8. Prinsip lain sama dengan terjemahan *al-Dharīʿa* dan *Tafṣīl*: kutipan Al-Qur'an mengikuti Terjemahan Kemenag RI dengan rujukan (Surah: ayat) di badan teks; transliterasi IJMES untuk istilah konseptual; tanpa aksara Arab di badan terjemahan; tanpa tanda pisah panjang dan menengah; tanpa penanda halaman; nama tokoh dalam bentuk lazim Indonesia.

---

## 3. Glosarium

Glosarium ini terdiri atas tiga bagian. Bagian 3.1 memetakan baris-baris glosarium terjemahan *al-Dharīʿa* (dan beberapa baris glosarium terjemahan *Tafṣīl*) yang istilahnya benar-benar terpakai dalam terjemahan ini, dengan kolom yang sama (Arab, transliterasi, padanan Indonesia, Inggris, daya dan disposisi, definisi *al-Mufradāt* = M, definisi *Kashshāf* = K, rumusan *al-Dharīʿa* = D), ditambah kolom letak kemunculan pertama dalam risalah-risalah ini (R1 sampai R4 = Risalah Pertama sampai Keempat). Padanan dalam terjemahan ini mengikuti kolom padanan Indonesia tersebut. Bagian 3.2 memuat istilah yang khas atau baru dalam risalah-risalah ini. Bagian 3.3 mendaftar catatan istilah di badan terjemahan. Tanda † menandai istilah yang dalam terjemahan *al-Dharīʿa* diberi catatan *al-Mufradāt* atau *Kashshāf*.

### 3.1 Istilah yang Dipetakan dari Glosarium *al-Dharīʿa* dan *Tafṣīl*


**Jiwa, Daya-Dayanya, dan Watak** (glosarium *al-Dharīʿa* 3.2)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| العقل | ʿaql | **akal** † | intellect, reason | daya pikir · daya dan keutamaan induk | Dipakai untuk daya yang siap menerima ilmu, dan untuk ilmu yang diperoleh dengan daya itu; karena itu Ali berkata: akal ada dua, yang tertabiat dan yang terdengar. | Dalam skema akhlak, keutamaan daya rasional disebut hikmah, tengah antara kelicikan dan kebebalan. | Induk keutamaan pertama; disempurnakan oleh ilmu; memiliki banyak tingkatan (Pasal II). | R2, Pasal Ketiga |
| العقل الغريزي / المكتسب | al-ʿaql al-gharīzī / al-muktasab (al-mustafād) | **akal bawaan / akal perolehan** | innate / acquired intellect | daya pikir · daya | Lihat *ʿaql*: "yang tertabiat" (*maṭbūʿ*) dan "yang terdengar" (*masmūʿ*). | - | Akal bawaan adalah daya; akal perolehan adalah ilmu yang diraih dengannya. | R2, Pasal Keempat |
| الغضب | ghaḍab | **amarah** † | anger / wrath | daya amarah · keadaan | Mendidihnya darah kalbu karena hendak membalas; bila disifatkan kepada Allah, maksudnya pembalasan. | Gerak jiwa yang bermula dari kehendak membalas; menurut yang lebih cermat, kualitas jiwa yang menggerakkan roh ke luar badan. | - | R1, Bab Kesepuluh |
| الفكر / الفكرة | fikr / fikra | **pikiran; daya pikir** † | thought, reflection | daya pikir · daya | Daya yang menjadi jalan bagi ilmu menuju yang diketahui; *tafakkur* ialah beredarnya daya itu menurut pandangan akal, khas manusia. | Menurut ahli logika terdahulu: gerak jiwa di antara hal-hal inteligibel melalui daya pengolah. | Berpusat di tengah otak, laksana raja di tengah kerajaan. | R2, Pasal Pertama |
| الحفظ | ḥifẓ | **daya hafal** | memory, retention | daya pikir · daya | Keadaan jiwa yang dengannya tetap tersimpan apa yang dihantarkan pemahaman; lawannya lupa. | - | Berpusat di bagian belakang otak; laksana bendahara raja. | R2, Pasal Ketujuh |
| الذكر | dhikr | **daya ingat; ingatan** | remembrance | daya pikir · daya | Keadaan jiwa yang memungkinkan manusia menjaga pengetahuan yang dimilikinya; seperti *ḥifẓ*, tetapi *ḥifẓ* ditinjau dari penyimpanannya, *dhikr* dari penghadirannya. | Lawan lupa; juga ucapan. | - | R2, Pasal Ketujuh |
| الهوى | hawā | **hawa nafsu** † | passion | daya syahwat · keadaan tercela bila menguasai | Kecenderungan jiwa kepada syahwat; dinamai demikian karena menjatuhkan pemiliknya ke segala bencana di dunia dan ke *hāwiya* di akhirat. | Mencintai dan menginginkan; lalu dominan untuk yang tidak terpuji; "ahli hawa" ialah ahli bidah. | Berebut kuasa dengan akal (Pasal I). | R1, Bab Keempat |
| الطبع / الطبيعة | ṭabʿ / ṭabīʿa | **tabiat** † | nature, disposition | - · watak bawaan | Mencetak sesuatu dengan rupa tertentu seperti mencetak mata uang; darinya *ṭabʿ* dan *ṭabīʿa* yang berarti perangai. | Kadang sinonim *ṭibāʿ*, kadang sinonim *ṭabīʿa*: sifat yang tertanam dalam jisim. | Nama bagi daya yang tidak dapat diubah. | R2, Pasal Ketujuh |
| الغريزة | gharīza | **naluri** | instinct | - · watak bawaan | Apa yang tertanam (*ghuriza*) pada manusia, seperti *naḥīta* (watak yang dipahat). | Tabiat; atau kemampuan yang menjadi sumber sifat-sifat zati. | Nama bagi daya yang tak dapat diubah. | R1, Bab Ketiga |
| الفطرة | fiṭra | **fitrah** | primordial nature | - · watak bawaan | Apa yang ditanamkan Allah pada manusia berupa kesanggupan mengenal iman. | Diperselisihkan maknanya dalam hadis fitrah: penciptaan dalam keadaan selamat, atau kesiapan menerima Islam. | - | R3, Tingkatan Amal-Amal Keagamaan |
| الهيئة | hayʾa | **keadaan (disposisi)** | disposition | - · - | Dipakai dalam definisi-definisi al-Rāghib: "keadaan bagi jiwa" (*hayʾa li-l-nafs*). | Rupa, bentuk, dan keadaan sesuatu. | - | R1, Bab Keenam |
| الوهم | wahm | **sangkaan** | estimation | daya pengidrak · - | - | - | Ketundukan jiwa menerima sesuatu tanpa dasar yang pasti (Pasal I). | R2, Pasal Pertama |
| الإرادة | irāda | **kehendak** † | will | daya penggerak · - | Asalnya daya yang tersusun dari syahwat, kebutuhan, dan harapan; lalu nama bagi keterdorongan jiwa kepada sesuatu disertai putusan bahwa ia layak dilakukan atau tidak. Pada Allah yang dimaksud hanyalah putusan itu. | Dalam bahasa: keterdorongan dan kecenderungan jiwa. | - | R1, Bab Kedua |

**Istilah Umum Akhlak dan Tujuan Manusia** (glosarium *al-Dharīʿa* 3.3)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الفضيلة | faḍīla | **keutamaan** † | virtue | - · keutamaan | Keunggulan; ada yang tidak dapat diusahakan (keunggulan jenis) dan ada yang aksidental sehingga dapat diusahakan. | Tidak ada entri. | Nama bagi apa yang membuat manusia memiliki keistimewaan atas yang lain dan yang mengantar kepada kebahagiaan; lawannya *radhīla*. | R1, Bab Kedua |
| الخير | khayr | **kebaikan** † | good | - · - | Apa yang diinginkan semua, seperti akal, keadilan, keutamaan, dan yang bermanfaat; ada yang mutlak dan yang terbatas. | Keutamaan dan kebajikan; para filsuf menyebut wujud kebaikan murni dan ketiadaan keburukan murni. | Kebaikan mutlak ialah yang dipilih demi dirinya sendiri dan yang karenanya dipilih yang lain; ada tiga: yang bermanfaat, yang indah, yang lezat. | R1, Bab Kedua |
| السعادة | saʿāda | **kebahagiaan** † | happiness | - · tujuan | Pertolongan urusan-urusan ilahi kepada manusia untuk meraih kebaikan; yang teragung adalah surga. | Dalam kalangan sufi: seruan azali. | Kebahagiaan mutlak ialah kebaikan hidup di akhirat: kekal, kuasa, ilmu, dan kaya tanpa lawannya. | R2, Mukadimah |
| العبادة | ʿibāda | **ibadah** † | worship | - · perbuatan | Puncak perendahan diri, yang tidak berhak menerimanya kecuali yang memiliki puncak karunia, yaitu Allah; ada ibadah karena ditundukkan dan ibadah dengan pilihan. | Puncak pengagungan. | Salah satu dari tiga tujuan penciptaan manusia (Pasal I). | R1, Bab Keenam |
| الخلافة | khilāfa | **kekhalifahan** † | vicegerency | - · kedudukan | Menggantikan yang lain, karena ketiadaannya, kematiannya, ketidakmampuannya, atau untuk memuliakan yang digantikan; dengan makna terakhir Allah menjadikan wali-wali-Nya khalifah di bumi. | Dalam syariat: imamah. | Hanya sah dengan kesucian jiwa. | R2, Pasal Pertama |
| الإنسانية | insāniyya | **kemanusiaan** | humanity | gabungan · himpunan keutamaan | *Uns*: lawan keliaran; manusia dinamai demikian karena tidak dapat hidup tanpa saling bersahabat. | Tidak ada entri. | Lihat 3.1c. | R1, Bab Pertama |
| الظرف | ẓarf | **keluwesan (keanggunan pergaulan)** | gracefulness | gabungan · himpunan keutamaan | Tidak ada entri dengan makna ini. | Tidak ada entri dengan makna ini. | Lihat 3.1c. | R1, Bab Kesebelas |
| الحسب / الشرف | ḥasab / sharaf | **kemuliaan asal / kehormatan** | noble descent / nobility | luar diri · keutamaan luar | Tidak ada entri dengan makna ini. | *Ḥasab*: keturunan dan kebangsawanan. | Lihat 3.1c. | R1, Bab Kesepuluh |

**Keutamaan Taufik, Keutamaan Badan, dan Keutamaan Luar** (glosarium *al-Dharīʿa* 3.4)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| القوة | quwwa | **kekuatan; daya** | strength; faculty | badan · keutamaan badan | Dipakai untuk kemampuan, untuk kesiapan pada sesuatu (potensi), dan untuk kekuatan badan. | Sumber perbuatan secara mutlak; mencakup daya langit, unsur, tumbuhan, dan hewan. | Keutamaan badan; juga istilah untuk daya jiwa. | R3, Mukadimah |
| الفقر | faqr | **kefakiran** † | poverty | luar diri · keadaan | Ada empat: kebutuhan asasi yang meliputi semua makhluk; ketiadaan harta; kefakiran jiwa, yaitu kerakusan; kefakiran kepada Allah. | Tidak ada entri. | Kefakiran dan ketakutan terhadapnya menjadi sebab teraturnya urusan manusia (Pasal VI). | R1, Bab Keenam |

**Akal, Ilmu, dan Iman** (glosarium *al-Dharīʿa* 3.5)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الحكمة | ḥikma | **hikmah** † | wisdom | daya pikir · keutamaan | Mengenai kebenaran dengan ilmu dan akal; dari Allah: mengenal dan mewujudkan segala sesuatu secara paling kokoh; dari manusia: mengenal yang ada dan melakukan kebaikan. | Mengokohkan perbuatan dan ucapan; dalam skema akhlak: keadaan daya rasional praktis yang tengah antara kelicikan dan kebebalan. | Dalam *al-Dharīʿa* disebut sebagai kebaikan mutlak: bermanfaat, indah, dan lezat. | R1, Bab Kesepuluh |
| الفهم | fahm | **pemahaman** † | understanding | daya pikir · keutamaan turunan | Keadaan pada manusia yang dengannya ia mewujudkan makna apa yang baik. | Tidak ada entri. | Pengantar akal; menangkap hal-hal partikular, sedang akal menangkap yang universal. | R2, Pasal Ketujuh |
| الفطنة | fiṭna | **kecerdasan (fatanah)** | intelligence, sagacity | daya pikir · keutamaan turunan | Tidak ada entri khusus. | Sama dengan pemahaman; atau baiknya kesiapan jiwa menangkap apa yang datang dari luar; lawannya *ghabāwa*. | Cepatnya menangkap sesuatu yang sengaja dibuat pelik, karena itu banyak dipakai untuk memecahkan teka-teki dan isyarat. | R2, Pasal Ketujuh |
| الذكاء | dhakāʾ | **ketajaman akal** | acuteness | daya pikir · keutamaan | Dari *dhakat al-nār*, api menyala terang. | Cepatnya kecerdasan; atau kuatnya daya jiwa yang siap memperoleh pendapat. | Ketangkasan dalam urusan dan cepatnya memutus kebenaran. | R2, Pasal Ketujuh |
| الجهل | jahl | **kebodohan** † | ignorance | daya pikir · keburukan | Ada tiga: kosongnya jiwa dari ilmu; meyakini sesuatu tidak sesuai kenyataannya; melakukan sesuatu tidak sebagaimana mestinya. | Jahil sederhana (tiadanya ilmu) dan jahil tersusun (keyakinan yang tidak sesuai kenyataan). | Manusia dalam kebodohan ada empat tingkat (Pasal II). | R1, Bab Kesepuluh |
| اليقين | yaqīn | **keyakinan** † | certitude | daya pikir · keadaan | Sifat ilmu di atas makrifat dan dirayah; tenangnya pemahaman disertai kukuhnya putusan. | Keyakinan pasti yang sesuai kenyataan dan tidak goyah oleh keraguan. | - | R3, Tingkatan Ilmu-Ilmu Agama |

**Tutur dan Diam** (glosarium *al-Dharīʿa* 3.6)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الصدق | ṣidq | **kejujuran** † | truthfulness | daya pikir · keutamaan | Kejujuran dan dusta pada asalnya dalam ucapan, khususnya berita; secara aksidental dalam jenis ucapan lain dan dalam perbuatan. | Kesesuaian berita dengan kenyataan; dibedakan antara kejujuran penutur dan kejujuran berita. | Hanya baik bila berkaitan dengan manfaat dan tidak mencelakakan orang; karena itu adu domba dan gunjingan buruk meski benar. | R1, Bab Kelima |
| النميمة | namīma | **adu domba** † | slander, tale-bearing | daya syahwat · keburukan | Tidak ada entri khusus. | Tidak ada entri. | Menyampaikan ucapan orang kepada orang lain untuk merusak; buruk walaupun benar. | R1, Bab Kesebelas |

**Daya Syahwat dan Turunannya (Pasal III)** (glosarium *al-Dharīʿa* 3.7)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الوقاحة | waqāḥa | **muka tebal (tak tahu malu)** | shamelessness | syahwat · keburukan (kurang) | Tidak ada entri. | Tidak ada entri. | Keras kepalanya jiwa dalam melakukan keburukan; lepas dari kemanusiaan; dari *ḥāfir waqāḥ*, kuku kaki yang keras. | R3, Tingkatan Amal-Amal Keagamaan |
| الوفاء | wafāʾ | **menepati janji (kesetiaan)** † | loyalty, fulfilment | gabungan · keutamaan | Menyempurnakan janji dan menepatinya. | Memelihara kasih dan janji. | Saudara kejujuran dan keadilan: jujur dengan lisan dan perbuatan sekaligus; khas manusia. | R1, Bab Ketujuh |
| العجب | ʿujb | **ujub (kagum diri)** † | self-conceit | gabungan · keburukan | *ʿAjab* dan *taʿajjub*: keadaan yang menimpa manusia karena tidak mengetahui sebab sesuatu (tidak mengenai *ʿujb* dalam arti akhlak). | Memandang diri dan amal diri, yakni membesarkan diri. | Sangkaan manusia bahwa dirinya layak mendapat kedudukan yang tidak layak baginya. | R3, Tingkatan Amal-Amal Keagamaan |
| اللذة | ladhdha | **kelezatan (kenikmatan)** † | pleasure | syahwat · keadaan | Tidak ada entri khusus. | Lawan rasa sakit; pengidrakan dan perolehan atas apa yang bagi yang mengidrak adalah kesempurnaan dan kebaikan. | Ada kelezatan akliah, badani, dan yang bercampur (Pasal III). | R1, Bab Kedua |
| العفة | ʿiffa | **kesucian diri** † | temperance, chastity | syahwat · keutamaan induk (tengah) | Hadirnya keadaan pada jiwa yang dengannya ia tercegah dari dikuasai syahwat; *mutaʿaffif*: yang mengupayakannya dengan latihan dan paksaan diri. | Keadaan daya syahwat yang tengah antara kedurjanaan dan padamnya syahwat. | Induk keutamaan; disempurnakan oleh warak; melahirkan kanaah. | R1, Bab Kesepuluh |
| الزهد | zuhd | **zuhud** † | asceticism | syahwat · keutamaan | Yang berpaling dari sesuatu dan rida dengan yang sedikit (*zahīd*). | Dalam bahasa: berpaling karena meremehkan; dalam syariat: mengambil sekadar keperluan dari yang pasti halal. | Membatasi diri pada yang sedikit; zuhud tanpa kanaah hanyalah pura-pura zuhud. | R1, Bab Pertama |

**Daya Amarah dan Turunannya (Pasal IV)** (glosarium *al-Dharīʿa* 3.8)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الشجاعة | shajāʿa | **keberanian** † | courage | amarah · keutamaan induk (tengah) | Tidak ada entri khusus (hanya di bawah *basāla*: keberanian disebut juga *basāla*). | Keadaan daya amarah yang tengah antara kenekatan (berlebih) dan kepengecutan (kurang). | Bila ditinjau dalam jiwa: teguhnya kalbu menghadapi kengerian; bila ditinjau dalam perbuatan: maju pada saat yang tepat; tengah antara kenekatan dan kepengecutan; lahir dari kekagetan dan amarah yang seimbang. | R1, Bab Kesepuluh |
| الخوف | khawf | **takut** † | fear | amarah · keadaan | Menanti hal yang tidak disukai berdasarkan tanda yang diduga atau diketahui; lawannya rasa aman. | Menurut ahli suluk: malu kepada maksiat dan pedih karenanya. | Cara menghilangkan takut (Pasal IV). | R3, Tingkatan Amal-Amal Keagamaan |
| الهيبة | hayba | **rasa segan** † | reverence, awe | - · keadaan | Tidak ada entri. | Lawan *uns* (keakraban). | Gentar yang mengundang ketundukan karena pengagungan; dipakai untuk setiap orang yang disegani. | R1, Bab Kedelapan |

**Keadilan, Kezaliman, Cinta, dan Kebencian (Pasal V)** (glosarium *al-Dharīʿa* 3.9)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| العدل / العدالة | ʿadl / ʿadāla | **keadilan** † | justice | seluruh daya · keutamaan induk | Kata yang menuntut makna kesetaraan, dipakai dengan memperhatikan hubungan; *ʿadl* untuk yang ditangkap mata batin (hukum), *ʿidl* untuk yang ditangkap indra; adil ialah membagi secara setara. | Dalam syariat: tercegah dari larangan-larangan agama, yaitu unggulnya sisi agama dan akal atas hawa nafsu dan syahwat; dalam skema akhlak: keadaan yang lahir dari terhimpunnya tiga keutamaan. | Titik tengah yang semua sisinya adalah *jawr*; laksana titik pusat lingkaran. | R1, Bab Keenam |
| المحبة / الحب | maḥabba / ḥubb | **cinta** † | love | gabungan · keadaan | Menghendaki apa yang dipandang atau diduga baik; ada tiga: cinta karena kenikmatan, karena manfaat, dan karena keutamaan. | Diperselisihkan: sinonim kehendak dalam arti kecenderungan, atau kualitas rohani yang timbul dari gambaran kesempurnaan mutlak. | Kecenderungan jiwa kepada apa yang dipandang atau diduga baik; ada yang alami dan yang atas pilihan. | R1, Bab Kedua |
| العشق | ʿishq | **cinta berahi (cinta yang berlebih)** † | passionate love | syahwat · keadaan | Tidak ada entri. | Tingkat cinta yang terakhir; berlebihnya cinta. | Cinta yang berlebih: tercela bila karena kenikmatan, terpuji bila karena keutamaan; tidak pernah karena manfaat. | R1, Bab Kelima |
| الصداقة | ṣadāqa | **persahabatan** † | friendship | gabungan · keutamaan | Benarnya keyakinan dalam kasih sayang; khas manusia. | Menurut ahli suluk: samanya kalbu dalam kesetiaan dan kekecewaan, dalam memberi dan menahan. | Lebih khusus daripada cinta; jarang terjadi di antara orang banyak. | R1, Mukadimah |
| الألفة | ulfa | **keakraban (kerukunan)** † | fellowship | gabungan · keadaan | Berkumpul disertai kecocokan. | Menurut ahli suluk: kecenderungan kalbu kepada yang biasa dengannya. | Apa yang terjadi di antara hewan disebut *ulfa*, bukan cinta. | R1, Bab Pertama |
| الود / المودة | wudd / mawadda | **kasih sayang** † | affection | gabungan · keadaan | Mencintai sesuatu dan mengharapkan keberadaannya. | Menurut ahli suluk: cinta yang bergejolak. | - | R1, Bab Kelima |
| التفرد / العزلة | tafarrud / ʿuzla | **menyendiri** † | solitude | - · keadaan | Tidak ada entri. | *ʿUzla* dari nafsu, *khalwa* dari orang lain. | Makruh kecuali bagi penguasa, orang bijak, dan ahli ibadah; terpuji bila menjauh dari orang rendah. | R1, Mukadimah |

**Keahlian, Penghidupan, Harta, dan Pemberian (Pasal VI)** (glosarium *al-Dharīʿa* 3.10)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الكسل | kasal | **kemalasan** | sloth | - · keburukan | Merasa berat terhadap apa yang semestinya tidak diberatkan; karena itu tercela. | Tidak ada entri. | - | R1, Bab Pertama |
| الإيثار | īthār | **mendahulukan orang lain** | altruism | gabungan · keutamaan tertinggi dalam pemberian | *Īthār*: mengutamakan; dari *athar* yang dipinjam untuk keutamaan. | Tidak ada entri. | Tingkat kemurahan yang tertinggi (Pasal VI). | R1, Bab Kelima |
| الجد / البخت | jadd / bakht | **nasib / keberuntungan** † | luck, fortune | - · - | Tidak ada entri untuk *bakht*. | *Bakht* sama dengan *jadd*. | Bagian nasib dalam harta lebih besar daripada jerih payah (*kadd*); sebaliknya dalam keutamaan. | R2, Mukadimah |

**Perbuatan (Pasal VII)** (glosarium *al-Dharīʿa* 3.11)

| Arab | Transliterasi | Padanan Indonesia | Inggris | Daya · Disposisi | M | K | D | Letak pertama |
|---|---|---|---|---|---|---|---|---|
| الروية | rawiyya | **pertimbangan** | deliberation | pikiran · - | Tidak ada entri. | Tidak ada entri. | Pembeda perbuatan berkehendak: dari pertimbangan (pilihan) atau tanpa pertimbangan. | R1, Bab Ketiga |

**Dari glosarium terjemahan *Tafṣīl* (3.2)**

| Arab | Transliterasi | Padanan Indonesia | Inggris | Definisi ringkas | Sumber | Catatan | Letak pertama |
|---|---|---|---|---|---|---|---|
| المعاد | maʿād | **hari kembali** | return, resurrection | Kembalinya manusia kepada Allah sesudah kematian; diingkari kaum naturalis (*ṭabīʿiyyūn*). | D | catatan *Tafṣīl* `p47` | R1, Bab Kedua |
| الجوهر | jawhar | **substansi** | substance / essence | Yang ada yang berdiri sendiri, lawan aksiden (*ʿaraḍ*); juga hakikat dan zat. Di sini arti pertama. Padanan "esensi" pada edisi pertama direvisi. | K | catatan *Tafṣīl* `k-jawhar` | R1, Bab Keempat |

Penyesuaian padanan: *ḥifẓ* diterjemahkan "hafalan" (bukan "daya hafal"), karena dalam Risalah Kedua ia didefinisikan sebagai hasilnya, yaitu "tetapnya rupa apa yang telah tercetak dalam jiwa"; *maʿād* diterjemahkan "tempat kembali" sesuai konteks ungkapan "kebaikan tempat kembali"; *wafāʾ* diterjemahkan "kesetiaan", padanan kedua dalam glosarium *al-Dharīʿa*, karena dalam risalah ini ia sifat sahabat, bukan tindakan menepati janji tertentu.

### 3.2 Istilah Khas *Rasāʾil*

Istilah-istilah berikut tidak terdapat dalam glosarium *al-Dharīʿa* dan *Tafṣīl*, atau terdapat di sana tetapi dipakai dalam arti yang khas dalam risalah-risalah ini. Definisinya diambil dari badan terjemahan dan catatan istilahnya. Kolom sumber: M = *al-Mufradāt*, K = *Kashshāf*, D = *al-Dharīʿa*, CM = catatan penyunting.

| Arab | Transliterasi | Padanan Indonesia | Inggris | Definisi ringkas | Sumber | Catatan | Letak pertama |
|---|---|---|---|---|---|---|---|
| المخالطة / الاختلاط | mukhālaṭa / ikhtilāṭ | **bergaul; pergaulan** | social intercourse | Berhimpun dan bercampur dengan manusia dalam urusan hidup, lawan *ʿuzla*, *tafarrud*, *mujānaba*; asalnya *khalṭ*, menghimpun bagian-bagian dua hal atau lebih. | M | `m-khalt` | R1, Mukadimah |
| المجانبة | mujānaba | **memisahkan diri** | avoidance | Menjauhi manusia; dipakai berpasangan dengan *ʿuzla* dan *tafarrud*. | - | `m-khalt` | R1, Mukadimah |
| الجبلّة | jibilla | **pembawaan ciptaan** | innate constitution | Keadaan yang padanya manusia diciptakan; dekat dengan *gharīza* dan *ṭabʿ*. | - | - | R1, Bab Pertama |
| مدنيّ بالطبع | madanī bi-l-ṭabʿ | **makhluk kota menurut tabiatnya** | political/civic by nature | Rumusan filsafat bahwa manusia tidak dapat hidup tanpa berkumpul dan saling membutuhkan. | CM | `s3` | R1, Bab Pertama |
| المشاكلة | mushākala | **keserupaan** | congeniality, likeness | Keserupaan dalam bentuk dan rupa (lawan *nidd*, keserupaan jenis, dan *shibh*, keserupaan kualitas); dalam risalah ini kecocokan naluriah yang menarik satu hal kepada yang lain. | M | `m-shakl` | R1, Mukadimah |
| الملاءمة / المنافرة | mulāʾama / munāfara | **kecocokan / penolakan** | affinity / repulsion | Kecocokan dan penolakan dalam asal penciptaan, yang sejenis dengan cinta dan permusuhan, terdapat juga pada hewan dan benda mati. | M | `m-nafr` | R1, Bab Ketiga |
| الطلسم | ṭilasm | **azimat** | talisman | Perkara luar biasa yang bersumber dari daya-daya langit yang aktif yang dipadukan dengan penerima-penerima bumi yang pasif. | K | `k-tilasm` | R1, Bab Ketiga |
| النفع / المنفعة | nafʿ / manfaʿa | **manfaat** | benefit, utility | Apa yang dipakai sebagai pertolongan untuk sampai kepada kebaikan; salah satu dari tiga sebab cinta (kelezatan, manfaat, keutamaan). | M | `m-naf` | R1, Bab Kedua |
| الخلّة / الخليل | khulla / khalīl | **persahabatan karib / sahabat karib** | intimate friendship / bosom friend | Kasih sayang yang disertai kebutuhan; dari *khalal* (celah), lalu dipinjam untuk kebutuhan dan kefakiran. | M | `m-khulla` | R1, Mukadimah |
| الأخوّة | ukhuwwa | **persaudaraan** | brotherhood | Kokohnya ikatan karena kelahiran atau karena cinta; dari *ākhiya*, tali tambatan hewan. | M | `m-akh` | R1, Bab Kelima |
| الوجد | wajd | *wajd* (kesedihan cinta) | ecstasy; grief of love | "Mendapati" dengan daya jiwa; dalam risalah ini kesedihan yang lahir dari cinta; dalam pemakaian sufi keadaan rohani yang datang kepada kalbu. | M, K | `m-wajd` | R1, Bab Kelima |
| الهيمان | hayamān | *hayamān* (kegilaan cinta) | love-madness | Semacam kegilaan yang lahir dari cinta berahi; asalnya dahaga yang sangat. | - | `p29` | R1, Bab Kelima |
| البلادة | balāda | **ketumpulan** | dullness | Tumpulnya orang yang mencinta, yang dibutakan dan ditulikan oleh cintanya. | - | `p27` | R1, Bab Kelima |
| المراد / المريد | murād / murīd | **yang dikehendaki / yang menghendaki** | the desired / the aspirant | Dalam pemakaian sufi: *murīd* penempuh jalan yang berusaha, *murād* yang ditarik oleh Allah (*al-sālik al-majdhūb*). | K | `k-murid` | R1, Bab Keenam |
| المداراة | mudārāt | **sikap lunak** | courtesy, tactful gentleness | Bersikap lunak kepada manusia demi kelangsungan pergaulan; "sepertiga dari hidup bersama". | - | - | R1, Bab Kedua Belas |
| الملّيّ | millī | **keagamaan** | religious (revealed) | Ilmu yang bersumber dari nukilan agama, lawan ilmu akliah. | - | `r-milla` | R2, Pasal Kelima |
| الحكميّ | ḥikamī | **hikmah (ilmu hikmah)** | philosophical | Ilmu yang dituntut oleh akal dan agama sekaligus: ilmu hitung, bintang, geometri, alam, firasat, kedokteran; logika sebagai alatnya. | - | `r-hikma2` | R2, Pasal Kelima |
| الذهن | dhihn | **daya tangkap** | mind, quickness of apprehension | Salah satu daya akal yang menjadi alat bagi ilmu, disebut bersama *dhakāʾ* dan *fiṭna*. | - | - | R2, Pasal Ketujuh |
| العقل الهيولانيّ | al-ʿaql al-hayūlānī | **akal hayulani** | material intellect | Nama filosofis akal bawaan, akal yang dengannya manusia terbedakan dari hewan dan taklif berlaku. | - | `r-ghariza2` | R2, Pasal Keempat |
| الضروريّ | ḍarūrī | **ilmu niscaya** | necessary knowledge | Ilmu yang diperoleh tanpa perantara; disebut juga akal bawaan dan fitrah. | - | - | R3, Tingkatan Ilmu-Ilmu Agama |
| الإنّيّة | inniyya | **keberadaan** | existence (that-it-is) | Adanya sesuatu; di sini keberadaan Sang Pencipta yang ditetapkan dengan penalaran. | - | - | R3, Tingkatan Ilmu-Ilmu Agama |
| الموهبة / علوم الحقائق | mawhiba / ʿulūm al-ḥaqāʾiq | **ilmu anugerah / ilmu-ilmu hakikat** | bestowed knowledge | Tersingkapnya keyakinan tanpa usaha; tingkatan ilmu keempat dan tertinggi. | - | `r-yaqin` | R3, Tingkatan Ilmu-Ilmu Agama |
| العلماء / الحكماء / الكبراء | ʿulamāʾ / ḥukamāʾ / kubarāʾ | **ulama / para hakim / para pembesar** | scholars / sages / the great ones | Tiga golongan menurut ilmu yang diperoleh: ilmu yang diusahakan, ilmu akhlak yang diamalkan, dan ilmu anugerah. | - | `p96` | R3, Tingkatan Ilmu-Ilmu Agama |
| القدرة | qudra | **kuasa** | power, capacity | Keadaan pada manusia yang dengannya ia mampu berbuat; bila disifatkan kepada Allah, tiadanya kelemahan. Dibedakan dari *quwwa*. | M | `m-qudra` | R3, Mukadimah |
| الزيغ / الغباوة / الرين / الانهماك | zaygh / ghabāwa / rayn / inhimāk | **penyimpangan / kebebalan / karat / tenggelam** | deviation / dullness / rust / immersion | Derajat-derajat turun dari keutamaan menuju keburukan, mengikuti redaksi *al-Dharīʿa*, Pasal Pertama. | D | `d53` | R3, Tingkatan Amal-Amal Keagamaan |
| الواحد | wāḥid | *wāḥid* (satu, esa) | one | Pada asalnya sesuatu yang darinya bilangan tersusun, sesuatu yang sama sekali tidak memiliki bagian; lalu dipakai untuk setiap yang ada dengan berbagai cara. | M | `m-wahid` | R4, Lafal al-Wāḥid |
| الأحد / الوحد | aḥad / waḥad | *aḥad* (esa) | the One | Kesatuan murni, masdar; asalnya *waḥad*, lalu dikhususkan untuk menyifati Allah; *waḥad* untuk selain-Nya berarti "yang sendiri". | M, K | `m-ahad`, `k-ahad` | R4, Lafal al-Aḥad |
| الوحدة / الكثرة | waḥda / kathra | **kesatuan / kebanyakan** | unity / multiplicity | *Waḥda* ialah kesendirian (*infirād*); segala yang disifati dengan wujud juga disifati dengan kesatuan. | M, K | `m-wahid` | R4, Lafal al-Wāḥid |
| الفيض | fayḍ | **limpahan** | emanation | Istilah para filsuf untuk keluarnya maujud dari Sang Pencipta; al-Rāghib hanya berisyarat kepadanya. | - | `p111` | R4, Penutup |

### 3.3 Daftar Catatan Istilah di Badan Terjemahan

Catatan istilah ada dua jenis. Catatan baru dari *al-Mufradāt* (`m-…`) dan *Kashshāf* (`k-…`) diberikan untuk istilah yang belum diberi catatan dalam terjemahan *al-Dharīʿa* dan *Tafṣīl*. Catatan rujukan (`r-…`) menunjuk nomor nota kaki terjemahan *al-Dharīʿa* (menurut urutan nota kaki dalam berkas dan DOCX-nya) atau nomor catatan terjemahan *Tafṣīl*, kadang disertai penjelasan pemakaian khas istilah itu dalam risalah ini. Daftar ini disusun menurut urutan kemunculan.

| Kunci | Istilah | Jenis | Letak |
|---|---|---|---|
| `m-khalt` | Bergaul (*mukhālaṭa*, *ikhtilāṭ*) | *al-Mufradāt* | R1, Mukadimah |
| `r-sadaqa` | Persahabatan (*ṣadāqa*) | rujukan *al-Dharīʿa* no. 364, 365 | R1, Mukadimah |
| `r-uzla` | Menyendiri (*ʿuzla*, *tafarrud*, *khalwa*) | rujukan *al-Dharīʿa* no. 373 | R1, Bab Pertama |
| `r-ulfa` | Keakraban (*ulfa*) | rujukan *al-Dharīʿa* no. 362 | R1, Bab Pertama |
| `m-shakl` | Keserupaan (*mushākala*, *shakl*) | *al-Mufradāt* | R1, Bab Pertama |
| `r-ins` | Manusia dan keakraban (*insān*, *uns*) | rujukan *al-Dharīʿa* no. 370; *Tafṣīl* no. 4 | R1, Bab Pertama |
| `r-kasal` | Kemalasan (*kasal*) | rujukan *al-Dharīʿa* no. 145 | R1, Bab Pertama |
| `r-zuhd` | Zuhud (*zuhd*) | rujukan *al-Dharīʿa* no. 285, 286 | R1, Bab Pertama |
| `r-mahabba` | Cinta (*maḥabba*) | rujukan *al-Dharīʿa* no. 360, 361, 73, 74 | R1, Bab Kedua |
| `r-fadila` | Keutamaan (*faḍīla*) | rujukan *al-Dharīʿa* no. 102 | R1, Bab Kedua |
| `m-naf` | Manfaat (*nafʿ*, *manfaʿa*) | *al-Mufradāt* | R1, Bab Kedua |
| `r-ladhdha` | Kelezatan (*ladhdha*) | rujukan *al-Dharīʿa* no. 265 | R1, Bab Kedua |
| `r-khayr` | Kebaikan (*khayr*) | rujukan *al-Dharīʿa* no. 99, 100 | R1, Bab Kedua |
| `m-nafr` | Penolakan (*munāfara*, *nafr*) | *al-Mufradāt* | R1, Bab Ketiga |
| `k-tilasm` | Azimat (*ṭilasm*) | *Kashshāf* | R1, Bab Ketiga |
| `r-ghariza` | Naluri (*gharīza*) | rujukan *al-Dharīʿa* no. 78 | R1, Bab Ketiga |
| `r-jawhar` | Substansi (*jawhar*, *jawhariyya*) | rujukan *Tafṣīl* no. 36 | R1, Bab Keempat |
| `r-hawa` | Hawa nafsu (*hawā*) | rujukan *al-Dharīʿa* no. 66 | R1, Bab Keempat |
| `m-hubb` | Cinta: asal kata (*ḥubb*, *ḥabba*) | *al-Mufradāt* | R1, Bab Kelima |
| `m-khulla` | Persahabatan karib (*khulla*, *khalīl*) | *al-Mufradāt* | R1, Bab Kelima |
| `r-wudd` | Kasih sayang (*wudd*, *mawadda*) | rujukan *al-Dharīʿa* no. 367 | R1, Bab Kelima |
| `m-akh` | Saudara (*akh*, *ukhuwwa*) | *al-Mufradāt* | R1, Bab Kelima |
| `r-ishq` | Cinta berahi (*ʿishq*) | rujukan *al-Dharīʿa* no. 277 | R1, Bab Kelima |
| `r-hawa2` | Hawa nafsu (*hawā*) | rujukan *al-Dharīʿa* no. 66, 67 | R1, Bab Kelima |
| `m-wajd` | Wajd (*wajd*, *wujūd*) | *al-Mufradāt* | R1, Bab Kelima |
| `r-sidq` | Kejujuran (*ṣidq*) | rujukan *al-Dharīʿa* no. 206, 207 | R1, Bab Kelima |
| `r-ibada` | Ibadah (*ʿibāda*) | rujukan *al-Dharīʿa* no. 46, 47; *Tafṣīl* no. 74 | R1, Bab Keenam |
| `k-murid` | Yang dikehendaki (*murād*) | *Kashshāf* | R1, Bab Keenam |
| `r-faqr` | Kefakiran (*faqr*) | rujukan *al-Dharīʿa* no. 287, 288 | R1, Bab Keenam |
| `r-wafa` | Kesetiaan (*wafāʾ*) | rujukan *al-Dharīʿa* no. 238, 239 | R1, Bab Ketujuh |
| `r-adl` | Keadilan (*ʿadl*, *ʿadāla*) | rujukan *al-Dharīʿa* no. 61; *Tafṣīl* no. 156 | R1, Bab Kedelapan |
| `r-hasab` | Kemuliaan keturunan (*ḥasab*) | rujukan *al-Dharīʿa* no. 106 | R1, Bab Kesepuluh |
| `r-hikma` | Hikmah, kesucian diri, keberanian (*ḥikma*, *ʿiffa*, *shajāʿa*) | rujukan *al-Dharīʿa* no. 38, 39, 56, 57, 58, 61 | R1, Bab Kesepuluh |
| `r-jahl` | Kebodohan (*jahl*) | rujukan *al-Dharīʿa* no. 186, 187 | R1, Bab Kesepuluh |
| `r-ghadab` | Amarah (*ghaḍab*) | rujukan *al-Dharīʿa* no. 295, 296 | R1, Bab Kesepuluh |
| `r-saada` | Kebahagiaan (*saʿāda*) | rujukan *al-Dharīʿa* no. 91, 92 | R2, Mukadimah |
| `r-wahm` | Sangkaan (*wahm*) | rujukan *Tafṣīl* no. 86 | R2, Pasal Pertama |
| `r-fikr` | Pikiran dan pertimbangan (*fikr*, *rawiyya*) | rujukan *al-Dharīʿa* no. 30 | R2, Pasal Pertama |
| `r-khilafa` | Kekhalifahan (*khilāfa*) | rujukan *al-Dharīʿa* no. 6; *Tafṣīl* no. 27 | R2, Pasal Pertama |
| `r-aql` | Akal (*ʿaql*) | rujukan *al-Dharīʿa* no. 93, 94; *Tafṣīl* no. 24 | R2, Pasal Ketiga |
| `r-ghariza2` | Akal bawaan dan akal perolehan (*al-ʿaql al-gharīzī*, *al-ʿaql al-mustafād*) | rujukan *al-Dharīʿa* no. 78 | R2, Pasal Keempat |
| `r-milla` | Keagamaan (*millī*) | rujukan (glosarium/bahasan) | R2, Pasal Kelima |
| `r-hikma2` | Hikmah (*ḥikma*) | rujukan *al-Dharīʿa* no. 38, 39; *Tafṣīl* no. 46 | R2, Pasal Kelima |
| `r-khayr2` | Kebaikan (*khayr*) | rujukan (glosarium/bahasan) | R2, Pasal Keenam |
| `r-tab` | Tabiat (*ṭabʿ*) | rujukan *al-Dharīʿa* no. 76, 77; *Tafṣīl* no. 56 | R2, Pasal Ketujuh |
| `r-quwa` | Daya (*quwwa*) | rujukan *Tafṣīl* no. 78 | R3, Mukadimah |
| `m-qudra` | Kuasa (*qudra*) | *al-Mufradāt* | R3, Mukadimah |
| `r-fitra` | Fitrah (*fiṭra*) | rujukan *al-Dharīʿa* no. 172, 173; *Tafṣīl* no. 172 | R3, Tingkatan Ilmu-Ilmu Agama |
| `r-yaqin` | Keyakinan (*yaqīn*) | rujukan *Tafṣīl* no. 159 | R3, Tingkatan Ilmu-Ilmu Agama |
| `r-khawf` | Takut (*khawf*) | rujukan *al-Dharīʿa* no. 311, 312, 73-74, 126, 127 | R3, Tingkatan Amal-Amal Keagamaan |
| `r-ujb` | Ujub (*ʿujb*) | rujukan *al-Dharīʿa* no. 261, 262, 263; *Tafṣīl* no. 28 | R3, Tingkatan Amal-Amal Keagamaan |
| `m-wahid` | Satu, esa (*wāḥid*, *waḥda*) | *al-Mufradāt* | R4, Lafal al-Wāḥid |
| `m-ahad` | Esa (*aḥad*) | *al-Mufradāt* | R4, Lafal al-Aḥad |
| `k-ahad` | Esa (*aḥad*) | *Kashshāf* | R4, Perbedaan antara al-Wāḥid dan al-Aḥad |

---

# TERJEMAHAN

# Risalah Pertama {.kitab-ke}

# Adab Bergaul dengan Manusia {.judul-kitab}

[Dengan nama Allah Yang Maha Pengasih, Maha Penyayang]{.basmalah}

Segala puji bagi Allah dengan pujian yang Dia ridai, dan selawat-Nya atas Muhammad, selawat yang mendekatkan beliau kepada-Nya dan melingkupinya dengan rida-Nya.

Aku memohon kepada Allah pertolongan untuk menghadap kepada-Nya, mendengarkan-Nya dengan saksama, sadar untuk mensyukuri-Nya, memandang dengan mata hati dalam urusan-Nya, bersungguh-sungguh dalam menaati-Nya, dan beradab baik dalam bermuamalah dengan-Nya; agar Dia menjadikan kami, di antara nikmat-nikmat-Nya, menginginkan apa yang merupakan pemberian yang kekal, bukan pinjaman yang akan diambil kembali; agar Dia melimpahkan selawat atas Nabi-Nya yang terpilih dan keluarganya; dan agar Dia menjadikan kami termasuk golongannya dengan rahmat-Nya.

Telah sampai kepadaku apa yang terjadi di majelis Syekh, semoga Allah memanjangkan umurnya, tentang bergaul (*mukhālaṭa*) dengan manusia dan menjauhi mereka.[^s1][^m-khalt] Orang-orang yang hadir di majelisnya berselisih pendapat: sebagian memuji sikap menjauhi, dan sebagian memuji sikap bergaul. Kemudian mereka berselisih tentang persahabatan (*ṣadāqa*):[^r-sadaqa] apakah maknanya memiliki wujud, ataukah ia nama yang tidak memiliki makna, sebagaimana kata salah seorang pendahulu ketika ditanya tentang sahabat: "Ia adalah nama yang tidak memiliki makna, makhluk yang tidak ada."[^d1][^s2] Dan jika maknanya memiliki wujud, apakah ia sesuatu yang patut diingini atau patut dihindari?

Semua itu, meskipun manusia telah berselisih tentangnya sejak dahulu, orang yang mengingkari keutamaan sahabat dan tidak mengakui keberadaan dan keutamaannya sungguh telah jauh dari kebenaran.

Maka aku ingin menjadikan hal itu sebuah kitab yang di dalamnya kusebutkan butir-butir yang halus dari apa yang dikatakan para ulama dan para bijak, lalu kujadikan ia hadiah, dengan menyengaja dalam hal itu apa yang dikatakan al-Mutanabbi:[^p1]

> Tiada kuda padamu untuk kau hadiahkan, tiada pula harta;
> maka biarlah tutur kata yang membahagiakan, bila keadaan tak membahagiakan.

Dalam menerima hadiah ini dariku, beliau, semoga Allah melanggengkan taufik-Nya kepadanya, (hendaklah memaklumi) bahwa isinya diambil dari beliau dan dikembalikan kepada beliau; maka yang kupersembahkan kepadanya hanyalah beberapa ikat kemangi dari tamannya sendiri. Ibnu al-Rumi berkata:[^p2]

> Sungguh engkau akan berterima kasih atas tutur kata yang kami hadiahkan kepadamu,
> yang keindahan dan kejelasannya kami timba darimu;
> sebab Allah, Yang Mahaperkasa lagi Mahaagung, berterima kasih atas perbuatan orang
> yang membacakan kepada-Nya wahyu dan Al-Qur'an-Nya sendiri.

Semoga Allah memeliharanya dan menjadi pelindungnya. Adab tidak memiliki pasar kecuali berkat perhatiannya, dan tidak laku kecuali berkat pemeliharaannya yang baik. Permata, sekalipun menjadi hiasan pakaian, nilainya hanyalah sebesar minat orang kepadanya.[^p3]

Daftar bab:

**Pertama**: tentang bergaul dengan manusia dan menyendiri dari mereka, serta keutamaan dan celaan keduanya.

**Kedua**: tentang cinta, macam-macamnya, dan sebab-sebab yang menuntutnya.

**Ketiga**: tentang keserupaan naluriah yang terdapat pada manusia dan seluruh maujud.[^p4]

**Keempat**: tentang pengutamaan macam-macam cinta dan penjelasan mana yang termasuk jenis yang mana.

**Kelima**: tentang hakikat cinta, persahabatan karib (*khulla*), kasih sayang, persahabatan, dan saudara-saudaranya, serta asal-usul kata-katanya.

**Keenam**: tentang cinta Allah kepada hamba-hamba-Nya dan cinta hamba-hamba kepada-Nya, persahabatan karib antara Dia dan mereka, serta bolehnya memakai ungkapan itu untuk-Nya.

**Ketujuh**: tentang perselisihan manusia dalam mengambil sahabat.

**Kedelapan**: tentang keutamaan mengambil sahabat.

**Kesembilan**: tentang jumlah sahabat yang baik untuk dimiliki.

**Kesepuluh**: tentang keadaan-keadaan yang diperhatikan seseorang dalam memilih dan mengambil sahabat.

**Kesebelas**: tentang keadaan-keadaan yang wajib diberikan seseorang kepada sahabatnya dan tidak ia tuntut darinya.

**Kedua belas**: tentang hidup bersama dan bergaul dengan berbagai lapisan manusia yang lain.

[^s1]: CM: Tidak diketahui dengan pasti siapa Syekh yang dimaksud. Mungkin ia Aḥmad bin Ibrāhīm al-Ḍabbī, wazir Bani Buwaih yang bergelar al-Kāfī al-Awḥad, yang menjadi wazir Fakhr al-Dawla sesudah wafatnya al-Ṣāḥib bin ʿAbbād (385 H). Al-Rāghib menyebutnya dalam dua karyanya yang lain, *Muḥāḍarāt al-Udabāʾ* dan *Majmaʿ al-Balāgha*.

[^m-khalt]: **Bergaul** (*mukhālaṭa*, *ikhtilāṭ*). Dalam *al-Mufradāt*: *khalṭ* ialah menghimpun bagian-bagian dua hal atau lebih, baik keduanya cair, padat, atau yang satu cair dan yang lain padat; ia lebih umum daripada *mazj* (mencampur). Sahabat, tetangga, dan mitra disebut *khalīṭ*; dari sini lahir istilah "dua mitra" (*al-khalīṭān*) dalam fikih, seperti *"Dan sesungguhnya kebanyakan dari orang-orang yang bersekutu itu berbuat zalim kepada yang lain"* (Shad: 24). Maka *mukhālaṭa* bukan sekadar bertemu, melainkan membaurkan hidup dengan hidup orang lain, yang dalam risalah ini dilawankan dengan *ʿuzla*, *tafarrud*, dan *mujānaba* (menyendiri, memisahkan diri, menjauhi). (*al-Mufradāt*, s.v. *kh-l-ṭ*.) *Kashshāf* tidak memuat entri *al-mukhālaṭa*.

[^r-sadaqa]: **Persahabatan** (*ṣadāqa*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 364 (`m-sadaqa`, *al-Mufradāt*) dan no. 365 (`k-sadaqa`, *Kashshāf*). Di sana persahabatan didefinisikan sebagai cinta yang lebih khusus, yang jarang terjadi di antara banyak orang.

[^d1]: CD: Ucapan yang sama dikutip dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan Persahabatan": "Karena langkanya sahabat, seorang bijak lain ditanya tentangnya, lalu menjawab: 'Ia adalah nama yang tidak memiliki makna, sebab ia adalah makhluk yang tidak ada.'" Di sana ucapan itu dijadikan tanda langkanya sahabat, bukan penolakan terhadap keberadaannya; di sini ia menjadi salah satu pihak dalam perselisihan yang hendak dijawab risalah ini. Sikap al-Rāghib di kedua tempat sama: orang yang mengingkari keutamaan sahabat telah keliru.

[^s2]: CM: Dalam risalah *al-Ṣadāqa wa-l-Ṣadīq* karya Abū Ḥayyān al-Tawḥīdī, sezaman dengan al-Rāghib, orang yang ditanya dengan pertanyaan ini disebut Rawḥ bin Zinbāʿ. Abū Ḥayyān juga mengutip syair yang mempertanyakan hal yang sama: "Kami mendengar nama sahabat, lalu kami mencari maknanya; apakah ia ada di bumi tetapi kami tidak menemukan jalan kepadanya, ataukah kata 'sahabat' hanyalah kiasan yang tidak ada hakikat di bawahnya?" Senada dengan itu bait yang terkenal: "Dikatakan bahwa hal yang mustahil ada tiga: hantu gurun, burung *ʿanqāʾ*, dan sahabat yang setia."

[^p1]: CP: Edisi tahkik membaca *mutaḥaddī* ("menantang"), dan penyunting memaknainya "mengikuti tuntutan makna bait Abū al-Ṭayyib, yaitu bermurah dengan kata-kata ketika harta tidak mencukupi". Makna ini tidak dikandung kata "menantang"; kami membacanya *mutaḥarriyan* ("menyengaja, mengikuti"), sejalan dengan terjemahan Turki ("beytinin muktezasınca", sesuai tuntutan baitnya). Kata *wa-mā māl* pada larik pertama dibaca *wa-lā māl*, sesuai bunyi bait dalam diwan al-Mutanabbi.

[^p2]: CP: Kalimat "maka yang kupersembahkan kepadanya" mengikuti pembetulan penyunting (*fa-minnī*, dari *fa-man* dalam naskah). Bait Ibnu al-Rumi dalam edisi tahkik tercetak dengan urutan larik yang tertukar dan diawali *la-ashkuranna* ("sungguh aku akan berterima kasih"); terjemahan Turki mengikuti bacaan itu ("sana teşekkür ederim"). Susunan yang benar adalah dua bait: bait pertama terdiri atas "…*ihdāʾanā laka manṭiqan*" dan "*minka stafadnā ḥusnahu wa-bayānahu*", bait kedua atas "*fa-llāhu ʿazza wa-jalla yashkuru fiʿla man*" dan "*yatlū ʿalayhi waḥyahu wa-qurʾānahu*". Kata pertamanya kami baca *la-tashkuranna* ("sungguh engkau akan berterima kasih"): bait kedua memberi alasan mengapa penerima hadiah tetap berterima kasih walaupun hadiah itu berasal darinya sendiri, sebagaimana Allah berterima kasih kepada orang yang membacakan firman-Nya sendiri. Inilah yang sesuai dengan maksud al-Rāghib.

[^p3]: CP: Edisi tahkik membaca *bi-qadri raghbatihim ʿanhu* ("sebesar keengganan mereka terhadapnya"), yang membalik maksud kalimat. Kami membaca *raghbatihim fīhi* ("minat mereka kepadanya"), sesuai terjemahan Turki ("insanların rağbetine göre"). Maksudnya: adab, seperti permata, baru bernilai bila ada yang menghargainya, dan Syekh itulah penghargaannya.

[^p4]: CP: Terjemahan Turki memahami *al-mashākil* di sini sebagai "problem-problem" (*problemler*), seolah dari *mushkil*. Isi Bab Ketiga menunjukkan bahwa yang dimaksud adalah keserupaan (*mushākala*): kecocokan dan penolakan alami di antara manusia, hewan, dan benda mati. Judul bab itu sendiri dalam edisi tahkik berbunyi *al-mushākala al-gharīziyya*.

## Bab Pertama: Bergaul dengan Manusia dan Menyendiri dari Mereka, serta Keutamaan dan Celaan Keduanya {.judul-bab}

Ketahuilah bahwa menyendiri dari manusia pada suatu waktu dan bergaul dengan mereka pada waktu yang lain adalah dua hal yang kadang-kadang menjadi keniscayaan bagi manusia dan kadang-kadang menjadi kewajiban atasnya. Sebab dalam sebagian keadaan manusia terpaksa menyendiri untuk menunaikan keperluan-keperluan pribadinya, dan dalam sebagian keadaan lain ia diseru untuk itu, seperti bermunajat kepada Tuhannya, memikirkan nikmat-nikmat-Nya, dan menunaikan keperluan-keperluan pribadi yang ia kerjakan sendiri tanpa orang lain.[^r-uzla] Sejalan dengan itu sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Dalam lembaran-lembaran Ibrahim tertulis: Wajib atas manusia, selama akalnya tidak dikalahkan, memiliki beberapa saat: saat ia bermunajat kepada Tuhannya, saat ia menghisab dirinya, saat ia merenungkan ciptaan Allah Ta'ala, dan saat ia menyendiri untuk keperluannya berupa makan dan minum."*

Namun dalam kebanyakan keadaannya ia terpaksa berkumpul dengan manusia, karena keperluannya bergantung pada mereka. Karena itu dikatakan: manusia adalah makhluk kota menurut tabiatnya (*madanī bi-l-ṭabʿ*).[^s3] Sebab mereka tidak dapat tidak saling berdamai satu sama lain, karena kekurangan yang ada pada mereka dan karena kebutuhan-kebutuhan niscaya sebagian mereka bergantung pada sebagian yang lain dalam mengurus urusan-urusan mereka. Seandainya tidak ada makhluk yang banyak, tidak seorang pun dari mereka akan memperoleh keperluan yang paling kecil dan ilmu yang paling rendah.

Karena itu, ketika Ibnu Abbas mendengar seseorang berkata, "Ya Allah, jadikanlah aku tidak membutuhkan manusia," ia berkata: "Hai orang, aku lihat engkau tidak memohon kepada Allah selain kematian! Manusia, selama mereka hidup, tidak dapat saling tidak membutuhkan. Katakanlah: Jadikanlah aku tidak membutuhkan orang-orang jahat."[^d2]

Karena kebutuhan sebagian mereka kepada sebagian yang lain, dijadikanlah bagi manusia, di antara seluruh hewan, daya cinta (*quwwat al-maḥabba*); sebab daya itu hanya dimiliki manusia. Adapun hewan-hewan lain tidak memilikinya, meskipun mereka memiliki daya keakraban (*ulfa*) dan keserupaan (*mushākala*).[^r-ulfa][^m-shakl][^d3]

Dalam syariat, manusia diseru, secara wajib maupun sunah, kepada berbagai perkumpulan, seperti salat Jumat dan salat berjamaah, haji, salat dua hari raya, berkumpul dalam jihad, dan sebagainya.[^d4] Wajib pula atasnya menemui para ulama untuk mempelajari sebagian ilmu; dalam sebagian yang lain ia diberi pilihan antara mempelajarinya sendiri dan merujuk kepada mereka lalu mengambil pendapat mereka. Allah juga mendorong manusia untuk saling bermusyawarah dalam urusan dunia mereka yang sulit bagi mereka, sampai-sampai Dia berfirman kepada Nabi-Nya: *"dan bermusyawarahlah dengan mereka dalam urusan itu"* (Ali 'Imran: 159). Semua itu tidak mungkin ia lakukan dalam keadaan menyendiri.

Dari uraian ringkas ini diketahui bahwa keterpaksaan manusia untuk berkumpul dengan manusia lebih besar daripada keterpaksaannya untuk menyendiri dari mereka. Di luar hal itu, manusia berselisih pendapat: apakah menyendiri lebih utama bagi manusia, ataukah berkumpul dan bergaul dengan mereka. Sebagian condong kepada pergaulan dengan manusia lalu memilihnya, dan sebagian enggan terhadapnya lalu membencinya.

Di antara hujah golongan pertama: manusia, menurut pembawaan ciptaannya (*jibilla*), menuntut untuk berkumpul dengan sesamanya. Manusia diciptakan seperti anggota-anggota satu tubuh yang tidak dapat saling tidak membutuhkan. Ia dinamai *insān* karena akrabnya (*uns*) sebagian mereka dengan sebagian yang lain, bukan seperti kata Abu Tammam:[^r-ins][^d5]

> Engkau dinamai *insān* karena engkau pelupa (*nāsī*).[^s4]

Diriwayatkan dalam atsar: *"Orang mukmin yang bergaul dengan manusia dan bersabar atas gangguan mereka lebih utama daripada orang mukmin yang tidak bergaul dengan manusia dan tidak bersabar atas gangguan mereka."*

Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, melarang bepergian seorang diri. Beliau bersabda: *"Seorang (musafir) adalah setan, dua orang adalah dua setan, tiga orang adalah rombongan, dan sebaik-baik teman seperjalanan adalah empat orang."*

Beliau juga bersabda: *"Orang mukmin itu akrab dan diakrabi; tidak ada kebaikan pada orang yang tidak akrab dan tidak diakrabi."*

Seorang bijak berkata: "Manusia yang paling bodoh ialah orang yang merasa akrab dengan kesendirian dan merasa ramai dalam khalwat."

Dikatakan: "Jauhilah menyendiri, karena dalam bertemu dengan manusia terdapat pelajaran yang bermanfaat dan nasihat yang luas."

Dik al-Jinn berkata, dan ia mengemukakan hujah di dalamnya:

> Siapa yang hidup di dunia tanpa kekasih,
> hidupnya di sana adalah hidup orang asing.
> Tiada pada bidadari surga sesuatu yang diingini Adam,
> andaikan Hawa tidak ada.
> Di Firdaus ia dahulu mengeluhkan sepi,
> maka ia tidak merasa akrab kecuali dengan kekasih.

Di antara hujah golongan kedua: manusia yang paling sempurna ialah yang paling tidak membutuhkan penolong;[^p5] perkumpulan-perkumpulan menularkan akhlak kebinatangan, tabiat-tabiat yang beraneka, dan kebiasaan yang tercela; dan kebanyakan ilmu yang pelik digali manusia dengan berpikir dalam keadaan menyendiri. Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bersabda: *"Hamba-hamba yang paling dicintai Allah ialah orang-orang yang bertakwa lagi tersembunyi, yang bila tidak hadir tidak dicari, dan bila hadir tidak dikenal; mereka itulah para pemimpin petunjuk dan pelita-pelita kegelapan."* Beliau, semoga salam atasnya, juga bersabda: *"Sebaik-baik manusia ialah seseorang di celah bukitnya bersama kambing-kambingnya; ia tidak mengenal manusia dan manusia tidak mengenalnya."*

Malik bin Dinar berkata kepada seorang rahib: "Berilah aku nasihat." Rahib itu menjawab: "Jika engkau mampu menjadikan tirai-tirai besi antara dirimu dan manusia, lakukanlah."

Abu al-Darda' berkata: "Waspadalah terhadap manusia, karena tidaklah mereka menunggangi seekor unta kecuali mereka melukai punggungnya, tidak pula punggung seekor kuda yang unggul kecuali mereka melumpuhkannya, dan tidak pula kalbu seorang mukmin kecuali mereka membakarnya."

Diceritakan tentang seorang saleh bahwa seseorang berkata kepadanya: "Berilah aku wasiat." Ia menjawab: "Sedikitkanlah mengenal manusia." Orang itu berkata: "Tambahkanlah." Ia menjawab: "Siapa yang sudah engkau kenal, perlakukanlah ia seolah-olah engkau tidak mengenalnya."[^s5]

Yang benar dalam hal ini ialah bahwa hidup liar menyendiri di gunung-gunung dan padang-padang tandus itu tercela. Sebab hal itu berarti melepaskan diri dari kemanusiaan (*insāniyya*), masuk ke dalam golongan orang-orang mati dan binatang-binatang liar, membatalkan daya-daya keutamaan yang dikhususkan bagi manusia, yaitu akal, keberanian, kesucian diri, dan keadilan, serta mewariskan kemalasan. Telah tetap bahwa kemalasan dan kesantaian termasuk keburukan yang paling besar, sebab keduanya menghalangi seseorang dari keutamaan-keutamaan.[^p6][^r-kasal] Sering kali setan menghiasi kemalasan dalam rupa zuhud, lalu orang bodoh tertipu olehnya, terlepas dari kemanusiaan, dan berzuhud terhadap keutamaan-keutamaan, dengan membayangkan bahwa ia sedang mengenakan pakaian zuhud.[^r-zuhd][^d6]

Bila hal itu telah tetap, maka manusia ada dua macam.

**Pertama**: orang yang telah memperbaiki akhlaknya, mematikan syahwatnya, dan mengenal dunia serta menguasainya dengan pengalaman, lalu ia memandanginya dengan perenungan dan pengambilan pelajaran.[^p7] Bagi orang ini menyendiri itu terpuji, sebab berkat apa yang telah ia hasilkan ia tidak membutuhkan pencarian keakraban dari luar; kesibukannya dalam khalwat adalah dengan ilmu yang mendidiknya dan ilmu lain yang mencukupinya. Dikatakan: "Siapa yang akrab dengan Allah akan merasa asing dari manusia."[^p8]

Dikatakan kepada Muhammad bin al-Nadr: "Tidakkah engkau merasa sepi karena lama duduk di rumah?" Ia menjawab: "Bagaimana aku merasa sepi, sedang Allah Ta'ala adalah teman duduk orang yang mengingat-Nya?"[^p9]

Hal itu ditanyakan pula kepada orang lain, lalu ia menjawab: "Aku adalah teman duduk Tuhanku. Bila aku ingin Dia berbicara kepadaku, aku membaca Kitab-Nya; dan bila aku ingin berbicara kepada-Nya, aku salat."

**Kedua**: orang yang akhlaknya belum terdidik, belum berjuang melawan nafsunya, dan belum memperoleh ilmu. Bagi orang ini menyendiri itu tidak disukai, sebab zatnya buruk menurut tabiatnya, dan yang buruk itu dijauhi. Bila ia menyendiri dengan dirinya dan tidak mendapati kesibukan dari luar, jiwanya membawanya condong kepada pikiran yang buruk, yang mengundang bisikan-bisikan jahat, sehingga setan menguasainya dan menghiasi tipu dayanya baginya. Maka bergejolaklah daya-dayanya yang saling bertentangan, yang belum pernah ia latih, lalu ia mencari semacam kemuliaan yang tidak layak ia dapatkan dan tidak ia miliki, atau syahwat yang tidak dapat ia capai, atau dapat ia capai lalu membinasakannya. Orang pun lari dari kerendahannya yang buruk itu; kesepian dalam menyendiri membawanya kepada terhalangnya kehidupan yang baik; dan ia tidak mengenal orang yang semestinya menjadi tempat orang seperti dia meminta tolong untuk mendidik dirinya, sehingga ia berlindung kepada orang-orang yang serupa dengannya dalam kebodohan:[^p10]

> Setiap sahabat condong kepada yang serupa dengannya,
> seperti akrabnya kumbang kotoran dengan kalajengking.[^d7]

Dari hakikat pembicaraan ini diperoleh kesimpulan bahwa menyendiri dari manusia, yang terlepas dari memelihara ilmu dan beribadah kepada Tuhan, adalah makruh dalam segala keadaan. Dan jelaslah benarnya orang yang berkata:

> Kesendirian orang berakal lebih baik
> daripada teman duduk yang buruk di sisinya;
> dan teman duduk yang baik lebih baik
> daripada duduknya seseorang seorang diri.

[^r-uzla]: **Menyendiri** (*ʿuzla*, *tafarrud*, *khalwa*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 373 (`k-uzla`, *Kashshāf*): sebagian sufi membedakan *khalwa* (menyendiri dari orang lain) dari *ʿuzla* (menyendiri dari nafsu dan apa yang menyibukkan dari Allah). Dalam risalah ini al-Rāghib memakai *ʿuzla*, *tafarrud*, *infirād*, dan *mujānaba* hampir bersinonim, semuanya dalam arti lahir: memisahkan diri dari pergaulan manusia.

[^s3]: CM: Ungkapan ini dijelaskan oleh Ibnu Miskawaih dalam *Tahdhīb al-Akhlāq*: manusia tidak diciptakan seperti makhluk yang hidup sendiri dan dapat bertahan dengan dirinya sendiri, seperti banyak binatang liar, hewan ternak, dan burung, melainkan membutuhkan berbagai macam pertolongan yang hanya sempurna dengan kehidupan kota dan berkumpulnya manusia. Abū Ḥayyān al-Tawḥīdī dalam *al-Ṣadāqa wa-l-Ṣadīq* menjelaskannya: manusia harus menolong dan meminta tolong, sebab ia tidak dapat sendirian memenuhi semua kemaslahatannya dan semua keperluannya. Tentang ungkapan ini dalam karya al-Rāghib sendiri, lihat terjemahan *al-Dharīʿa*, Pasal Keenam, "Kebutuhan Manusia untuk Berkumpul dan Saling Membantu".

[^d2]: CD: Kisah yang sama terdapat dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan dan Keburukan Menyendiri dari Manusia", tetapi di sana dinisbatkan kepada Amirul Mukminin Umar, bukan kepada Ibnu Abbas; penyunting edisi Arab juga mencatat perbedaan ini. Redaksi di *al-Dharīʿa* lebih ringkas ("aku lihat engkau memohon kematian kepada Allah"), dan kalimat "Manusia tidak dapat tidak saling membutuhkan selama mereka hidup" diletakkan sesudah kisah sebagai komentar al-Rāghib, bukan sebagai bagian dari ucapan sahabat. Penerjemah Turki mencatat bahwa ia tidak menemukan riwayat bersanad yang menisbatkan ucapan ini kepada Ibnu Abbas.

[^r-ulfa]: **Keakraban** (*ulfa*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 362 (`m-ulfa`, *al-Mufradāt*): *ilf* ialah berkumpul disertai kerekatan.

[^m-shakl]: **Keserupaan** (*mushākala*, *shakl*). Dalam *al-Mufradāt*: *mushākala* ialah keserupaan dalam bentuk dan rupa, sedang *nidd* keserupaan dalam jenis dan *shibh* keserupaan dalam kualitas; seperti *"Dan (azab) yang lain yang serupa itu (shaklihi) berbagai macam"* (Shad: 58), yakni yang serupa dalam bentuk dan perbuatan. Dikatakan bahwa *shikl* ialah kemanjaan; pada hakikatnya ia adalah keakraban yang ada di antara dua hal yang serupa dalam cara hidupnya; dari sini dikatakan: "Manusia itu bersesuaian dan saling mengakrabi" (*al-nās ashkāl wa-ullāf*). Asal *mushākala* dari *shakl*, yaitu mengikat kaki hewan tunggangan. (*al-Mufradāt*, s.v. *sh-k-l*.) *Kashshāf*: bagi para teolog dan filsuf, *mushākala* ialah kesatuan dalam bentuk, bersinonim dengan *tashākul*; bagi ahli badi', ia adalah menyebut sesuatu dengan lafal lain karena berdampingan dengannya. (*Kashshāf*, s.v. *al-mushākala*.) Penjelasan *al-Mufradāt* bahwa *shikl* adalah "keakraban di antara yang serupa" menerangkan mengapa di sini *mushākala* disandingkan dengan *ulfa*, dan mengapa Bab Ketiga membahasnya sebagai dasar naluriah bagi cinta.

[^d3]: CD: Ada perbedaan istilah dengan *al-Dharīʿa*, Pasal Kelima, "Hakikat Cinta dan Macam-Macamnya". Di sana cinta dibagi menjadi cinta alami, yang "ada pada manusia dan hewan" dan dikatakan ada pula pada benda mati seperti besi dan magnet, dan cinta pilihan, yang khusus bagi manusia, sedang yang terjadi di antara dua hewan disebut keakraban. Di sini kata "cinta" dibatasi pada manusia, dan yang ada pada hewan hanya disebut keakraban dan keserupaan. Dengan kata lain, "cinta" dalam risalah ini sama dengan "cinta pilihan" dalam *al-Dharīʿa*; Bab Ketiga nanti menjelaskan alasannya: cinta "tidak terjadi kecuali dari pertimbangan dan pikiran", sedang kecocokan pada hewan dan benda mati hanya "sejenis cinta".

[^d4]: CD: Dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta", perkumpulan-perkumpulan ibadah yang sama (salat berjamaah lima kali sehari, salat Jumat sekali sepekan, salat hari raya dua kali setahun, haji sekali seumur hidup) diterangkan sebagai sarana yang disyariatkan "agar dengan berkumpulnya mereka keakraban menjadi kokoh, dan karenanya kasih sayang terjadi". Di sini perkumpulan-perkumpulan itu dikemukakan sebagai bukti bahwa manusia lebih banyak dituntut berkumpul daripada menyendiri.

[^r-ins]: **Manusia dan keakraban** (*insān*, *uns*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 370 (`m-ins`, *al-Mufradāt*), dan terjemahan *Tafṣīl*, catatan no. 4 (`r-ins`): dalam *al-Mufradāt*, manusia dinamai *insān* karena ia diciptakan dalam bentuk yang tidak dapat tegak kecuali dengan akrabnya satu sama lain; dikatakan pula ia dinamai demikian karena ia akrab dengan segala yang dibiasakannya; dan ada yang berpendapat asalnya *insiyān*, dari lupa (*nisyān*). Al-Rāghib di sini memilih pendapat pertama dan menolak yang terakhir.

[^d5]: CD: Dalam *al-Dharīʿa*, Pasal Kelima, "Anjuran Bergaul dengan Orang-Orang Baik dan Menjauhi Orang-Orang Jahat", asal kata yang sama diberi arah yang sedikit berbeda: "Manusia disebut *ins* hanyalah karena ia akrab dengan apa yang dilihatnya", yakni akrab dengan apa yang dibiasakannya, sehingga ia mudah menyerap akhlak teman-temannya. Di sini keakraban itu adalah keakraban antarmanusia yang menjadi dasar kehidupan bersama.

[^s4]: CM: Larik pertamanya: "Jangan sekali-kali engkau melupakan janji-janji itu, sebab…". Ibnu Miskawaih dalam *Tahdhīb al-Akhlāq* juga menyalahkan penjelasan Abu Tammam ini dan menyatakan bahwa kata *insān* diambil dari *uns*, bukan dari *nasiya*.

[^p5]: CP: Teks Arab berbunyi *anna al-insāna atammuhum wa-aghnāhum ʿan al-muʿāwin*. Terjemahan Turki dan penyunting memahaminya "manusia adalah makhluk yang paling sempurna dan paling tidak membutuhkan penolong". Kata ganti *-hum* ("di antara mereka") menunjuk manusia, bukan makhluk; maka kami memahaminya sebagai pernyataan tentang tingkatan manusia: yang paling sempurna di antara mereka adalah yang paling tidak membutuhkan orang lain. Pemahaman ini juga lebih sesuai sebagai bantahan terhadap hujah golongan pertama.

[^s5]: CM: Dalam *al-Ṣadāqa wa-l-Ṣadīq*, Abū Ḥayyān menisbatkan wasiat ini kepada Sufyān al-Thawrī: seseorang berkata kepadanya, "Berilah aku wasiat," ia menjawab, "Sedikitkanlah mengenal manusia, dan anggaplah asing orang yang engkau kenal di antara mereka."

[^p6]: CP: Edisi tahkik membaca *al-kasal min al-rāḥa* ("kemalasan karena kesantaian"), padahal kalimat berikutnya memakai kata ganti ganda ("sebab keduanya menghalangi"). Kami membaca *al-kasal wa-l-rāḥa*, sesuai terjemahan Turki ("Rahat yaşam ve tembelliğin") dan catatan penyunting sendiri ("kemalasan dan kesantaian termasuk keburukan terbesar").

[^r-kasal]: **Kemalasan** (*kasal*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 145 (`m-kasal`, *al-Mufradāt*): merasa berat terhadap apa yang semestinya tidak diberatkan, karena itu tercela. Dalam *al-Dharīʿa*, Pasal Pertama, kemalasan dalam mengejar kebaikan adalah derajat pertama turunnya manusia dari keutamaan; dan dalam Pasal Keenam, "Pujian terhadap Usaha dan Celaan terhadap Kemalasan", "siapa yang menganggur dan bermalas-malasan, ia terlepas dari kemanusiaan, bahkan dari kehewanan, dan menjadi sejenis orang mati", gagasan yang sama dengan kalimat di atas.

[^r-zuhd]: **Zuhud** (*zuhd*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 285 (`m-zuhd`, *al-Mufradāt*) dan no. 286 (`k-zuhd`, *Kashshāf*): orang yang zuhud terhadap sesuatu ialah yang berpaling darinya dan rela dengan yang sedikit. Permainan kata di sini: orang malas yang menyangka dirinya zuhud sebenarnya "berzuhud" terhadap keutamaan, yakni berpaling dari hal yang semestinya dikejar.

[^d6]: CD: Bandingkan *al-Dharīʿa*, Pasal Kelima, "Keutamaan dan Keburukan Menyendiri dari Manusia": "menyendiri membatalkan kemanusiaan, dan tidak tampak keutamaan apa pun dari pelakunya. Siapa yang menyangka baik terhadap penyendirian, itu hanya karena tidak ada sesuatu pun yang tampak darinya, dan dalam hal ini orang-orang mati pun ikut serta." Kesimpulannya sama, tetapi pengecualiannya dirumuskan berbeda. Di *al-Dharīʿa* menyendiri makruh kecuali bagi tiga orang: penguasa, orang bijak, dan ahli ibadah; di sini pengecualian didasarkan pada keadaan jiwa: menyendiri terpuji bagi orang yang akhlaknya telah terdidik dan ilmunya telah mencukupinya, dan tercela bagi yang belum.

[^p7]: CP: Edisi tahkik membaca *wa-qatalahā ikhtibāran fa-huwa yurhiquhā tafakkuran wa-iʿtibāran*. Ungkapan *qatala al-shayʾa khubran* (atau *ʿilman*) berarti "mengenal sesuatu sampai tuntas"; maka "menguasainya dengan pengalaman". Kata *yurhiquhā* ("membebaninya") tidak cocok dengan konteks; kami membacanya *yarmuquhā* ("memandanginya"), yang dalam tulisan tangan hanya berbeda sedikit. Terjemahan Turki memahami keseluruhannya "menghabiskan waktunya dengan perenungan dan pengambilan pelajaran".

[^p8]: CP: Edisi tahkik membaca *istawḥasha min al-nār* ("merasa asing dari neraka"), dan penyunting memaknainya "siapa yang menyendiri dari orang-orang jahat…". Yang benar *min al-nās* ("dari manusia"), sebagaimana dicatat penerjemah Turki, yang merujuk *al-Kashkūl* karya Bahāʾ al-Dīn al-ʿĀmilī. Ucapan ini juga dikutip al-Rāghib dengan bunyi *min al-nās* dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan dan Keburukan Menyendiri dari Manusia"; terjemahannya di atas mengikuti redaksi terjemahan *al-Dharīʿa*.

[^p9]: CP: Penyunting dan penerjemah Turki mengidentifikasi tokoh ini sebagai Muḥammad bin Naṣr al-Marwazī (w. 294 H), ahli fikih mazhab Syafi'i. Teks menulis "Muḥammad bin al-Naḍr" (dengan titik yang hilang dalam OCR), dan kisah ini terkenal sebagai kisah Muḥammad bin al-Naḍr al-Ḥārithī, ahli zuhud dari Kufah pada abad kedua Hijriah, yang dikenal suka menyendiri dan yang jawabannya diriwayatkan dengan bunyi "Bagaimana aku merasa sepi, sedang Dia berfirman: Aku adalah teman duduk orang yang mengingat-Ku?". Identifikasi dengan al-Marwazī karena itu kemungkinan besar keliru.

[^p10]: CP: Kalimat ini sangat rusak dalam edisi tahkik. Kami membacanya, dengan bantuan terjemahan Turki: *fa-tahīju bihi quwāhu al-mutaḍādda allatī lam yurīḍhā* ("daya-dayanya yang saling bertentangan, yang belum ia latih"; teks: *lam yarḍa*, "yang tidak ia ridai"); *fa-yuhrabu min danāʾatihi* ("orang lari dari kerendahannya"; teks: *fa-yahrubu*, "maka ia lari"); *wa-addathu waḥshat al-ʿuzla ilā ḥirmān ʿayshihi* ("kesepian membawanya kepada terhalangnya kehidupan"; teks: *ḥurmat ʿayshihi*); *wa-jahila man ḥaqqu mithlihi an yastaʿīna bihi fī tahdhībihi fa-yafzaʿu ilā mushākilihi* ("dan ia tidak mengenal orang yang semestinya menjadi tempatnya meminta tolong… sehingga ia berlindung kepada yang serupa dengannya").

[^d7]: CD: Perumpamaan yang sama dipakai dalam *al-Dharīʿa*, Pasal Kedua, "Wajibnya Mengendalikan Orang-Orang yang Tampil Mengajar dan Bahaya Membiarkan Mereka", tentang orang-orang bodoh yang mendapat dukungan orang awam karena keserupaan mereka: "setiap sahabat condong kepada yang serupa dengannya, seperti akrabnya kumbang kotoran dengan kalajengking." Terjemahan larik di atas mengikuti redaksi itu.

## Bab Kedua: Definisi Cinta, Macam-Macamnya, dan Sebab-Sebab yang Menuntutnya {.judul-bab}

Cinta (*maḥabba*) ialah menghendaki apa yang dilihat atau disangka baik oleh manusia.[^r-mahabba][^d8]

Sebab tujuan manusia dalam segala yang ia usahakan adalah keutamaan, manfaat, dan kelezatan.[^r-fadila][^m-naf][^r-ladhdha] Cinta terjadi untuk ketiga tujuan itu, bila ia bergantung padanya. Karena itu terlihat bahwa cinta orang-orang saleh dan orang-orang baik adalah karena keutamaan, cinta para pedagang dan penjual karena manfaat, dan cinta anak-anak muda dan orang-orang yang berkelapangan karena kelezatan.

Bila hal ini telah tetap, maka orang yang tujuannya keutamaan, dengan tercapainya keutamaan itu ia memperoleh pula manfaat dan kelezatan; orang yang tujuannya manfaat, dengan tercapainya manfaat itu ia memperoleh kelezatan, tetapi tidak keutamaan; dan orang yang tujuannya kelezatan tidak memperoleh keutamaan, dan jarang pula memperoleh manfaat.

Siapa yang mencintai orang lain karena keutamaan, cintanya tidak berubah; sebab keutamaan tidak berubah zatnya, maka demikian pula apa yang bergantung padanya. Siapa yang mencintai karena kelezatan, kasih sayangnya terputus dengan terputusnya kelezatan itu. Demikian pula manfaat: bila ia terputus dan harapan akannya pun terputus, terputus pula cinta yang lahir karenanya. Bagaimana dapat diharapkan kekalnya sesuatu yang bergantung pada sebab yang tidak kekal? Maka cinta yang bergantung pada keduanya cepat hilang dan cepat pula melekat.

Dalam cinta yang dituntut oleh manfaat dan kelezatan terjadi saling mendahului dan tertinggal: cinta itu bisa datang dari salah satu pihak saja tanpa yang lain, bisa pula salah satunya lebih dahulu daripada yang lain; dan bila terjadi pada kedua pihak, kadarnya berbeda sesuai kadar tercapainya apa yang dicari.

Boleh jadi dua orang yang bersahabat berbeda tujuannya: tujuan salah satunya kelezatan dan tujuan yang lain manfaat, atau tujuan salah satunya suatu manfaat dan tujuan yang lain manfaat yang lain. Karena itulah dikenal sebutan "kasih sayang pelacuran" (*al-mawadda al-qiḥābiyya*) dan "kasih sayang yang penuh celaan" (*al-mawadda al-lawwāma*): bila tujuan si pencinta (*ʿāshiq*) adalah bersenang-senang sedang tujuan yang dicintai adalah harta, keduanya tidak henti-hentinya saling mengeluh.[^p11][^d9]

Adapun cinta karena keutamaan, yaitu cinta karena Dzat Allah Ta'ala, ia bersih dari semua cela ini.[^p12] Dialah yang dikecualikan dalam firman Allah Ta'ala: *"Teman-teman karib pada hari itu saling bermusuhan satu sama lain, kecuali mereka yang bertakwa"* (az-Zukhruf: 67). Itu pula yang dimaksud Abu al-'Atahiyah dengan ucapannya:

> Tiada suatu kaum saling berbagi ketulusan bukan karena Dzat Allah,
> kecuali mereka berpisah dengan saling membenci.

Cinta juga dibagi dengan cara lain; dikatakan bahwa ia ada tiga.

**Pertama**: cinta kepada apa yang merupakan kebaikan sempurna, yaitu yang berkaitan dengan kebaikan tempat kembali (*maʿād*).[^r-khayr]

**Kedua**: cinta kepada apa yang bukan kebaikan sempurna, yaitu yang berkaitan dengan manfaat yang indah dan syahwat yang mubah.

**Ketiga**: cinta kepada apa yang sama sekali bukan kebaikan, yaitu setiap syahwat terhadap yang terlarang, seperti zina, liwath, dan meminum khamar.

[^r-mahabba]: **Cinta** (*maḥabba*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 360 (`m-mahabba`, *al-Mufradāt*) dan no. 361 (`k-mahabba`, *Kashshāf*). Definisi dalam risalah ini ("menghendaki apa yang dilihat atau disangka baik") sama persis dengan definisi *al-Mufradāt*, s.v. *ḥ-b-b*, yang juga membagi cinta menjadi tiga: karena kelezatan, karena manfaat, dan karena keutamaan. Tentang *irāda* (kehendak), lihat nota kaki no. 73 (`m-irada`) dan no. 74 (`k-irada`).

[^d8]: CD: Dalam *al-Dharīʿa*, Pasal Kelima, "Hakikat Cinta dan Macam-Macamnya", cinta didefinisikan sebagai "condongnya jiwa kepada apa yang ia lihat atau sangka baik". Risalah ini mengikuti rumusan *al-Mufradāt* ("menghendaki"), bukan rumusan *al-Dharīʿa* ("condongnya jiwa"). Perbedaannya bukan sekadar redaksi: dengan "kehendak", cinta menjadi perbuatan jiwa yang berkaitan dengan pertimbangan, sesuai dengan pernyataan Bab Ketiga bahwa cinta "tidak terjadi kecuali dari pertimbangan dan pikiran"; sedang "condong" mencakup pula kecenderungan alami, sesuai dengan pengakuan *al-Dharīʿa* tentang adanya cinta alami pada hewan dan benda mati. Pembagian tiga tujuan (keutamaan, manfaat, kelezatan) sejalan dengan pembagian empat macam cinta pilihan dalam *al-Dharīʿa* (syahwat, manfaat, campuran, keutamaan); lihat nota kaki *al-Dharīʿa* no. 363 tentang kesejajarannya dengan tiga macam persahabatan dalam tradisi filsafat etika.

[^r-fadila]: **Keutamaan** (*faḍīla*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 102 (`m-fadila`, *al-Mufradāt*).

[^m-naf]: **Manfaat** (*nafʿ*, *manfaʿa*). Dalam *al-Mufradāt*: *nafʿ* ialah apa yang dipakai sebagai pertolongan untuk sampai kepada kebaikan-kebaikan; apa yang menjadi jalan menuju kebaikan adalah kebaikan, maka manfaat adalah kebaikan, dan lawannya mudarat (*ḍurr*), seperti *"dan tidak kuasa untuk (menolak) bahaya terhadap dirinya dan tidak dapat (mendatangkan) manfaat"* (al-Furqan: 3). (*al-Mufradāt*, s.v. *n-f-ʿ*.) Definisi ini menjelaskan kedudukan manfaat di antara tiga tujuan: ia baik bukan karena dirinya, melainkan karena menjadi sarana. Karena itu cinta karena manfaat bertahan hanya selama sarananya bertahan. *Kashshāf* tidak memuat entri khusus *al-nafʿ*.

[^r-ladhdha]: **Kelezatan** (*ladhdha*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 265 (`k-ladhdha`, *Kashshāf*): lawan rasa sakit; pengidrakan dan perolehan atas apa yang bagi yang mengidrak adalah kesempurnaan dan kebaikan.

[^p11]: CP: Edisi tahkik memisahkan kedua sebutan ini dan menjadikan *al-mawadda al-lawwāma* awal kalimat baru, sehingga terjemahan Turki membedakan "cinta yang rendah" dari "cinta yang mencela". Susunan kalimatnya lebih tepat dibaca sebagai satu kalimat: kedua sebutan itu diberikan kepada kasih sayang dengan tujuan yang berbeda, dan contoh pencinta yang mencari kesenangan dan yang dicintai yang mencari harta menjelaskan keduanya sekaligus: disebut "pelacuran" karena pertukaran kesenangan dengan harta, dan disebut "penuh celaan" karena keduanya selalu saling mengeluh. *Qiḥāb* (bentuk jamak *qaḥba*) berarti pelacur. Contoh ini berasal dari tradisi filsafat etika tentang persahabatan, yang menyebut pertengkaran pencinta dan yang dicintai sebagai contoh persahabatan yang tujuan kedua pihaknya tidak sama.

[^d9]: CD: Kasus ini adalah "cinta yang tersusun dari keduanya" dalam *al-Dharīʿa*, Pasal Kelima, "Hakikat Cinta dan Macam-Macamnya": "seperti orang yang mencintai orang lain karena manfaat, sedang orang lain itu mencintainya karena syahwat". Di *al-Dharīʿa* ia disebut sebagai macam ketiga tanpa penilaian; di sini ia diberi nama yang merendahkan dan dikatakan selalu disertai saling mengeluh.

[^p12]: CP: Edisi tahkik membaca *fa-taʿziya* ("maka ia adalah penghibur"), dan penyunting memaknainya "satu-satunya pengganti yang tepat bagi cinta karena manfaat atau kelezatan". Kami membacanya *fa-muʿarrāt* ("bersih, terlepas") *min hādhihi al-maʿāyib kullihā*, sesuai terjemahan Turki ("tüm bu kusurlardan berîdir").

[^r-khayr]: **Kebaikan** (*khayr*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 99 (`m-khayr`, *al-Mufradāt*) dan no. 100 (`k-khayr`, *Kashshāf*): dalam *al-Mufradāt*, kebaikan ada yang mutlak, yang diinginkan dalam segala keadaan oleh semua orang, dan ada yang terbatas, yang menjadi kebaikan bagi seseorang dan keburukan bagi yang lain. Pembagian "kebaikan sempurna" dan "bukan kebaikan sempurna" di sini sejajar dengan pembagian itu.

## Bab Ketiga: Keserupaan Naluriah pada Manusia dan Seluruh Maujud {.judul-bab}

Telah dikemukakan bahwa cinta khusus dimiliki manusia, tidak dimiliki hewan-hewan lain, sebab cinta tidak terjadi kecuali dari pertimbangan (*rawiyya*) dan pikiran, dan hal itu tidak dimiliki hewan-hewan lain. Namun disebutkan bahwa dalam asal penciptaan terdapat kecocokan-kecocokan (*mulāʾamāt*) yang sejenis dengan cinta dan penolakan-penolakan (*munāfarāt*) yang sejenis dengan permusuhan.[^m-nafr] Hal itu tidak hanya ada pada manusia, tetapi juga pada hewan-hewan lain dan pada banyak benda mati. Contohnya kecocokan antara dua yang sejenis, seperti keserupaan seekor kuda dengan kuda lain dan penolakannya terhadap kuda yang lain lagi; demikian pula keadaan pada anjing dan hewan-hewan lain.

Sebagaimana hal itu terjadi di antara satu jenis, ia juga terjadi di antara dua jenis, seperti kecocokan antara biawak padang pasir dan kalajengking, dan penolakan antara gagak dan burung hantu. Adapun pada benda mati, contohnya ialah yang terjadi antara batu magnet dan besi, dan penolakan antara batu yang lari dari cuka dan cuka.[^p13][^d10]

Dikatakan bahwa hal itu adalah sesuatu yang diciptakan Allah Ta'ala dalam asal penciptaan, dan dari situlah timbul azimat (*ṭilasm*), sebab azimat adalah penguasaan sebagian tabiat-tabiat ini atas sebagian yang lain.[^k-tilasm] Sebagian orang berkata: karena itu nama *ṭilasm* telah mengisyaratkan makna ini, sebab bila dibalik ia menjadi *musallaṭ* ("yang dikuasakan").

Kecocokan-kecocokan ini menjadi sebab terjadinya banyak cinta yang utama, bukan yang karena manfaat dan syahwat, dan menjadi sebab terjadinya permusuhan naluriah (*gharīziyya*).[^r-ghariza] Kepada hal inilah diisyaratkan oleh salah seorang filsuf yang berkata: "Allah menciptakan roh-roh sekaligus dalam bentuk seperti bola, kemudian membaginya di antara makhluk-makhluk. Maka bila sebuah roh bertemu dengan belahannya dan saudara kembarnya, ia mencintai dan akrab dengannya, karena kesesuaian kedua belahan itu dan berpasangannya kedua bagian; dan bila ia bertemu dengan yang jauh darinya, ia menolaknya sesuai kadar jauhnya."[^p14]

Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, telah menyatakan makna ini dengan terang. Beliau bersabda: *"Roh-roh itu bagaikan pasukan yang dihimpun; yang saling mengenal di antara mereka akan bersatu, dan yang saling mengingkari di antara mereka akan berselisih."* Seorang penyair menyinggung makna ini:

> Kalbu-kalbu memiliki petunjuk-petunjuk dari kalbu-kalbu lain
> tentang kasih sayang, sebelum tubuh-tubuh saling menyaksikan.

Al-Abbas bin al-Ahnaf mengambil makna ini, lalu berkata:

> Katakan kepada perempuan yang melukiskan cintanya
> kepada lelaki yang dimabuk rindu dengan menyebut-nyebutnya:
> Tidaklah aku berkata selain kebenaran yang kukenal;
> aku mendapati buktinya dari kalbuku sendiri.
> Kalbuku dan kalbumu diciptakan secara ajaib;
> keduanya saling menarik dengan tulusnya cinta.

Ada pula yang tidak membedakan kasih sayang karena keutamaan dari yang lain; ketika ia melihat bahwa kasih sayang karena kelezatan tidak memiliki sifat ini, ia mulai menentang sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, dengan kebodohannya, lalu berkata:

> Demi hidupku, telah berdusta orang-orang yang mendakwa
> bahwa kalbu membalas kalbu;
> seandainya benar seperti yang mereka dakwakan,
> tentulah tiada pencinta yang bersikap dingin kepada kekasihnya.

Sebagaimana cinta terjadi karena keserupaan ini, saling membenci terjadi karena perbedaan. Atas dasar ini orang-orang utama membenci orang-orang rendah.[^p15] Karena penolakan yang menuntut kebencian ini pula kita diperingatkan terhadap orang yang tidak disukai kalbu kita tanpa sebab. Diriwayatkan dalam atsar: *"Bila kalian membenci seseorang tanpa keburukan yang ia lakukan kepada kalian, waspadalah terhadapnya; dan bila kalian mencintai seseorang tanpa kebaikan yang lebih dahulu ia berikan kepada kalian, harapkanlah kebaikannya."*

Selanjutnya, di antara manusia ada yang terlihat dicintai karena keutamaan yang khusus ada pada jiwanya, sehingga kalbu orang-orang baik condong kepadanya dengan kuat tanpa sebab dari luar; dan di antara mereka ada yang sebaliknya, terlihat dibenci karena kekurangan yang khusus ada pada jiwanya. Nabi, semoga salam atasnya, telah mengingatkan hal itu dengan sabdanya: *"Bila Allah mencintai seorang hamba, Dia melimpahkan cinta kepadanya ke dalam air, sehingga tidak seorang pun meminumnya kecuali ia mencintainya; dan bila Dia membenci seorang hamba, Dia melimpahkan kebencian kepadanya ke dalam air, sehingga tidak seorang pun meminumnya kecuali ia membencinya."*[^p16][^d11]

Bila uraian ringkas ini telah tergambar, diketahuilah bahwa sebab-sebab cinta ada empat.[^p17]

Dua orang telah berselisih pendapat. Salah seorang dari mereka mendakwa bahwa sesuatu hanya mencintai yang serupa dan mirip dengannya, dan bahwa saling mencintai menuntut kesatuan, sedang sesuatu tidak akan bersatu kecuali dengan yang serupa dan sebanding dengannya. Karena itu orang utama tidak akrab dengan orang jahat, tidak pula orang bijak dengan orang bodoh; masing-masing akrab dengan yang serupa dan sejenis dengannya.

Yang lain mendakwa bahwa sesuatu hanya mencintai lawannya, yang berada di ujung terjauh darinya dalam kemuliaan, demi mencari keadaan seimbang (*iʿtidāl*). Sebab orang yang buruk rupa tidak merindukan yang buruk rupa, melainkan yang elok; dan orang fakir tidak berhasrat mendekati orang fakir, melainkan berhasrat bergaul dengan orang kaya.

Kedua orang itu memandang secara parsial lalu menghukumi secara universal. Yang pertama memandang cinta yang utama; ketika ia melihat orang utama hanya mencintai orang utama demi keutamaan, ia menghukumi setiap cinta demikian. Yang kedua memandang cinta karena manfaat dan karena kelezatan; ia melihat orang fakir mencintai orang kaya demi manfaat yang sampai kepadanya dari orang itu, dan orang buruk rupa mencintai yang elok demi kelezatan yang ia peroleh darinya, lalu ia pun menghukumi setiap cinta dengan hukum universal.

Siapa yang memperhatikan macam-macam cinta dan sebab-sebabnya sebagaimana dirinci para peneliti, yang telah dikemukakan pembahasannya, akan jelas baginya hakikat hal itu.

[^m-nafr]: **Penolakan** (*munāfara*, *nafr*). Dalam *al-Mufradāt*: *nafr* ialah gelisah menjauhi sesuatu atau menuju sesuatu, seperti takut menjauhi sesuatu atau lari kepadanya; dikatakan *nafara ʿan al-shayʾ nufūran*, seperti *"tidak menambah (apa-apa) kepada mereka, bahkan semakin jauh mereka (dari kebenaran)"* (Fatir: 42). (*al-Mufradāt*, s.v. *n-f-r*.) *Munāfara* adalah bentuk timbal baliknya: dua hal yang saling menjauhi, lawan *mulāʾama* (saling cocok). *Kashshāf* tidak memuat entri *al-munāfara* maupun *al-mulāʾama*.

[^p13]: CP: Edisi tahkik membaca *al-ḥajar al-hārib min al-ḥall wa-bayna al-ḥall*, dan penyunting menafsirkannya sebagai gaya sentrifugal; terjemahan Turki mengikutinya ("merkezden ayrılan taş ile merkez", batu yang terlempar dari pusat dan pusat). Tafsiran itu tidak berdasar. Bacaan yang benar adalah *al-khall* ("cuka"), dengan titik yang hilang: "batu yang lari dari cuka" adalah contoh yang dikenal dalam pembahasan sifat-sifat khas benda (*khawāṣṣ*), sejajar dengan batu magnet yang menarik besi. Yang dimaksud agaknya batu berkapur yang, bila dituangi cuka, berbuih dan bergerak seolah menjauh darinya.

[^d10]: CD: Contoh batu magnet dan besi juga dipakai dalam *al-Dharīʿa*, Pasal Kelima, "Hakikat Cinta dan Macam-Macamnya", untuk cinta alami ("dikatakan pula bahwa ia ada pada benda-benda mati, seperti keterikatan antara besi dan batu magnet"). Di sana gejala ini disebut cinta; di sini ia hanya "sejenis cinta", sebab cinta dalam arti sebenarnya disyaratkan dengan pertimbangan dan pikiran. Lihat juga catatan d3.

[^k-tilasm]: **Azimat** (*ṭilasm*). *Kashshāf*: ia adalah perkara luar biasa yang sumbernya daya-daya langit yang aktif yang dipadukan dengan penerima-penerima bumi yang pasif, untuk menimbulkan hal-hal yang ganjil. (*Kashshāf*, s.v. *al-ṭilasm*.) Definisi ini sejalan dengan penjelasan di atas: azimat bekerja dengan "menguasakan" sebagian tabiat atas sebagian yang lain, memanfaatkan kecocokan dan penolakan yang tertanam dalam asal penciptaan. Al-Rāghib hanya meriwayatkannya sebagai pendapat orang ("dikatakan", "sebagian orang berkata"). *Al-Mufradāt* tidak memuat entri ini.

[^r-ghariza]: **Naluri** (*gharīza*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 78 (`k-gharizah`, *Kashshāf*): tabiat, atau kemampuan yang menjadi sumber sifat-sifat zati.

[^p14]: CP: Kisah roh-roh yang diciptakan berbentuk bola lalu dibelah dikenal dalam sastra cinta Arab sebagai pendapat "sebagian filsuf" (misalnya dalam *al-Zahra* karya Muḥammad bin Dāwūd al-Iṣfahānī dan *Ṭawq al-Ḥamāma* karya Ibn Ḥazm), dan asalnya adalah mitos yang diceritakan Aristophanes dalam *Symposium* karya Plato tentang manusia yang semula bulat lalu dibelah dua. Kata *rubʿ* ("seperempat") dalam edisi tahkik tidak jelas maksudnya; terjemahan Turki memahaminya "roh dari seperempat bola". Kami memahaminya sebagai sebuah bagian atau roh, sesuai konteks.

[^p15]: CP: Edisi tahkik membaca *yaqī al-fuḍalāʾ li-l-andhāl* ("orang-orang utama menjaga orang-orang rendah"), yang tidak sesuai dengan konteks. Kami membacanya *yaqlī al-fuḍalāʾu al-andhāla* ("orang-orang utama membenci orang-orang rendah"). Terjemahan Turki memahaminya "orang-orang utama tidak bersahabat dengan orang-orang rendah". Kata *al-baʿḍ* sesudahnya dibaca *al-bughḍ* ("kebencian").

[^p16]: CP: Dalam edisi tahkik hadis ini terpotong: *alqā bughḍahu fī al-māʾ fa-lā yashrabuhu aḥad illā abghaḍahu*, sehingga cinta Allah justru menghasilkan kebencian. Bagian yang hilang (tentang cinta) dilengkapi sesuai redaksi hadis yang sama dalam *al-Dharīʿa* dan sesuai pelengkapan penerjemah Turki, yang merujuk *al-Ṣadāqa wa-l-Ṣadīq* karya Abū Ḥayyān. Penyunting dan penerjemah Turki mencatat bahwa hadis dengan redaksi ini tidak ditemukan dalam kitab-kitab hadis; Abū Ḥayyān menyebutnya sebagai ucapan orang ("mereka berkata").

[^d11]: CD: Hadis yang sama dan gagasan yang sama dikemukakan dalam *al-Dharīʿa*, Pasal Kelima, "Orang yang Dicintai Manusia". Terjemahannya di atas mengikuti redaksi terjemahan *al-Dharīʿa*. Di sana al-Rāghib menjelaskan sebabnya: orang yang dipelihara Allah, lalu Dia menjernihkan substansinya dan membaikkan rohnya, memperoleh cahaya yang mengalir ke dalam perasaan orang yang melihatnya sehingga orang itu mencintainya. Di sini sebab yang sama disebut "keutamaan yang khusus ada pada jiwanya".

[^p17]: CP: Keempat sebab itu tidak disebut satu per satu. Dari urutan uraian dapat disimpulkan bahwa yang dimaksud ialah keutamaan, manfaat, dan kelezatan (Bab Kedua), ditambah keserupaan naluriah (Bab Ketiga), yang membuat seseorang dicintai atau dibenci tanpa sebab dari luar. Penyunting juga menyimpulkan demikian.

## Bab Keempat: Pengutamaan Macam-Macam Cinta dan Penjelasan Mana yang Termasuk Jenis yang Mana {.judul-bab}

Telah dikemukakan bahwa cinta karena keutamaan membawa serta manfaat dan kelezatan, dan cinta karena manfaat membawa serta kelezatan, tetapi tidak sebaliknya; sebab manfaat tidak mengandung keutamaan, dan kelezatan sama sekali tidak mengandung keutamaan, dan tidak pula mengandung manfaat kecuali sedikit.

Bila hal itu telah tetap, wajib diketahui bahwa cinta Allah kepada hamba-hamba-Nya, cinta orang-orang utama kepada Allah, cinta Rasul kepada mereka dan cinta mereka kepada Rasul, cinta para ulama satu sama lain, cinta mereka kepada murid-murid mereka dan cinta murid-murid itu kepada mereka, cinta para pemimpin kepada yang dipimpin, dan cinta orang yang diutamakan kepada orang yang ia diutamakan atasnya, semuanya adalah cinta karena keutamaan.

Adapun cinta orang yang diungguli kepada orang yang mengunggulinya, cinta yang dipimpin kepada pemimpinnya, cinta suami istri satu sama lain bila keduanya bertujuan menata kehidupan bersama,[^p18] serta cinta tuan kepada budaknya dan budak kepada tuannya, semuanya termasuk cinta karena manfaat.

Adapun cinta saudara-saudara dan kerabat satu sama lain, ia bersifat naluriah, dan kadang-kadang karena manfaat. Cinta anak kepada kedua orang tuanya demikian pula, dan cinta kedua orang tua kepada anaknya bersifat naluriah. Kemudian, ketika anak masih kecil, cinta itu disertai kelezatan dan harapan akan manfaat; ketika ia sudah dapat melayani keduanya, cinta itu disertai manfaat; dan bila keduanya memperhatikannya lalu menghiasinya dengan adab yang baik, cinta keduanya kepadanya menjadi tergolong cinta karena keutamaan.[^p19]

Adapun cinta kepada harta dan kedudukan, cinta suami istri satu sama lain dan cinta pencinta kepada yang dicintainya bila tujuan keduanya tidak lain hanyalah persetubuhan, dan cinta teman bersenda gurau kepada teman bersenda guraunya, semuanya karena kelezatan. Kadang-kadang dalam sebagiannya terdapat manfaat, yaitu bila hal itu dilakukan menurut kadar yang semestinya, di tempat yang semestinya, dan dengan cara yang semestinya.[^p20]

Jika ditanyakan: Apa sebab berlebihnya cinta seorang ayah kepada anaknya, sampai-sampai ia menginginkan untuk anaknya apa yang ia inginkan untuk dirinya sendiri, gembira melihatnya lebih utama daripada dirinya, tidak merasa tidak senang bila dikatakan kepadanya, "Anakmu lebih utama daripada engkau," cintanya kepadanya bertambah dari hari ke hari, dan ia begitu tergila-gila kepadanya hingga menjadi pandir, lalu karenanya ia menjadi bahan tertawaan yang dijadikan perumpamaan, sehingga dikatakan: "Ia kagum kepada anu seperti kagumnya seseorang kepada anaknya," dan "Seorang anak tampak elok di mata ayahnya"?

Dijawab: Sebabnya ialah bahwa pada anak itu terhimpun hampir seluruh sebab cinta. Selain adanya cinta naluriah kepadanya, sang ayah melihat anaknya sebagai dirinya sendiri, sebagai salinan rupanya dalam pribadi yang lain. Maka ia mencintainya seperti cintanya kepada dirinya sendiri, bahkan lebih dari itu, sebab ia melihat anaknya sebagai bagian dirinya yang tetap tinggal sesudahnya; dan perhatian manusia terhadap dirinya tertuju kepada yang akan datang, bukan kepada yang telah lalu.

Karena manusia, bila keadaannya bertambah sedikit demi sedikit dan ia naik dalam keutamaan setingkat demi setingkat, tidak merasa berat bila dikatakan kepadanya, "Engkau hari ini lebih utama daripada engkau kemarin," demikian pula keadaannya terhadap anaknya bila dikatakan kepadanya, "Ia lebih utama daripada engkau dahulu," sebab anak itu, secara perkiraan, adalah dirinya sendiri.[^p21]

Adapun bertambahnya cintanya dengan berlalunya hari, itu karena makin kokohnya pengenalannya terhadap anaknya, makin bertambahnya kegembiraannya, dan makin pastinya ia akan kekalnya rupanya. Adapun keterpesonaannya kepada anaknya seperti keterpesonaannya kepada dirinya sendiri, itu karena anak itu adalah dirinya; sebagaimana aib-aib manusia pada dirinya sendiri tersembunyi darinya, demikian pula aib-aib itu tersembunyi darinya pada anaknya.

Jika ditanyakan: Mengapa anak tidak mencintai ayahnya sebagaimana ayah mencintainya, padahal ia sama dengan ayahnya dalam makna-makna yang telah disebutkan; bahkan ia membenci dan tidak menyukainya, sampai-sampai Allah Ta'ala, karena mengetahui hal itu pada keduanya, mewasiatkan anak untuk berbuat baik kepada ayahnya dengan firman-Nya: *"maka sekali-kali janganlah engkau mengatakan kepada keduanya perkataan 'ah' dan janganlah engkau membentak keduanya, dan ucapkanlah kepada keduanya perkataan yang baik"* (al-Isra': 23), dan memperingatkan ayah terhadap anaknya dengan firman-Nya, Mahaperkasa Yang Berfirman: *"Sesungguhnya hartamu dan anak-anakmu hanyalah cobaan (bagimu)"* (at-Taghabun: 15)?

Dijawab: Anak pasti mencintai ayahnya karena kesamaan substansi (*jawhariyya*) di antara keduanya,[^r-jawhar] tetapi cintanya kepada ayahnya lebih kecil daripada cinta ayah kepadanya, karena beberapa hal.[^p22]

**Pertama**: meskipun anak adalah ayah itu sendiri, ayah adalah bagian yang pergi sedang anak adalah bagian yang tinggal; dan telah ditetapkan bahwa perhatian manusia tertuju kepada bagian dirinya yang tinggal, bukan kepada yang telah lalu.

**Kedua**: manusia lebih mencintai apa yang ia usahakan daripada cinta yang diusahakan kepada yang mengusahakannya. Karena itu tuan lebih mencintai budaknya daripada budak mencintai tuannya.

**Ketiga**: anak tidak mengenal ayahnya kecuali sesudah masa yang panjang, dan tidak menyadari manfaat keberadaan ayahnya kecuali sesudah beberapa waktu; sedang ayah telah terpaut kepadanya sejak air maninya menetap di sulbinya.

**Keempat**: selain itu, kadang-kadang timbul hal-hal yang mengalahkan cinta naluriah itu lalu melenyapkannya, yaitu keinginan si anak terhadap harta ayahnya, kesibukannya menanggung biaya hidup ayahnya, dan kemalasannya menunaikan kewajiban hak-hak ayahnya.[^p23]

Jika ditanyakan: Maka cinta seseorang kepada dirinya sendiri termasuk jenis yang mana? Dijawab: Hal itu berbeda-beda.

Allah Ta'ala menciptakan manusia dari campuran-campuran yang berbeda-beda (*amshāj*), dan menyusun di dalamnya daya-daya yang saling berlainan, yaitu akal, amarah, dan syahwat, yang masing-masing menariknya; lalu ia diperintahkan untuk meletakkan setiap daya pada tempat yang diperintahkan baginya.[^p24][^t1] Hendaklah ia mengobati jiwanya dengan meminta pertolongan kepada anugerah akal dan memohon taufik Tuhan, Yang Mahaperkasa lagi Mahaagung, agar ia sampai kepada tujuan yang terjauh. Bila ia berbuat demikian terhadap jiwanya, cintanya kepada jiwanya adalah cinta karena keutamaan. Bila ia menguasakan daya amarah dan syahwatnya atas akalnya, mengikuti hawa nafsunya, dan menjadi budak syahwatnya serta alat bagi perut dan kemaluannya, maka cintanya kepada dirinya adalah cinta syahwat, jika memang ia masih mempunyai cinta kepadanya; sebab bagaimana ia dapat dikatakan mencintainya, padahal ia berbuat buruk kepadanya?[^p25]

Seorang bijak berkata kepada seorang sultan yang meminta, "Berilah aku wasiat": "Jika engkau mampu untuk tidak berbuat buruk kepada orang yang engkau cintai, lakukanlah." Sultan itu bertanya: "Apakah seseorang berbuat buruk kepada orang yang ia cintai?" Ia menjawab: "Ya, kepada dirimu sendiri: jika engkau mendurhakai Allah, sungguh engkau telah berbuat buruk kepadanya."

Jika ditanyakan: Ucapanmu ini menuntut bahwa cinta manusia kepada dirinya itu terpuji, padahal riwayat-riwayat datang dengan kebalikannya. Tidakkah engkau lihat diriwayatkan: *"Siapa yang mencintai dirinya, Allah membencinya dan manusia membencinya"*?

Dijawab: Yang dimaksud dengan itu hanyalah cinta karena syahwat, dan telah dikemukakan bahwa cinta semacam itu tercela.

Cinta kadang-kadang dicela dan kadang-kadang dipuji, sesuai dengan kepada apa ia dinisbatkan dan dengan apa ia diukur. Bila yang dimaksud dengannya adalah hawa nafsu dan apa yang diserukan syahwat, maka itu tercela; atas dasar itu dikatakan: *"Cintamu kepada sesuatu membuat buta dan tuli."*[^r-hawa][^d12] Bila yang dimaksud adalah apa yang dituntut akal dalam cinta kepada keutamaan, seperti yang terdapat dalam cinta kepada Allah Ta'ala, kepada Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, dan kepada orang-orang saleh, maka itu terpuji; dan hal itu jelas.

[^p18]: CP: Dalam edisi tahkik tertulis *idhā taḥarrayā iṣlāḥ al-rūḥāniyya* ("bila keduanya bertujuan memperbaiki kerohanian"). Penyunting mencatat bahwa kata itu tidak jelas dalam naskah, dan penerjemah Turki menilai ungkapan itu tidak sesuai dengan konteks. Dalam deretan cinta karena manfaat, ungkapan "memperbaiki kerohanian" memang janggal; yang dituntut konteks adalah tujuan duniawi bersama, seperti menata rumah tangga dan kehidupan. Terjemahan di atas mengikuti tuntutan konteks itu; bacaan asli kata tersebut belum dapat dipastikan. Bandingkan cinta suami istri karena kelezatan dalam paragraf berikutnya.

[^p19]: CP: Edisi tahkik mengulang kalimat "cinta anak kepada kedua orang tuanya demikian pula, dan cinta kedua orang tua kepada anaknya bersifat naluriah" dua kali, dan penyunting sendiri mencatat pengulangan itu; kalimat kedua diabaikan. Kata *ṭarāʾat al-walad* dipahami penyunting sebagai "dorongan anak", tetapi yang dimaksud adalah *ṭarāʾa*/*ṭarāwa*, yakni masa muda dan lembutnya anak (masa kecil), lawan dari masa ia sudah dapat melayani orang tuanya. Kata yang tidak jelas dalam naskah dibaca *fa-ḥallayāhu* ("lalu keduanya menghiasinya").

[^p20]: CP: Edisi tahkik membaca *bi-qadri mā yuḥibbu, ḥaythu mā yajibu ʿalā mā yajibu*. Kata pertama dibaca *yajibu*, sehingga terbentuk rumus tiga syarat yang lazim dalam etika al-Rāghib: menurut kadar yang semestinya, di tempat yang semestinya, dan dengan cara yang semestinya. Terjemahan Turki mengikuti bacaan tahkik dan memahaminya "bila kadar cinta kedua pihak sama". Kata *al-malhā li-l-malhā* dibaca *al-mulhī li-l-mulhā*, yakni orang yang menghibur dan yang dihibur, kawan bersenda gurau.

[^p21]: CP: Edisi tahkik membaca *idhā yurīdu li-nafsihi ḥālan fa-ḥālan* ("bila ia menghendaki untuk dirinya keadaan demi keadaan"); kami membacanya *yazīdu* ("bertambah"), sejajar dengan "naik dalam keutamaan setingkat demi setingkat". Ungkapan "anak adalah dirinya secara perkiraan" (*huwa huwa taqdīran*) berarti bahwa anak bukan ayah itu sendiri secara hakiki, tetapi dianggap demikian karena ia kelanjutan dari wujud dan rupanya.

[^r-jawhar]: **Substansi** (*jawhar*, *jawhariyya*). Lihat catatan istilah *jawhar* dalam terjemahan *Tafṣīl*, catatan no. 36 (`k-jawhar`). Di sini *jawhariyya* berarti kesamaan asal dan pembawaan antara ayah dan anak, yakni bahwa anak berasal dari substansi ayahnya.

[^p22]: CP: Pembagian empat sebab ini menggemakan pembahasan filsafat etika tentang mengapa orang tua lebih mencintai anaknya daripada anak mencintai orang tuanya, dan mengapa pemberi kebaikan lebih mencintai penerima kebaikan daripada sebaliknya: orang tua mengenal anaknya sebagai bagian dari dirinya sejak awal, sedang anak baru mengenal orang tuanya sesudah waktu yang lama; dan seseorang mencintai hasil karyanya seperti seniman mencintai karyanya. Sebab kedua ("manusia lebih mencintai apa yang ia usahakan") dipahami keliru oleh penyunting ("anak lebih mencintai apa yang ia ambil dari ayahnya daripada ayahnya sendiri"); yang dimaksud adalah ayah yang "mengusahakan" anak, seperti tuan yang memperoleh budaknya.

[^p23]: CP: Terjemahan Turki menisbatkan ketiga penghalang ini kepada ayah (ayah menginginkan harta anaknya, ayah malas menunaikan kewajibannya). Konteksnya adalah berkurangnya cinta anak kepada ayahnya, maka ketiganya adalah keadaan si anak. Kata *tūfī ʿalā* berarti "melebihi, mengalahkan".

[^p24]: CP: Edisi tahkik membaca *min ashbāḥ mukhtalifa* ("dari sosok-sosok yang berbeda-beda"), dan penyunting menafsirkannya sebagai sistem-sistem organ tubuh. Kami membacanya *min amshāj mukhtalifa* ("dari campuran-campuran yang berbeda-beda"), dengan mengacu kepada firman Allah: *"Sungguh, Kami telah menciptakan manusia dari setetes mani yang bercampur (amshāj)"* (al-Insan: 2). Kalimat sesudahnya ("menyusun di dalamnya daya-daya yang saling berlainan") sesuai dengan penafsiran ayat itu dalam *Tafṣīl* (lihat catatan t1).

[^t1]: CT: Dalam *Tafṣīl*, Bab Keempat, "Daya-Daya Segala Sesuatu yang Terhimpun dalam Diri Manusia", al-Rāghib menafsirkan *amshāj* dalam al-Insan: 2 sebagai "bercampur dari daya-daya berbagai hal yang berbeda". Di sana manusia menghimpun daya-daya seluruh alam sehingga disebut alam kecil; di sini yang disebut hanya tiga daya jiwa (akal, amarah, syahwat) yang masing-masing menarik manusia ke arahnya, dan tugas manusia adalah meletakkan setiap daya pada tempatnya.

[^p25]: CP: Edisi tahkik membaca *raʾy yuḥibbuhā wa-huwa musīʾ ilayhā*, yang tidak bermakna; kami membacanya *annā yuḥibbuhā* ("bagaimana ia mencintainya"). Terjemahan Turki juga memahaminya sebagai pertanyaan ("Kişi kötülük ettiği birini seviyor olabilir mi?"). Ungkapan *āla li-ʿāriyat baṭnihi wa-farjihi* tidak jelas; kami menerjemahkannya secara umum "alat bagi perut dan kemaluannya".

[^r-hawa]: **Hawa nafsu** (*hawā*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 66 (`m-hawa`, *al-Mufradāt*).

[^d12]: CD: Hadis yang sama dipakai dalam *al-Dharīʿa*, Pasal Ketiga, "Ujub", dengan kesimpulan yang sejalan: "Asal ujub adalah cinta manusia kepada dirinya. … Siapa yang buta dan tuli sulit melihat aib-aibnya." Di sini al-Rāghib lebih membedakan: cinta kepada diri tercela bila ia cinta syahwat, dan terpuji bila ia berarti menuntun diri kepada keutamaan. Kalimat sebelumnya tentang ayah yang tidak melihat aib anaknya "sebagaimana aib-aib manusia pada dirinya sendiri tersembunyi darinya" menerapkan gagasan yang sama.

## Bab Kelima: Hakikat Kasih Sayang, Cinta, Persahabatan, dan Saudara-Saudaranya, serta Asal-Usul Katanya {.judul-bab}

Cinta ialah mengutamakan apa yang engkau lihat atau sangka baik.[^p26] Telah dikemukakan bahwa hal itu hanya ada pada manusia; adapun yang ada pada hewan adalah keakraban.

Asal kata ini adalah *ḥabb* (biji-bijian). Darinya dipinjam *ḥabbat al-qalb* (biji kalbu), karena diserupakan dengannya, sebab bentuknya tergambar seperti bentuk biji. Maka dikatakan *ḥabba fulān* (si fulan menjadi tercinta), yang asalnya *ḥabuba*, seperti *ẓarufa* dan *karuma*; kemudian dikatakan *aḥbabtuhu* (aku mencintainya), seperti *akramtuhu*. Adapun *ḥabibtuhu*, asalnya berarti "aku mengenai biji kalbunya", seperti *shaghaftuhu*, "aku mengenai selaput (*shaghāf*) kalbunya"; tetapi dalam pemakaian lazim ia berlaku seperti *aḥbabtuhu*, sampai-sampai *maḥbūb* dipakai sebagai ganti *muḥabb* (yang dicintai). *Al-ḥibb* berarti yang dicintai, seperti *niqḍ* dalam arti yang dirombak. *Ḥubābuka an yakūna kadhā*, dikatakan maknanya: puncak cintamu, yakni hakikat cintamu terbatas padanya; seperti *murāduka kadhā* (yang engkau kehendaki adalah anu), *munāka kadhā* (angan-anganmu adalah anu), dan *quṣārāka*, yakni hal yang padanya engkau membatasi diri.[^m-hubb]

Ungkapan mereka *aḥabba al-baʿīr* (unta itu "mencintai"), bila unta mogok tidak mau berjalan, dipinjam dari *aḥabba*. Itu berasal dari pembayangan mereka seperti yang tampak dalam ucapan: *"Cintamu kepada sesuatu membuat buta dan tuli,"* dan ucapan penyair:

> Cinta itu buta, tak punya mata.

Seakan-akan unta yang mogok itu dibayangkan dalam rupa pencinta yang dirundung duka. Tidakkah engkau lihat dikatakan: "Ia menjadi mogok dalam cintanya"? Atas dasar itu pula ucapan penyair:

> Hawa cinta menahanku di tempat engkau berada; maka tiada bagiku
> jalan untuk mundur darinya dan tiada pula untuk maju.

Dikatakan: "Ia termangu-mangu dalam cintanya," maka dipakailah ungkapan "tertahannya cinta". Ketumpulan (*balāda*) orang yang mencinta itulah yang menunjukkan alasan dipinjamnya kata *iḥbāb* untuk mogoknya unta.[^p27]

Adapun persahabatan karib (*khulla*) ialah kasih sayang yang disertai kebutuhan. Asalnya dari *khalal*, yaitu celah di antara dua hal. Lalu kata itu dipinjam untuk kelemahan (*wahn*) suatu urusan, dan untuk kefakiran, seperti ucapan "aku menutup *khalla*-nya" (aku menutupi kebutuhannya); orang fakir disebut *khalīl* karena celah yang menimpanya. Kemudian kata itu dipinjam untuk kasih sayang. Pemakaian itu dapat dibenarkan dengan menyerupakan (sahabat karib) dengan orang fakir, seakan-akan ia membayangkan kefakirannya kepada sahabatnya. Dapat pula ia dipakai dalam makna timbal balik, seperti *mukhāll*, sehingga dua sahabat karib adalah dua penutup: masing-masing menutup celah yang lain. Dikatakan pula: (disebut demikian) karena cinta masing-masing menyusup ke dalam kalbu yang lain. Atas dasar itu penyair berkata:[^m-khulla][^p28]

> Engkau telah menyusup ke jalan rohku,
> dan karena itulah sahabat karib dinamai *khalīl*.

Adapun kasih sayang (*mawadda*) ialah mencintai sesuatu disertai mengangankannya. Bila dikatakan *wadidtu kadhā*, hakikatnya: aku mencintainya dan mengangankan tercapainya; meskipun kadang-kadang kata ini dipakai untuk salah satu dari kedua makna itu tanpa yang lain.[^r-wudd]

Adapun persaudaraan (*ukhuwwa*) ialah kokohnya ikatan karena kelahiran atau karena cinta. Dikatakan "di antara keduanya ada *ākhiya*", yakni ikatan yang berlaku seperti persaudaraan; asalnya *ākhiya* ialah tali tambatan yang tertancap di tanah untuk mengikat hewan tunggangan.[^m-akh]

Adapun cinta berahi (*ʿishq*) ialah cinta yang berlebihan. Seorang bijak ditanya tentangnya, lalu menjawab: "Kegilaan hawa nafsu, tidak terpuji dan tidak pula tercela." Ia juga berkata: "Ia adalah gerak jiwa yang kosong." Dikatakan pula: "Ia adalah ketamakan yang lahir dalam kalbu, kemudian tumbuh, lalu terhimpun kepadanya bahan-bahan kerakusan dan kekeraskepalaan, hingga mewariskan duka yang besar."[^r-ishq][^d13] Al-Mutanabbi berkata:

> Tiadalah cinta berahi itu selain keteperdayaan dan ketamakan,
> kalbu menyodorkan dirinya lalu ia pun terluka.

Kata ini kadang-kadang dipakai untuk keutamaan, sebagaimana dipakai untuk yang bermanfaat dan yang lezat. Seseorang berkata: "Sungguh aku berahi kepada kedermawanan sebagaimana perempuan yang cantik diberahikan." Abu al-Syis berkata:

> Ia berahi kepada kemuliaan-kemuliaan dan menanggung bebannya,
> padahal kemuliaan-kemuliaan itu sedikit yang berahi kepadanya.

Adapun *hayamān* ialah semacam kegilaan yang lahir dari cinta berahi. Asalnya dahaga yang sangat: dikatakan *rajul hayamān*, seperti *ʿaṭshān* (orang yang dahaga). Dahaga pun dipakai untuk cinta: dikatakan "aku dahaga kepadanya" dan "aku haus akan pertemuan dengannya".[^p29]

Adapun hawa nafsu (*hawā*) ialah cinta kepada kelezatan secara berlebihan; karena itu ia selalu tercela. Ibnu Abbas berkata: "Hawa nafsu adalah tuhan yang disembah," lalu membaca: *"Maka pernahkah kamu melihat orang yang menjadikan hawa nafsunya sebagai tuhannya"* (al-Jasiyah: 23). Asal katanya *hawiya*, dengan pola *ʿalima*. Allah, Yang Mahaperkasa lagi Mahaagung, berfirman: *"dan janganlah engkau mengikuti hawa nafsu, karena akan menyesatkan engkau dari jalan Allah"* (Shad: 26), dan berfirman: *"dan janganlah engkau mengikuti orang yang hatinya telah Kami lalaikan dari mengingat Kami, serta menuruti keinginannya"* (al-Kahf: 28). Beliau, semoga salam atasnya, bersabda: *"Durhakailah hawa nafsumu dan kaum perempuan, lalu taatilah siapa yang engkau kehendaki."* Dikatakan: ia dinamai *hawā* karena ia menjerumuskan (*yahwī*) pemiliknya ke dalam neraka, atau karena ia menjadikan kalbu seperti di udara (*hawāʾ*), tidak menetap.[^r-hawa2] *Ṣabwa* ialah melakukan perbuatan anak kecil (*ṣabī*).

*Wajd* ialah kesedihan yang didapati manusia dalam kalbunya, yang diwariskan oleh cinta. Yang menunjukkan bahwa ia berasal dari *wujūd* (mendapati) ialah dipakainya kata "merasa" untuknya, seperti ucapan penyair:[^m-wajd]

> Demi hak cinta, sungguh aku merasakan karena cinta
> bara di hatiku dan remuk di tulang-tulangku.

Adapun persahabatan (*ṣadāqa*) ialah saling mencintai secara setara demi kebaikan yang murni. Dikatakan "saling mencintai", bukan "cinta", karena persahabatan tidak terjadi sebelum ada dari kedua pihak; sedang cinta kadang dikatakan untuk yang ada dari satu pihak saja tanpa yang lain, dan untuk apa yang dirasakan manusia terhadap benda-benda mati dan hewan-hewan lain. Dikatakan "demi kebaikan yang murni" untuk mengecualikan cinta karena manfaat dan karena kelezatan; sebab yang demikian itu pada hakikatnya bukan persahabatan, meskipun lafal itu kadang dipakai untuknya karena diserupakan dengan cinta yang utama dan digambarkan dalam rupanya.

Karena definisi yang kami sebutkan itulah dikatakan: "Sahabat adalah orang lain yang tidak lain adalah engkau, hanya saja ia berbeda darimu dalam pribadi." Dikatakan pula: "Persahabatan adalah bersatunya jiwa-jiwa yang secara aktual terpisah dalam banyak pribadi."[^d14][^p30] Makna ini diisyaratkan al-Mutanabbi dengan ucapannya:

> Sahabatmu adalah dirimu, bukan orang yang kau sebut kawan karibmu,
> meskipun banyak basa-basi dan kata-katanya.

Kata ini berasal dari *ṣidq* (kejujuran), yaitu kesesuaian kabar dengan apa yang dikabarkan. Asalnya pada ucapan, tetapi dipakai pula pada keyakinan dan perbuatan; dikatakan: "Ia jujur dalam keyakinannya dan dalam keberaniannya maju." Allah Ta'ala mendustakan orang-orang munafik dengan firman-Nya: *"dan Allah menyaksikan bahwa orang-orang munafik itu benar-benar orang pendusta"* (al-Munafiqun: 1), yakni dalam keyakinan mereka, bukan dalam ucapan mereka.[^r-sidq]

[^p26]: CP: Di sini cinta didefinisikan dengan *īthār* ("mengutamakan"), sedang di awal Bab Kedua dengan *irāda* ("menghendaki"). Keduanya dekat: dalam *al-Mufradāt*, s.v. *ḥ-b-b*, al-Rāghib menjelaskan bahwa *istiḥbāb* yang dihubungkan dengan kata *ʿalā* bermakna *īthār*, seperti *"jika mereka lebih mencintai (istaḥabbū) kekafiran daripada iman"* (at-Taubah: 23). Terjemahan Turki juga membaca *īthār* ("seçmendir").

[^m-hubb]: **Cinta: asal kata** (*ḥubb*, *ḥabba*). Dalam *al-Mufradāt*: *ḥabb* dan *ḥabba* dipakai untuk gandum, jelai, dan makanan sejenis, serta untuk biji tanaman wangi; *ḥibb* ialah yang sangat dicintai; *ḥabbat al-qalb* (biji kalbu) karena diserupakan dengan biji dalam bentuknya. *Ḥababtu fulānan* pada asalnya berarti "aku mengenai biji kalbunya", seperti *shaghaftuhu*, *kabadtuhu*, dan *faʾadtuhu* (aku mengenai selaput kalbunya, hatinya, jantungnya); *aḥbabtu fulānan* berarti "aku menjadikan kalbuku sasaran bagi cintanya"; tetapi dalam pemakaian lazim *maḥbūb* diletakkan di tempat *muḥabb*, dan *ḥababtu* dipakai di tempat *aḥbabtu*. *Aḥabba al-baʿīr* ialah bila unta mogok dan menetap di tempatnya, seakan ia mencintai tempat ia berhenti; dan *ḥubābuka an tafʿala kadhā* berarti puncak cintamu adalah itu. Seluruh uraian kebahasaan bab ini adalah perluasan dari entri tersebut. (*al-Mufradāt*, s.v. *ḥ-b-b*.)

[^p27]: CP: Kalimat ini rusak dalam edisi tahkik. Kami membaca *wa-qīla: taladdada fī hawāhu* ("ia termangu-mangu dalam cintanya"; teks: *taladhdhadha*, "ia menikmati", yang oleh penyunting dibetulkan dari *taladha*) *fa-stuʿmila wuqūf al-hawā*. Kata *al-balāda* ("ketumpulan") oleh penerjemah Turki dianggap salah tulis dan diterjemahkan "retorika" (*belâğat*); kami mempertahankannya, sebab justru ketumpulan orang yang mencinta, yang dibutakan dan ditulikan oleh cintanya dan tertahan di tempatnya, yang menjelaskan mengapa unta yang mogok dikatakan "mencintai". Kata *li-l-ḥirān* ("untuk mogok") mengikuti pembetulan penyunting (teks: *li-l-jirān*).

[^m-khulla]: **Persahabatan karib** (*khulla*, *khalīl*). Dalam *al-Mufradāt*: *khalal* ialah celah di antara dua hal; *khalal* dalam suatu urusan seperti kelemahan di dalamnya, diserupakan dengan celah di antara dua hal; *khalla* ialah kerusakan yang menimpa jiwa, entah karena syahwatnya kepada sesuatu entah karena kebutuhannya kepadanya, sehingga *khalla* ditafsirkan sebagai kebutuhan. *Khulla* ialah kasih sayang, entah karena ia menyusup (*takhallul*) ke dalam jiwa, entah karena ia menembus jiwa seperti anak panah menembus sasaran, entah karena sangatnya kebutuhan kepadanya. Di sana pula al-Rāghib mengutip bait "Engkau telah menyusup ke jalan rohku…", dan menolak pendapat Abū al-Qāsim al-Balkhī bahwa Allah boleh dikatakan mencintai hamba tetapi tidak boleh dikatakan menjadikannya sahabat karib: bila kedua kata dipakai untuk Allah, yang dimaksud dengan keduanya adalah semata-mata berbuat baik. (*al-Mufradāt*, s.v. *kh-l-l*.) *Kashshāf* tidak memuat entri khusus *al-khulla*. Persoalan ini dibahas dalam Bab Keenam.

[^p28]: CP: Beberapa kata dalam kalimat ini tidak jelas dalam naskah, dan penyunting mencatatnya. Kami membaca *wa-l-khalīlān al-sāddān, kullu wāḥidin minhumā yasuddu khalala al-ākhar* ("dua sahabat karib adalah dua penutup, masing-masing menutup celah yang lain") dan *li-takhallul maḥabbat kullin minhumā qalba al-ākhar* ("karena cinta masing-masing menyusup ke dalam kalbu yang lain"). Kalimat terakhir tercetak dua kali dalam edisi tahkik.

[^r-wudd]: **Kasih sayang** (*wudd*, *mawadda*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 367 (`m-wudd`, *al-Mufradāt*): mencintai sesuatu dan mengangankan keberadaannya. Definisi dalam risalah ini hampir sama persis.

[^m-akh]: **Saudara** (*akh*, *ukhuwwa*). Dalam *al-Mufradāt*: asalnya *akhw*, yaitu orang yang bersekutu dengan orang lain dalam kelahiran, dari kedua pihak atau dari salah satunya, atau dari penyusuan; lalu dipinjam untuk setiap orang yang bersekutu dengan orang lain dalam kabilah, agama, keterampilan, muamalah, kasih sayang, dan hubungan-hubungan lain, seperti *"Sesungguhnya orang-orang mukmin itu bersaudara"* (al-Hujurat: 10). (*al-Mufradāt*, s.v. *a-kh-w*.) Risalah ini menambahkan asal kata yang lain, *ākhiya* (tali tambatan), yang menekankan unsur ikatan yang kokoh. *Kashshāf* tidak memuat entri khusus *al-ukhuwwa*.

[^r-ishq]: **Cinta berahi** (*ʿishq*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 277 (`k-ishq`, *Kashshāf*): *ʿishq* ialah tingkatan terakhir dari cinta, cinta yang berlebihan dan sangat.

[^d13]: CD: Dalam *al-Dharīʿa*, Pasal Ketiga, "Pernikahan yang Baik dan yang Buruk", dikutip ucapan-ucapan yang sejenis: "Kegilaan yang pemiliknya tidak diberi pahala karenanya", "Penyakit jiwa yang kosong, yang tidak memiliki cita-cita", dan "pilihan yang buruk yang bertemu dengan jiwa yang kosong". Di sana *ʿishq* yang dibahas hanya yang bersifat syahwat, dan dinilai sebagai kedunguan. Dalam Pasal Kelima, "Hakikat Cinta dan Macam-Macamnya", *ʿishq* dibagi: karena kelezatan tercela, karena keutamaan terpuji, dan "ia tidak terjadi karena manfaat". Pernyataan di bawah ini, bahwa kata *ʿishq* "dipakai untuk keutamaan sebagaimana dipakai untuk yang bermanfaat dan yang lezat", bertentangan dengan pengecualian manfaat itu. Mungkin al-Rāghib di sini hanya melaporkan pemakaian bahasa, sedang di *al-Dharīʿa* ia menetapkan hakikatnya (lihat nota kaki *al-Dharīʿa* no. 366).

[^p29]: CP: Edisi tahkik membaca *wa-aṣluhu farṭ al-ʿishq* ("asalnya berlebihnya cinta berahi"), yang hanya mengulang kalimat sebelumnya. Kami membaca *farṭ al-ʿaṭash* ("dahaga yang sangat"), sebab kalimat berikutnya menjelaskan kata ini dengan *ʿaṭshān* dan dengan pemakaian "dahaga" untuk cinta; *al-Mufradāt*, s.v. *h-y-m*, juga menjelaskan *hayamān* sebagai "sangat dahaga", dan *huyām* sebagai penyakit unta karena dahaga "yang dijadikan perumpamaan bagi orang yang sangat berahinya".

[^r-hawa2]: **Hawa nafsu** (*hawā*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 66 (`m-hawa`, *al-Mufradāt*) dan no. 67 (`k-hawa`, *Kashshāf*). Asal kata "menjerumuskan pemiliknya" diambil dari *al-Mufradāt*: hawa nafsu dinamai demikian karena ia menjerumuskan pemiliknya di dunia ke dalam setiap malapetaka dan di akhirat ke dalam *hāwiya* (neraka). Kedua ayat di atas mengikuti redaksi terjemahan *al-Dharīʿa*, Pasal Pertama, "Penjelasan Perebutan Hawa Nafsu dengan Akal".

[^m-wajd]: ***Wajd*** (*wajd*, *wujūd*). Dalam *al-Mufradāt*: "mendapati" (*wujūd*) ada beberapa macam: dengan salah satu dari lima indra, seperti "aku mendapati rasanya"; dengan daya syahwat, seperti "aku mendapati kenyang"; dengan daya amarah, seperti mendapati kesedihan dan kemarahan; dan dengan akal atau melalui akal, seperti mengenal Allah. (*al-Mufradāt*, s.v. *w-j-d*.) Maka *wajd* dalam arti kesedihan cinta adalah "mendapati" dengan daya jiwa, dan karena itu dapat dipakaikan kata "merasa". Dalam pemakaian kaum sufi yang dicatat *Kashshāf*, *wajd* kemudian menjadi istilah untuk keadaan rohani yang datang kepada kalbu tanpa diusahakan; makna itu belum dimaksud di sini.

[^d14]: CD: Ucapan pertama sejalan dengan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Persahabatan": "Seorang bijak ditanya tentang sahabat, lalu menjawab: 'Ia adalah engkau dalam jiwa, hanya saja ia orang lain dalam wujud.'" Redaksinya di sini sedikit berbeda ("orang lain yang tidak lain adalah engkau, hanya saja ia berbeda darimu dalam pribadi"). Di *al-Dharīʿa* ucapan itu diletakkan sebagai tanda besarnya manfaat sahabat; di sini ia diturunkan dari definisi persahabatan sebagai saling mencintai secara setara.

[^p30]: CP: *Bi-l-fiʿl* ("secara aktual") mengikuti bacaan edisi tahkik; penyunting menyebut bahwa naskah membaca *bi-l-ʿaql* ("dengan akal") dan menganggapnya salah tulis. Maksudnya: jiwa-jiwa itu terpisah dalam kenyataan karena berada dalam banyak pribadi, tetapi bersatu dalam persahabatan.

[^r-sidq]: **Kejujuran** (*ṣidq*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 206 (`m-sidq`, *al-Mufradāt*) dan no. 207 (`k-sidq`, *Kashshāf*): kejujuran ialah kesesuaian ucapan dengan apa yang ada dalam hati dan dengan apa yang dikabarkan. Penjelasan tentang orang munafik yang berdusta dalam keyakinan, bukan dalam ucapan, juga terdapat dalam *al-Dharīʿa*, Pasal Kedua, "Kejujuran dan Pujiannya, Dusta dan Celaannya".

## Bab Keenam: Cinta Allah kepada Hamba-Hamba-Nya dan Cinta Hamba-Hamba kepada-Nya, Persahabatan Karib antara Dia dan Mereka, serta Pemakaian Ungkapan Itu untuk-Nya {.judul-bab}

Ketahuilah bahwa menisbatkan cinta kepada Allah, Yang Mahaperkasa lagi Mahaagung, telah dibolehkan; maka dikatakan: Muhammad adalah kekasih (*ḥabīb*) Allah. Allah Ta'ala berfirman: *"maka kelak Allah akan mendatangkan suatu kaum, Dia mencintai mereka dan mereka pun mencintai-Nya"* (al-Ma'idah: 54), dan berfirman: *"ikutilah aku, niscaya Allah mencintaimu"* (Ali 'Imran: 31). Seorang perempuan terdengar berkata ketika tawaf di Baitullah: "Demi cinta-Mu kepadaku, wahai Tuhan, rahmatilah aku." Dikatakan kepadanya: "Tidakkah cukup engkau berkata: Demi cintaku kepada-Mu?" Ia menjawab: "Allah Ta'ala berfirman: *'Dia mencintai mereka dan mereka pun mencintai-Nya'*; Dia mendahulukan cinta-Nya kepada mereka atas cinta mereka kepada-Nya."

Jika ditanyakan: Bagaimana sah menisbatkan cinta kepada Allah, Yang Mahaperkasa lagi Mahaagung, sehingga dikatakan bahwa Dia mencintai hamba-hamba-Nya yang saleh, dengan makna yang telah dirumuskan dalam definisinya?[^p31] Dijawab: Cinta memiliki permulaan dan kesempurnaan. Permulaannya ialah terkhususkannya pencinta dengan suatu keadaan (*hayʾa*) tertentu, dan kesempurnaannya ialah keluarnya kebaikan dari pencinta kepada yang dicintai sesuai dengan tuntutan cinta. Manusia perlu terkhusus dengan keadaan ini karena kekurangannya; seandainya ia sempurna, ia tidak membutuhkan keadaan itu. Telah tetap bahwa Allah Yang Maha Pencipta suci dari segala kekurangan. Maka bila Dia disifati mencintai, itu tidak berarti bahwa Dia memiliki suatu keadaan, melainkan bahwa Dia melimpahkan kebaikan-kebaikan kepada hamba-hamba-Nya dengan cara paling sempurna yang dituntut oleh cinta yang utama.[^d15]

Atas dasar itu pula, bila Dia disifati adil, yang dimaksud adalah bahwa perbuatan-perbuatan yang adil keluar dari-Nya, bukan bahwa Dia menjadi memiliki suatu keadaan; Mahatinggi Allah dari keadaan-keadaan. Atas dasar itu pula, bila dikatakan "Allah mendengar orang yang memuji-Nya", yang dimaksud bukan permulaan perbuatan (mendengar), melainkan kesempurnaan dan tuntutannya, yaitu bahwa Dia senantiasa mengawasi untuk memberi balasan.

Adapun cinta hamba-hamba kepada-Nya, wajib engkau ketahui bahwa ibadah kepada Allah ada tiga macam: karena mengikuti kebiasaan; karena menginginkan kehidupan dunia atau akhirat; atau karena mencari rida Tuhan dan memelihara kebenaran.[^r-ibada]

Abu Zaid berkata:[^p32] "Siapa yang menyembah Allah karena kebiasaan, ia orang yang zalim; siapa yang menyembah-Nya karena harap dan takut, ia orang yang pertengahan; dan siapa yang menyembah-Nya karena cinta, ia orang yang lebih dahulu (berbuat kebaikan)." Kemudian ia membaca firman Allah Ta'ala: *"Kemudian Kitab itu Kami wariskan kepada orang-orang yang Kami pilih di antara hamba-hamba Kami, lalu di antara mereka ada yang menzalimi diri sendiri, ada yang pertengahan dan ada (pula) yang lebih dahulu berbuat kebaikan dengan izin Allah"* (Fatir: 32).

Siapa yang tujuannya dalam ibadah adalah agar Allah memberinya harta atau kedudukan, itulah kedudukan paling hina yang dapat dicapai seorang hamba.[^p33] Dikatakan: "Siapa yang menyembah Allah demi suatu imbalan, ia orang yang tercela."

Cinta kepada Allah Ta'ala ialah bahwa hamba mengenal-Nya sampai batas terjauh kemampuan manusia, menyembah dan menaati-Nya, serta melampaui ketaatan dengan anggota badan menuju ketaatan dengan lintasan-lintasan hati.[^p34] Al-Syibli berkata kepada seseorang yang banyak berzikir kepada Allah: "Aku lihat zikir telah menyibukkanmu dari Yang Diingat!"

Di antara hak cinta kepada-Nya ialah bahwa hamba memutus tali-tali yang mengikat dirinya dengan hal-hal yang terindra, sehingga ia tidak menoleh kepadanya kecuali sekadar yang tidak dapat tidak; cintanya tidak bertambah karena karunia yang diberikan kepadanya, dan tidak berkurang karena cobaan yang menimpanya.[^p35] Bila hamba telah berbuat demikian, ia mencintai Allah pada saat itu, dan ia termasuk orang yang disifati Allah Ta'ala dalam firman-Nya, Yang Mahaperkasa lagi Mahaagung: *"(yaitu) orang-orang yang beriman dan hati mereka menjadi tenteram dengan mengingat Allah. Ingatlah, hanya dengan mengingat Allah hati menjadi tenteram"* (ar-Ra'd: 28), dan termasuk orang yang dijanjikan-Nya dengan firman-Nya: *"Dan keridaan Allah lebih besar"* (at-Taubah: 72).

Hal ini diberitakan oleh riwayat dari Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bahwa Allah Ta'ala berfirman: *"Tidaklah hamba-Ku mendekatkan diri kepada-Ku dengan sesuatu yang lebih Aku cintai daripada apa yang Aku wajibkan kepadanya. Hamba-Ku senantiasa mendekatkan diri kepada-Ku dengan amalan-amalan sunah hingga Aku mencintainya. Bila Aku telah mencintainya, Aku menjadi pendengarannya yang dengannya ia mendengar, penglihatannya yang dengannya ia melihat, lisannya yang dengannya ia berbicara, dan tangannya yang dengannya ia menggenggam."* Di dalamnya terdapat isyarat yang menakjubkan.

Diceritakan dari Aristoteles suatu ucapan yang menguatkan sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, yaitu bahwa ia berkata: "Siapa yang dicintai Allah, Dia memeliharanya sebagaimana para sahabat saling memelihara, dan berbuat baik kepadanya."[^p36] Ungkapan ini dianggap buruk oleh sebagian ahli kalam, padahal ia tidak jauh (dari kebenaran) bagi orang yang *"menggunakan pendengarannya, sedang dia menyaksikannya"* (Qaf: 37) dan merenungkannya dengan kehadiran hati. Allah Ta'ala berfirman kepada Musa, semoga salam atasnya: *"Sesungguhnya Aku memilih (melebihkan) engkau"* (al-A'raf: 144). Sebagian sufi berkata: "Siapa yang dicintai Allah, dialah yang dikehendaki (*murād*), dan kedudukannya adalah kedudukan orang yang difirmankan kepadanya: *'Bukankah Kami telah melapangkan dadamu (Muhammad)?'* (asy-Syarh: 1)."[^k-murid] Atas dasar inilah dikatakan: Muhammad adalah kekasih Allah.

Adapun persahabatan karib (*khulla*), dikatakan bahwa ia dinisbatkan kepada hamba dan tidak dinisbatkan kepada-Nya. Maka dikatakan: Ibrahim adalah sahabat karib (*khalīl*) Allah, dan tidak dikatakan: Allah adalah sahabat karib Ibrahim.

Jika ditanyakan: (Mengapa) orang menahan diri dari memakai ungkapan itu, padahal diketahui bahwa *khalīl* termasuk nama-nama korelatif (*mutaḍāyifa*), yang adanya salah satunya menuntut adanya yang lain dan hilangnya salah satunya menuntut hilangnya yang lain, seperti saudara, sahabat, ayah, dan anak? Dijawab: Hal itu memang demikian pada *khalīl* yang berarti sahabat; tetapi yang dimaksud dengan ucapan "Ibrahim adalah *khalīl* Allah" bukan semata persahabatan, melainkan kefakiran kepada-Nya.[^r-faqr] Ibrahim dikhususkan dengan nama ini, meskipun seluruh maujud sama dengannya dalam kefakiran kepada-Nya, karena suatu makna yang ada padanya. Yaitu, ketika ia telah tidak membutuhkan segala sesuatu yang membuat berkecukupan dari harta benda dunia dan bersandar kepada Allah dengan sebenar-benarnya, ia sampai pada keadaan ketika Jibril bertanya kepadanya, "Adakah engkau punya keperluan?", ia menjawab, "Kepadamu, tidak." Ia bersabar ketika dilemparkan ke dalam api dan ketika menyerahkan anaknya untuk disembelih. Demikian pula ucapan Musa, semoga salam atasnya: *"Ya Tuhanku, sesungguhnya aku sangat memerlukan sesuatu kebaikan (makanan) yang Engkau turunkan kepadaku"* (al-Qasas: 24). Maka ia tidak menoleh kepada sesuatu pun yang membuat berkecukupan, dan tidak menganggap selain Dia sebagai kekayaan; karena ia tidak membutuhkan selain-Nya, ia menjadi fakir kepada-Nya, maka ia dikhususkan dengan nama ini. Seandainya kita mengetahui seseorang yang memiliki sifat ini, tentu kita membolehkan pemakaian sebutan itu untuknya.[^d16]

Lafal "fakir" yang dimaksud di sini adalah yang terpuji, yang dijadikan Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, sebagai angan-angannya ketika beliau berdoa: *"Ya Allah, hidupkanlah aku dalam keadaan miskin, matikanlah aku dalam keadaan miskin, dan kumpulkanlah aku dalam golongan orang-orang miskin."* Ia bukan yang dimaksud dalam sabda beliau: *"Hampir-hampir kefakiran menjadi kekafiran."* Sebab yang dimaksud di sana adalah tiadanya harta yang membuat berkecukupan bagi orang yang menyengaja membiasakan diri dengannya dan mengira bahwa itulah kekayaan, sehingga ia merasa cukup dengannya.

Jika ditanyakan: Bolehkah memakai lafal sahabat (*ṣadīq*), kekasih (*wadīd*), dan saudara untuk Allah? Dijawab: Tidak boleh sedikit pun dari itu. Sebab dalam definisi persahabatan telah disebutkan bahwa ia adalah saling mencintai secara setara; kasih sayang mengandung makna mengangankan; dan saudara pada asalnya diletakkan untuk orang yang engkau dan dia dihimpun oleh nasab keayahan. Mahatinggi Allah, Raja Yang Sebenarnya, dari disifati dengan sesuatu dari itu.

[^p31]: CP: Penyunting mencatat bahwa ungkapan *ʿalā al-maʿnā alladhī ḥudda fī ḥaddihā* tidak jelas dalam naskah; penerjemah Turki menerjemahkannya menurut konteks. Yang dimaksud adalah definisi cinta dalam Bab Kedua dan Kelima ("menghendaki/mengutamakan apa yang dilihat atau disangka baik"), yang mengandaikan kekurangan pada pencinta.

[^d15]: CD: Prinsip "permulaan dan kesempurnaan" ini adalah kaidah tafsir al-Rāghib untuk sifat-sifat yang dinisbatkan kepada Allah: dari suatu keadaan jiwa manusia, yang dinisbatkan kepada Allah hanyalah ujungnya, yaitu perbuatan yang lahir darinya. Dalam *al-Mufradāt*, s.v. *ḥ-b-b*, rumusannya singkat: "Cinta Allah kepada hamba adalah pemberian nikmat-Nya kepadanya, dan cinta hamba kepada-Nya adalah mencari kedekatan di sisi-Nya"; lihat pula nota kaki *al-Dharīʿa* no. 361 (`k-mahabba`), yang mengutip pendapat jumhur ahli kalam bahwa cinta Allah kepada hamba adalah kehendak-Nya untuk memuliakan dan memberi mereka pahala. Kaidah yang sama berlaku untuk "keadilan" (*ʿadl*) dan "mendengar" dalam paragraf berikutnya.

[^r-ibada]: **Ibadah** (*ʿibāda*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 46 (`m-ibada`, *al-Mufradāt*) dan no. 47 (`k-ibada`, *Kashshāf*), dan terjemahan *Tafṣīl*, catatan no. 74 (`r-ibada`).

[^p32]: CP: Penyunting menduga tokoh ini Abū Zayd al-Balkhī (w. 322 H), filsuf dan sastrawan. Ucapan tentang tiga tingkat penyembah yang dihubungkan dengan Fatir: 32 lebih bercorak sufi, dan bentuk tulisan *Abū Zayd* mudah tertukar dengan *Abū Yazīd* (al-Bisṭāmī); identitasnya tidak dapat dipastikan dari teks ini.

[^p33]: CP: Edisi tahkik membaca *fa-huwa aḥsanu manzilatin yantahī ilayhā al-ʿabd* ("itulah kedudukan terbaik yang dapat dicapai seorang hamba"), yang bertentangan dengan konteks dan dengan kalimat sesudahnya ("ia orang yang tercela"). Kami membacanya *akhassu* ("paling hina"), yang dalam tulisan hanya berbeda titik. Terjemahan Turki berusaha mendamaikannya dengan menambahkan "di dunia", tetapi tetap mempertahankan "terbaik".

[^p34]: CP: Edisi tahkik membaca *ʿalā ghāyat ṭuruq al-sharr* ("pada puncak jalan-jalan keburukan"), yang dipahami penyunting sebagai "dalam keadaan susah dan fakir"; terjemahan Turki mengikutinya ("dalam keadaan paling buruk dan sulit"). Kami membacanya *ʿalā ghāyat ṭawq al-bashar* ("sampai batas terjauh kemampuan manusia"), yang sesuai dengan susunan kalimat: pengenalan, lalu ibadah dan ketaatan, lalu ketaatan batin.

[^p35]: CP: Edisi tahkik membaca kata *minḥa* ("karunia") dua kali: "tidak bertambah karena karunia … dan tidak berkurang karena karunia". Kata kedua dibaca *miḥna* ("cobaan"), yang hanya berbeda urutan huruf.

[^p36]: CP: Ucapan ini sejalan dengan bagian akhir *Etika Nikomakhea* karya Aristoteles (Buku X), yang menyatakan bahwa jika para dewa memperhatikan urusan manusia, mereka tentu berbuat baik kepada orang yang paling mencintai dan memuliakan akal, sebagai kepada orang-orang yang mereka cintai (*philoi*). Karya itu dikenal dalam terjemahan Arab dan dipakai para penulis etika seperti Ibnu Miskawaih. Keberatan sebagian ahli kalam agaknya terletak pada penyerupaan hubungan Allah dan hamba dengan hubungan dua sahabat, yang menurut paragraf terakhir bab ini memang tidak boleh diungkapkan dengan kata "sahabat".

[^k-murid]: **Yang dikehendaki** (*murād*) dan **yang menghendaki** (*murīd*). *Kashshāf*: *murīd* adalah pelaku dari *irāda*; bagi kaum sufi ia punya dua makna: (1) pencinta, yaitu penempuh jalan yang ditarik (*al-sālik al-majdhūb*); (2) orang yang mengikuti, yang mata batinnya diterangi Allah dengan cahaya petunjuk sehingga ia selalu melihat kekurangannya dan berusaha mencari kesempurnaan. Abū ʿUthmān berkata: *murīd* ialah orang yang kalbunya telah mati dari segala sesuatu selain Allah. (*Kashshāf*, s.v. *al-murīd*.) Dalam pasangan istilah sufi ini, *murād* adalah orang yang dikehendaki dan ditarik Allah tanpa jerih payah pencarian, seperti Nabi yang dadanya dilapangkan tanpa ia minta; karena itu "kekasih Allah" dijelaskan dengan "yang dikehendaki". *Al-Mufradāt* tidak memuat pemakaian ini.

[^r-faqr]: **Kefakiran** (*faqr*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 287 (`m-faqr`, *al-Mufradāt*) dan no. 288 (`k-ghina`, *Kashshāf*): dalam *al-Mufradāt*, *faqr* dipakai dalam empat makna, yang terakhir adalah kefakiran kepada Allah, seperti dalam doa "Ya Allah, kayakanlah aku dengan kefakiran kepada-Mu". Kefakiran Ibrahim yang dimaksud di sini adalah makna keempat ini, bukan makna pertama (kebutuhan yang meliputi semua maujud) dan bukan makna kedua (tidak memiliki harta).

[^d16]: CD: Penjelasan tentang *khalīl* sebagai "yang fakir kepada Allah" sejalan dengan pembagian makna *faqr* dalam *al-Dharīʿa*, Pasal Ketiga, "Kanaah dan Zuhud" (lihat nota kaki *al-Dharīʿa* no. 287). Dalam *al-Mufradāt*, s.v. *kh-l-l*, al-Rāghib memberi dua penjelasan untuk *"Dan Allah telah menjadikan Ibrahim sebagai kesayangan(-Nya)"* (an-Nisa': 125): Ibrahim dinamai *khalīl* karena kefakirannya kepada Allah dalam setiap keadaan, atau karena *khulla* berarti kasih sayang yang menyusup ke dalam jiwa; dan bila kata itu dipakai untuk Allah, yang dimaksud semata-mata berbuat baik. Di sini hanya penjelasan pertama yang dipakai, sebab penjelasan kedua akan menuntut timbal balik yang ditolak pada akhir bab ini.

## Bab Ketujuh: Perselisihan Manusia dalam Mengambil Sahabat {.judul-bab}

Manusia berselisih pendapat tentang mengambil sahabat dan menghindarinya.

Orang yang menghindarinya berhujah bahwa di antara manusia banyak orang jahat dan sedikit orang baik, sampai-sampai dikatakan: "Sebaik-baik manusia ialah yang paling jauh darimu," dan "Sebaik-baik manusia ialah yang belum engkau uji."[^p37] Seorang bijak berkata: "Seandainya dunia dipenuhi binatang buas dan ular, aku tidak takut kepada keduanya; tetapi seandainya dari manusia hanya tersisa satu orang, aku takut kepadanya." Seakan disepakati kebenarannya ucapan al-Mutanabbi:

> Aku pun mulai meragukan orang yang kupilih sebagai sahabat,
> karena aku tahu ia hanyalah salah seorang dari manusia.

Kemudian, karena segala sesuatu tampak gangguannya dan jelas wataknya dengan ujian yang paling ringan serta sebab dan pengamatan yang paling sedikit, kecuali manusia, sebab ia mengenakan pakaian kemunafikan dan riya, lalu berlagak berani dan berlagak dermawan tanpa keberanian dan kedermawanan, maka wajib berhati-hati terhadap mereka dan sedapat mungkin tidak membutuhkan mereka. Karena itu seorang bijak berkata: "Waspadalah terhadap orang yang engkau percayai, sebab titipan-titipan manusia tidak hilang kecuali di tangan orang-orang tepercaya."[^p38] Abu Tammam berkata dengan kata-kata yang paling fasih:

> Berubah-ubahnya kawan, bila engkau selidiki,
> akan membuatmu lupa akan panjangnya perubahan zaman.

Seandainya sahabat itu ada pun, semestinya ia tetap tidak dibutuhkan; maka bagaimana lagi bila ia tidak ada? Seorang bijak ditanya tentang sahabat, lalu menjawab: "Ia adalah nama yang tidak memiliki makna, makhluk yang tidak ada." Yang lain berkata: "Manusia yang paling jauh perjalanannya ialah orang yang melakukan perjalanan untuk mencari sahabat." Seseorang berkata kepada al-Fudhail: "Tunjukkanlah aku kepada seorang saudara yang dapat kuandalkan." Ia menjawab: "Itu barang hilang yang tidak akan ditemukan." Penyair berkata:

> Aku mencari kasih sayang manusia yang sehat; alangkah ajaibnya!
> Yang kucari adalah sesuatu yang tak pernah luput dari penyakit.

Betapa banyak bencana menimpa orang yang tertipu oleh seorang sahabat dan merasa tenteram dengan seorang kawan, sedang orang yang mengamalkan ucapan orang bijak selamat darinya: "Siapa yang mampu memisahkan diri dari manusia, hendaklah ia memisahkan diri dari mereka; dan siapa yang tidak mampu dengan tubuhnya, hendaklah ia memisahkan diri dari mereka dengan kalbunya."

Orang yang menginginkannya berkata: Manusia, meskipun banyak orang jahat di antara mereka dan terdapat pamer dan riya pada mereka, tidak akan kehilangan orang yang dicari sama sekali, bila ia bersungguh-sungguh mencari saudara yang dapat ia jadikan kawan dan sahabat yang dapat ia jadikan orang kepercayaan. Kesetiaan (*wafāʾ*) tidak hilang dari manusia, meskipun jarang.[^r-wafa]

Diriwayatkan bahwa Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, mempersaudarakan para sahabatnya dua kali. Seandainya ucapan mereka "sahabat" hanyalah lafal kosong atau khayalan belaka, tentu Ali, semoga Allah meridainya, tidak berkata: "Hendaklah kalian memiliki saudara-saudara, karena mereka adalah bekal zaman dalam agama dan dunia."[^p39] Tidakkah engkau lihat Allah Ta'ala menceritakan ucapan penghuni neraka Jahanam: *"Maka (sekarang) kita tidak mempunyai pemberi syafaat (penolong), dan tidak pula mempunyai teman yang akrab"* (asy-Syu'ara': 100-101)? Orang yang berkata "nama yang tidak memiliki makna" bermaksud menunjukkan sedikitnya keberadaan sahabat, dengan menempuh cara orang yang mengungkapkan sesuatu yang sedikit dengan penafian dan ketiadaan.[^d17]

[^p37]: CP: Kedua ucapan ini rusak dalam edisi tahkik. Yang pertama tertulis *khayr al-nās abqāhum* ("yang paling kekal/paling lama hidup"); penerjemah Turki mengusulkan *atqāhum* ("yang paling bertakwa"), tetapi keduanya tidak menunjang hujah orang yang menghindari sahabat. Kami menduga bacaan aslinya *abʿaduhum* ("yang paling jauh"). Yang kedua tertulis *man lam tajid bihi*, yang tidak bermakna; penyunting memaknainya "yang engkau pegang erat karena langkanya". Kami membacanya *man lam tujarribhu* ("yang belum engkau uji"), sejalan dengan kalimat sesudahnya tentang manusia yang wataknya baru tampak dengan ujian. Keduanya bacaan dugaan.

[^p38]: CP: Edisi tahkik membaca *fa-inna dharāʾiʿ al-nās* ("sarana-sarana manusia"), dan penyunting menjelaskannya secara dipaksakan ("harapan tidak kecewa kecuali pada orang-orang yang kita percayai"); terjemahan Turki memahaminya "kepercayaan manusia tidak dikhianati kecuali oleh orang-orang yang mereka percayai". Kami membaca *wadāʾiʿ al-nās* ("titipan-titipan manusia"): barang titipan hanya diserahkan kepada orang tepercaya, maka hanya di tangan merekalah titipan dapat hilang.

[^r-wafa]: **Kesetiaan** (*wafāʾ*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 238 (`m-wafa`, *al-Mufradāt*) dan no. 239 (`k-wafa`, *Kashshāf*).

[^p39]: CP: Edisi tahkik membaca *lafẓan ḥulwan* ("lafal yang manis"); kami membacanya *lafẓan khulwan* ("lafal kosong"), sejajar dengan "khayalan belaka" (*wahman mursalan*) dan dengan ucapan "nama yang tidak memiliki makna". Tentang dua kali persaudaraan: menurut para ahli sirah, yang pertama di antara kaum Muhajirin di Makkah sebelum hijrah, dan yang kedua antara Muhajirin dan Anshar di Madinah; demikian dicatat penerjemah Turki dengan merujuk Ibn Ḥajar, *Fatḥ al-Bārī*.

[^d17]: CD: Penafsiran ini sama dengan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Persahabatan", yang mengutip ucapan "nama yang tidak memiliki makna" dengan pengantar "karena langkanya sahabat". Di sana pula al-Rāghib merangkum kedua pihak dalam bab ini dalam satu kalimat: "Siapa yang menyangka dirinya mampu tidak membutuhkan sahabat, ia tertipu; dan siapa yang menyangka mudah menemukannya, ia dungu."

## Bab Kedelapan: Keutamaan Mengambil Sahabat {.judul-bab}

Mengambil saudara adalah tabiat manusia. Hal itu disaksikan oleh condongnya setiap orang kepada yang sesuai dengannya. Maka sahabat lebih baik bagi seseorang daripada dirinya sendiri. Seorang bijak berkata: "Saudara yang saleh lebih baik bagimu daripada dirimu sendiri, sebab jiwa itu selalu menyuruh kepada keburukan, sedang saudara yang saleh tidak menyuruhmu kecuali kepada kebaikan." Dikatakan: *"Orang mukmin adalah cermin saudaranya."*

Seorang bijak berkata: "Sungguh aku sangat heran terhadap orang yang mengajarkan kepada anak-anaknya kisah-kisah para raja dan peristiwa-peristiwa mereka, tetapi tidak terlintas dalam benak mereka perkara kasih sayang dan kebaikan-kebaikan umum yang dihasilkan oleh cinta dan keakraban." Tidak ada jalan bagi seseorang untuk hidup tanpa sahabat, meskipun dunia condong kepadanya dengan segala yang diingini. Maka beruntunglah orang yang diberi sahabat sedang ia tidak memegang kekuasaan, dan lebih besar lagi keberuntungan orang yang diberi sahabat ketika memegang kekuasaan. Sebab orang yang mengurus urusan rakyat perlu mengetahui keadaan mereka, dan tidak cukup baginya dua telinga, dua mata, dan satu kalbu. Bila ia menemukan saudara-saudara yang tepercaya, dengan mereka ia menemukan mata, telinga, dan kalbu, sehingga ia mengetahui yang gaib dalam rupa yang hadir; dan hal itu tidak ia dapati kecuali pada sahabat, kawan, dan orang yang menyayanginya.[^d18]

Aristoteles menulis kepada Iskandar: "Ketahuilah bahwa engkau menguasai tubuh-tubuh dengan kekuasaan; maka lampauilah itu menuju kalbu-kalbu dengan berbuat baik."

Ali bin Abdullah bin Abbas berkata kepada salah seorang khalifah: "Carilah cinta rakyat, sebab ketaatan karena cinta lebih utama daripada ketaatan karena segan."[^d19]

Seorang bijak ditanya: "Perbendaharaan manakah yang paling baik?" Ia menjawab: "Sahabat yang baik." Yang lain berkata: "Sungguh aku heran terhadap orang yang bersedih padahal ia memiliki sahabat yang utama." Dikatakan: "Tidak ada kebanggaan kecuali dengan sahabat yang utama. Sahabat lebih utama daripada saudara kandung, sebab saudara kandung adalah kerabat tubuh, sedang sahabat adalah kerabat roh."

Dikatakan kepada Ibnu al-Muqaffa': "Manakah yang lebih engkau cintai, sahabatmu atau kerabatmu?" Ia menjawab: "Aku mencintai kerabat hanya bila ia menjadi sahabat." Abu Nuwas berkata:

> Mustahil! Kekerabatan dan nasab takkan mendekatkan
> pada hari ketika akhlak dan perangai menjauhkan.
> Kasih sayang Salman menjadi pertalian darah baginya,
> sedang antara Nuh dan anaknya tiada pertalian darah.[^p40]

Seorang bijak berkata: "Manfaat sahabat yang saleh (bagi seseorang) lebih besar daripada manfaat dirinya bagi dirinya sendiri. Sebab jiwanya selalu menyuruh kepada keburukan dan hawa nafsunya menentang akalnya dalam hal-hal yang menyangkut dirinya; sedang saudara yang saleh menyuruhnya (kepada kebaikan), dan hawa nafsu tidak mencampuri akal saudara itu dalam pandangannya."[^p41]

Sebagian orang berkata: "Di antara keutamaan persahabatan ialah bahwa ia tidak membutuhkan keadilan, yang merupakan keutamaan yang paling kuat. Sebab keadilan dibutuhkan untuk menghindari kezaliman, sedang dua orang sahabat tidak saling menzalimi, bahkan masing-masing memberi yang lain lebih dari yang semestinya."[^r-adl][^d20] Maka benarlah ucapan Amr bin al-Ahtam, atau Ibnu al-Rumi:

> Sesungguhnya kegembiraan, bila engkau lukiskan
> sampai ke puncak hakikatnya,
> adalah kawan karib penuh kasih yang engkau akrabi,
> dan kembali kepada kecukupan.

[^d18]: CD: Kalimat terakhir sama dengan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Persahabatan": "Siapa yang menemukan saudara-saudara yang tepercaya, dengan mereka ia menemukan mata, telinga, dan kalbu yang semuanya untuknya, sehingga ia melihat yang gaib dalam rupa yang hadir." Terjemahan di atas mengikuti redaksi itu. Di *al-Dharīʿa* kalimat ini berlaku umum bagi setiap orang; di sini ia dikhususkan bagi orang yang memegang kekuasaan.

[^d19]: CD: Bandingkan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta": "Ketaatan karena cinta lebih utama daripada ketaatan karena takut, sebab ketaatan karena cinta datang dari dalam, sedang ketaatan karena takut datang dari luar dan lenyap bila sebabnya lenyap"; dan "rasa segan membuat orang menjauh, sedang cinta merekatkan". Tentang *hayba* (rasa segan), lihat nota kaki *al-Dharīʿa* no. 316 (`k-hayba`).

[^p40]: CP: Dalam edisi tahkik keempat larik ini tercetak dengan urutan yang tertukar, dan kata *afḍat* ("sampai kepada") dibaca *aqṣat* ("menjauhkan"), sesuai tuntutan makna. "Baginya" menunjuk Nabi: Salman al-Farisi, orang asing, menjadi seperti keluarga Nabi karena kasih sayangnya, sedang putra Nuh terputus dari ayahnya karena kekafirannya (Hud: 45-46).

[^p41]: CP: Kalimat ini rusak dalam edisi tahkik: *nafʿ al-ṣadīq al-ṣāliḥ akthar min nafʿihi li-dhātihi* dan *wa-hawāhu lā yashrabu ʿaqlahu*. Catatan pinggir naskah yang dikutip penyunting ("manfaat sahabat lebih besar daripada manfaatnya bagi dirinya sendiri, renungkanlah") membantu memahami kalimat pertama; kata *yashrabu* dibaca *yashūbu* ("mencampuri, mengeruhkan"). Maksudnya: seseorang tidak dapat menilai dirinya dengan jernih karena hawa nafsunya ikut campur, sedang sahabat menilainya tanpa campur tangan hawa nafsu itu. Gagasan ini diulang dari awal bab.

[^r-adl]: **Keadilan** (*ʿadl*, *ʿadāla*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 61 (`m-adl`, *al-Mufradāt*), dan terjemahan *Tafṣīl*, catatan no. 156 (`r-adl`).

[^d20]: CD: Gagasan yang sama menjadi pembuka *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta": "Seandainya manusia saling mencintai dan bermuamalah dengan cinta, niscaya mereka tidak membutuhkan keadilan. Dikatakan: Keadilan adalah pengganti cinta, yang dipakai di tempat cinta tidak ada." Di sana yang dikatakan tidak membutuhkan keadilan adalah cinta; di sini persahabatan. Gagasan ini berasal dari tradisi filsafat etika tentang persahabatan, yang menyatakan bahwa bila orang-orang bersahabat mereka tidak membutuhkan keadilan, sedang orang-orang yang adil masih membutuhkan persahabatan.

## Bab Kesembilan: Jumlah Sahabat yang Baik untuk Dimiliki {.judul-bab}

Orang berselisih pendapat tentang hal itu. Sebagian berkata: memperbanyak sahabat lebih utama, dengan membenarkan ucapan penyair:

> Perbanyaklah kawan sebanyak engkau mampu, sebab mereka
> tiang penopang dan sandaran bila engkau meminta tolong kepada mereka;
> seribu kawan karib dan sahabat bukanlah jumlah yang banyak,
> sedang seorang musuh sudah terlalu banyak.[^p42]

Sebagian yang lain berkata: menyedikitkan sahabat lebih utama.

Telah tetap bahwa sahabat itu langka dan bahwa bahaya dalam memperolehnya besar; maka bagaimana mungkin manusia menemukan sahabat yang banyak! Benarlah al-Haritsi dalam ucapannya:

> Bila engkau merata-ratakan keakrabanmu kepada semua orang,
> engkau takkan henti mendapat dan menemani sahabat yang buruk.

Ibnu al-Rumi berkata tentang lebih utamanya menyedikitkan sahabat:

> Musuhmu diperoleh dari sahabatmu,
> maka janganlah engkau memperbanyak kawan;
> sebab penyakit, kebanyakan yang engkau lihat,
> berasal dari makanan atau minuman.

Seandainya seseorang menemukan mereka pun, ia tidak akan mampu memelihara mereka semua. Sebab di antara syarat memelihara sahabat ialah bergembira dengan kegembiraannya dan berduka dengan dukanya. Bila sahabat banyak, keadaan-keadaan mereka yang saling bertentangan menumpuk padanya, sehingga ia perlu menyertai mereka dalam keadaan-keadaan itu: bergembira dengan kegembiraan yang satu dan berduka dengan duka yang lain, berusaha bersama usaha yang satu dan berdiam bersama diamnya yang lain, dan keadaan-keadaan serupa itu. Hal itu menghalanginya menunaikan hak-hak mereka dengan sempurna, sehingga ia pasti lalai dalam sebagian yang wajib bagi mereka; lagi pula banyaknya hak mereka menyibukkannya dari keperluan dan urusan pribadinya.[^p43] Karena itu al-Fudhail berkata: "Di antara tanda dangkalnya akal seseorang ialah banyaknya sahabatnya." Dikatakan pula: "Hendaklah kawan-kawan bagimu seperti api: sedikitnya memberi manfaat dan banyaknya membinasakan."

Adapun memberi pertolongan, menampakkan kasih sayang, dan membalas salam dengan salam, itu dianjurkan (terhadap semua orang). Ibnu al-Muqaffa' berkata: "Berikanlah kepada sahabatmu harta dan darahmu, kepada kenalanmu pertolongan dan pemberianmu, dan kepada orang banyak uluran tanganmu dan wajahmu yang ceria." Bagus sekali ucapan penyair:

> Wahai anakku, kebajikan itu perkara yang mudah:
> wajah yang cerah dan kata-kata yang lembut.

[^p42]: CP: Dalam edisi tahkik keempat larik ini tercetak dengan urutan yang tertukar; susunan di atas mengikuti rima dan makna. Penyunting mencatat bahwa Abū Ḥayyān dalam *al-Ṣadāqa wa-l-Ṣadīq* mengutip ucapan al-Ḥasan al-Baṣrī yang sejalan dengan larik terakhir: "Janganlah membeli kasih sayang seribu orang dengan permusuhan satu orang."

[^p43]: CP: Alasan ini sama dengan alasan yang dikemukakan dalam tradisi filsafat etika tentang persahabatan: tidak mungkin bersahabat sempurna dengan banyak orang, sebab sulit bergembira bersama banyak orang dan berduka bersama mereka sekaligus, karena bisa jadi seseorang harus bergembira bersama yang satu dan berduka bersama yang lain pada waktu yang sama. Terjemahan Turki membaca bait al-Haritsi di atas dengan *ʿammamta* ("engkau merata-ratakan"), sesuai sumber-sumber lain, sebagai ganti *ʿajamta* ("engkau menguji") dalam edisi tahkik.

## Bab Kesepuluh: Keadaan-Keadaan yang Harus Diperhatikan Seseorang dalam Memilih dan Mengambil Sahabat {.judul-bab}

Dari uraian terdahulu telah tetap adanya sahabat dan keutamaannya, tetapi ia sedikit. Bagaimana tidak sedikit, padahal induk keutamaan sedikit susunya, sedang induk kekurangan banyak beranak! Setiap maujud di alam, di antara kedua ujungnya, yang paling utama dan yang paling rendah, terdapat perbedaan; tetapi tidak ada perbedaan seperti perbedaan antara manusia dan manusia.[^p44]

> Mereka, meski saling berdekatan dalam keserupaan,
> sungguh berjauhan dalam keutamaan-keutamaan:
> besi mata tombak Rudaini dan besi tumitnya sama,
> tetapi jauh jarak antara yang di atas dan yang di bawah.[^p45]

Penyair berkata:

> Tak pernah kulihat yang serupa berbeda-beda seperti manusia
> dalam keutamaan, hingga seribu orang dihitung setara dengan seorang.

Kemudian, setiap maujud lebih mudah dipilih daripada manusia. Sebab manusia, karena ia khusus dapat mengenakan kemunafikan, pamer, dan riya, lalu tampil dalam rupa yang bukan rupanya dan berlagak dengan akhlak yang bukan akhlaknya, sulit dikenal.

Maka orang yang ingin memilih sahabat yang dapat ia andalkan dan menjadi sandarannya dalam kesenangan dan kesusahan wajib terlebih dahulu membedakan kasih sayang karena tamak dan kelezatan dari persahabatan yang murni, agar ia tidak terjatuh dalam kekeliruan, lalu menyangka lemak pada orang yang gemuknya adalah bengkak, sehingga ia memilih sebagai sahabat seorang musuh yang menebarkan bau busuk di tengah harumnya kesturi persahabatan.[^d21] Kebanyakan manusia adalah saudara karena tamak dan musuh karena nikmat. Setiap kasih sayang yang diikat oleh tamak akan dilepaskan oleh putus asa, dan siapa yang mengasihimu karena suatu perkara akan berpaling ketika perkara itu habis.[^p46]

Hendaklah ia tidak memilih sahabat karena elok rupanya:

> Keelokan pada wajah seorang pemuda bukanlah kemuliaan baginya,
> bila tidak ada pada perbuatan dan akhlaknya.

Tidak pula karena kekuatan tubuhnya:

> Kesabaran itu, keutamaannya dikenal dengan roh:
> itulah kesabaran para raja, bukan dengan tubuh.

Tidak pula karena kemuliaan keturunan yang diwarisinya tanpa kemuliaan baru dari dirinya sendiri:

> Kemuliaan keturunan yang diwarisi, semoga tak lagi berguna,
> tidaklah terhitung kecuali disertai kemuliaan lain yang diusahakan;
> bila sebatang dahan tidak berbuah, meski ia cabang
> dari pohon-pohon yang berbuah, orang menghitungnya kayu bakar.[^r-hasab]

Tidak pula karena kekayaannya, sebab harta itu datang dan pergi; terkadang seseorang pada suatu hari menjadi miskin, padahal ia tetap terpuji.

Tetapi hendaklah ia memilihnya karena hikmahnya, kesucian dirinya, keberaniannya, dan keadilannya, yang merupakan keutamaan-keutamaan jiwa manusia;[^r-hikma][^d22] agar duduk bersamanya menjadi keberuntungan, cintanya selamat, dan persaudaraannya mulia; bila engkau menemaninya ia menghiasimu, bila engkau meminta tolong kepadanya ia menolongmu, dan bila engkau membutuhkannya ia membantumu.[^p47]

Maka yang pertama wajib atasnya dalam memilih sahabat ialah:

**Pertama**: menjauhi orang bodoh dalam persahabatan.[^r-jahl]

**Kedua**: memperhatikan bagaimana keadaannya ketika marah dan bagaimana muamalahnya ketika murka. Dikatakan: "Bila engkau ingin bersaudara dengan seseorang, buatlah ia marah terlebih dahulu; jika ia bersikap adil kepadamu dalam kemarahannya, (bersaudaralah dengannya); jika tidak, waspadalah terhadapnya."[^r-ghadab]

**Ketiga**: jauhilah setiap orang yang suka berbantah dan bertengkar. Tepat sekali ucapan penyair:

> Jauhilah, jauhilah berbantah-bantahan, karena ia
> penyeru kepada keburukan dan penarik keburukan.

Ketahuilah bahwa orang yang menemani seorang sahabat akan dinisbatkan kepada orang yang ditemaninya.[^p48]

Inilah himpunan sifat yang, bila engkau dapati pada seseorang, bersungguh-sungguhlah untuk menangkapnya, dan ketahuilah bahwa dialah sahabat yang diangankan orang-orang utama; dan bila engkau dapati sebagian besarnya, tangkaplah ia dan berpeganglah pada persaudaraannya.

[^p44]: CP: Edisi tahkik membaca *wa-lā tafāwut bayna insān wa-insān* ("dan tidak ada perbedaan antara manusia dan manusia"). Penyunting memahaminya secara harfiah, lalu mengkritik al-Rāghib dengan mengutip ayat tentang derajat orang berilmu dan orang bertakwa; terjemahan Turki juga memahaminya "tidak ada perbedaan (secara esensial)". Pemahaman ini bertentangan dengan dua syair dan hadis yang dikutip sesudahnya, yang semuanya menegaskan besarnya perbedaan antarmanusia ("seribu orang dihitung setara dengan seorang"; "manusia itu seperti seratus unta, hampir tidak engkau dapati di antaranya seekor tunggangan"). Maka kalimat itu harus dipahami, atau dibetulkan, sebagai *wa-lā tafāwut ka-l-tafāwut bayna insān wa-insān*: tidak ada perbedaan di antara maujud lain yang sebesar perbedaan antarmanusia. Kritik penyunting karena itu tidak tepat. Ungkapan "induk keutamaan sedikit susunya" (*jadūd*: kambing yang susunya kering) menyatakan bahwa yang baik jarang lahir. Penyunting juga menyebut sabda Nabi: *"Manusia itu seperti seratus ekor unta, hampir tidak engkau dapati di antaranya seekor tunggangan,"* yang dalam edisi tahkik tercetak di catatan kaki.

[^p45]: CP: Keempat larik ini tercetak dengan urutan yang tertukar dan kata-kata yang rusak dalam edisi tahkik. Kami membaca kata pertama sebagai *wa-hum* ("mereka"), dan *al-rāghibī* sebagai *al-rudaynī*, nama tombak Rudaini yang terkenal dalam syair Arab. Maksudnya: mata tombak dan tumit tombak dibuat dari besi yang sama, tetapi yang satu di atas untuk menikam dan yang lain di bawah untuk ditancapkan ke tanah. Penyunting mencatat bahwa al-Rāghib juga mengutip kedua bait ini dalam *Majmaʿ al-Balāgha* di bawah judul "Keunggulan orang yang tinggi atas orang yang rendah". Terjemahan Turki memahaminya sebagai pedang.

[^d21]: CD: Perumpamaan yang sama dipakai dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan Persahabatan": "Memilih orang yang dapat engkau andalkan untuk dijadikan sahabat adalah perkara sulit, sebab orang yang kurang terkadang berpihak kepadamu sehingga engkau menyangkanya orang utama, lalu engkau menjadi seperti orang yang menyangka lemak pada orang yang gemuknya adalah bengkak." Terjemahan di atas mengikuti redaksi itu. Perumpamaan ini berasal dari bait al-Mutanabbi: "Kulindungkan pandangan-pandanganmu yang jujur dari menyangka lemak pada orang yang gemuknya adalah bengkak."

[^p46]: CP: Edisi tahkik membaca *yaḥulluhā al-baʾs* ("dilepaskan oleh kesusahan"); kami membacanya *al-yaʾs* ("putus asa"), yakni putus asa dari tercapainya apa yang diinginkan, sebagai lawan dari tamak. Dalam kalimat sebelumnya, *arāḥa* berarti "berbau busuk".

[^r-hasab]: **Kemuliaan keturunan** (*ḥasab*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 106 (`k-hasab`, *Kashshāf*).

[^r-hikma]: **Hikmah, kesucian diri, keberanian** (*ḥikma*, *ʿiffa*, *shajāʿa*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 38 (`m-hikma`) dan no. 39 (`k-hikma`), no. 56 (`m-iffa`) dan no. 57 (`k-iffa`), no. 58 (`k-shajaa`); tentang keadilan, no. 61 (`m-adl`).

[^d22]: CD: Keempat keutamaan ini adalah empat keutamaan pokok dalam *al-Dharīʿa*, Pasal Pertama, yang di sana dirumuskan sebagai hikmah (dari daya pikir), kesucian diri (dari daya syahwat), keberanian (dari daya amarah), dan keadilan (dari keselarasan ketiganya). Di sini ia dijadikan ukuran memilih sahabat, sebagai lawan dari empat ukuran lahir yang ditolak: keelokan rupa, kekuatan tubuh, keturunan, dan kekayaan. Dalam Bab Pertama keempatnya disebut "daya-daya keutamaan yang dikhususkan bagi manusia", dengan "akal" di tempat "hikmah".

[^p47]: CP: Edisi tahkik membaca *idhā ṣaḥibtahu zāraka* ("bila engkau menemaninya ia mengunjungimu"); kami membacanya *zānaka* ("ia menghiasimu"), ungkapan yang lazim dalam sifat sahabat yang baik. Kata *ʿānaka* dipahami sebagai "membantumu". Terjemahan Turki mengikuti bacaan tahkik.

[^r-jahl]: **Kebodohan** (*jahl*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 186 (`m-jahl`) dan no. 187 (`k-jahl`).

[^r-ghadab]: **Amarah** (*ghaḍab*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 295 (`m-ghadab`) dan no. 296 (`k-ghadab`).

[^p48]: CP: Kalimat ini tidak utuh dalam edisi tahkik (*wa-iʿlam anna man yuṣāḥibu ṣāḥiban ilā mustaṣḥabihi*); penyunting memahaminya "hendaklah ia memelihara persahabatannya", dan terjemahan Turki mengikutinya. Kami menduga ada kata kerja yang hilang, seperti *yunsabu* ("dinisbatkan"), sehingga maknanya sejalan dengan bait yang dikutip dalam *al-Dharīʿa*, Pasal Kelima, "Anjuran Bergaul dengan Orang-Orang Baik": "Tentang seseorang jangan bertanya, tetapi tanyalah tentang temannya, sebab setiap teman meneladani yang disertainya." Bacaan ini dugaan.

## Bab Kesebelas: Keadaan-Keadaan yang Wajib Diberikan Seseorang kepada Sahabatnya dan Tidak Ia Tuntut darinya {.judul-bab}

Bila engkau ingin menangkap seorang sahabat, atau telah menangkapnya lalu ingin agar ia tidak lepas dari jeratmu, hendaklah engkau berhias dengan akhlak yang telah disebutkan, dan berakhlak dengan akhlak yang tidak engkau tuntut dari saudaramu, tetapi engkau berikan kepadanya.[^p49]

Menjadi kewajibanmu untuk bersikap mudah perangai dan baik dalam bersaudara dengan sahabatmu, bahkan dengan semua orang; menyambutnya di saat lapang dengan wajah yang cerah dan akhlak yang lapang; menjabat tangannya bila engkau melihatnya, dan bercanda dengannya dengan canda yang pantas bagi kalian berdua, karena hal itu membangkitkan kasih sayang.[^d23]

Hendaklah engkau memperlakukan semua orang yang berhubungan dengannya, dari budak sampai pelayan, dengan cara yang sama, sehingga hal itu tampak pada pandanganmu, gerak-gerikmu, keramahan, dan keceriaanmu, dan dengan itu ia makin percaya akan kasih sayangmu. Seorang bijak ditanya: "Dengan apa keadaanmu meninggi di atas kawan-kawan sebayamu?" Ia menjawab: "Dengan menyambut orang yang kutemani dengan kata yang baik dan makna yang halus."

Hendaklah engkau mengikutsertakannya dalam kelapanganmu dan, sedapat mungkin, tidak membutuhkannya dalam kesempitanmu; engkau meneguk yang pahit dan memberi minum saudara-saudaramu yang manis; dan engkau menjadi seperti orang yang dikatakan tentangnya:[^p50]

> Abu Malik menyimpan kefakirannya
> untuk dirinya sendiri, dan menebarkan kekayaannya.

Janganlah terlintas dalam benakmu untuk mengungkit-ungkit kebaikan yang engkau berikan kepadanya, apalagi mengucapkannya dengan lisanmu; sebab mengungkit-ungkit, meskipun kecil, meruntuhkan kebaikan, meskipun besar.[^d24]

Waspadalah jangan sampai engkau lupa memperhatikan persaudaraan karena kedudukan yang engkau peroleh dari penguasa. Perhatikanlah betapa dipandang baik makna ucapan penyair:

> Seorang pemuda yang oleh kekuasaan justru ditambahi keinginan akan pujian,
> ketika kekuasaan mengubah setiap kawan karib.

Dan betapa dipandang buruk keadaan orang yang menempuh jalan seperti ini:

> Kulihat engkau, ketika mendapat harta, sedang kami digigit
> zaman yang pada tajam taringnya engkau lihat kelaparan,
> mencari-cari kesalahan kami untuk menahan pemberian;
> tahanlah hartamu, tetapi jangan jadikan kekayaanmu sebagai dosa kami.

Janganlah engkau bersikap asing terhadap mereka, sehingga engkau menjadi seperti orang yang dikatakan Salih bin Abdul Quddus:

> Ia menyombong kepada kawan-kawannya karena kekayaan,
> hingga ia tak lagi mengedipkan mata karena kesombongannya.
> Semoga Allah mengembalikannya kepada keadaannya semula,
> sebab dalam kefakirannya ia lebih baik.

Bila engkau melihat saudaramu telah memperoleh suatu kedudukan, janganlah engkau menuntutnya tetap pada keadaannya semula terhadapmu, sebagaimana engkau mewajibkan hal itu atas dirimu; tetapi bayangkanlah bahwa sikap manja merusak kehormatan. Amalkanlah ucapan Ziyad: "Bila engkau punya sahabat lalu ia menjadi pejabat atau memperoleh ketinggian, dan masih tersisa untukmu sepersepuluh dari pergaulannya, maka ia bukan sahabat yang buruk."

Kewajibanmu, bila engkau melihatnya masih memperhatikanmu seperti kemarin, ialah tidak meninggalkan penghormatan kepadanya, meneladani orang yang berkata: "Bila penguasa menjadikanmu ayah, jadikanlah ia tuanmu." Bila engkau sendiri yang menjadi penguasa, jauhilah memperlakukannya sebagai pelayan dalam hal yang memberatkannya; sebab bukanlah termasuk kasih sayang bahwa seseorang memperlakukan saudaranya sebagai pelayan. Hisyam berkata: "Kami tidak menjadikan saudara-saudara sebagai budak."

Hendaklah engkau tidak meninggalkan memakmurkan kasih sayang dengan berkunjung. Dikatakan: "Tiga hal menambah keakraban dan kepercayaan: berkunjung ke tempat tinggal, bersesuaian, dan bercakap-cakap."[^p51] Hal itu tentu setelah memperhatikan sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Berkunjunglah sesekali, niscaya cinta bertambah."* Ketahuilah bahwa siapa yang takut dirinya menjadi beban tidak akan menjadi beban, dan siapa yang merasa aman dari menjadi beban, dialah yang menjadi beban.

Janganlah engkau bersikap asing kepadanya karena ia tidak mengunjungimu ketika ia tidak membutuhkanmu. Dikatakan: "Hakikat cinta ialah bahwa kebaikan tidak menambahnya dan sikap dingin tidak menguranginya." Kasih sayang yang diubah oleh sedikitnya pertemuan sungguh kasih sayang yang rusak.[^p52]

Bila engkau telah mengetahui ketulusan kasih sayangnya, ajaklah ia meninggalkan rasa sungkan dalam hal-hal yang memungkinkan keakraban tanpa canggung. Dikatakan: "Kasih sayang itu terhijab selama rasa sungkan menguasainya; bila niat telah benar dan kepercayaan telah kokoh, gugurlah beban berjaga-jaga." Tetapi janganlah berlebihan dalam bersikap lepas selama engkau belum mengenal lekuk dan tonjolannya. Dikatakan: "Jadikanlah keakrabanmu hal terakhir yang engkau berikan dari kasih sayangmu." Yunus bin Ubaid berkata: "Bila kami telah yakin akan kasih sayang saudara kami, tidak merugikannya bila ia tidak mendatangi kami."

Hendaklah engkau segera menolongnya pada saat ia membutuhkan. Dikatakan: "Peliharalah sahabat, walaupun di atas kebakaran." Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bersabda: *"Tolonglah saudaramu, baik ia berbuat zalim maupun dizalimi."*

Janganlah engkau mencelanya bila ia enggan menolongmu dalam kebatilan yang engkau inginkan dan menahan diri dari kezaliman yang engkau bebankan kepadanya. Sebab tidak ada kekekalan bagi kemunafikan, dan tidak ada kesetiaan bagi orang yang berpura-pura berakhlak dan mengada-ada. Siapa yang melampaui kebenaran demi menyenangkanmu ketika ia rida, hampir pasti ia akan melampauinya untuk menyakitimu ketika ia murka; dan siapa yang mengutamakanmu atas Tuhannya, tidak aman bahwa ia akan mengutamakan sebagian hamba-Nya atasmu. Bagus sekali orang yang berkata dalam doanya: "Ya Allah, aku berlindung kepada-Mu dari orang yang tidak mencari kasih sayangku yang tulus kecuali dengan mengikuti syahwatku."[^p53]

Bila engkau melihatnya menyimpang dalam hal yang tidak merugikan agama, tidak meruntuhkan muruah, dan tidak mendatangkan duka bagimu dan baginya, lalu ia meminta bantuanmu, hendaklah engkau membantunya, sambil melantunkan:

> Bukankah aku hanyalah dari Ghaziyyah: bila ia sesat,
> aku pun sesat; dan bila Ghaziyyah mendapat petunjuk, aku pun mendapat petunjuk.

dan meneladani orang yang berkata:

> Aku bagaikan cermin: kutemui
> setiap wajah dengan bayangannya sendiri.

Hal itu hanya baik dalam hal yang tidak membawa kepada kemunafikan dan riya.

Bila engkau melihat suatu aib padanya, janganlah engkau memejamkan mata terhadapnya, sebab orang mukmin adalah cermin saudaranya; tetapi hendaklah engkau memberitahukannya kepadanya dengan cara yang lembut. Dokter yang lembut terkadang dengan kelembutan dan keramahan mencapai apa yang tidak dicapai dokter yang kasar dengan susah payah dan pemotongan, atau dengan makanan mencapai apa yang tidak dicapai yang lain dengan obat. Hendaklah peringatanmu kepadanya di tempat sepi, bukan di hadapan orang banyak. Dikatakan: "Siapa yang menasihati saudaranya di tempat sepi, sungguh ia telah menghiasinya; dan siapa yang menasihatinya di hadapan orang banyak, sungguh ia telah mencemarkannya."[^p54][^d25]

Janganlah engkau meninggalkan memuji perbuatan-perbuatannya yang baik, dengan menyengaja kejujuran dan menjauhi sanjungan palsu dan kemunafikan, sebab kemunafikan tidak membawa keberuntungan:

> Dalam kalbu ada petunjuk tentang kalbu
> ketika ia menjumpainya,
> dan dalam mata ada ukuran-ukuran dan keserupaan
> tentang mata.

Amirul Mukminin berkata kepada orang yang memujinya, sedang ia mengetahui sanjungan palsu itu: "Aku di bawah apa yang engkau katakan, dan di atas apa yang ada dalam hatimu." Janganlah pujian itu melampaui keadaannya; dikatakan: "Memuji seseorang dengan apa yang tidak ada padanya adalah buruk." Usahakanlah agar pujianmu kepadanya diucapkan di belakangnya, sebab itu lebih baik.[^d26]

Waspadalah jangan sampai ada orang yang leluasa menggunjing sahabatmu di hadapanmu, sebab engkau adalah matanya dan penggantinya di tengah manusia, bahkan engkau adalah dirinya. Bila hal itu sampai kepadanya, ia tidak ragu bahwa itu terjadi atas pendapat dan keinginanmu, sehingga engkau menjadi musuhnya.

Waspadalah terhadap orang yang menyampaikan kepadamu perkataan yang dihiasi dan dusta yang dipoles, hingga bila setan telah menguasaimu, ia beralih dari sindiran kepada terang-terangan. Sebab orang yang mengadu domba di antara manusia tidak dapat dipercaya kalajengking-kalajengking dan ular-ularnya terhadap sahabat. Seorang bijak berkata: "Para pengadu domba, bila merasakan bahwa kasih sayang telah bertaut di antara saudara-saudara, mereka mengerahkan tipu daya lalu meruntuhkannya dari fondasinya." Bayangkanlah apa yang disebutkan dalam kitab *Kalīla wa Dimna* tentang serigala dan pembinasaannya terhadap binatang-binatang buas yang besar.[^p55][^d27]

Janganlah engkau mencelanya atas setiap kesalahan. Renungkanlah ucapan Basysyar tentang itu:

> Bila dalam segala perkara engkau mencela
> sahabatmu, takkan kau temui orang yang tak kau cela;
> maka hiduplah seorang diri, atau sambunglah saudaramu, sebab ia
> sesekali melakukan dosa dan sesekali menjauhinya.

Tetapi janganlah engkau meninggalkan mencelanya dalam hal yang, bila engkau mencelanya, ia dapat menyimpulkan keinginanmu akan kasih sayangnya dan jernihnya batinmu dalam ketulusan kepadanya. Benarlah orang yang berkata:

> Meninggalkan celaan, bila seorang saudara
> layak mendapat celaan darimu, adalah jalan menuju perpisahan.

Ia juga berkata:

> Ketahuilah, yang dibenci hanyalah orang yang tidak dicela.

Seorang bijak berkata: "Celaan itu ada dua: celaan yang menghidupkan kasih sayang, yaitu yang berkenaan dengan kasih sayang itu sendiri; dan celaan yang mematikannya, yaitu celaan atas satu dosa yang terjadi hanya sekali."

Hendaklah engkau menjauhi berbantah-bantahan dengan sahabat, sebab hal itu memutus kasih sayang dari akarnya: berbantah-bantahan adalah sebab perselisihan, dan perselisihan adalah sebab perpisahan. Seorang Badui ditanya: "Apa pendapatmu tentang berbantah-bantahan?" Ia menjawab: "Apa yang dapat kukatakan tentang sesuatu yang merusak persahabatan yang lurus dan melepaskan ikatan yang kokoh? Yang pertama ada padanya ialah bahwa ia menjadi jalan menuju saling mengalahkan, dan saling mengalahkan adalah sebab fitnah yang paling kuat." Dikatakan: "Luaslah rumah orang yang bersikap lunak, dan sempitlah jalan orang yang suka berbantah."

Jauhilah jangan sampai terlintas dalam benakmu untuk merendahkan seorang sahabat di majelis yang ramai, dengan menampakkan bahwa engkau hendak berdiskusi dengannya; sebab itu sumber permusuhan dan penghimpun lenyapnya keakraban. Waspadalah jangan sampai engkau kikir kepada sahabatmu dengan ilmu yang ia inginkan, atau sampai kepadanya kabar bahwa engkau ingin memilikinya sendiri tanpa dia dan mengutamakan dirimu dengan sesuatu darinya atas dia.

Hendaklah engkau menanggung darinya apa yang tidak lepas dari manusia, berupa sikap dingin atau gangguan kecil. Dikatakan: "Tanggunglah dari saudaramu tiga kezaliman: kezaliman amarah, kezaliman sikap manja, dan kezaliman sikap dingin." Nisbatkanlah apa yang tampak darinya, sedapat mungkin, kadang kepada lemahnya tabiat manusia dan kadang kepada kelalaian dan kurangnya pengendalian diri; sebab dua orang yang saling mencinta, bila tidak saling memaafkan banyak hal yang tidak disukai, tidak lama lagi akan saling membenci.[^p56] Dikatakan: "Janganlah menghukum saudaramu karena dosa yang engkau sendiri pernah menghadap Tuhanmu dengannya," dan janganlah menyangka bahwa engkau akan menemukan orang yang tidak memiliki aib:

> Siapakah orang yang seluruh perangainya diridai?
> Cukuplah seseorang dipandang mulia bila aib-aibnya dapat dihitung.

Buzurjmihr ditanya: "Adakah sahabat yang tanpa aib?" Ia menjawab: "Orang yang tanpa aib semestinya tidak mati." Dikatakan: "Bagaimana engkau menuntut satu macam akhlak dari saudaramu, padahal ia terdiri dari empat tabiat?"[^p57]

Hendaklah engkau berbaik sangka kepada sahabatmu dalam setiap keadaan, dengan mengambil pelajaran dari ucapan Ibnu al-Muqaffa': "Orang berakal wajib mendustakan sangkaan yang paling buruk dengan sangkaan yang paling baik, agar ia memiliki kasih sayang yang tulus dan kalbu yang tenang." Hendaklah pula ia bersungguh-sungguh menjauhi segala yang membuat sahabatnya murka, dengan mengambil pelajaran dari ucapan penyair:

> Kalian memancing murkaku, dan penyelidikan kalian mengubah
> perangai jiwa yang batinnya penuh ketulusan;
> perlakuan kasar tak lama akan membuat jiwa mulia
> yang lembut wataknya menjadi keras dan pahit;
> jiwa itu tak lain setetes air dalam cekungan:
> bila tak dikeruhkan, jernihlah kolamnya.[^p58]

Janganlah engkau meninggalkan memakmurkan kasih sayang dengan segala cara yang mungkin. Sebab setiap yang dimiliki, apalagi persaudaraan, seperti tunggangan, pakaian, dan rumah, bila diabaikan pemeliharaannya akan rusak; dan tidaklah mudarat rusaknya sesuatu dari itu seperti mudarat rusaknya persaudaraan, sebab saudara bisa berbalik menjadi musuh dan manfaatnya berbalik menjadi mudarat. Karena itu dikatakan:

> Waspadalah terhadap musuhmu sekali,
> dan waspadalah terhadap sahabatmu seribu kali;
> sebab terkadang sahabat berbalik,
> maka ia lebih tahu jalan mencelakakan.

Orang berakal tidak semestinya merasa aman dari hal itu:

> Sesungguhnya orang yang telah menguji zaman lalu tidak takut
> akan berbolak-baliknya siang dan malam, sungguh bukan orang yang berakal.
> Maka jangan sekali-kali berputus asa dari kasih sayang musuh yang memendam dendam,
> dan jangan sekali-kali merasa aman dari putusnya hubungan kekasih.[^p59]

Ketahuilah bahwa dalam memutus hubungan dengan sahabat ada dua hal yang tidak menguntungkan orang yang memilih salah satunya: engkau dinisbatkan kepada buruknya pilihan pada awal kasih sayang, atau kepada kebosanan. Memutusnya hanya dibenarkan bagimu bila engkau melihatnya memiliki sebagian besar akhlak rendah yang telah disebutkan dan engkau tidak mendapati jalan untuk memperbaikinya; atau engkau melihatnya enggan kepadamu padahal engkau menghadap dan condong kepadanya, dan engkau telah memastikan hal itu darinya (dahulu telah dikatakan tentang orang yang memberikan hasrat kepada orang yang memberinya keengganan: "Aku tidak tahu mana di antara keduanya yang lebih tercela"); atau engkau melihatnya berbuat kejahatan kepadamu yang tidak sanggup ditanggung oleh kesabaran.[^p60] Sebab kejahatan itu ada dua macam: kejahatan yang menghalangimu dari tujuan terjauh dan kebahagiaan terbesar, yaitu perkara-perkara yang abadi, dan itulah yang diperhitungkan; dan kejahatan yang menghalangimu dari suatu tujuan duniawi, yang ditanggung oleh orang-orang yang berjiwa mulia.

Dalam meninggalkannya, amalkanlah ucapan al-Aqra' bin Habis:

> Aku berpaling seperti berpalingnya orang yang tetap bersikap baik
> ketika pemilik kasih sayang berubah dari keadaannya;
> dan sungguh dalam setiap keadaan aku terhadapnya,
> baik ketika urusan berpaling maupun ketika menghadap,
> tetap memelihara yang terbaik di antara kita,
> demi menjaga dan memuliakan persaudaraan.

[^p49]: CP: Penyunting memberi nomor urut 1 sampai 36 pada butir-butir bab ini dan menyatakan bahwa nomor-nomor itu tidak ada dalam naskah. Terjemahan ini tidak memakai nomor tersebut dan menyajikan butir-butir itu sebagai paragraf, sesuai dengan susunan asli.

[^d23]: CD: Bandingkan *al-Dharīʿa*, Pasal Kelima, "Anjuran Bergaul dengan Orang-Orang Baik dan Menjauhi Orang-Orang Jahat": manusia dalam pergaulan hendaknya menguatkan diri "dari sisi daya pikir dengan tutur kata yang menyenangkan, dari sisi daya amarah dengan bersikap santun, dan dari sisi daya syahwat dengan kemurahan", sehingga ia menjadi *ẓarīf*, dan *ẓarf* ialah "terhimpunnya alat-alat pergaulan, yaitu wajah yang cerah, daya tanggung, dan sikap yang lembut". Tentang canda yang pantas, lihat *al-Dharīʿa*, Pasal Kedua, "Senda Gurau dan Tawa": senda gurau terpuji bila dilakukan secara sederhana, tetapi batas sederhananya sulit ditentukan.

[^p50]: CP: Edisi tahkik membaca *an tushrikahu fī bishrika* ("dalam keceriaanmu"); kami membacanya *fī yusrika* ("dalam kelapanganmu"), sebagai pasangan *fī ʿusrika* ("dalam kesempitanmu"). Dalam bait sesudahnya, *ʿanāhu* dibaca *ghināhu* ("kekayaannya"), pasangan *faqrahu* ("kefakirannya"). Penyunting menyebut bait ini milik al-Mutanakhkhil al-Hudhalī.

[^d24]: CD: Dalam *al-Dharīʿa*, Pasal Keenam, "Macam-Macam Kemurahan dan Apa yang Dimurahkan", salah satu syarat kemurahan ialah memberi "tanpa mengungkit dan tanpa menyakiti".

[^p51]: CP: Edisi tahkik membaca *al-ziyāra fī al-rijāl* ("berkunjung di antara laki-laki"), dan penyunting menjelaskannya "bukan di antara laki-laki dan perempuan". Kami membacanya *fī al-riḥāl* ("ke tempat-tempat tinggal"), yang sesuai dengan ungkapan Arab.

[^p52]: CP: Edisi tahkik membaca *wa-in lam yatanakkar lahu bi-tark ziyāratika*, yang tidak utuh; terjemahan Turki memahaminya sebagai larangan ("jangan marah kepada sahabatmu karena ia tidak mengunjungimu"). Kami membacanya *wa-an lā tatanakkara lahu bi-tarkihi ziyārataka*. Dalam kalimat sebelumnya, *man khāfa an yuthqila lam yuthqil* dibaca menurut maksudnya ("siapa yang takut menjadi beban tidak akan menjadi beban"), sebab teks tahkik (*yunqal*) tidak bermakna.

[^p53]: CP: Beberapa kata dalam paragraf ini dibaca ulang: *fī bāṭil tarūmuhu* ("kebatilan yang engkau inginkan"; teks: *tarwīhi*), *wa-yakuffa ʿan jawr tasūmuhu* ("dan menahan diri dari kezaliman yang engkau bebankan"; teks: *wa-yakfīka*), dan *fī masarratika* ("demi menyenangkanmu"; teks: *fī sīratika*), sebagai pasangan *fī masāʾatika* ("untuk menyakitimu"). Doa di akhir paragraf dipahami: orang yang mengambil hati kita dengan menuruti syahwat kita bukanlah pencinta yang tulus. Terjemahan Turki memahami keseluruhan paragraf dengan cara yang sama.

[^p54]: CP: Edisi tahkik membaca *fī al-ḥalā* dan menjelaskannya sebagai *al-khalāʾ* ("tempat sepi"); kami mengikuti penjelasan itu. Ungkapan *an tuqifahu ʿalayhi waqfan laṭīfan* ("memberitahukannya kepadanya dengan lembut") dibaca dari *an tafqahu ʿalayhi* dalam teks. Kata *al-ʿanāʾ* ("susah payah") mengikuti pembetulan penyunting (teks: *al-baqāʾ*).

[^d25]: CD: Bandingkan *al-Dharīʿa*, Pasal Ketiga, "Ketulusan Menasihati": ketulusan menasihati ialah "memurnikan cinta kepada orang lain dalam menampakkan apa yang menjadi kemaslahatannya", dan ia wajib terhadap semua manusia. Di sana pula al-Rāghib mengingatkan bahwa banyaknya nasihat mewariskan kecurigaan, sejalan dengan anjuran di sini untuk menasihati dengan lembut dan di tempat sepi.

[^d26]: CD: *Al-Dharīʿa*, Pasal Kedua, "Sebutan Baik berupa Pujian dan Sanjungan", membahas sisi yang lain: orang yang dipuji. Di sana dikutip sabda Nabi kepada orang yang memuji orang lain di hadapannya ("Engkau telah mematahkan punggungnya") dan anjuran bagi orang yang dipuji untuk berdoa, "Ya Allah, jadikanlah aku lebih baik dari apa yang mereka sangka"; dan dikatakan bahwa orang utama tidak suka disanjung di hadapannya, terutama oleh pemuji yang berlebihan. Anjuran di sini untuk memuji sahabat di belakangnya sejalan dengan itu.

[^p55]: CP: Yang dimaksud adalah kisah dalam *Kalīla wa Dimna*, bab "Singa dan Sapi": Dimna, seekor serigala (dalam versi lain anjing hutan), iri melihat persahabatan singa dengan sapi Syatrabah, lalu mengadu domba keduanya sampai singa membunuh sapi itu dan kemudian menyesal. Penerjemah Turki meringkas kisah ini dalam catatannya. Kalimat "mereka meruntuhkannya dari fondasinya" mengikuti pembetulan penyunting (teks: *munqaḍūn niṣfahā*).

[^d27]: CD: Tentang adu domba (*namīma*), lihat *al-Dharīʿa*, Pasal Kedua, "Gunjingan dan Adu Domba": adu domba ialah "membocorkan ucapan seseorang kepada orang lain dengan maksud merusak hubungan keduanya", dan "jarang sekali engkau dapati seorang pencela kecuali ia sendiri tercela". Di sini al-Rāghib menerapkannya secara khusus pada persahabatan.

[^p56]: CP: Penerjemah Turki mencatat bahwa edisi tahkik membaca *mā yabdū minka* ("apa yang tampak darimu"), padahal konteks menuntut *minhu* ("darinya"), dan bahwa catatan penyunting pada tempat ini keliru mengulang catatan sebelumnya. Kami mengikuti pembetulan itu. Kata *yujawwizā* dipahami sebagai *yatajāwazā* ("saling memaafkan").

[^p57]: CP: "Empat tabiat" ialah empat campuran (panas, dingin, basah, kering) yang menurut kedokteran dan filsafat alam klasik menyusun tubuh manusia; karena tersusun dari unsur-unsur yang berlawanan, keadaan dan akhlak manusia pun tidak mungkin seragam. Penyunting menduga yang dimaksud adalah daya-daya jiwa (akal, amarah, syahwat); dugaan itu kurang tepat, sebab daya-daya itu tiga. Bait sebelumnya milik Basysyar bin Burd.

[^p58]: CP: Kata pertama bait ini tercetak *tajannabtum* ("kalian menghindari"); kami membacanya *tajannaytum* ("kalian memancing, mencari-cari"), yang sesuai dengan kelanjutannya. Penyunting tidak menemukan penyairnya.

[^p59]: CP: Keempat larik ini tercetak dengan urutan yang tertukar dalam edisi tahkik. Larik kedua dibaca *la-ghayru labībi* ("sungguh bukan orang yang berakal"), dan kata *ṣadm* ("hantaman") di akhir dibaca *ṣarm* ("putusnya hubungan"), yang sesuai dengan tema bab ini.

[^p60]: CP: Kalimat dalam kurung sangat rusak dalam edisi tahkik (*fa-qad qīla qadīman li-man aʿṭā al-raghba man aʿṭāhu al-zahāda, wa-mā adrī ayyuhumā al-umm*); terjemahan di atas mengikuti pemahaman yang paling dekat dengan konteks, yaitu kecaman terhadap orang yang terus mendekati orang yang menolaknya. Terjemahan Turki memahaminya secara berbeda.

## Bab Kedua Belas: Hidup Bersama dan Bergaul dengan Seluruh Lapisan Manusia {.judul-bab}

Tidaklah pantas bagi orang berakal membatasi pemakaian akhlak-akhlak yang telah disebutkan itu hanya kepada sahabat-sahabatnya, sebagaimana tidak baik baginya membatasi jamuan dan kebaikannya hanya kepada kerabat dan penduduk negerinya.[^p61] Sebab bila ia membatasi hal itu kepada kerabat tanpa orang asing, jarak antara dia dan anjing sudah dekat, sebab anjing pun mencurahkan (kesetiaannya) kepada orang-orang yang dikenalnya. Yang semestinya bagi orang berakal ialah meneladani apa yang diriwayatkan dari Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Sesungguhnya kalian tidak akan dapat melapangkan manusia dengan harta kalian, maka lapangkanlah mereka dengan akhlak kalian,"* dan sabdanya: *"Maukah aku tunjukkan kepada kalian sesuatu yang terpuji tanpa kerugian? Akhlak yang lapang dan menahan diri dari yang buruk."*[^p62]

Hendaklah engkau menemui mereka dengan wajah yang cerah, sebab dikatakan: "Keceriaan adalah inti kasih sayang dan sarana memperoleh pujian";[^p63] dengan sikap lunak (*mudārāt*), sebab dikatakan: "Sepertiga dari hidup bersama adalah bersikap lunak kepada manusia," dan rendah hati adalah salah satu jerat kemuliaan; dan dengan pura-pura lalai terhadap apa yang masih dapat dibiarkan, sebab dikatakan: "Hidup bersama terhimpun dalam satu takaran penuh: dua pertiganya kecerdikan dan sepertiganya pura-pura lalai."

Hendaklah ia mengamalkan apa yang dikatakan Amirul Mukminin, semoga selawat Allah atasnya: "Bila engkau ingin manusia mencintaimu, cintailah bagi mereka apa yang engkau cintai bagi dirimu sendiri." Seorang bijak ditanya: "Adakah kedermawanan yang dengannya aku dapat meliputi semua manusia?" Ia menjawab: "Ya, engkau mencintai kebaikan bagi mereka." Hendaklah pula ia memperlakukan orang yang duduk bersamanya sebagaimana diperintahkan Ibnu Abbas, semoga Allah meridainya, ketika ia berkata: "Teman duduk memiliki tiga hak atasku: aku memandangnya bila ia datang, aku melapangkan tempat baginya bila ia duduk, dan aku mendengarkannya bila ia berbicara." Hendaklah ia memperhatikan bahwa Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, tidak pernah terlihat menjulurkan kedua kakinya di hadapan orang yang duduk bersamanya, dan tidak pernah memegang tangan seseorang lalu menarik tangannya dari tangan orang itu sebelum orang itu sendiri yang melepaskannya.

Hendaklah ia bersungguh-sungguh menjauhi orang yang jahat dan lari darinya seperti lari dari singa. Bila ia terpaksa bergaul dengannya, hendaklah ia bersungguh-sungguh bersikap lunak kepadanya; sebab dikatakan: "Bukanlah orang bijak orang yang tidak bergaul secara baik dengan orang yang tidak dapat tidak ia gauli, sampai Allah memberinya kelapangan dan jalan keluar."

Hendaklah ia berusaha, sedapat mungkin, tidak menjadikan seorang pun musuh baginya. Kalilah berkata: "Orang berakal tidak semestinya terbawa oleh kepercayaannya pada kekuatannya untuk menarik permusuhan, sebagaimana pemilik penawar racun tidak semestinya meminum racun karena mengandalkan obat-obatnya."[^s6] Jalannya agar ia tidak memiliki musuh ialah menjauhi apa yang mewariskan permusuhan dengan segenap usaha dan kemampuannya. Bila ia kebetulan memiliki musuh tanpa ia sengaja, hendaklah ia bersungguh-sungguh mematikan permusuhannya. Aristoteles berkata: "Segerakanlah (menghadapi) permusuhan dengan persaudaraan sebelum apinya berkobar, sebab memadamkannya sebelum menyebar itu mudah."[^p64]

Wajib pula menampakkan kasih sayang kepadanya, sebab menampakkan kasih sayang kepada musuh termasuk siasat orang-orang berakal. Sebagian orang berkata: "Alangkah baiknya seseorang yang pandai bersikap lunak kepada musuhnya hingga ia memadamkan kobaran apinya." Dipandang baik pula ucapan al-Tanukhi:[^d28]

> Temuilah musuh dengan wajah yang tak bermuka masam,
> yang hampir meneteskan air keceriaan;
> sebab manusia yang paling teguh ialah yang menemui musuh-musuhnya
> dengan tubuh berisi dendam berbalut pakaian kasih sayang.

Abu al-Qasim al-Husain bin Muhammad bin al-Fadl al-Raghib, semoga Allah merahmatinya, berkata:[^p65] Ini cukup untuk apa yang dimaksud. Kami menutup kitab ini dengan memuji Allah dan menyanjung-Nya. Bagi-Nya segala puji selamanya dan syukur yang tulus, sebagaimana Dia layak menerimanya, atas limpahan nikmat-Nya kepada seluruh makhluk-Nya. Selawat-Nya atas Nabi Muhammad, semoga Allah melimpahkan selawat dan salam kepadanya, beserta keluarga dan seluruh sahabatnya. Amin.

[^p61]: CP: Edisi tahkik membaca *wa-ahl waladihi* ("keluarga anaknya"); kami mengikuti usul penerjemah Turki, *ahl baladihi* ("penduduk negerinya"), yang dalam tulisan hanya berbeda titik.

[^p62]: CP: Edisi tahkik membaca *al-khuluq al-shaḥīḥ* ("akhlak yang kikir"), yang bertentangan dengan maksudnya; kami mengikuti pembetulan penerjemah Turki, *al-khuluq al-fasīḥ* ("akhlak yang lapang"), yang juga terdapat dalam riwayat al-Bayhaqī dan Ibn ʿAsākir. Penyunting dan penerjemah Turki mencatat bahwa kedua ucapan ini tidak ditemukan sebagai hadis dalam kitab-kitab hadis; yang kedua dinukil Ibn al-Jawzī sebagai ucapan al-Shaʿbī.

[^p63]: CP: Edisi tahkik membaca *al-bashāsha munn al-mawadda*, yang tidak bermakna. Terjemahan Turki memahaminya *mukhkh* ("inti, sumsum"); bacaan lain yang mungkin ialah *fakhkh* ("jerat"), sejajar dengan "rendah hati adalah salah satu jerat kemuliaan" dan dengan ucapan Ali yang terkenal, "Keceriaan adalah tali jerat kasih sayang". Kami mengikuti terjemahan Turki.

[^s6]: CM: Ucapan ini terdapat dalam *Kalīla wa Dimna*, bab "Burung Hantu dan Burung Gagak", tetapi di sana diucapkan oleh burung gagak, bukan oleh Kalilah seperti disebut al-Rāghib: "Orang berakal, meskipun yakin akan kekuatan dan keutamaannya, tidak semestinya hal itu membawanya menarik permusuhan atas dirinya karena mengandalkan pendapat dan kekuatan yang ada padanya, sebagaimana orang yang memiliki penawar racun tidak semestinya meminum racun karena mengandalkan apa yang ada padanya."

[^p64]: CP: Edisi tahkik membaca *lā tuʿāwid al-ʿadāwa bi-l-ikhāʾ* ("janganlah mengulangi permusuhan dengan persaudaraan"; menurut penyunting, naskah menulis *lā ʿād*); terjemahan Turki memahaminya "janganlah memperbarui permusuhan dengan saudara-saudaramu sebelum apinya berkobar". Kami membacanya *bādir al-ʿadāwa bi-l-ikhāʾ* ("segerakanlah menghadapi permusuhan dengan persaudaraan"), yang sesuai dengan alasannya: memadamkan api sebelum menyebar itu mudah.

[^d28]: CD: Nasihat untuk bersikap ramah kepada musuh terdapat pula dalam *al-Dharīʿa*, Pasal Kelima, "Anjuran Bergaul dengan Orang-Orang Baik dan Menjauhi Orang-Orang Jahat": hendaklah ia bersikap ramah "kepada para penentang, dan kepada orang-orang yang hanya punya kepentingan syahwat di antara mereka, sebagaimana kepada saudara; bersabar terhadap mereka dan tersenyum kepada mereka, dengan harapan mereka kembali menjadi saudara dan untuk menjaga diri dari keburukan mereka". Di *al-Dharīʿa* tujuannya disebut dua: mengembalikan musuh menjadi saudara dan menjaga diri; bait al-Tanukhi di sini hanya menonjolkan yang kedua, bahkan dengan menyembunyikan dendam di balik keramahan. Tentang macam-macam musuh, lihat *al-Dharīʿa*, Pasal Kelima, "Permusuhan", dan nota kaki *al-Dharīʿa* no. 374 (`m-adawa`).

[^p65]: CP: Dalam teks tertulis *ibn al-Faḍl*; dalam sumber-sumber biografi nama kakek al-Rāghib biasanya ditulis *al-Mufaḍḍal*. Kalimat penutup ini, menurut penyunting, menjadi bukti tegas bahwa risalah ini karya al-Rāghib.

# Risalah Kedua {.kitab-ke}

# Keutamaan Manusia dengan Ilmu-Ilmu {.judul-kitab}

Dan hanya kepada-Nya kami memohon pertolongan.[^p66] Aku memohon kepada Allah Ta'ala agar menjadikan kami termasuk orang yang memandang dengan mata hati, berpikir, dan mengambil pelajaran, lalu dengan itu memperoleh sandaran; agar menjadikan kami mendapat petunjuk untuk memeriksa aib-aib kami; agar memberi kami taufik kepada apa yang baik bagi orang berakal untuk dipilih dan bagi orang beragama untuk diutamakan; agar menjadikan keinginan kami tertuju pada apa yang merupakan pemberian yang kekal, bukan pinjaman yang dititipkan; dan agar melimpahkan selawat atas Nabi-Nya yang terpilih dan Rasul-Nya yang diridai.

Ketika aku melihat Ustaz, semoga Allah menjaganya, menempuh jalan para pendahulunya dalam memelihara kemuliaan keturunan, mencintai dengan tabiatnya untuk menimba adab, dan bergairah memilih keutamaan-keutamaan dan menjauhi keburukan-keburukan,[^s7] aku ingin memperkenalkan kepadanya kaidah-kaidah yang benar: bahwa keutamaan yang sempurna dan kebahagiaan yang puncak terletak pada menghiasi jiwa dengan ilmu-ilmu yang bermanfaat, di dunia maupun di akhirat, dan itulah yang diutamakan oleh orang-orang berakal.

Kebahagiaan itu, meskipun ada tiga, yaitu kebahagiaan luar, berupa harta, kedudukan, dan keadaan yang terpandang; kebahagiaan badan, yaitu sehatnya campuran anggota-anggota, sempurnanya tubuh, dan keindahan; dan kebahagiaan jiwa, yaitu adab-adab yang terpuji dan ilmu-ilmu yang mulia, maka yang paling mulia adalah yang terakhir, sebab ialah yang tetap di tengah berubah-ubahnya keadaan dan yang bermanfaat di dua negeri.[^r-saada][^d29]

Seorang bijak menumpang sebuah kapal bersama para pemilik harta. Kapal itu pecah, harta mereka tenggelam, dan mereka semua menjadi fakir kecuali dia, sebab ilmunya adalah kekayaannya. Seseorang berkata kepadanya: "Aku akan kembali ke negeriku; adakah keperluanmu kepada kaummu?" Ia menjawab: "Katakan kepada mereka: bila kalian mengambil harta, ambillah harta yang tidak ikut tenggelam bila kapal pecah. Adapun harta (biasa), ia tidak terpuji bagi setiap orang, melainkan bagi sebagian orang saja, yaitu bila di dalam kalbunya ada kecukupan."

Diriwayatkan bahwa Plato ditawari harta yang banyak, lalu ia berkata: "Apa yang akan kuperbuat dengan sesuatu yang diberikan oleh nasib, dijaga oleh kekikiran, dan dibinasakan oleh kemurahan?"

Adapun keelokan rupa, tepat sekali orang yang berkata:

> Keelokan pada wajah seorang pemuda bukanlah kemuliaan baginya,
> bila tidak ada pada perbuatan dan akhlaknya.

Seorang bijak ditanya tentang orang tampan yang kosong dari keutamaan. Ia menjawab: "Rumahnya memang bagus, tetapi penghuninya buruk." Orang bodoh yang memiliki keelokan dan harta adalah keledai yang diberi tali kekang dari emas dan pakaian kain bergaris.

> Tiada berguna bagi kuda beban hiasan talinya,
> ketika kuda-kuda murni pilihan dilepas untuk berpacu.

Orang yang berbangga dengan sesuatu dari itu seperti budak perempuan yang berbangga dengan tandu tuannya. Seorang bodoh pernah berbangga dengan rumah, tanah, tunggangan, dan perabot. Seorang bijak berkata kepadanya: "Wahai pemuda, seandainya benda-benda ini dapat berbicara lalu berkata, 'Keindahan-keindahan ini milik kami, bukan milikmu,' maka apa yang menjadi milikmu? Apa yang akan engkau katakan kepadanya?" Dengan itu ia mengingatkan bahwa tidak ada keutamaan baginya karena hartanya.

Seorang kaya yang kosong dari keutamaan mengundang seorang bijak ke rumahnya. Orang bijak itu melihat seorang yang rendah dan rumah yang mewah, lalu ia meludah ke wajah orang itu. Orang itu berkata: "Wahai orang bijak, kebodohan macam apa yang tampak darimu ini?" Ia menjawab: "Ini tidak lain adalah hikmah. Aku memperhatikan, dan tidak kulihat di rumah ini sesuatu pun kecuali telah memenuhi kesempurnaan yang layak baginya, selain engkau; dan ludah itu semestinya dibuang ke tempat yang paling hina. Engkaulah yang paling hina di rumahmu."[^d30]

Wajib atas orang yang diarahkan kepada keutamaan yang sempurna untuk menghadirkan dalam benaknya beberapa hal.

**Pertama**: kebahagiaan ini tidak diperoleh kecuali di atas jembatan kepayahan, dan bagian kesungguhan (*jidd*) di dalamnya lebih besar daripada bagian nasib (*jadd*); bahkan engkau melihatnya tidak tercapai kecuali dengan kesungguhan semata. Berbeda dengan dua kebahagiaan yang lain, sebab keduanya adalah nasib yang terkadang terlewat oleh pencarinya dan diperoleh oleh orang yang tidak mengusahakannya. Dikatakan: "Ilmu tidak akan memberimu sebagiannya sampai engkau memberinya seluruh dirimu, dan tidak akan memeliharamu sampai engkau meminjamkan kepadanya kesungguhan dan jerih payahmu."[^d31]

> Katakan kepada orang yang mengharap perkara-perkara yang tinggi
> tanpa bersungguh-sungguh: engkau mengharap yang mustahil.

Sungguh telah melampaui batas orang yang berangan-angan menjadi seperti orang yang bersusah payah.

**Kedua**: siapa yang mencari yang agung mempertaruhkan yang agung, dan "siapa yang meminang perempuan cantik tidak merasa mahal maharnya". Siapa yang cita-citanya menjulang kepada perkara-perkara yang tinggi, semestinya jalan yang rendah tidak menghalangi cita-citanya. Tepat sekali orang yang berkata:

> Seandainya bukan karena kesulitan, semua orang akan menjadi pemimpin:
> kedermawanan memiskinkan dan keberanian membunuh.

**Ketiga**: kebahagiaan ini, meskipun awalnya tidak lepas dari semacam kesedihan dan rasa sakit, bila jiwa dipaksa menjalaninya dan dibuat merasakannya, jiwa akan menganggapnya enak dan menikmatinya, tidak seperti kelezatan-kelezatan badan dan syahwat-syahwat jasmani. Kelezatan badan berganti dan berubah, sedang kelezatan jiwa dengan ilmu abadi dan kekal. Siapa yang telah merasakan ilmu dan mengenal kelezatannya, ia tahu bahwa seseorang:

> kadang merasa lezat dengan muruah, padahal ia menyakitkan;
> dan siapa yang dimabuk cinta merasa lezat dengan derita cintanya.

Adapun keengganan kebanyakan orang terhadap keutamaan ini disebabkan ketidaktahuan mereka akan manisnya. Bagaimana mengetahui manisnya rasa yang lezat orang yang belum mencicipinya? Bagaimana mencicipinya orang yang tidak menyaksikannya? Bagaimana menyaksikannya orang yang tidak mencarinya? Bagaimana mencarinya orang yang jiwanya tidak merindukannya? Dan bagaimana jiwa merindukannya bila ia tidak pernah ditawarkan kepadanya? Semoga Allah menjadikan kami termasuk orang yang dicukupkan oleh limpahan karunia-Nya dan bahan nikmat-Nya dari ketergelinciran.

Isi pasal-pasal risalah ini secara ringkas:

**Pertama**: penjelasan tentang keutamaan manusia atas seluruh hewan.

**Kedua**: hal yang tanpanya manusia tidak berhak atas keutamaan.

**Ketiga**: keutamaan akal.

**Keempat**: macam-macam akal.

**Kelima**: macam-macam pengetahuan yang diusahakan.

**Keenam**: ilmu yang paling utama dan paling bermanfaat.

**Ketujuh**: apa yang dibutuhkan oleh pencarian ilmu, serta cara belajar dan mengajarkannya.

[^p66]: CP: Dalam edisi tahkik risalah ini tidak memiliki judul dan langsung diawali "Dan hanya kepada-Nya kami memohon pertolongan", sehingga agaknya bagian pembukanya (basmalah dan judul) hilang. Judul di atas mengikuti judul yang dipakai terjemahan Turki (*Risāla fī Faḍīlat al-Insān bi-l-ʿUlūm*), yang sesuai dengan isinya. Dalam doa pembuka, *li-faqd ʿuyūbinā* dibaca *li-tafaqqud ʿuyūbinā* ("memeriksa aib-aib kami").

[^s7]: CM: Ustaz yang dimaksud mungkin sama dengan Syekh dalam Risalah Pertama, yaitu wazir Aḥmad bin Ibrāhīm al-Ḍabbī (w. 399 H); lihat catatan s1. Kata *muhawwaman* dalam teks tidak jelas; kami memahaminya menurut konteks ("bergairah"), sejalan dengan terjemahan Turki.

[^r-saada]: **Kebahagiaan** (*saʿāda*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 91 (`m-saada`, *al-Mufradāt*) dan no. 92 (`k-saada`, *Kashshāf*).

[^d29]: CD: Dalam *al-Dharīʿa*, Pasal Pertama, "Macam-Macam Nikmat Allah Ta'ala yang Dianugerahkan dan yang Diusahakan", tiga kebahagiaan ini ditempatkan di bawah kebahagiaan akhirat, yang paling tinggi: sesudahnya keutamaan jiwa, keutamaan badan, dan keutamaan luar. Di sini kebahagiaan jiwa disamakan dengan ilmu dan adab, dan dijadikan pokok seluruh risalah.

[^d30]: CD: Kedua kisah terakhir, orang tampan yang kosong dari keutamaan ("Rumahnya memang bagus, tetapi penghuninya buruk") dan orang bijak yang meludah ke wajah orang kaya, terdapat pula dalam *al-Dharīʿa*, Mukadimah Pengarang, dengan redaksi yang sedikit berbeda: di sana orang bijak itu melihat "rumah yang baru diperbarui dan permadani yang terbentang", dan jawabannya lebih ringkas. Terjemahan ucapan pertama mengikuti redaksi terjemahan *al-Dharīʿa*. Di sana pula disebut perumpamaan keledai yang pelananya kain sutra bergaris.

[^d31]: CD: Ucapan ini terdapat pula dalam *al-Dharīʿa*, Pasal Kedua, "Apa yang Wajib Diupayakan Murid", dengan kelanjutan yang berbeda: "dan bila engkau telah memberinya seluruh dirimu, pemberiannya kepadamu atas sebagiannya pun masih belum pasti". Di sana ucapan itu dipakai untuk melarang murid menyombongkan diri terhadap gurunya dan terhadap ilmu; di sini untuk menegaskan bahwa kebahagiaan jiwa hanya dicapai dengan kesungguhan.

## Pasal Pertama: Keutamaan Manusia atas Seluruh Hewan {.judul-bab}

Jisim-jisim yang tumbuh ada tiga: tumbuhan, hewan, dan manusia.

Tumbuhan hanya memiliki (daya) makan dan tumbuh. Hewan, selain itu, memiliki syahwat, amarah, dan indra: ia mengidrak hal-hal yang hadir dengan indra dan hal-hal yang jauh dengan sangkaan (*wahm*), dan ia bergerak untuk mengganti apa yang terurai dari badannya dan untuk mengalahkan apa yang membahayakannya.[^r-wahm] Manusia, selain semua itu, memiliki daya pikir dan pertimbangan (*rawiyya*).[^r-fikr]

Maka manusia memiliki apa yang dimiliki keduanya dan dikhususkan dengan apa yang tidak dimiliki keduanya. Allah memberi setiap hewan suatu perbuatan yang khusus baginya dan yang dikerjakannya menurut tabiatnya: sebagian menurut tabiatnya membangun bangunan bundar, sebagian membangun bangunan persegi, sebagian menenun, sebagian menggali, dan sebagian mengumpulkan dan menyimpan; sampai-sampai kera dengan tabiatnya mengejek dan burung beo meniru-niru.[^p67]

Dia menjadikan bagi masing-masing pakaian sesuai dengan yang Dia pandang mencukupinya, dan senjata sesuai dengan yang Dia pandang maslahat baginya untuk dibawa: sebagian Dia beri alat untuk lari, yaitu kecepatan berlari; sebagian Dia beri tombak, seperti tanduk pada sapi; sebagian Dia beri gada, seperti kuku pada keledai dan kuda; dan sebagian Dia beri anak panah, seperti duri pada landak. Bagi manusia Dia menjadikan daya pikir dan pertimbangan, yang dengannya ia dapat sampai kepada perbuatan-perbuatan yang Dia khususkan baginya, serta kepada senjata-senjata dan pakaian-pakaian yang Dia jadikan baginya.[^p68][^t2]

Karena keutamaan ini, yaitu daya akal yang dengannya hikmah diidrak dan perbuatan yang kokoh dikerjakan, Allah menjelaskan keagungan manusia dengan firman-Nya: *"Dan sungguh, Kami telah memuliakan anak cucu Adam, dan Kami angkut mereka di darat dan di laut, dan Kami beri mereka rezeki dari yang baik-baik dan Kami lebihkan mereka di atas banyak makhluk yang Kami ciptakan dengan kelebihan yang sempurna"* (al-Isra': 70). Dikatakan: "yang baik-baik" yang Dia rezekikan kepada mereka ialah daya akal dan pembelajarannya.

Karena Allah Ta'ala mengkhususkan manusia dengan itu, Dia menjadikannya khalifah di bumi. Allah Ta'ala berfirman: *"Dialah yang menjadikan kamu sebagai khalifah-khalifah di bumi"* (Fatir: 39), dan berfirman: *"dan menjadikan kamu khalifah di bumi; maka Dia akan melihat bagaimana perbuatanmu"* (al-A'raf: 129).[^r-khilafa] Maka tetaplah bahwa manusia adalah makhluk paling utama yang diciptakan Allah di alam ini.

[^r-wahm]: **Sangkaan** (*wahm*). Lihat terjemahan *Tafṣīl*, catatan no. 86 (`k-wahm`, *Kashshāf*): daya batin yang mengidrak makna-makna parsial yang tidak terindra dari hal-hal yang terindra, seperti domba yang menangkap permusuhan serigala. Penyunting dan penerjemah Turki memahami *wahm* di sini sebagai "naluri"; tetapi yang dimaksud al-Rāghib adalah daya sangkaan dalam arti teknis itu: daya yang membuat hewan menangkap apa yang tidak hadir di hadapan indranya.

[^r-fikr]: **Pikiran dan pertimbangan** (*fikr*, *rawiyya*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 30 (`m-fikr`, *al-Mufradāt*). Dalam glosarium terjemahan *al-Dharīʿa* dan *Tafṣīl*, *rawiyya* dipadankan dengan "pertimbangan". Penyunting mencatat bahwa naskah menulis kata ini dengan hamzah (*ruʾya*, "penglihatan"), dan menilai yang dimaksud adalah *rawiyya*; penilaian itu tepat.

[^p67]: CP: Edisi tahkik membaca *ḥattā inna al-qadr bi-ṭabʿihi yaskharu* ("sampai-sampai periuk dengan tabiatnya mengejek"), dan penyunting menjelaskannya sebagai bunyi periuk yang mendidih; terjemahan Turki membacanya *qadar* ("takdir"). Keduanya keliru: yang benar *al-qird* ("kera"), hewan yang terkenal meniru-niru dan mengejek, berpasangan dengan burung beo yang meniru suara. Kata *yashqā* dibaca *yashuqqu* ("menggali, membelah"), sejalan dengan deretan keterampilan hewan.

[^p68]: CP: Edisi tahkik membaca *fa-li-baʿḍin ālat al-ḥarb, wa-hādhā al-ʿurf* ("alat perang, yaitu jengger/surai"). Kami mengikuti pembetulan penerjemah Turki: *ālat al-harab, wa-huwa al-ʿadw* ("alat untuk lari, yaitu kecepatan berlari"), yang didukung oleh redaksi yang sama dalam *Tafṣīl* (lihat catatan t2). Bagian akhir kalimat (*ilā ittijāh al-afʿāl*) dipahami sebagai "sampai kepada perbuatan-perbuatan".

[^t2]: CT: Uraian tentang senjata hewan dan akal manusia sama dengan *Tafṣīl*, Bab Kelima Belas, "Petunjuk Segala Sesuatu kepada Kemaslahatannya": "Sebagian Dia beri alat untuk lari, seperti kecepatan berlari; sebagian Dia beri tombak untuk menangkis, seperti tanduk pada sapi dan kambing; sebagian Dia beri gada, seperti kuku pada kuda dan keledai; dan sebagian Dia beri anak panah, seperti duri pada landak." Terjemahan di atas mengikuti redaksi itu. Di *Tafṣīl* uraian ini dipakai untuk membantah anggapan bahwa manusia diciptakan kurang karena tidak diberi senjata dan pakaian; di sini untuk menunjukkan keunggulan manusia atas hewan. Ayat al-Isra': 70 juga dikutip dalam *Tafṣīl*, Bab Ketiga Belas, "Manusia sebagai Tujuan Alam".

[^r-khilafa]: **Kekhalifahan** (*khilāfa*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 6 (`m-khilafa`, *al-Mufradāt*), dan terjemahan *Tafṣīl*, catatan no. 27 (`r-khilafa`).

## Pasal Kedua: Hal yang Tanpanya Manusia Tidak Berhak atas Keutamaan {.judul-bab}

Setiap maujud di alam ini memiliki perbuatan yang khusus baginya, yang tidak disertai oleh selainnya dan tidak dapat digantikan dengan sempurna oleh selainnya. Itu hukum yang berlaku pada maujud-maujud atas, seperti matahari, bulan, dan bintang-bintang, dan pada maujud-maujud bawah, seperti kuda dan unta. Kuda untuk berlari kencang, dan unta untuk menempuh jalan jauh yang menghauskan. Demikian pula alat-alat tajam, seperti pedang, pisau, dan gergaji: tidak satu pun dari jenis-jenis ini dapat menggantikan yang lain dengan sempurna; gergaji tidak cocok untuk apa yang cocok bagi pedang, dan pedang tidak cocok untuk apa yang cocok bagi gergaji. Anggota-anggota badan pun serupa, seperti tangan, kaki, mata, mulut, dan lidah.[^p69]

Maka manusia pun memiliki perbuatan yang khusus baginya, yang karenanya ia diciptakan, yaitu pikiran dan pertimbangan, yang dengannya ia sampai kepada ilmu dan amal yang kokoh. Karena itulah ia dijadikan khalifah di bumi, dan itulah yang dimaksud Allah dengan firman-Nya: *"Aku tidak menciptakan jin dan manusia melainkan agar mereka beribadah kepada-Ku"* (adz-Dzariyat: 56). Ibadah ialah memperoleh ilmu yang hakiki dan melakukan amal yang kokoh sesuai dengan tuntutan ilmu.[^d32]

Bila telah tetap bagimu bahwa kemuliaan setiap maujud sesuai dengan baiknya perbuatan yang khusus baginya keluar darinya dan dengan kehendaknya akan perbuatan itu, (ketahuilah bahwa) perbuatan dan kebaikan perbuatan, meskipun keduanya berkaitan dengan satu zat, adalah dua hal yang berlainan; sebab terkadang sesuatu berbuat tetapi tidak membaguskan perbuatannya.[^p70] Setiap yang darinya keluar perbuatan, bila perbuatan itu tidak sempurna, berkuranglah nilainya sesuai kekurangannya, sampai-sampai terkadang ia dipakai seperti yang lebih rendah darinya. Kuda, bila tidak cakap sebagai tunggangan, dipakai seperti keledai dengan pelana beban atau seperti kambing untuk disembelih; dan pedang, bila kurang dari apa yang dituntut substansinya, dipakai seperti kapak dan gergaji. Demikian pula manusia: bila ia tidak terdidik dalam apa yang semestinya ia kuasai dengan baik, dan kurang dalam daya ilmiah dan daya amaliahnya, berkuranglah nilainya, dan terkadang ia diperlakukan seperti binatang.[^d33]

Uraian ini menunjukkan benarnya ucapan Ali, semoga salam atasnya: "Nilai setiap orang adalah apa yang ia kuasai dengan baik," dan "Manusia adalah anak-anak dari apa yang mereka kuasai dengan baik."

Telah tetap bahwa manusia, selama ia tidak berilmu, lebih buruk daripada binatang. Sebab setiap binatang telah diberi kadar (pengetahuan) yang menjadi kemaslahatannya, pakaian sesuai kebutuhannya, dan senjata sesuai kemampuannya untuk membawanya; sedang manusia diberi, sebagai ganti semua yang diberikan kepada hewan, pertimbangan, yang bila ia asah dan pergunakan, dengannya ia memperoleh semua itu dan lebih banyak lagi; dan bila ia tidak mempergunakannya, tanpa ragu ia lebih rendah daripada hewan. Karena itu Allah Ta'ala berfirman tentang orang-orang bodoh: *"Mereka itu hanyalah seperti hewan ternak, bahkan lebih sesat jalannya"* (al-Furqan: 44). Mereka menjadi "lebih sesat jalannya" karena hewan ternak tidak memiliki jalan untuk memperoleh keutamaan, sedang mereka memiliki jalan untuk itu; bila mereka tidak melakukannya, tanpa ragu mereka lebih sesat jalannya.[^p71] Benarlah orang yang berkata:

> Tak pernah kulihat pada aib-aib manusia sesuatu
> seperti kurangnya orang-orang yang mampu mencapai kesempurnaan.

Keutamaan manusia pun menjadi jelas bila ia memperhatikan penyucian jiwanya. Manusia memiliki dua daya: daya kebinatangan, yaitu syahwat dan amarah yang ada padanya; dan daya kemalaikatan, yaitu pikiran dan pertimbangan yang ada padanya. Ia diseru untuk menyucikan daya kemalaikatannya dan menyelisihi daya syahwatnya, dan penyucian substansinya diserahkan kepadanya: jika ia melakukannya, ia telah menyucikannya; jika tidak, ia telah mengotorinya. Kepada uraian ini Allah mengisyaratkan dengan firman-Nya: *"Demi jiwa serta penyempurnaan (ciptaan)nya, maka Dia mengilhamkan kepadanya (jalan) kejahatan dan ketakwaannya, sungguh beruntung orang yang menyucikannya (jiwa itu), dan sungguh rugi orang yang mengotorinya"* (asy-Syams: 7-10). Dia menggandengkan keberuntungan dengan penyuciannya dan kerugian dengan pengotorannya.[^t3]

Maka tetaplah bahwa tidak ada yang lebih buruk bagi manusia daripada kosong dari keutamaan-keutamaan duniawi dan keagamaan. Sebab bila ia demikian, ia termasuk rakyat jelata "yang mengeruhkan air dan menaikkan harga": bila ia hidup, ia tidak terpuji; dan bila ia mati, ia tidak dirasa hilang.[^p72]

[^p69]: CP: Judul pasal ini dalam edisi tahkik dan dalam daftar pasal berbunyi *mā lā yastaḥiqqu bihi al-insān al-faḍīla* ("apa yang dengannya manusia tidak berhak atas keutamaan"), padahal isinya menjelaskan perbuatan khas yang menjadi dasar keutamaan manusia. Kami memahaminya *mā lā yastaḥiqqu al-insān al-faḍīla illā bihi* ("hal yang tanpanya manusia tidak berhak atas keutamaan"); terjemahan Turki memahaminya secara harfiah ("hal-hal yang tidak memberi manusia keutamaan").

[^d32]: CD: Bandingkan *al-Dharīʿa*, Pasal Pertama, "Tujuan Manusia Diciptakan", yang menjabarkan tujuan penciptaan manusia dalam tiga hal: memakmurkan bumi, beribadah, dan menjadi khalifah. Di sini ketiganya dipadatkan: ibadah didefinisikan sebagai "memperoleh ilmu yang hakiki dan melakukan amal yang kokoh", dan kekhalifahan diturunkan dari daya pikir. Adz-Dzariyat: 56 juga dibahas dalam *al-Dharīʿa*, Pasal Keenam, "Keadaan Manusia dalam Memelihara Urusan Dunia dan Akhirat", ketika al-Rāghib membantah orang yang menjadikan ayat itu dalil bahwa yang paling utama adalah para ahli ibadah yang menolak dunia sama sekali.

[^p70]: CP: Kalimat ini rusak dalam edisi tahkik (*wa-irādatihi yaḥsibuhu … fa-humā qawiyyān*), dan penyunting mencatat bahwa sebagian katanya tidak jelas. Kami membaca *fa-humā ghayrān* ("keduanya dua hal yang berlainan"), yang sesuai dengan alasannya ("sebab terkadang sesuatu berbuat tetapi tidak membaguskan perbuatannya"). Terjemahan Turki membacanya "dua faktor yang kuat". Kata yang tidak jelas sesudah "kuda, bila tidak …" dipahami menurut padanannya dalam *al-Dharīʿa* (lihat catatan d33). Frasa *quwwatihi al-ʿāʾima wa-l-ʿāmila* dibaca *al-ʿālima wa-l-ʿāmila* ("daya ilmiah dan daya amaliah").

[^d33]: CD: Perumpamaan yang sama terdapat dalam *al-Dharīʿa*, Pasal Pertama, "Tujuan Manusia Diciptakan": "Setiap sesuatu yang diadakan untuk suatu perbuatan, kemuliaannya terletak pada sempurnanya perbuatan itu terwujud darinya, dan kerendahannya terletak pada hilangnya perbuatan itu darinya … Kuda, bila tidak lagi layak untuk berlari maju dan mundur dalam pertempuran, dijadikan hewan pengangkut beban atau disiapkan untuk disembelih; dan pedang, bila tidak lagi layak untuk memotong, dijadikan gergaji." Di sana pula dikutip al-Furqan: 44. Terjemahan Turki mencatat bahwa ucapan Ali "Nilai setiap orang adalah apa yang ia kuasai dengan baik" juga dikutip al-Rāghib dalam *al-Dharīʿa* dan *al-Mufradāt*.

[^p71]: CP: Edisi tahkik membaca *li-anna al-anʿām lā sabīl lahā illā ilā istifādat al-faḍīla* ("tidak ada jalan baginya kecuali untuk memperoleh keutamaan"), yang membalik maksudnya. Kata *illā* ("kecuali") dibuang, sesuai dengan kelanjutan kalimat ("sedang mereka memiliki jalan untuk itu") dan dengan pemahaman terjemahan Turki.

[^t3]: CT: Pembagian dua daya ini sejalan dengan *Tafṣīl*, Bab Kelima, "Terbentuknya Manusia Sedikit demi Sedikit hingga Menjadi Manusia yang Sempurna": "Jiwa manusia berada di antara dua daya: daya syahwat dan daya akal"; jiwa manusia berada di antara daya syahwat, yang dengannya ia berhasrat kepada kelezatan badan dan kebinatangan, dan daya akal, yang dengannya ia berhasrat kepada ilmu dan perbuatan yang indah; penyunting mengutip bagian ini. Di sini daya akal disebut "daya kemalaikatan", dan penyucian jiwa diserahkan kepada pilihan manusia.

[^p72]: CP: Ungkapan ini berasal dari jawaban Ṣaʿṣaʿa bin Ṣūḥān kepada Muawiyah ketika diminta menggambarkan manusia: "Penunggang kuda yang membela negeri, petani yang berusaha memakmurkan, orang alim yang sibuk dengan agama, dan rakyat jelata di antara mereka yang mengeruhkan air dan menaikkan harga" (dicatat penyunting dan penerjemah Turki dari *al-Amālī* karya Abū ʿAlī al-Qālī). Al-Rāghib juga memakai ungkapan ini dalam *al-Dharīʿa*, Pasal Keenam, "Kewajiban Mencari Penghidupan", tentang para penganggur: "Tidak ada faedah pada orang-orang seperti mereka kecuali mengeruhkan sumber-sumber air dan menaikkan harga-harga." Kata *ghāfilan* dalam teks dibaca *ghuflan* ("kosong"), sesuai usul penyunting.

## Pasal Ketiga: Keutamaan Akal {.judul-bab}

Ketahuilah bahwa akal adalah alat bagi setiap ilmu dan setiap kebaikan; dengannya dikenal setiap yang baik dan yang buruk.[^r-aql] Karena itu dikatakan: "Akal adalah raja, dan perangai-perangai adalah rakyatnya; bila ia lemah dalam mengurus mereka, kerusakan sampai kepada mereka." Buzurjmihr berkata: "Akal adalah penasihat yang lurus dan penolong yang membahagiakan; siapa yang menaatinya akan diselamatkannya, dan siapa yang mendurhakainya akan dibinasakannya." Dikatakan: "Orang berakal ialah yang memiliki pengawas dari akalnya atas seluruh syahwatnya."

Maka setiap keutamaan yang tidak diawasi akal lebih layak disebut kekurangan dan lebih layak dijauhi, sebab ia adalah keburukan yang dinamai dengan nama keutamaan dan sifat tercela yang disifati terpuji, karena ia berpotensi membinasakan pemiliknya.[^p73] Karena itu dikatakan: "Siapa yang akalnya bukan sifat baik yang paling menguasainya, kebinasaannya ada pada sifat baik yang paling menguasainya."[^d34]

Dikatakan: "Akal tanpa adab adalah kefakiran, dan adab tanpa akal adalah kebinasaan"; maka lihatlah betapa jauh jarak antara kefakiran dan kebinasaan! Dikatakan pula: "Janganlah meneladani perbuatan orang yang tidak memiliki ikatan akal."

Karena tidak ada keutamaan pada manusia yang terlepas dari akal, dan akal yang sempurna tidak terlepas dari keutamaan-keutamaan, seorang bijak berkata: "Keajaiban yang paling ajaib ialah akal tanpa kemuliaan budi dan kemuliaan budi tanpa akal," sebagai peringatan bahwa yang satu tidak terlepas dari yang lain. Dikatakan: "Akal memegang tali kekang keutamaan." Hal ini diungkapkan oleh riwayat bahwa ketika Adam turun (ke bumi), Jibril datang kepadanya dan berkata: "Allah menghadirkan kepadamu akal, agama, dan rasa malu agar engkau memilih salah satunya." Adam berkata: "Aku memilih akal." Jibril, semoga salam atasnya, berkata kepada agama dan rasa malu: "Pergilah kalian." Keduanya menjawab: "Kami diperintahkan untuk tidak berpisah dari akal di mana pun ia berada."

[^r-aql]: **Akal** (*ʿaql*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 93 (`m-aql`, *al-Mufradāt*) dan no. 94 (`k-aql`, *Kashshāf*), dan terjemahan *Tafṣīl*, catatan no. 24 (`r-aql`).

[^p73]: CP: Edisi tahkik membaca *lam yūf al-ʿaql ʿalayhā*; kami mengikuti pembetulan penyunting, *lam yushrif* ("tidak mengawasi"). Frasa *maẓinna an turdiyahu* berarti "tempat yang disangka akan membinasakannya", yakni berpotensi membinasakan.

[^d34]: CD: Ucapan ini terdapat dalam *al-Dharīʿa*, Pasal Kedua, "Keutamaan Akal", sebagai ucapan para ahli hikmah, dengan bunyi yang berbeda pada ujungnya: "siapa yang akalnya bukan sifat baik yang paling menguasainya, kebinasaannya ada pada sifat *buruk* yang paling menguasainya." Di sini, dalam naskah dan juga dalam terjemahan Turki, ujungnya berbunyi "sifat *baik* yang paling menguasainya", dan bunyi ini justru sesuai dengan konteks risalah: keutamaan yang tidak diawasi akal, seperti keberanian tanpa akal atau kemurahan tanpa akal, dapat membinasakan pemiliknya. Maka perbedaan ini agaknya disengaja: di *al-Dharīʿa* ucapan itu menegaskan bahwa akal harus mengalahkan keburukan, di sini bahwa akal harus memimpin kebaikan.

## Pasal Keempat: Macam-Macam Akal {.judul-bab}

Akal ada dua. Pertama, akal bawaan (*gharīzī*), yang dengannya manusia menjadi manusia dan terbedakan dari seluruh hewan; bila anak kecil telah mencapai usia tertentu, akal itu menjadi kuat padanya, dan dengannya taklif berlaku ketika ia balig; para filsuf terdahulu menamainya akal hayulani (*al-ʿaql al-hayūlānī*). Kedua, akal luar yang diperoleh (*mustafād*) dengan berbagai jalan kecerdasan, yang berlaku sebagai kelanjutan dari akal yang pertama.[^r-ghariza2][^d35]

Diriwayatkan dari Amirul Mukminin: "Akal ada dua: akal yang baru (diperoleh) dan akal pembawaan. Bila keduanya terhimpun pada seseorang, dialah yang tak tertandingi; dan bila hanya ada salah satunya, akal pembawaan yang lebih utama." Ia lebih utama karena akal perolehan tidak tercapai sebagaimana mestinya kecuali bagi orang yang memiliki akal bawaan.[^p74]

Yang menunjukkan hal itu ialah riwayat dari Nabi, semoga salam atasnya, bahwa beliau bersabda: *"Ketika Allah Ta'ala menciptakan akal, Dia berfirman kepadanya: Menghadaplah! Maka ia menghadap. Kemudian Dia berfirman kepadanya: Berbaliklah! Maka ia berbalik. Kemudian Dia berfirman: Demi kemuliaan dan keagungan-Ku, tidaklah Aku menciptakan makhluk yang lebih mulia bagi-Ku daripadamu; denganmu Aku mengambil dan denganmu Aku memberi."* Inilah akal bawaan; karena itu penciptaannya dinisbatkan kepada Allah Ta'ala.[^d36]

Diriwayatkan bahwa beliau, semoga salam atasnya, bersabda: *"Tidak ada seorang pun yang memperoleh sesuatu yang lebih utama daripada akal yang menunjukkannya kepada petunjuk dan mengembalikannya dari kebinasaan."* Yang beliau maksud adalah akal perolehan; karena itu beliau menjadikannya perolehan manusia. Yang menjelaskan hal itu ialah sabda beliau, semoga salam atasnya: *"Wahai Ali, bila manusia mendekatkan diri kepada Pencipta mereka dengan berbagai macam kebajikan, maka dekatkanlah dirimu kepada-Nya dengan berbagai macam akal, niscaya engkau mendahului mereka dalam derajat dan kedekatan, di sisi manusia di dunia dan di sisi Allah di akhirat."*

Kepada akal inilah Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, mengisyaratkan. Dikatakan (kepada seseorang): "Alangkah berakalnya orang Nasrani ini!" Ia menjawab: "Orang berakal ialah orang yang mengesakan Allah Ta'ala dan beramal dengan menaati-Nya." Sejalan dengan itu apa yang dikisahkan Allah tentang penghuni neraka: *"Sekiranya (dahulu) kami mendengarkan atau memikirkan (peringatan itu) tentulah kami tidak termasuk penghuni neraka yang menyala-nyala"* (al-Mulk: 10).[^d37]

[^r-ghariza2]: **Akal bawaan dan akal perolehan** (*al-ʿaql al-gharīzī*, *al-ʿaql al-mustafād*). Lihat glosarium terjemahan *al-Dharīʿa* (entri *al-ʿaql al-gharīzī / al-muktasab*: "akal bawaan / akal perolehan") dan nota kaki *al-Dharīʿa* no. 78 (`k-gharizah`). Istilah *al-ʿaql al-hayūlānī* ("akal hayulani", akal material) berasal dari para filsuf, yang menamai tingkat pertama akal dengan nama materi pertama (*hayūlā*) karena ia semata-mata kesiapan untuk menerima bentuk-bentuk inteligibel, sebagaimana materi siap menerima segala bentuk.

[^d35]: CD: Pembagian yang sama terdapat dalam *al-Dharīʿa*, Pasal Kedua, "Keutamaan Akal", subbahasan "Macam-Macam Akal": "akal bawaan (*gharīzī*), yaitu daya yang siap menerima ilmu-ilmu, yang keberadaannya pada anak kecil seperti keberadaan pohon kurma di dalam biji dan bulir di dalam benih; dan akal perolehan (*mustafād*), yaitu yang dengannya daya itu menjadi kuat". Di *al-Dharīʿa* akal perolehan dibagi lagi menjadi yang diperoleh tanpa pilihan dan yang diperoleh dengan pilihan; di sini ditambahkan nama filosofis akal bawaan (*hayūlānī*) dan kaitannya dengan taklif.

[^p74]: CP: Edisi tahkik membaca *kānat al-naḥīza awwalahumā* ("akal pembawaan yang pertama dari keduanya"); kami membacanya *awlāhumā* ("yang lebih utama dari keduanya"), sesuai dengan kalimat penjelasnya ("Ia lebih utama karena …"). Dalam *al-Dharīʿa* ucapan Ali tentang dua akal dikutip dalam bentuk syair ("Akal ada dua: yang tertabiat dan yang terdengar …"), dan penyunting mengutipnya pada tempat ini.

[^d36]: CD: Hadis ini dikutip dalam *al-Dharīʿa*, Pasal Kedua, "Keutamaan Akal", dan dalam *Tafṣīl*, Bab Kedua, "Genus-Genus Segala yang Ada dan Kedudukan Manusia di Antaranya", dengan awal "Yang pertama kali diciptakan Allah Ta'ala adalah akal" dan dengan tambahan pada akhirnya ("denganmu Aku memberi pahala, dan denganmu Aku menghukum"). Terjemahan di atas mengikuti redaksi terjemahan *al-Dharīʿa*. Penerapannya berbeda: di *al-Dharīʿa* hadis ini menjadi dalil bahwa akal adalah substansi dan makhluk pertama, dan di *Tafṣīl* bahwa yang inteligibel diadakan sebelum yang terindra; di sini hadis itu menunjuk akal bawaan, yang penciptaannya dinisbatkan kepada Allah, sebagai lawan akal perolehan yang dinisbatkan kepada usaha manusia. Kedua hadis sesudahnya juga dikutip dalam *al-Dharīʿa* pada tempat yang sama, untuk akal perolehan.

[^d37]: CD: Kisah orang Nasrani ini dan ayat al-Mulk: 10 dikutip dalam *al-Dharīʿa*, Pasal Kedua, "Akal Perolehan yang Duniawi dan yang Ukhrawi", sebagai contoh "sedikitnya penghargaan terhadap pengetahuan duniawi"; di sana penjawabnya adalah seseorang yang berkata kepada orang yang menyifati orang Nasrani sebagai berakal: "Diam! Orang berakal hanyalah orang yang mengesakan Allah Ta'ala dan beramal dengan menaati-Nya." Terjemahan jawaban dan ayat di atas mengikuti redaksi itu. Dengan demikian, yang dimaksud dengan "akal" dalam kisah ini adalah akal perolehan yang ukhrawi.

## Pasal Kelima: Macam-Macam Pengetahuan yang Diusahakan {.judul-bab}

Pengetahuan ada dua macam: yang diperoleh tanpa perantara dan yang diperoleh dengan perantara.

Yang diperoleh tanpa perantara ada dua. Pertama, yang diperoleh dari indra, seperti pengetahuan tentang warna, suara, yang dicecap, dan yang diraba. Kedua, yang diperoleh dari akal secara spontan (*badīhatan*) tanpa berpikir, seperti pengetahuan bahwa dua dan dua adalah empat; bahwa setiap dua jisim, bila yang satu dibandingkan dengan yang lain, adakalanya sama, lebih besar, atau lebih kecil; bahwa sesuatu yang sama dengan dua hal yang sama, maka ketiganya sama; bahwa tidak ada perantara antara penetapan dan penafian; bahwa keseluruhan lebih besar daripada bagian; dan bahwa satu jisim tidak berada di dua tempat dalam satu keadaan. Semua ini tidak membutuhkan premis, tetapi orang-orang berakal mengidraknya dengan sekadar memperhatikan, sebagaimana yang mengindra mengidrak yang terindra dengan bersentuhan langsung dengannya.[^p75]

Adapun yang diperoleh dengan perantara ialah yang membutuhkan pemikiran dan penggalian, baik dengan perantaraan indra maupun dengan perantaraan akal. Keduanya adakalanya akliah, adakalanya keagamaan (*millī*), dan adakalanya dituntut oleh keduanya sekaligus.[^r-milla]

Yang akliah ialah mengenal Allah Ta'ala dan mengenal kenabian Nabi-Nya.

Yang keagamaan ialah mengenal Kitab Allah, qiraahnya, takwilnya, dan tafsirnya, dan sunah Nabi-Nya, serta apa yang digali dari keduanya berupa fikih, kalam, nasihat-nasihat, dan zuhud; kitab-kitab ilmu bahasa dan nahwu adalah alat dan tiangnya.

Yang hikmah (*ḥikamī*) ialah mengenal ilmu hitung, ilmu bintang, geometri, ilmu alam, firasat, dan kedokteran; dan dikatakan: logika adalah alat baginya.[^r-hikma2]

Jalan sampai kepada ilmu-ilmu ada tiga.

**Pertama**: dari bahan-bahan langit, yaitu keadaan permulaan (penciptaan) dan pengembalian, cara pahala dan siksa, dan pokok-pokok ibadah.

**Kedua**: dari dalil-dalil yang digali, seperti mengenal barunya alam, mengenal Allah, mengenal kenabian, dan mengenal wajibnya pembalasan.[^p76]

**Ketiga**: dari jalan pengalaman, seperti firasat, tafsir mimpi, ilmu jejak (*qiyāfa*), ramalan burung (*zajr*), ilmu hitung, ilmu bintang, mengenal waktu-waktu bercocok tanam, pengalaman-pengalaman, dan umumnya cara-cara mencari penghasilan.

Ketiganya diperoleh manusia dengan taufik Allah Ta'ala, dan taufik adalah tiang setiap yang dicari.[^d38]

[^p75]: CP: Edisi tahkik membaca *kull jinsayn* ("setiap dua jenis"); penyunting mencatat bahwa kata itu tidak jelas. Kami mengikuti penerjemah Turki, *kull jismayn* ("setiap dua jisim"), yang sesuai dengan contoh berikutnya. Kalimat "sesuatu yang sama dengan dua hal yang sama, maka ketiganya sama" dilengkapi menurut maksudnya, sebab penyunting mencatat ada kata yang hilang. Kata yang tidak jelas sesudah "mengidraknya" dibaca *bi-l-mulāḥaẓa* ("dengan memperhatikan"), sesuai bacaan penyunting.

[^r-milla]: **Keagamaan** (*millī*). *Millī* dinisbatkan kepada *milla* (agama, syariat), dan dalam klasifikasi ilmu berarti ilmu yang bersumber dari nukilan agama, sebagai lawan ilmu akliah. Al-Rāghib menambahkan kelompok ketiga, yang dituntut oleh akal dan agama sekaligus, dan menyebutnya ilmu hikmah (*ḥikamī*).

[^r-hikma2]: **Hikmah** (*ḥikma*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 38 (`m-hikma`) dan no. 39 (`k-hikma`), dan terjemahan *Tafṣīl*, catatan no. 46 (`r-hikma`). Penyunting mengutip ucapan al-Rāghib, yang terdapat dalam *al-Dharīʿa*, Pasal Kedua, "Perbedaan antara Ilmu dan Akal, serta antara Ilmu, Makrifat, Dirayah, dan Hikmah": "Hubungan ilmu-ilmu dengan hikmah, dari satu segi, seperti hubungan anggota-anggota dengan badan, karena ilmu-ilmu itu adalah bagian-bagiannya." Di sana pula dinyatakan bahwa dalam pengetahuan syariat hikmah adalah nama bagi ilmu-ilmu akliah; di sini ilmu hikmah dibedakan dari ilmu akliah dalam arti mengenal Allah dan kenabian.

[^p76]: CP: Edisi tahkik membaca *maʿrifat ḥudūth al-ʿilm* ("barunya ilmu"); kami mengikuti pembetulan penerjemah Turki, *ḥudūth al-ʿālam* ("barunya alam"), yang merupakan pokok pertama ilmu kalam dan yang sesuai dengan deretan sesudahnya.

[^d38]: CD: *Al-Dharīʿa*, Pasal Kedua, "Jalan-Jalan Memperoleh Ilmu", membagi jalan ilmu menjadi empat: (1) spontanitas akal dan benturan indra; (2) perenungan dengan premis-premis akliah atau indrawi; (3) kabar dari manusia, didengar atau dibaca; (4) wahyu. Pembagian di sini berbeda susunannya: pengetahuan tanpa perantara (indra dan spontanitas akal) sejajar dengan jalan pertama; "dalil-dalil yang digali" sejajar dengan jalan kedua; "bahan-bahan langit" sejajar dengan jalan keempat; sedang jalan ketiga *al-Dharīʿa* (kabar) diganti dengan "pengalaman". Pembagian ilmu menjadi akliah, keagamaan, dan hikmah juga tidak sama dengan "Pembatasan Macam-Macam Ilmu" dalam *al-Dharīʿa*, yang membagi ilmu menurut hubungannya dengan lafaz dan makna.

## Pasal Keenam: Ilmu yang Paling Utama dan Paling Bermanfaat {.judul-bab}

Manusia, dalam hal-hal yang mereka upayakan, adalah pencari kebaikan; dan definisi kebaikan ialah apa yang dicari oleh semua. Yang menunjukkan bahwa itulah definisinya ialah bahwa akal melarang usaha dan gerak yang tidak berujung, dan hal itu diketahui dengan prinsip-prinsip pertama akal. Setiap perbuatan yang dilakukan orang berakal dimaksudkan untuk suatu kebaikan; maka kebaikan adalah apa yang dicari oleh semua, tetapi terkadang pencarinya keliru dan peminangnya salah. Benarlah Abu al-'Atahiyah dalam ucapannya:[^r-khayr2]

> Setiap orang mencari daya upaya yang ia harapkan
> untuk menolak mudarat dan meraih manfaat.
> Namun orang keliru dalam mengatur keadaannya,
> hingga kadang ia memilih susah payah daripada ketenangan.[^d39]

Bila hal itu telah tetap, maka seseorang berusaha untuk salah satu dari tiga hal: untuk menyelamatkan jiwa dari penderitaan dan mendekatkannya kepada kekekalan abadi dan kenikmatan yang kekal; untuk menyelamatkan badan dari penderitaan di negeri dunia; atau untuk mencari apa yang membuat badan senang, berupa apa yang menjadi kemaslahatannya, seperti harta, kedudukan, dan para penolong.[^p77] Setiap satu dari itu memiliki ilmu yang dengannya ia dicapai.

Ilmu yang paling utama ialah yang berkaitan dengan yang dicari yang paling utama; dan yang dicari yang paling utama ialah yang bila tercapai tidak hilang dan bila diperoleh tidak dirampas, yaitu kekekalan abadi. Adapun badan, harta, kedudukan, dan para penolong adalah pinjaman-pinjaman yang akan diambil kembali: mereka meninggalkanmu dan engkau meninggalkan mereka. Perumpamaannya ialah firman Allah Ta'ala: *"Sesungguhnya perumpamaan kehidupan dunia itu, hanya seperti air (hujan) yang Kami turunkan dari langit"* (Yunus: 24).

Maka tetaplah bahwa ilmu itu tiga: yang paling utama ialah ilmu agama, yang dengannya diperoleh kekekalan abadi; kemudian ilmu badan; kemudian ilmu mencari penghidupan.[^d40]

[^r-khayr2]: **Kebaikan** (*khayr*). Lihat catatan r-khayr di atas. Definisi "apa yang dicari oleh semua" sama dengan rumusan *al-Mufradāt*, s.v. *kh-y-r*: kebaikan ialah apa yang diinginkan oleh semua, seperti akal, keadilan, keutamaan, dan sesuatu yang bermanfaat. Dalil bahwa akal melarang gerak yang tidak berujung adalah dalil para filsuf: setiap perbuatan dimaksudkan untuk sesuatu yang lain, dan rangkaian itu harus berakhir pada sesuatu yang dicari demi dirinya sendiri, yaitu kebaikan tertinggi.

[^d39]: CD: Bait-bait Abu al-'Atahiyah ini dikutip pula dalam *al-Dharīʿa*, Pasal Pertama, "Macam-Macam Nikmat Allah Ta'ala yang Dianugerahkan dan yang Diusahakan", sesudah kalimat "Dalam mengupayakan hal itu manusia ada dua golongan: pencari kebaikan dan pelari dari keburukan". Terjemahan di atas mengikuti redaksi terjemahan *al-Dharīʿa*.

[^p77]: CP: Edisi tahkik membaca *wa-l-taʿlīm al-abadī* ("pengajaran yang abadi"); kami membacanya *wa-l-tanʿīm al-abadī* ("kenikmatan yang abadi"), pasangan *al-baqāʾ al-sarmadī* ("kekekalan abadi"). Frasa *li-ṭalab man yaṭību bi-l-badan* dibaca *li-ṭalab mā yaṭību bihi al-badan* ("mencari apa yang membuat badan senang"). Penyunting menduga *al-ālām* ("penderitaan") adalah *al-āthām* ("dosa-dosa"); dugaan itu tidak perlu, sebab penderitaan jiwa di akhirat adalah lawan dari kenikmatan abadi.

[^d40]: CD: Bandingkan *al-Dharīʿa*, Pasal Kedua, "Apa yang dengannya Keutamaan Ilmu Diketahui": keutamaan suatu ilmu diketahui dengan dua hal, mulianya buahnya dan kokohnya dalilnya; "buah ilmu agama ialah sampainya manusia kepada kehidupan abadi, sedang buah ilmu kedokteran ialah sampainya kepada kehidupan dunia yang terputus". Di sini hanya ukuran pertama (buah) yang dipakai, dan urutannya dilengkapi dengan ilmu mencari penghidupan pada tingkat ketiga.

## Pasal Ketujuh: Apa yang Dibutuhkan Pencari Ilmu, serta Cara Belajar dan Mengajarkannya {.judul-bab}

Pencari ilmu membutuhkan lima hal: tiga dari langit, yaitu baiknya tabiat, kecukupan, dan panjangnya umur; satu dari pihaknya sendiri, yaitu perhatian yang sungguh-sungguh; dan satu dari pihak gurunya, yaitu nasihat yang tulus.

### Baiknya Tabiat {.judul-pasal}

Baiknya tabiat ialah bahwa ia banyak menerima; kuat menghafal apa yang ia terima; paham terhadap apa yang ia hafal; merenungkan apa yang ia pahami; dan kuat mengingat apa yang ia renungkan; dan bersama itu ia memiliki daya tangkap (*dhihn*), ketajaman akal (*dhakāʾ*), dan kecerdasan (*fiṭna*). Semua itu adalah daya-daya akal, seperti alat-alat baginya, dan perlu didefinisikan agar hakikat-hakikatnya tergambar.

Tabiat (*ṭabʿ*) ialah daya menggambarkan makna-makna; kata ini berasal dari *ṭabʿ al-khātam* (cetakan cincin stempel).[^r-tab] Hafalan (*ḥifẓ*) ialah tetapnya rupa apa yang telah tercetak dalam jiwa. Pemahaman (*fahm*) ialah mengidrak apa yang telah dihafal. Pikiran (*fikr*) ialah menyaring apa yang telah dipahami. Ingatan (*dhikr*) ialah menyingkap tirai dari apa yang telah dipikirkan. Daya tangkap (*dhihn*) ialah perenungan jiwa terhadap apa yang menjadi konsekuensi dari apa yang telah ia pahami dan pikirkan. Ketajaman akal (*dhakāʾ*) ialah cepatnya perenungan itu; kata ini berasal dari *dhakat al-nār* (api menyala).[^d41]

### Kecukupan dan Panjangnya Umur {.judul-pasal}

Adapun kecukupan ialah bahwa ia memperoleh sekadar bekal hidup yang membuatnya tidak perlu bekerja mencari nafkah, dan yang karena banyaknya tidak menjadi kesibukan yang menghalanginya dari menekuni belajar. Dalam kekayaan jiwa ada yang mencukupimu, yaitu sekadar menutup kebutuhan; bila lebih dari itu, orang yang kaya dengannya justru menjadi fakir.[^p78] Buzurjmihr berkata: "Janganlah mewariskan harta kepada anak kecuali sekadar yang menjadi penolong baginya dalam mencari ilmu."

Adapun panjangnya umur, Hippokrates berkata: "Keahlian itu panjang, umur itu pendek, percobaan itu berbahaya, dan keputusan itu sulit." Ini dalam ilmu badan; maka apa sangkaanmu tentang ilmu agama?[^p79] Panjangnya umur dibutuhkan karena akal tidak menjadi kokoh kecuali dengan pengalaman, dan pengalaman tidak tercapai kecuali dengan masa umur yang panjang yang di dalamnya keadaan-keadaan berganti.

### Perhatian yang Sungguh-Sungguh {.judul-pasal}

Adapun perhatian, ia dijalankan dengan memelihara beberapa hal: sebagian diperhitungkan pada dirinya sendiri, sebagian dalam kaitannya dengan ilmu, dan sebagian dalam kaitannya dengan guru.

Yang diperhitungkan pada dirinya sendiri ialah apa yang dikatakan seorang bijak: "Tidak mungkin seseorang menampung ilmu-ilmu yang mulia sebelum ia menghapus dari benaknya perkara-perkara yang rendah, sehingga seluruh akhlaknya menjadi baik." Karena itu Hippokrates berkata: "Badan-badan yang tidak bersih, setiap kali engkau tambah makanannya, bertambah pula penyakitnya." Dikatakan: "Ilmu-ilmu yang suci hanya untuk kalbu-kalbu yang suci."[^p80][^d42]

Yang diperhitungkan dalam kaitannya dengan ilmu, haknya ialah sebagai berikut.

Ia mengetahui tujuan yang karenanya ia menempuh jalan ilmu itu, dan mengetahui jalan terpendek kepadanya.

Ia mendahulukan yang paling penting, yaitu yang tidak boleh tidak diketahui, sebab yang diperhitungkan dalam setiap bidang adalah pokok-pokok sebelum cabang-cabang. Dikatakan: "Suatu kaum kehilangan kesampaian karena meninggalkan pokok-pokok." Yaitu dengan mencari genus ilmu sebelum cabangnya, dan spesiesnya sebelum partikular-partikularnya, sebab partikular-partikular tidak mampu ia kuasai.

Ia tidak berambisi mencapai ujungnya yang terjauh. Aristoteles berkata: "Aku tidak menuntut ilmu untuk mencapai ujungnya yang terjauh dan menguasai puncaknya, tetapi (untuk mengetahui) apa yang tidak boleh tidak diketahui oleh orang berakal."

Ia tidak mengarahkan cita-citanya dari ilmu kepada apa yang di luar kemampuan manusia untuk diidrak, sebab itu kebodohan yang berlebihan. Ia melewati apa yang sulit ia capai, dengan menyengaja ucapan penyair:[^p81]

> Bila engkau tak mampu mengerjakan sesuatu, tinggalkanlah,
> dan beralihlah kepada apa yang engkau mampu.

Ia mengambil, bila mungkin, sebagian dari umumnya ilmu. Diriwayatkan dari Amirul Mukminin: "Ilmu itu terlalu banyak untuk dihitung, maka ambillah dari setiap ilmu yang terbaiknya." Ia tidak melampaui satu bab ke bab lain dan tidak naik kepada suatu ilmu sebelum mengokohkan yang pertama, sebab berjejalnya ilmu dalam kalbu merugikan pemahaman.

Perhatiannya terhadap mutu apa yang ia hasilkan lebih besar daripada memperbanyak apa yang ia ketahui. Dikatakan: "Pohon tidak tercela karena sedikit buahnya bila buahnya bermanfaat."[^p82][^d43]

Ia mengunci atas dirinya apa yang telah ia kuasai agar tidak lepas, sebab penyakit ilmu adalah lupa. Al-Hasan berkata: "Kekanglah jiwa-jiwa ini, karena ia selalu ingin menjulang; dan asahlah ia, karena ia cepat usang."

Ia tidak memusuhi ilmu yang tidak ia ketahui. Dikatakan: "Manusia adalah musuh apa yang tidak mereka ketahui." Allah Ta'ala berfirman: *"Bahkan yang sebenarnya, mereka mendustakan apa yang mereka belum mengetahuinya dengan sempurna"* (Yunus: 39).

Ia tidak peduli dengan kepayahan yang menimpanya. Permata-permata yang mulia tidak dicapai kecuali dengan mempertaruhkan diri; dan ilmu tidak akan memberimu sebagiannya sampai engkau memberinya seluruh dirimu, dan bila engkau telah memberinya seluruh dirimu, pemberiannya kepadamu atas sebagiannya pun masih belum pasti.

Ia tidak membebani dirinya melebihi kemampuannya, dengan memperhatikan sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Sesungguhnya orang yang memaksa tunggangannya hingga terputus di jalan, tidak ada jarak yang ia tempuh dan tidak ada punggung tunggangan yang ia sisakan,"* dan ucapan Umar: "Dirimu adalah tungganganmu; bila engkau berlemah lembut kepadanya, ia sanggup memikul; dan bila engkau memaksanya, ia terputus di jalan."[^d44]

Ia melindungi dan mengistirahatkan jiwanya bila ia khawatir akan kejemuannya. Muawiyah berkata: "Setiap jiwa memiliki kejemuan, maka lindungilah ia." Dikatakan: "Istirahatkanlah kalbu, niscaya ia menampung zikir; kalbu bila dipaksa menjadi buta."

Ia tidak merasa enggan bertanya tentang apa yang tidak ia ketahui. Daghfal ditanya: "Dengan apa engkau memperoleh ilmu ini?" Ia menjawab: "Dengan lisan yang banyak bertanya dan kalbu yang banyak berpikir." Amirul Mukminin berkata: "Ilmu adalah perbendaharaan, dan kuncinya adalah bertanya."

Ia tidak merasa enggan belajar di masa tua sebagaimana di masa muda. Seorang bijak ditanya: "Apakah pantas bagi orang tua untuk belajar?" Ia menjawab: "Jika kebodohan buruk baginya, ilmu baik baginya." Yang lain ditanya: "Kapan belajar pantas bagi manusia?" Ia menjawab: "Selama hidup pantas baginya."

Ia wajib menulis apa yang ia dengar dari hal-hal yang belum ia ketahui. Dikatakan: "Ikatlah ilmu dengan tulisan." Dikatakan pula: "Ilmu adalah bijih emas; jadikanlah kitab-kitab pelindungnya dan pena-pena penampungnya." Tetapi ia tidak mencukupkan diri dengan tulisan sampai dadanya menyimpan apa yang baik darinya. Tidak ada kebaikan dalam ilmu yang tidak menyeberang bersamamu ke lembah, tidak hadir bersamamu, tidak masuk bersamamu ke pemandian, dan tidak melintas bersamamu ke majelis. Siapa yang ilmunya di dalam keranjangnya, sedikit hujahnya terhadap lawan dan banyak kebutuhannya kepada kitab.

Ia wajib tidak mencari suatu macam ilmu dari yang bukan genusnya, seperti mencari hukum-hukum fikih dari nahwu atau hukum-hukum kedokteran dari fikih; siapa yang mencari sesuatu bukan dari tempatnya tidak akan mendapatkan yang dicarinya.

Kekeliruan seorang pelaku suatu ilmu tidak boleh membawanya untuk menghukumi rusaknya ilmu itu dan meninggalkan manfaatnya, seperti yang dilakukan orang awam: bila mereka mendapati seorang dokter atau ahli nujum keliru dalam hukumnya, mereka merendahkan kedokteran dan ilmu nujum. Ia wajib menilai sehat dan sakitnya setiap keahlian dengan apa yang menunjukkannya pada zatnya. Pelakunya tidak menunjukkan kelemahan keahlian itu, sebab tidak ada hubungan di antara keduanya selain bahwa ia menampilkan keahlian itu dengan mengerjakannya, adakalanya dengan jujur dan adakalanya dengan dusta.[^d45]

Hak orang yang unggul dalam suatu ilmu ialah tidak menganggap banyak ilmunya bila dibandingkan dengan ilmu itu sendiri, tetapi hanya bila dibandingkan dengan pengetahuannya sendiri tentang bidang yang ia tekuni.[^p83] Al-Hasan menyebut firman Allah Ta'ala: *"sedangkan kamu tidak diberi pengetahuan melainkan sedikit"* (al-Isra': 85), lalu berkata: "Setiap orang alim menyangka ilmunya banyak." Ia menganggap dangkal akal Adi bin al-Riqa' dalam ucapannya:

> Aku telah berilmu hingga aku tak lagi bertanya kepada seorang pun
> tentang satu ilmu pun untuk menambahnya,

sampai-sampai seorang ulama berkata: "Aku ingin melihatnya, menamparnya, menjewer telinganya, dan membawanya melewati satu ilmu demi satu ilmu, lalu memperlihatkan kepadanya bahwa ia tidak mengetahui sesuatu pun darinya selain syair, yang dalam hal itu pun ada orang alim yang menyamainya, bahkan mengunggulinya."

Haknya ialah berjalan dalam mencari ilmu dengan meneladani kebenaran, bukan dengan bertaklid kepada tokoh-tokoh dan para pendahulu, dan bukan untuk mencari kepemimpinan. Amirul Mukminin Ali, semoga Allah memuliakan wajahnya, berkata: *"Wahai Harits, kebenaran telah dikaburkan bagimu. Kebenaran tidak dikenali dengan orang-orang; kenalilah kebenaran, niscaya engkau mengenal ahlinya."* Allah Ta'ala berfirman mencela taklid: *"Dan demikian juga ketika Kami mengutus seorang pemberi peringatan sebelum engkau (Muhammad) dalam suatu negeri, orang-orang yang hidup mewah (di negeri itu) selalu berkata, Sesungguhnya kami mendapati nenek moyang kami menganut suatu (agama) dan sesungguhnya kami sekadar pengikut jejak-jejak mereka. (Rasul itu) berkata, Apakah (kamu akan mengikutinya juga) sekalipun aku membawa untukmu (agama) yang lebih baik daripada apa yang kamu peroleh dari (agama) yang dianut nenek moyangmu. Mereka menjawab, Sesungguhnya kami mengingkari (agama) yang kamu diperintahkan untuk menyampaikannya"* (az-Zukhruf: 23-24). Beliau, semoga salam atasnya, bersabda mencela orang yang mencari ilmu demi kepemimpinan: *"Siapa yang mempelajari ilmu untuk berbangga di hadapan para ulama, berbantah dengan orang-orang bodoh, mengambil (harta) dari para penguasa, atau memalingkan wajah manusia kepadanya, ia masuk neraka."*[^p84]

Hendaklah tujuannya adalah amal. Nabi, semoga salam atasnya, berdoa: *"Ya Allah, aku berlindung kepada-Mu dari ilmu yang tidak bermanfaat, kalbu yang tidak khusyuk, dan jiwa yang tidak kenyang."*

Adapun yang diperhitungkan dalam kaitannya dengan guru ialah sebagai berikut.

Hendaklah ia mengagungkan dan mencintai gurunya. Iskandar ditanya: "Manakah yang lebih engkau cintai, gurumu atau ayahmu?" Ia menjawab: "Guruku, sebab ia sebab kehidupanku yang kekal, sedang ayahku sebab kehidupanku yang fana." Umar, semoga Allah meridainya, berkata: "Hormatilah orang yang kalian belajar darinya."

Hendaklah ia tidak merasa enggan terhadap orang yang ia belajar darinya. Beliau, semoga salam atasnya, bersabda: *"Hikmah adalah barang hilang orang mukmin; di mana pun mereka menemukannya, hendaklah mereka mengikatnya."* Seorang bijak terlihat menulis sesuatu dari seorang banci, lalu ia dicela karenanya. Ia berkata: "Permata yang berharga tidak tercemar oleh dangkalnya orang yang menawarkannya dan rendahnya penjualnya." Seorang bijak berkata: "Aku belajar dari segala sesuatu yang terbaiknya, bahkan dari babi kebiasaannya bangun pagi untuk keperluannya, dari kucing kelembutannya dalam meminta, dan dari anjing kesetiaannya kepada pemiliknya."

Hendaklah ia tidak merasa enggan terhadap sikap keras yang menimpanya dari gurunya dan pelayanan yang ia berikan kepadanya. Dikatakan: "Bila engkau diatur untuk kebaikan, bersikaplah seperti orang sakit terhadap dokter; sebab orang yang memberimu minum yang pahit agar engkau sehat lebih baik daripada orang yang menuangkan ke mulutmu yang manis agar engkau sakit." Hendaklah ia tidak bertanya kepadanya untuk menyulitkan. Dikatakan: "Bila engkau duduk bersama orang alim, bertanyalah kepadanya untuk memahami, bukan untuk menyulitkan."[^d46]

### Nasihat Guru yang Tulus {.judul-pasal}

Adapun guru yang tulus, haknya ialah sebagai berikut.

Ia memandang menyebarkan ilmu sebagai kewajiban. Beliau, semoga salam atasnya, bersabda: *"Siapa yang mengetahui suatu ilmu lalu menyembunyikannya, Allah Ta'ala akan mengekangnya pada hari Kiamat dengan kekang dari api,"* dan bersabda: *"Janganlah kalian menahan ilmu, sebab dalam hal itu ada kerusakan agama kalian,"* lalu membaca firman Allah: *"Sungguh, orang-orang yang menyembunyikan apa yang telah Kami turunkan berupa keterangan-keterangan dan petunjuk"* (al-Baqarah: 159).

Ia memperlakukan setiap murid sesuai dengan ilmunya, tidak mengutamakan yang kaya atas yang fakir. Abu al-'Aliyah berkata tentang firman Allah: *"Dan janganlah kamu memalingkan wajah dari manusia (karena sombong)"* (Luqman: 18): maknanya hendaklah yang fakir dan yang kaya sama di sisimu dalam ilmu. Tetapi ia wajib tidak menzalimi ilmu dengan meletakkannya bukan pada tempatnya. Dikatakan: "Janganlah kalian meletakkan hikmah pada yang bukan ahlinya, sehingga kalian menzaliminya; dan janganlah menahannya dari ahlinya, sehingga kalian menzalimi mereka."

Ia memilih untuk setiap murid apa yang sesuai dengan tabiatnya. Salah seorang murid Aristoteles ditanya tentang suatu ilmu yang tidak layak bagi penanyanya, lalu ia berkata: "Setiap tanah ada tanamannya dan setiap bangunan ada fondasinya; ilmu ini tidak dapat dicapai dengan tangga-tangga tabiatmu."[^p85]

Ia menyusun apa yang ia ajarkan dengan susunan yang memudahkan murid mengidraknya. Ia tidak bersikap kasar kepada murid sehingga menjadi keras, dan tidak terlalu lunak sehingga diremehkan. Ia memperhatikan ucapan seorang bijak: "Bila engkau dikunjungi seseorang yang ingin bertambah ilmunya, janganlah bersikap seperti musuhnya, tetapi bersikaplah seperti dokter terhadap orang sakit."

Pendapat-pendapatnya benar; ia tidak menjajakan kebatilan kepada muridnya, melainkan tujuannya membela kebenaran dan melimpahkan kebaikan, bukan mengalahkan lawan dan memperoleh harta.[^d47]

Ia tidak merasa enggan, bila ditanya tentang apa yang tidak ia ketahui, untuk berkata: "Aku tidak tahu", dengan meneladani Malik bin Anas, imam negeri hijrah, semoga Allah meridainya. Ia ditanya tentang beberapa masalah lalu berkata: "Aku tidak tahu." Ia dicela karena itu, lalu berkata: "Para malaikat tidak malu untuk berkata: *'Mahasuci Engkau, tidak ada yang kami ketahui selain apa yang telah Engkau ajarkan kepada kami'* (al-Baqarah: 32)." Dikatakan kepada Abu Amr: "Buruk bagi orang sepertimu untuk berkata aku tidak tahu." Ia menjawab: "Lebih buruk dari itu bila aku berkata lalu keliru."

Inilah himpunan apa yang dimaksud untuk dijelaskan dalam risalah ini. Maka hendaklah Ustaz merenungkannya, semoga Allah melimpahkan akal kepadanya, menjaganya dengan kedudukan keutamaan, dan menjadikannya termasuk orang yang lebih banyak memandang dengan mata adabnya daripada dengan mata nasabnya.[^p86]

[^r-tab]: **Tabiat** (*ṭabʿ*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 76 (`m-tab`, *al-Mufradāt*) dan no. 77 (`k-tab`, *Kashshāf*), dan terjemahan *Tafṣīl*, catatan no. 56 (`r-tab`): dalam *al-Mufradāt*, *ṭabʿ* ialah mencetak sesuatu dengan rupa tertentu, seperti mencetak mata uang dan stempel. Di sini *ṭabʿ* dipakai dalam arti khusus: daya menerima rupa makna-makna, seperti lilin menerima cetakan stempel.

[^d41]: CD: *Al-Dharīʿa*, Pasal Kedua, "Hal-Hal yang Mengikuti Akal", memberi definisi-definisi yang lebih panjang dan sebagian berbeda: *dhakāʾ* ialah "ketangkasan dalam urusan dan cepatnya memutus kebenaran", juga dari *dhakat al-nār*; *dhihn* ialah daya jiwa yang siap memperoleh pendapat; pemahaman ialah "pengantar akal"; ingatan ialah "adanya sesuatu di dalam kalbu atau di lisan"; dan "tetapnya rupa sesuatu di dalam kalbu disebut *ḥifẓ*". Di sini daya-daya itu disusun sebagai tahap-tahap berurutan: menerima, menghafal, memahami, memikirkan, mengingat. Tentang istilah-istilah ini, lihat pula nota kaki *al-Dharīʿa* no. 114 (`m-fahm`), no. 115 (`m-hifz`), no. 160 (`k-dhaka`), dan no. 168 (`m-dhikr`).

[^p78]: CP: Penyunting mencatat bahwa naskah berlubang di tempat ini dan melengkapi dua kata. Kalimat ini agaknya menyatakan bahwa kekayaan yang sejati adalah kekayaan jiwa, dan harta yang melebihi kebutuhan membuat pemiliknya fakir karena menyibukkannya.

[^p79]: CP: Ucapan pertama adalah aforisme pembuka dalam *Aforisme* (*al-Fuṣūl*) Hippokrates: "Hidup itu singkat, keahlian itu panjang, kesempatan itu sempit, percobaan itu berbahaya, dan keputusan itu sulit", yang terkenal dalam terjemahan Arab dengan bunyi "umur itu pendek dan keahlian itu panjang".

[^p80]: CP: Edisi tahkik membaca *al-ʿulūm al-ẓāhira* ("ilmu-ilmu yang tampak"), dan penyunting menjelaskannya dengan susah payah. Kami membacanya *al-ṭāhira* ("yang suci"), pasangan *al-qulūb al-ṭāhira* ("kalbu-kalbu yang suci").

[^d42]: CD: Syarat ini sama dengan syarat pertama dalam *al-Dharīʿa*, Pasal Kedua, "Apa yang Wajib Diupayakan Murid": "menyucikan jiwanya dari akhlak yang buruk, sebagaimana tanah dibersihkan dari tumbuhan yang buruk untuk ditaburi benih. Telah dijelaskan bahwa yang suci hanya berdiam di rumah yang suci." Seluruh bagian tentang murid dan guru dalam pasal ini sejajar dengan dua bahasan berurutan dalam *al-Dharīʿa*, "Apa yang Wajib Diupayakan Murid" dan "Apa yang Wajib Diupayakan Guru terhadap Murid-Muridnya", serta bahasan "Anjuran Mengambil Bekal Secukupnya dari Setiap Ilmu"; di sini uraiannya lebih rinci dan disusun sebagai daftar.

[^p81]: CP: Edisi tahkik membaca *an yatakhaṭṭā mā tayassara min bulūghihi* ("melewati apa yang mudah dicapai"), yang membalik maksud bait sesudahnya. Kami membacanya *mā taʿassara* ("apa yang sulit dicapai"). Bait ini milik ʿAmr bin Maʿdīkarib.

[^p82]: CP: Edisi tahkik membaca *al-shajara lā yuthnīhā al-ḥaml* ("pohon tidak dibengkokkan oleh muatannya"); kami mengikuti bunyi ucapan yang sama dalam *al-Dharīʿa* (lihat catatan d43): *lā yashīnuhā qillat al-ḥaml* ("tidak tercela karena sedikit buahnya").

[^d43]: CD: Tiga anjuran terakhir sejalan dengan *al-Dharīʿa*, Pasal Kedua, "Anjuran Mengambil Bekal Secukupnya dari Setiap Ilmu dan Mencukupkan Diri dengannya": ucapan Ali ("Ilmu itu banyak, maka ambillah dari setiap sesuatu yang terbaiknya"), larangan melampaui satu cabang ilmu sebelum mengokohkannya ("sebab berjejalnya ilmu di pendengaran menyesatkan pemahaman"), dan ucapan "pohon tidak tercela karena sedikit buahnya bila buahnya bermanfaat". Di sana pula: "banyak orang kehilangan kesampaian karena meninggalkan pokok-pokok".

[^d44]: CD: Hadis ini dikutip dalam *al-Dharīʿa*, Pasal Ketiga, "Macam-Macam Kelezatan dan Rinciannya", untuk menjelaskan "kelahapan terhadap ilmu" (*naham fī al-ʿilm*): "seseorang membebani dirinya dengan apa yang tidak sanggup dipikul daya-dayanya sehingga ia terputus di tengah jalan". Terjemahan hadis di atas mengikuti redaksi itu. Dalam ucapan Umar, *tabiʿtahā* dibaca *ʿannaftahā* ("memaksanya"), sesuai maksudnya.

[^d45]: CD: Anjuran ini sama dengan *al-Dharīʿa*, Pasal Kedua, "Apa yang dengannya Keutamaan Ilmu Diketahui": "Tidak semestinya suatu ilmu dihukumi rusak karena kekeliruan yang terjadi dari para ahlinya, seperti perbuatan orang awam … Itulah kebiasaan mereka dalam kedokteran dan ilmu nujum; mereka menilai keahlian dengan pelakunya." Di sana pula dikutip ucapan Ali kepada al-Harits, yang di sini diletakkan dalam anjuran tentang taklid; terjemahannya mengikuti redaksi terjemahan *al-Dharīʿa*.

[^p83]: CP: Kalimat ini kurang jelas dalam edisi tahkik (*an lā yastakthira ʿilma nafsihi bi-l-iḍāfa ilā al-ʿilm fī nafsihi bal bi-l-iḍāfa ilā ʿilmihi alladhī yataʿāṭāhu*). Maksudnya agaknya: bila ia mengukur pengetahuannya dengan luasnya ilmu itu sendiri, ia akan melihatnya sedikit; ia hanya tampak banyak bila diukur dengan dirinya sendiri. Contoh Adi bin al-Riqa' sesudahnya menunjukkan kesalahan mengukur ilmu dengan diri sendiri.

[^p84]: CP: Dalam edisi tahkik tercetak "untuk berhias, ia masuk neraka" di tengah hadis; penyunting menilai kata-kata itu sisipan penyalin, dan kami mengikutinya dengan meletakkan "ia masuk neraka" di akhir.

[^d46]: CD: Jawaban Iskandar dikutip pula dalam *al-Dharīʿa*, Pasal Kedua, "Apa yang Wajib Diupayakan Guru terhadap Murid-Muridnya"; terjemahannya mengikuti redaksi itu. Perumpamaan murid sebagai orang sakit terhadap dokter juga terdapat dalam *al-Dharīʿa*, "Apa yang Wajib Diupayakan Murid": "Sebagaimana hak orang sakit ialah menyerahkan dirinya kepada dokter yang tulus … demikian pula hak murid, bila ia mendapati guru yang tulus, ialah menaati perintahnya." Di sini perumpamaan itu dipakai dua kali: untuk sikap murid terhadap guru, dan untuk sikap guru terhadap murid.

[^p85]: CP: Edisi tahkik membaca *li-kull tarkība gharsun*; penyunting mencatat kata itu tidak jelas dan menduganya "pohon". Kami membacanya *li-kull turba gharsun* ("setiap tanah ada tanamannya"), yang sejajar dengan "setiap bangunan ada fondasinya".

[^d47]: CD: *Al-Dharīʿa*, Pasal Kedua, "Apa yang Wajib Diupayakan Guru terhadap Murid-Muridnya", menekankan bahwa guru tidak boleh mengharapkan imbalan: "siapa yang menjual ilmu dengan harta benda dunia telah menentang Allah Ta'ala dalam hukum-Nya", sebab ilmu dilayani dan tidak melayani. Anjuran tentang menempatkan hikmah pada ahlinya dan berbicara sesuai kadar pemahaman juga terdapat dalam bahasan sesudahnya, "Wajibnya Mencegah Orang-Orang Bodoh dari Hakikat Ilmu", dengan ucapan Isa putra Maryam: "Janganlah kalian meletakkan hikmah pada yang bukan ahlinya, sehingga kalian menzaliminya"; terjemahan ucapan itu di atas mengikuti redaksi tersebut. Dalam kalimat "ia tidak menjajakan kebatilan", kata *yurabbiʿ* dalam teks dibaca *yurawwij*.

[^p86]: CP: Kata kerja *yarmuqu* ("memandang") dalam doa penutup ini menguatkan bacaan *yarmuquhā* yang kami usulkan dalam Risalah Pertama, Bab Pertama (catatan p7).

# Risalah Ketiga {.kitab-ke}

# Tingkatan Ilmu-Ilmu dan Amal-Amal {.judul-kitab}

[Dengan nama Allah Yang Maha Pengasih, Maha Penyayang]{.basmalah}

Dan hanya kepada-Nya kami memohon pertolongan. Segala puji bagi Allah dengan sebenar-benar pujian, dan selawat-Nya atas junjungan kami Muhammad, Nabi dan hamba-Nya, beserta keluarganya.[^p87]

Sesungguhnya perbuatan orang-orang mukmin yang paling mulia di antara sesama mereka adalah saling mencintai dan saling akrab. Sebab cinta di antara manusia lebih utama daripada keadilan: cinta di antara mereka tidak terlepas dari keadilan, sedang keadilan terkadang terlepas dari cinta.[^p88] Karena itu salah seorang peneliti berkata: "Keadilan di alam ini adalah pengganti cinta, yang dipakai di tempat cinta tidak ada."[^d48] Karena itu pula, ketika Umar, semoga Allah meridainya, berkata kepada pembunuh saudaranya, Zaid bin al-Khaththab: "Aku tidak mencintaimu sesudah engkau membunuh saudaraku," orang itu menjawab: "Maka (berlakulah) adil, bila tidak ada cinta."[^s8] Atas makna itu pula peribahasa yang terkenal: "Kalau tidak menjadi istri kesayangan, setidaknya tidak lalai."

Cinta adalah salah satu hal yang dengannya Allah memuliakan syariat ilahi dan agama yang lurus, dan Dia menjadikannya tatanan bagi keduanya. Dia menganugerahkannya kepada Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, dan membesarkan (nikmat) keakraban orang-orang mukmin dengan firman-Nya: *"Walaupun kamu menginfakkan semua (kekayaan) yang berada di bumi, niscaya kamu tidak dapat mempersatukan hati mereka"* (al-Anfal: 63). Allah Ta'ala berfirman: *"Muhammad adalah utusan Allah, dan orang-orang yang bersama dengan dia bersikap keras terhadap orang-orang kafir, tetapi berkasih sayang sesama mereka"* (al-Fath: 29). Cukuplah sebagai keutamaannya bahwa Dia berfirman: *"maka kelak Allah akan mendatangkan suatu kaum, Dia mencintai mereka dan mereka pun mencintai-Nya"* (al-Ma'idah: 54): Dia menjadikan cinta di antara Dia dan hamba-hamba-Nya yang saleh, dan mendahulukan cinta-Nya kepada mereka atas cinta mereka kepada-Nya.[^p89]

Penduduk satu negeri, bahkan pemeluk satu agama, bila saling mencintai, mereka saling menyambung; bila saling menyambung, mereka saling menolong; bila saling menolong, mereka bekerja; bila bekerja, mereka memakmurkan; dan bila memakmurkan, mereka menjadi banyak dan berjaya.[^d49]

Untuk menumbuhkan cinta, Allah memerintahkan berkumpul dan melarang bercerai-berai. Dia berfirman: *"Dan berpegangteguhlah kamu semuanya pada tali (agama) Allah, dan janganlah kamu bercerai berai"* (Ali 'Imran: 103), dan berfirman: *"Dia (Allah) telah mensyariatkan kepadamu agama yang telah diwasiatkan-Nya kepada Nuh dan apa yang telah Kami wahyukan kepadamu (Muhammad) dan apa yang telah Kami wasiatkan kepada Ibrahim, Musa dan Isa yaitu tegakkanlah agama (keimanan dan ketakwaan) dan janganlah kamu berpecah belah di dalamnya"* (asy-Syura: 13). Beliau, semoga salam atasnya, bersabda: *"Seandainya aku diundang kepada (hidangan) kaki kambing, niscaya aku datangi,"* dan itu beliau lakukan agar diteladani dalam keakraban, bukan untuk mendorong kerakusan dalam makanan. Beliau bersabda: *"Orang mukmin ialah yang bergaul dengan manusia dan bersabar atas gangguan mereka,"* bersabda: *"Orang mukmin bagi orang mukmin lainnya seperti bangunan yang sebagiannya menguatkan sebagian yang lain,"* dan bersabda: *"Orang-orang mukmin seperti satu tubuh; bila sebagiannya sakit, seluruhnya ikut merasakan."*

Untuk mendorong keakraban, agama ilahi mensyariatkan berkumpulnya penduduk satu kampung di masjid-masjid untuk salat lima waktu; berkumpulnya penduduk satu negeri di satu masjid jami' setiap pekan; berkumpulnya penduduk satu wilayah, dari kota dan pedesaannya, setiap tahun pada hari-hari raya di lapangan; dan berkumpulnya penduduk negeri-negeri dan desa-desa yang berjauhan, sekali seumur hidup, di Makkah untuk haji dan umrah. Tidak dicukupkan dari mereka untuk menegakkan ibadah-ibadah ini sendiri-sendiri; semua itu agar keakraban mereka menjadi kokoh dengan berkumpul.[^d50]

Yang kumaksud dengan cinta di sini tidak lain adalah cinta yang dituntut oleh keutamaan, bukan yang dituntut oleh kelezatan atau manfaat, atau yang lahir dari keduanya. Sebab itu semua adalah kasih sayang yang datang tiba-tiba, penuh celaan, dan cepat lenyap; yang kekal hanyalah cinta karena keutamaan, yang tetap di dunia dan di akhirat. Kepada keduanya (yang lenyap dan yang kekal) Allah Ta'ala memaksudkan firman-Nya: *"Teman-teman karib pada hari itu saling bermusuhan satu sama lain, kecuali mereka yang bertakwa"* (az-Zukhruf: 67).[^p90]

Cintaku kepada Ustaz termasuk jenis cinta karena keutamaan, yang diarahkan oleh syariat dan dituntut oleh agama.[^s9] Beliau, semoga Allah melanggengkan taufik-Nya, berkobar dan menyala marahnya karena suatu ucapan yang diceritakan kepadanya tentang diriku tidak sebagaimana mestinya, dan beliau menyampaikan kepada sebagian teman majelisku tentang diriku apa yang sesuai dengan kebebasan dan keutamaannya. Tidak lama kemudian hal itu diselidiki, dan ternyata ia tidak berakar, tidak bercabang, dan tidak berpangkal.

Dalam menyingkap hal itu, aku hanya bermaksud dua hal. Pertama, memberitahunya agar tidak bersandar dalam kabar-kabar kepada orang yang tidak menjaga ucapannya. Kedua, (mengikuti) seorang saleh yang dikatakan kepadanya: "Si fulan berburuk sangka kepadamu; biarkanlah ia, agar timbanganmu menjadi berat karenanya." Ia menjawab: "Aku tidak suka timbanganku menjadi berat dengan dosa-dosa saudara-saudaraku."

Tetapi lama sekali keherananku terhadap syekh yang utama itu, semoga Allah menjaganya, karena beberapa hal yang kulihat darinya.[^s10]

**Pertama**: caranya mengingkari aku mengucapkan lafal "daya" (*quwwa*), dengan alasan bahwa lafal ini dipakai oleh para filsuf, dan agar aku mengucapkan "kuasa" (*qudra*) sebagai gantinya; seakan-akan ia tidak mengetahui perbedaan di antara keduanya dalam pemakaian orang awam, apalagi orang-orang khusus.[^r-quwa][^m-qudra]

**Kedua**: tuduhan-tuduhan, sindiran-sindiran, bahkan pernyataan-pernyataannya yang terang, yang ia lontarkan untuk mencari muka kepada para pengikut dan pendukungnya, dengan merendahkan dan menjatuhkan diriku.

**Ketiga**: bertambahnya ucapan demi ucapan darinya ketika ia melihat dariku kesabaran dan ketenangan dalam menanggapinya; sedang aku tidak melihat ada salahnya dan ruginya menanggung (ucapan) seorang syekh yang mulia atas diriku, selama tidak mendatangkan aib yang sebenarnya bagiku.[^p91] Sufyan bin Dinar berkata: "Sejak aku mengenal mereka, celaan mereka tidak menyakitiku dan pujian mereka tidak menggembirakanku."[^p92]

Yang lebih mengherankan dari itu ialah dugaannya, atau perkiraannya, bahwa di balik ilmu kalam tidak ada ilmu yang dipedulikan Allah, sebagaimana dikatakan: "Di balik Abbadan tidak ada desa lagi." Jauh, jauh sekali! Di balik itu ada ladang-ladang dan tanah-tanah, *"dan (begitu pula) tanah yang belum kamu injak"* (al-Ahzab: 27); *"Dan karena mereka tidak mendapat petunjuk dengannya maka mereka akan berkata, Ini adalah dusta yang lama"* (al-Ahqaf: 11).

> Tinggalkanlah rampasan yang diteriakkan di sekeliling kemah-kemahnya,
> tetapi ceritakanlah kepadaku, bagaimana kisah unta-unta tunggangan itu?[^p93]

Maksudku dalam risalah ini ialah menjelaskan kepada Ustaz, semoga Allah melanggengkan pertolongan-Nya kepadanya, tingkatan-tingkatan syariat dan amal-amalnya secara ringkas, agar ia mengetahui darinya dari mana orang yang memulai harus memulai dan ke mana ia berakhir; apakah tujuannya adalah keahlian kalam, sekalipun ada yang berkata demikian atau meriwayatkannya dari orang yang lebih luas pengetahuannya; serta tingkatan-tingkatan yang dengannya manusia mencapai puncak dalam keutamaan sehingga ia dekat kepada Penciptanya, dan tingkatan-tingkatan yang dengannya manusia mencapai puncak dalam keburukan sehingga ia jauh dari-Nya sejauh-jauhnya. Kita memohon kepada Allah Ta'ala agar memudahkan jalan kita dengan menyucikan jiwa kita, untuk meraih limpahan taufik-Nya, dengan rahmat-Nya.

### Tingkatan Ilmu-Ilmu Agama {.judul-pasal}

Ilmu-ilmu agama, secara ringkas, ada empat.[^p94]

**Pertama**: ilmu yang diperoleh tanpa perantara. Sebagian orang menamainya akal bawaan, para ahli kalam menamainya ilmu niscaya (*ḍarūrī*), dan para ahli ibadah menamainya fitrah, yang diisyaratkan firman Allah Ta'ala: *"(sesuai) fitrah Allah disebabkan Dia telah menciptakan manusia menurut (fitrah) itu"* (ar-Rum: 30), dan firman-Nya: *"Dan (ingatlah) ketika Tuhanmu mengeluarkan dari sulbi anak cucu Adam keturunan mereka"* (al-A'raf: 172).[^r-fitra]

**Kedua**: ilmu yang diperoleh dengan pertimbangan dan penalaran, yaitu mengenal barunya unsur-unsur melalui kaidah-kaidah, menetapkan keberadaan (*inniyya*) Sang Pencipta, Mahaagung pujian-Nya, dan menetapkan keesaan-Nya.

**Ketiga**: ilmu yang diidrak dari arah kenabian dengan bantuan akal. Ia memiliki dua cabang: keyakinan dan amal. Yang berkaitan dengan keyakinan ialah yang tujuannya meyakini kebenaran di dalamnya, bukan kebatilan; itulah yang diberitakan dalam firman-Nya: *"Barangsiapa ingkar kepada Allah, malaikat-malaikat-Nya, kitab-kitab-Nya, rasul-rasul-Nya, dan hari kemudian, maka sungguh, orang itu telah tersesat sangat jauh"* (an-Nisa': 136), dan dalam riwayat dari Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, ketika Jibril, semoga salam atasnya, bertanya kepadanya tentang iman. Beliau menjawab: *"Engkau beriman kepada Allah, malaikat-malaikat-Nya, kitab-kitab-Nya, rasul-rasul-Nya, kebangkitan sesudah mati, dan kepada takdir, baik dan buruknya, dari Allah Ta'ala."* Jibril bertanya: *"Bila aku melakukan itu, apakah aku mukmin?"* Beliau menjawab: *"Ya."* Yang berkaitan dengan amal ialah yang tujuannya diyakini lalu diamalkan sesuai dengannya. Ia ada dua macam: fikih, dan ilmu akhlak, yang oleh kaum sufi dinamai nusuk dan zuhud, yaitu tahapan-tahapan jiwa menuju kesuciannya, penjernihan kalbu dari kotoran, mematikan syahwat, dan menundukkan hawa nafsu.

**Keempat**: ilmu-ilmu hakikat, yang disebut juga ilmu-ilmu anugerah (*mawhiba*), yaitu tersingkapnya keyakinan (*yaqīn*).[^r-yaqin]

Ilmu anugerah tidak dapat dicapai kecuali dengan mengamalkan ilmu-ilmu lahir, banyak beribadah, dan menyucikan jiwa dari kotoran dan noda. Mustahil orang yang belum membersihkan kalbunya dan belum menyucikan jiwanya berharap mencapainya. Kalbu itu seperti wadah; selama wadah tidak disucikan, cahaya ilahi tidak terwujud di dalamnya. Itulah yang difirmankan Allah Ta'ala: *"Maka apakah orang-orang yang dibukakan hatinya oleh Allah untuk (menerima) agama Islam lalu dia mendapat cahaya dari Tuhannya (sama dengan orang yang hatinya membatu)?"* (az-Zumar: 22). Jika sebagian ahli debat mengingkarinya dengan berkata bahwa kami tidak mengidraknya dan tidak mengenalnya, ia tidak jauh (dari benar) dalam pengakuannya:

> Dapatkah mata kelelawar melihat matahari?

Tetapi jika ia mengingkari adanya hal itu sama sekali, ia terikat dan dikalahkan oleh sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Siapa yang mengamalkan apa yang ia ketahui, Allah mewariskan kepadanya ilmu tentang apa yang belum ia ketahui,"* dan oleh riwayat dari Amirul Mukminin, semoga Allah meridainya: "Hikmah berkata: Siapa yang mencariku tetapi tidak mampu mencapaiku, hendaklah ia mengamalkan yang terbaik dari apa yang ia ketahui dan meninggalkan yang terburuk dari apa yang ia ketahui." Ketika ia, semoga salam atasnya, ditanya: "Adakah padamu ilmu dari Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, yang tidak sampai kepada selainmu?" ia menjawab: "Tidak, kecuali Kitab Allah dan sisa (isi) lembarannya."[^p95] Maka terkadang Allah memberikannya kepada siapa yang Dia kehendaki; bahkan ada hujah untuk itu dalam firman Allah Ta'ala: *"Dan orang-orang yang mendapat petunjuk, Allah akan menambah petunjuk kepada mereka dan menganugerahi ketakwaan mereka"* (Muhammad: 17). Dia menjelaskan bahwa mereka dianugerahi tambahan petunjuk dan pemberian takwa karena mereka telah mendapat petunjuk.

Maka orang-orang yang memperoleh ilmu yang diusahakan, seperti kalam, fikih, dan semacamnya, adalah para ulama; orang-orang yang memperoleh ilmu akhlak lalu mengamalkannya adalah para hakim (*ḥukamāʾ*); dan orang-orang yang memperoleh ilmu anugerah adalah para pembesar (*kubarāʾ*). Karena itu Nabi, semoga salam atasnya, bersabda: *"Bertanyalah kepada para ulama, duduklah bersama para pembesar, dan bergaullah dengan para hakim."*[^p96] Beliau bersabda demikian karena bertanya kepada ulama membawamu kepada pengenalan tauhid Allah secara pasti dan kepada hukum-hukum syariat; duduk bersama para hakim membawamu kepada hikmah dan kepada pengenalan aib-aib jiwa dan kehalusan warak; dan bergaul dengan para pembesar mematikan darimu setiap penyakit dan memperlihatkanmu kerajaan langit.

Kepada hal inilah Allah Ta'ala membangkitkan kerinduan kita dengan firman-Nya "agar kamu dapat mengambil pelajaran", ketika Dia berfirman: *"Sesungguhnya Allah menyuruh (kamu) berlaku adil dan berbuat kebajikan, memberi bantuan kepada kerabat, dan Dia melarang (melakukan) perbuatan keji, kemungkaran dan permusuhan. Dia memberi pengajaran kepadamu agar kamu dapat mengambil pelajaran"* (an-Nahl: 90). Seandainya mengambil pelajaran (*tadhakkur*) ini bukan perkara yang tidak dapat dicapai dengan mudah, tidak akan disyaratkan atas kita untuk berhias dengan amal-amal ini, yang merupakan himpunan ibadah dan kemuliaan akhlak. Makna-makna yang terkandung dalam ayat ini terkandung pula dalam firman-Nya: *"Dan barangsiapa menyucikan dirinya, sesungguhnya dia menyucikan diri untuk kebaikan dirinya sendiri"* (Fatir: 18), dan firman-Nya: *"Sungguh beruntung orang yang menyucikan diri (dengan beriman)"* (al-A'la: 14).

Pengetahuan jenis ini adalah ucapan yang baik yang kepadanya orang-orang mukmin diberi petunjuk, sebagaimana firman Allah Ta'ala: *"Dan mereka diberi petunjuk kepada ucapan-ucapan yang baik dan diberi petunjuk (pula) kepada jalan (Allah) yang terpuji"* (al-Hajj: 24). Ia adalah cahaya yang disebut dalam firman-Nya: *"Perumpamaan cahaya-Nya, seperti sebuah lubang yang tidak tembus, yang di dalamnya ada pelita besar"* (an-Nur: 35). Dan ia adalah tulisan yang disebut dalam firman-Nya: *"Mereka itulah orang-orang yang dalam hatinya telah ditanamkan Allah keimanan dan Allah telah menguatkan mereka dengan pertolongan yang datang dari Dia"* (al-Mujadilah: 22).

Inilah empat kedudukan, yang sebagiannya tersusun atas sebagian yang lain: dengan pengetahuan-pengetahuan niscaya yang disusun Allah Ta'ala dalam diri kita, kita sampai kepada pengetahuan yang diusahakan; dengan yang diusahakan kita sampai kepada apa yang datang kepada kita dari arah kenabian; dan dengan mengamalkan serta melatih diri dengannya, dan dengan berlindung kepada Allah Ta'ala, kita mengharapkan semisal hakikat-hakikat itu.[^d51]

### Tingkatan Amal-Amal Keagamaan {.judul-pasal}

Sebagaimana ilmu-ilmu agama, secara ringkas, memiliki empat tingkatan yang tersusun satu atas yang lain, demikian pula amal-amal keagamaan.[^p97]

**Pertama**: meninggalkan perbuatan keji atau menjauhi keburukan. Sebab itu jalan menuju perbuatan baik, seperti (fondasi) bagi bangunan: terkadang ada fondasi tanpa bangunan, tetapi tidak ada bangunan tanpa fondasi. Karena itu dikatakan: dengan menjauhi keburukan akhlak kita sampai kepada perolehan keutamaan, dan dengan meninggalkan kekotoran kita mampu melakukan kebaikan-kebaikan. Siapa yang melakukan suatu kebaikan hendaklah ia menjauhi segala yang menyelisihinya; jika tidak, (perbuatannya) belum keluar dari keadaannya sebagai keburukan. Inilah derajat orang-orang yang takut dan tingkatan pertama orang-orang bertakwa.

**Kedua**: melakukan kebaikan-kebaikan, berupa menegakkan kewajiban-kewajiban dan menyertainya dengan sunah-sunah yang dikukuhkan; inilah derajat orang-orang yang berharap.

**Ketiga**: terus-menerus melakukan kebaikan-kebaikan hingga berbuat baik menjadi sesuatu yang lezat bagi manusia, bukan sesuatu yang dipaksakan dan dibenci, sebagaimana sabda Nabi, semoga Allah melimpahkan selawat dan salam kepadanya: *"Dan dijadikan penyejuk mataku dalam salat."* Beliau menamainya "penyejuk mata" karena menganggapnya nikmat.

**Keempat**: tindakan batin manusia, apalagi yang lahir, berada di atas rida Yang Mahabenar; ia menjaga lintasan-lintasan hatinya, memperhatikan pikiran-pikirannya, dan dalam semua keadaannya menyaksikan kerajaan langit dan bumi.

Inilah keadaan yang dilukiskan Haritsah bin Malik ketika Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bertanya kepadanya: *"Bagaimana keadaanmu, wahai Haritsah?"* Ia menjawab: *"Pagi ini aku menjadi mukmin yang sebenar-benarnya."* Beliau bersabda: *"Setiap kebenaran memiliki hakikat; apakah hakikat imanmu?"* Ia menjawab: *"Jiwaku telah berpaling dari dunia, maka aku membuat siangku dahaga dan malamku terjaga; seakan-akan aku melihat Arasy Tuhanku tampak nyata, seakan-akan aku melihat penghuni surga di surga saling mengunjungi, dan penghuni neraka di neraka saling melolong."* Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bersabda: *"Seorang mukmin yang kalbunya diterangi Allah dengan cahaya iman; engkau telah mengenal, maka tetaplah."*[^p98]

Kepada hal itu beliau, semoga salam atasnya, mengingatkan dengan sabdanya: *"Allah berfirman: Tidaklah seorang hamba mendekatkan diri kepada-Ku dengan sesuatu seperti apa yang Aku wajibkan kepadanya. Hamba senantiasa mendekatkan diri kepada-Ku dengan amalan-amalan sunah hingga Aku mencintainya. Bila Aku telah mencintainya, Aku menjadi pendengarannya yang dengannya ia mendengar, penglihatannya yang dengannya ia melihat, dan tangannya yang dengannya ia menggenggam."*

Siapa yang telah sampai kepada kedudukan ini disebut *murīd*, *khalīl*, dan *ḥabīb*, sesuai tingkatan mereka. Dalam sebagian kitab para bijak tertulis bahwa Allah Ta'ala, bila mencintai seorang hamba, memeliharanya sebagaimana seorang sahabat memelihara sahabatnya. Janganlah ucapan seperti ini diingkari, sebab Allah Ta'ala berfirman: *"maka kelak Allah akan mendatangkan suatu kaum, Dia mencintai mereka dan mereka pun mencintai-Nya"* (al-Ma'idah: 54), dan berfirman kepada Musa, semoga salam atasnya: *"dan Aku telah memilihmu (menjadi rasul) untuk diri-Ku"* (Taha: 41). Orang yang tidak melampaui kedudukan debat dan tidak akrab dengan pengetahuan-pengetahuan akliah tidak punya jalan selain menolak berita-berita seperti ini, yang keadaannya seperti kata penyair:[^p99]

> Nasab yang seakan padanya ada cahaya dari matahari dhuha
> dan tiang dari fajar subuh.

Ilmu dan amal saling menyertai. Iman, meskipun mencakup keduanya dan menjadi nama bagi keduanya, jarang disebut Allah sendirian tanpa Dia sertakan penyebutan amal sebagai penguat, seperti firman-Nya: *"Dan orang-orang yang beriman dan mengerjakan kebajikan"* (al-Baqarah: 82), dan firman-Nya: *"dan memberikan kabar gembira kepada orang yang beriman, yang mengerjakan kebajikan, bahwa mereka akan mendapat balasan yang baik, mereka kekal di dalamnya untuk selama-lamanya"* (al-Kahf: 2-3). Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bersabda: *"Segala sesuatu itu remeh kecuali ilmu,"* kemudian bersabda: *"Tidaklah ilmu itu kecuali yang diamalkan, dan tidaklah amal itu kecuali yang ikhlas,"* lalu membaca: *"Maka barangsiapa mengharap pertemuan dengan Tuhannya maka hendaklah dia mengerjakan kebajikan"* (al-Kahf: 110). Allah Ta'ala berfirman: *"(Itu) sangatlah dibenci di sisi Allah jika kamu mengatakan apa-apa yang tidak kamu kerjakan"* (ash-Shaff: 3). Beliau bersabda: *"Ilmu itu dua: ilmu di kalbu dan ilmu di lisan. Ilmu kalbu itulah yang bermanfaat, sedang ilmu lisan adalah hujah Allah atas makhluk-Nya."*

Dikatakan: "Ilmu adalah permulaan dan amal adalah kesempurnaan." Permulaan tanpa kesempurnaan sia-sia, dan kesempurnaan tanpa permulaan mustahil. Orang yang mengetahui kebaikan tetapi tidak berbuat baik, karena ilmunya ia menjadi jahat dan karena amalnya ia menjadi fasik; dan hal itu tidak diridai akal mana pun. Penyair berkata:

> Seandainya engkau dapat mengambil manfaat dari ilmumu sambil memeluk dosa-dosa besar,
> maka jadikanlah perumpamaan orang yang meminum racun padahal ia tahu racun itu membahayakan.[^d52][^t4]

Manusia naik ke derajat kekhususan dan kedekatan melalui empat kedudukan takwa: takut, harap, kehendak, dan cinta. Bila ia takut akan kebesaran Tuhannya, ia menahan diri dari hawa nafsu; bila ia berharap, ia pun takut (kehilangan yang diharapkan); bila ia berkehendak, ia bersabar dalam mencapai yang dicari; dan bila ia mencinta, ia meninggalkan segala selain Yang Mahabenar.[^r-khawf][^p100] Beliau, semoga salam atasnya, bersabda: *"Cintamu kepada sesuatu membuat buta dan tuli."* Seorang bijak berkata: maknanya, cinta itu membutakan para wali dari melihat selain Sang Pencipta, Mahaperkasa dan Mahatinggi Dia, sebagaimana cinta (kepada dunia) membutakan orang-orang kafir dan fasik dari memperhatikan selain dunia.

Sebagaimana mendekat kepada Allah Ta'ala melalui empat kedudukan, demikian pula menjauh dari-Nya melalui empat kedudukan: kemalasan, meninggalkan amal, muka tebal (*waqāḥa*), dan tenggelam (*inhimāk*). Bila ia malas memelihara ibadah-ibadah, kalbunya menyimpang dan ia dihukum dengan dipalingkan. Bila ia meninggalkan amal, kalbunya berkarat dan ia dihukum dengan hijab. Bila ia bermuka tebal, kalbunya tertutup dan ia dihukum dengan dijauhkan. Dan bila ia tenggelam, kalbunya dicap dan ia dihukum dengan diusir dari surga.[^d53] Kami berlindung kepada Allah dari kedudukan ini, (yang pelakunya) kami dapati seperti:

> Kedua tangannya satu tangan yang panjang menjangkau kehinaan,
> tetapi untuk mencari ketinggian, ia diciptakan pendek.

dan yang menahannya dari mencapai kedudukan (tinggi):

> ia memiliki cita-cita yang terlalu rendah untuk dikatakan tentangnya:
> "Seakan-akan ia telah menjulang melampaui jangkauan cita-cita."

Inilah tingkatan-tingkatan ilmu dan amal yang berkenaan dengan keutamaan-keutamaan keagamaan. Maka hendaklah para pembesar sahabat-sahabat kami yang menisbatkan diri kepada keadilan di negeri kami, yang menganggap rida mereka sendiri sebagai keadilan, melihat di mana mereka dari kedudukan-kedudukan ini![^s11]

Maksudku bukanlah mencela tauhid Allah dan keadilan-Nya; keduanya adalah pakaian dalam dan pakaian luarku, perhiasan dan selendangku, yang dengannya aku berhias di dunia dan akhirat.[^p101] Tetapi persoalannya ada pada sebagian orang yang menamai dirinya dengan keduanya, seperti orang hitam dinamai kafur dan kerikil dinamai leher jenjang: ia rela dari kekuasaan dengan khotbah, dan dari pernikahan dengan pinangan; kerjanya hanyalah memburu dan memanjang-manjangkan pengafiran seorang muslim, penfasikan seorang mukmin, tuduhan ateis terhadap orang yang beruntung memiliki ilmu yang kokoh, pembodohan terhadap orang yang berhias dengan amal saleh, dan larangan terhadap orang yang menelaah sesuatu dari pengetahuan-pengetahuan yang menyuburkan akal atau menghasilkan keutamaan.

Seandainya keberadaan Abu Hasyim, yang kemarin menimbulkan keramaian dengan pembicaraannya tentang keesaan Allah Ta'ala, sudah cukup meyakinkan, tentulah sebagian dari (tanda-tanda dalam) firman-Nya: *"Sesungguhnya pada penciptaan langit dan bumi, pergantian malam dan siang, kapal yang berlayar di laut dengan (muatan) yang bermanfaat bagi manusia, apa yang diturunkan Allah dari langit berupa air, lalu dengan itu dihidupkan-Nya bumi setelah mati (kering), dan Dia tebarkan di dalamnya bermacam-macam binatang, dan perkisaran angin dan awan yang dikendalikan antara langit dan bumi"* (al-Baqarah: 164) lebih meyakinkan lagi.[^s12] Demikian pula dalam memperhatikan diri kita, daya-dayanya, dan keajaiban keadaannya, yang diingatkan Allah Ta'ala dengan firman-Nya: *"Dan (juga) pada dirimu sendiri. Maka apakah kamu tidak memperhatikan?"* (adz-Dzariyat: 21), dan dalam merenungkan bumi, gunung-gunung kokoh yang Dia jadikan di atasnya, keberkahan yang Dia letakkan padanya, dan makanan-makanan yang Dia tentukan di dalamnya, terdapat tanda bagi orang yang mengambil pelajaran, dan sebagian kecil dari apa yang ada di alam sudah cukup bagi orang yang berpikir. Tetapi mereka *"lupa kepada Allah, sehingga Allah menjadikan mereka lupa akan diri sendiri"* (al-Hasyr: 19). Ya, *"Bahkan yang sebenarnya, mereka mendustakan apa yang mereka belum mengetahuinya dengan sempurna dan belum mereka peroleh penjelasannya. Demikianlah halnya umat-umat yang ada sebelum mereka telah mendustakan (rasul)"* (Yunus: 39), dan mereka berkata dalam diri mereka: *"Sekiranya itu sesuatu yang baik, tentu mereka tidak pantas mendahului kami (beriman) kepadanya"* (al-Ahqaf: 11).

Itu bukanlah celaan dariku terhadap Abu Hasyim. Langkahnya telah panjang menuju usaha-usaha mulia, baik usahanya dalam Islam, keras pijakannya atas orang-orang ateis, dan ucapan-ucapannya memutihkan wajah putra-putra Islam. Tetapi tidak semestinya seorang hamba melupakan firman Allah Ta'ala: *"niscaya Allah akan mengangkat (derajat) orang-orang yang beriman di antaramu dan orang-orang yang diberi ilmu beberapa derajat"* (al-Mujadilah: 11), dan firman-Nya: *"dan di atas setiap orang yang berpengetahuan ada yang lebih mengetahui"* (Yusuf: 76).[^p102]

Orang yang mengingkari hal itu dapat dimaafkan. Seseorang berkata kepada Plato: "Aku melihat manusia, tetapi tidak melihat kemanusiaan." Ia menjawab: "Karena engkau diberi apa yang dengannya engkau melihat manusia, tetapi tidak diberi apa yang dengannya engkau melihat kemanusiaan."[^p103]

Kami memohon kepada Allah agar memberi kami taufik kepada petunjuk kami dan membuat kami melihat dengan jelas di dalamnya:

> Siapa yang jiwanya tidak mengenal kadarnya,
> orang lain melihat darinya apa yang tidak ia lihat.

Seorang bijak berkata: "Tidak ada yang lebih jauh dari kebenaran daripada dusta, sebab ia lawannya; tetapi orang yang riya lebih buruk keadaannya daripada pendusta, sebab ia berdusta dalam perbuatan dan ucapannya sekaligus." Karena itu Nabi, semoga Allah melimpahkan selawat dan salam kepadanya, bersabda: *"Orang yang berlagak kenyang dengan apa yang tidak ia miliki seperti orang yang memakai dua pakaian palsu."* Kemudian orang yang ujub lebih buruk keadaannya daripada keduanya, sebab ia berdusta dalam ucapan, perbuatan, dan keyakinannya.[^r-ujb] Pendusta berdusta dengan ucapannya, dan orang yang riya dengan ucapan dan perbuatannya; keduanya mengetahui perbuatan mereka, dan bila engkau menasihati keduanya, diamnya mereka membantumu (menduga) penerimaan mereka. Sedang orang yang ujub berdusta dalam keduanya dan dalam keyakinannya, sebab ia tidak mengetahui dustanya; bila engkau mengingatkannya, ia tidak sadar. Kemudian, pendusta dan orang yang riya terkadang memberi manfaat dengan perbuatan mereka, seperti nakhoda yang takut tenggelam di suatu tempat yang menakutkan, lalu menggembirakan para penumpang bahwa tempat yang menakutkan itu telah dilewati dan menampakkan kegembiraan kepada mereka, agar mereka tidak panik karena takut tenggelam sehingga kepanikan itu membawa mereka kepada kebinasaan. Demikian pula pemimpin terkadang bersikap riya agar rakyatnya meneladaninya; sedang orang yang ujub sama sekali tidak memiliki bagian semacam itu.[^d54]

Semoga Allah melindungi Ustaz, semoga Allah memanjangkan umurnya di tempat ini dan memeliharanya dari mata bencana-bencana dan peristiwa-peristiwa, dan menyibukkannya dengan apa yang merupakan pemberian yang kekal, bukan pinjaman, dengan rahmat-Nya. Sesungguhnya Dia Mahakuasa atas apa yang Dia kehendaki.[^p104]

[^p87]: CP: Judul risalah ini tidak tercantum pada halaman judul naskah; penyunting mengambil judul "Tingkatan Ilmu-Ilmu" dari catatan di akhir naskah dan menyisipkannya sebagai subjudul. Terjemahan Turki memberinya judul *Risāla fī Marātib al-ʿUlūm wa-l-Aʿmāl al-Dunyawiyya* ("tingkatan ilmu-ilmu dan amal-amal duniawi"). Kata "duniawi" dalam judul itu mengikuti pembetulan penyunting yang keliru (lihat catatan p97); karena itu judul di atas tidak memakainya. Subjudul-subjudul di dalam risalah ini ditambahkan untuk memudahkan pembacaan; subjudul sisipan penyunting yang tidak sesuai dengan isi ("Antara Ahlus Sunnah dan Para Pengaku Muktazilah") tidak dipakai.

[^p88]: CP: Edisi tahkik membaca *wa-l-maḥabba fī al-nās faḍl min al-ʿadāla*, dan penyunting memahaminya "cinta adalah bagian dan cabang dari keadilan"; terjemahan Turki mengikutinya ("adaletin bir parçasıdır"). Alasannya justru menunjukkan sebaliknya: cinta selalu disertai keadilan, sedang keadilan tidak selalu disertai cinta; maka cinta mencakup keadilan dan melebihinya. Kami membacanya *afḍal min al-ʿadāla* ("lebih utama daripada keadilan").

[^d48]: CD: Ucapan ini dikutip dalam *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta": "Seandainya manusia saling mencintai dan bermuamalah dengan cinta, niscaya mereka tidak membutuhkan keadilan. Dikatakan: Keadilan adalah pengganti cinta, yang dipakai di tempat cinta tidak ada." Terjemahan di atas mengikuti redaksi itu. Lihat pula Risalah Pertama, Bab Kedelapan, catatan d20.

[^s8]: CM: Menurut satu riwayat, pembunuh itu menjawab Umar: "Adapun cinta, yang memedulikannya hanyalah kaum perempuan." Peribahasa "kalau tidak menjadi istri kesayangan, setidaknya tidak lalai" (*illā ḥaẓiyyatan fa-lā aliyyatan*) diucapkan untuk menasihati agar bersikap lunak kepada orang lain supaya memperoleh sebagian yang dibutuhkan dari mereka; al-Rāghib juga mengutipnya dalam *Majmaʿ al-Balāgha*. Zaid bin al-Khaththab gugur dalam Perang Yamamah; pembunuhnya disebut dalam sumber-sumber sejarah sebagai Abū Maryam al-Ḥanafī, yang kemudian masuk Islam.

[^p89]: CP: Tentang perempuan yang berdalil dengan urutan "Dia mencintai mereka dan mereka pun mencintai-Nya", lihat Risalah Pertama, Bab Keenam, awal bab.

[^d49]: CD: Rantai ini sama dengan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta": "Setiap kaum, bila saling mencintai, mereka saling menyambung; bila saling menyambung, mereka saling menolong; bila saling menolong, mereka bekerja; bila bekerja, mereka memakmurkan; dan bila memakmurkan, mereka berumur panjang." Terjemahan di atas mengikuti redaksi itu, kecuali mata rantai terakhir: di *al-Dharīʿa* tertulis *ʿummirū* ("berumur panjang"), sedang di sini *amirū* ("menjadi banyak dan berjaya"; terjemahan Turki: "menjadi pemimpin").

[^d50]: CD: Uraian tentang perkumpulan ibadah ini sejajar dengan *al-Dharīʿa*, Pasal Kelima, "Keutamaan Cinta" ("Semua itu agar dengan berkumpulnya mereka keakraban menjadi kokoh, dan karenanya kasih sayang terjadi"), dan dengan Risalah Pertama, Bab Pertama. Di sini ditambahkan umrah dan penegasan bahwa ibadah-ibadah itu tidak dicukupkan dengan dikerjakan sendiri-sendiri.

[^p90]: CP: *Mawaddāt fujāʾiyya wa-lawwāma wa-muḍmaḥilla*: kasih sayang karena kelezatan dan manfaat datang tiba-tiba, disertai saling mencela, dan cepat lenyap; lihat Risalah Pertama, Bab Kedua, tentang "kasih sayang yang penuh celaan" (*al-mawadda al-lawwāma*) dan tentang az-Zukhruf: 67.

[^s9]: CM: Ustaz yang dimaksud agaknya sama dengan yang dituju Risalah Pertama dan Kedua, yaitu wazir Aḥmad bin Ibrāhīm al-Ḍabbī; lihat catatan s1. Penyunting tidak dapat menemukan keterangan tentang peristiwa yang disinggung di sini: agaknya sebagian teman majelis Ustaz mengadukan al-Rāghib kepadanya, lalu Ustaz marah dan berbicara buruk tentang al-Rāghib, sehingga al-Rāghib menulis risalah ini untuk menjelaskan sikapnya.

[^s10]: CM: Penyunting belum dapat mengetahui nama syekh ini; ia menduga syekh itu salah seorang pengikut Abū Hāshim al-Jubbāʾī, tokoh Muktazilah yang disebut di bagian akhir risalah. Dugaan ini sesuai dengan isi risalah: syekh itu menolak istilah filsafat dan menganggap ilmu kalam puncak ilmu.

[^r-quwa]: **Daya** (*quwwa*). Lihat terjemahan *Tafṣīl*, catatan no. 78 (`k-quwa`, *Kashshāf*), dan glosarium terjemahan *al-Dharīʿa* (entri *quwwa*: "kekuatan; daya"). Dalam *al-Mufradāt*, s.v. *q-w-y*, al-Rāghib sendiri mencatat bahwa *quwwa* kadang dipakai dalam arti *qudra* (kuasa), dan bahwa "*quwwa* yang dipakai untuk kesiapan paling banyak dipakai oleh para filsuf", dalam dua arti: "si fulan penulis dalam potensi", yakni ia memiliki pengetahuan menulis tetapi tidak sedang memakainya, atau yakni ia dapat belajar menulis. Maka al-Rāghib mengakui bahwa pemakaian *quwwa* dalam arti potensi berasal dari para filsuf; yang ia tolak ialah anggapan bahwa lafal itu sendiri milik para filsuf dan dapat diganti begitu saja dengan *qudra*, padahal maknanya berbeda.

[^m-qudra]: **Kuasa** (*qudra*). Dalam *al-Mufradāt*: *qudra*, bila disifatkan kepada manusia, adalah nama bagi suatu keadaan (*hayʾa*) padanya yang dengannya ia mampu melakukan sesuatu; bila disifatkan kepada Allah Ta'ala, ia berarti tiadanya kelemahan pada-Nya. Mustahil selain Allah disifati dengan kuasa yang mutlak dalam makna, meskipun lafalnya kadang dipakai; yang semestinya dikatakan tentang selain-Nya adalah "kuasa atas anu". (*al-Mufradāt*, s.v. *q-d-r*.) Perbedaannya dengan *quwwa* jelas: *quwwa* dapat berarti kekuatan badan, daya jiwa, atau potensi yang belum aktual, sedang *qudra* berkaitan dengan kemampuan untuk berbuat. Kaum Muktazilah banyak memakai *qudra* dalam pembahasan perbuatan manusia; agaknya karena itu syekh tersebut menuntut agar *quwwa* diganti dengan *qudra*.

[^p91]: CP: Edisi tahkik membaca *li-mā raʾā minnī fī mujāwabatihi jumalan thiqalan* ("kalimat-kalimat yang berat"); terjemahan Turki memahaminya "ketika ia melihat aku memberinya jawaban yang semestinya". Kalimat sesudahnya ("aku tidak melihat ada salahnya menanggung ucapan seorang syekh yang mulia") menunjukkan bahwa al-Rāghib menahan diri dalam menanggapinya; karena itu kami memahaminya sebagai kesabaran dan ketenangan. Bacaan pasti kata-kata itu belum dapat ditetapkan.

[^p92]: CP: Edisi tahkik membaca *wa-lā sarranī minhum jaḥd* ("pengingkaran mereka tidak menggembirakanku"); kami mengikuti usul penerjemah Turki, *ḥamd* ("pujian"), pasangan *dhamm* ("celaan"). Kata pertama yang tidak jelas dalam naskah dibaca *mā nālanī*.

[^p93]: CP: Bait Imruʾ al-Qays. Menurut kisahnya, ia bertamu kepada Khālid bin Sadūs al-Nabhānī, lalu unta-untanya dirampas perampok; Khālid meminjam unta-unta tunggangannya untuk mengejar para perampok, tetapi unta-unta tunggangan itu pun dirampas pula. Bait ini menjadi perumpamaan bagi kerugian kedua yang lebih memalukan daripada yang pertama. Maksud al-Rāghib: biarlah soal fitnah terhadap dirinya berlalu; yang lebih patut dibicarakan adalah anggapan syekh itu bahwa tidak ada ilmu di balik kalam. Kisah ini dicatat penerjemah Turki.

[^p94]: CP: Kata *al-diyāna* (agama) di sini mencakup seluruh ilmu yang berkaitan dengan agama, termasuk ilmu niscaya dan ilmu akliah yang menjadi dasarnya; karena itu kami menerjemahkannya "ilmu-ilmu agama", bukan "ilmu-ilmu keagamaan" dalam arti sempit ilmu nukilan.

[^r-fitra]: **Fitrah** (*fiṭra*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 172 (`m-fitra`) dan no. 173 (`k-fitra`), dan terjemahan *Tafṣīl*, catatan no. 172 (`r-fitra`). Di sini fitrah disamakan dengan akal bawaan (lihat Risalah Kedua, Pasal Keempat) dan dengan ilmu niscaya para ahli kalam.

[^r-yaqin]: **Keyakinan** (*yaqīn*). Lihat glosarium terjemahan *al-Dharīʿa* dan *Tafṣīl* (entri *yaqīn*: "sifat ilmu di atas makrifat dan dirayah"), dan terjemahan *Tafṣīl*, catatan no. 159 (`m-yaqin`).

[^p95]: CP: Riwayat ini, dalam *Ṣaḥīḥ al-Bukhārī*, berbunyi: "Tidak, kecuali Kitab Allah, atau pemahaman yang diberikan kepada seorang muslim, atau apa yang ada dalam lembaran ini." Kalimat al-Rāghib sesudahnya ("Maka terkadang Allah memberikannya kepada siapa yang Dia kehendaki") merujuk kepada "pemahaman yang diberikan" itu, yang dalam naskah ini tidak tercantum. Isi lembaran itu, menurut riwayat yang sama, adalah hukum diat, pembebasan tawanan, dan larangan membunuh muslim karena orang kafir.

[^p96]: CP: Penyunting memahami "beliau" di sini sebagai Ali; penerjemah Turki menunjukkan bahwa ucapan ini diriwayatkan sebagai hadis marfu' dari Abū Juḥayfa, dengan urutan yang berbeda dalam sebagian riwayat ("duduklah bersama para ulama, bertanyalah kepada para pembesar, dan bergaullah dengan para hakim"), dan sanadnya sangat lemah. Dalam penjelasan sesudahnya al-Rāghib menukar dua kata kerja: "duduk bersama" untuk para hakim dan "bergaul" untuk para pembesar.

[^d51]: CD: Pembagian empat tingkat ilmu ini tidak terdapat dalam *al-Dharīʿa*. Di sana (Pasal Kedua, "Jalan-Jalan Memperoleh Ilmu") yang dibagi empat adalah jalan-jalan memperoleh ilmu: spontanitas akal dan indra, perenungan, kabar, dan wahyu; ilham kepada kalbu (*muḥaddath*) dimasukkan ke dalam macam wahyu. Di sini "ilmu hakikat" atau "ilmu anugerah" dijadikan tingkat tersendiri di atas ilmu kenabian yang diamalkan, dengan dalil-dalil sufi. Lihat juga Risalah Kedua, Pasal Kelima, tentang tiga jalan ilmu.

[^p97]: CP: Dalam naskah tertulis *al-aʿmāl al-dīniyya* ("amal-amal keagamaan"), dan di akhir bagian ini "keutamaan-keutamaan keagamaan"; penyunting mengubah keduanya menjadi *al-dunyawiyya* ("duniawi") dengan anggapan bahwa bagian pertama tentang ilmu agama dan bagian kedua tentang amal dunia, dan terjemahan Turki mengikutinya. Pembetulan itu keliru: keempat tingkatan yang diuraikan (meninggalkan yang keji, menegakkan kewajiban dan sunah, menikmati ketaatan, dan menjaga batin di atas rida Allah) semuanya amal keagamaan, sejajar dengan empat tingkat ilmu agama. Karena itu bacaan naskah dipertahankan.

[^p98]: CP: Edisi tahkik membaca *ʿaraftu nafsī* ("aku mengenal jiwaku"); kami membacanya *ʿazafat nafsī ʿan al-dunyā* ("jiwaku berpaling dari dunia"), sesuai riwayat hadis ini dalam sumber-sumber yang dikutip penyunting sendiri. Kata *yataʿāwarūn* dibaca *yataʿāwawn* ("saling melolong"), juga sesuai riwayat itu.

[^p99]: CP: Uraian tentang cinta Allah dan ucapan "sebagian kitab para bijak" ini sama dengan Risalah Pertama, Bab Keenam, tempat ucapan itu dinisbatkan kepada Aristoteles (lihat catatan p36 dan k-murid). Di sini ayat yang dikutip untuk Musa adalah Taha: 41, bukan al-A'raf: 144. Bait penyair (Abu Tammam) melukiskan sesuatu yang terlalu terang untuk diingkari.

[^d52]: CD: Keterkaitan ilmu dan amal diuraikan pula dalam *al-Dharīʿa*, Pasal Kedua, "Anjuran Mengambil Bekal Secukupnya dari Setiap Ilmu": "Tidakkah engkau lihat bahwa dalam umumnya Al-Qur'an penyebutan iman tidak dilepaskan dari penyebutan amal saleh …? Dikatakan: ilmu adalah fondasi dan amal adalah bangunan."

[^t4]: CT: *Tafṣīl*, Bab Kedua Puluh Tiga, "Macam-Macam Ibadah berupa Ilmu dan Amal": "Ibadah ada dua macam: ilmu dan amal. Semestinya keduanya saling menyertai, sebab ilmu seperti fondasi dan amal seperti bangunan; sebagaimana fondasi tidak berguna selama tidak ada bangunan, dan bangunan tidak akan kokoh selama tidak ada fondasi, demikian pula ilmu tidak berguna tanpa amal, dan amal tidak berguna tanpa ilmu." Perumpamaan fondasi dan bangunan di sini dipakai untuk hubungan antara meninggalkan keburukan dan melakukan kebaikan (tingkat pertama amal), sedang di *Tafṣīl* untuk hubungan antara ilmu dan amal; penyunting mengutip bagian *Tafṣīl* ini.

[^r-khawf]: **Takut** (*khawf*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 311 (`m-khawf`) dan no. 312 (`k-khawf`); tentang *irāda*, no. 73-74; tentang takwa, no. 126 (`m-taqwa`) dan no. 127 (`k-taqwa`).

[^p100]: CP: "Bila ia berharap, ia pun takut" (*matā rajā khashiya*): harapan dan takut tidak terpisah, sebagaimana dijelaskan al-Rāghib dalam *al-Mufradāt*, s.v. *r-j-w*: karena harap dan takut saling menyertai, kata *rajāʾ* kadang dipakai dalam arti takut. Maka orang yang berharap bersungguh-sungguh berbuat baik karena takut kehilangan apa yang diharapkannya. Empat kedudukan ini sejajar dengan empat tingkat amal di atas: takut untuk yang pertama, harap untuk yang kedua, kehendak untuk yang ketiga, dan cinta untuk yang keempat.

[^d53]: CD: Empat derajat turun ini sama dengan *al-Dharīʿa*, Pasal Pertama, "Naik ke Derajat-Derajat Keutamaan dan Turun darinya ke Keburukan yang Paling Rendah": kemalasan yang mewariskan penyimpangan (*zaygh*); kebebalan (*ghabāwa*), yaitu meninggalkan perenungan dan membenci amal, yang mewariskan karat (*rayn*); muka tebal (*waqāḥa*), yang mewariskan kerasnya kalbu; dan tenggelam dalam yang batil, yang mewariskan cap dan gembok di atas kalbu. Istilah-istilahnya diterjemahkan mengikuti redaksi itu. Empat derajat naik dalam *al-Dharīʿa* berbeda: orang-orang yang bertobat, orang-orang saleh, para syuhada, dan para *shiddiq* (an-Nisa': 69); di sini keempatnya dirumuskan sebagai takut, harap, kehendak, dan cinta.

[^s11]: CM: Yang dimaksud adalah kaum Muktazilah, yang menamai diri mereka "ahli keadilan dan tauhid" (*ahl al-ʿadl wa-l-tawḥīd*). Ungkapan "di negeri kami" termasuk sedikit tempat dalam karya-karya al-Rāghib yang menyinggung lingkungannya sendiri.

[^p101]: CP: Edisi tahkik membaca *shiʿārī wa-diyārī* ("syiarku dan negeriku"); kami membacanya *shiʿārī wa-dithārī* ("pakaian dalamku dan pakaian luarku"), pasangan yang lazim dalam bahasa Arab dan sejajar dengan "perhiasan dan selendangku". Pernyataan ini penting: al-Rāghib menerima tauhid dan keadilan Allah sebagai pokok akidah, dan hanya menolak klaim sebagian orang bahwa kedua pokok itu milik mereka.

[^s12]: CM: Abū Hāshim ʿAbd al-Salām bin Muḥammad al-Jubbāʾī (w. 321 H), putra Abū ʿAlī al-Jubbāʾī, salah seorang tokoh utama Muktazilah; sebagian besar Muktazilah sesudahnya mengikuti mazhabnya. (Penyunting menyimpulkan dari kata "kemarin" bahwa al-Rāghib hidup lebih awal daripada yang biasa disebut; kesimpulan itu tidak kuat, sebab "kemarin" dapat berarti masa yang belum lama berlalu.) Kalimat ini sangat ringkas dalam naskah; terjemahan Turki memahaminya sama: seandainya keberadaan Abu Hasyim meyakinkan orang tentang keesaan Allah, tentu tanda-tanda dalam ciptaan lebih layak meyakinkan mereka.

[^p102]: CP: Edisi tahkik membaca *lā yajibu an yunsā ʿabduhu* ("tidak wajib hamba-Nya dilupakan"); kami mengikuti pemahaman penerjemah Turki: *lā yajibu an yansā al-ʿabd* ("tidak semestinya seorang hamba melupakan").

[^p103]: CP: Edisi tahkik membaca *wa-maʿdhūr an unkira dhālika* ("aku dimaafkan bila mengingkari"); kami membacanya *wa-maʿdhūrun man ankara dhālika* ("orang yang mengingkari hal itu dapat dimaafkan"). Dalam sumber-sumber Yunani, dialog ini biasanya dinisbatkan kepada Antisthenes atau Diogenes yang berkata kepada Plato: "Aku melihat kuda, tetapi tidak melihat kekudaan", dan Plato menjawab: "Karena engkau memiliki mata untuk melihat kuda, tetapi tidak memiliki mata untuk melihat kekudaan." Al-Rāghib memakainya untuk memaafkan orang yang hanya mengenal ilmu yang dapat dijangkaunya.

[^r-ujb]: **Ujub** (*ʿujb*). Lihat terjemahan *al-Dharīʿa*, nota kaki no. 261 (`m-ujb`) dan no. 262 (`k-ujb`), dan terjemahan *Tafṣīl*, catatan no. 28 (`r-ujb`); tentang riya, nota kaki *al-Dharīʿa* no. 263 (`k-riya`).

[^d54]: CD: Perbandingan pendusta, orang riya, dan orang ujub ini sama dengan *al-Dharīʿa*, Pasal Ketiga, "Ujub", termasuk perumpamaan nakhoda dan riya seorang pemimpin; terjemahan bagian itu mengikuti redaksi terjemahan *al-Dharīʿa*. Alasannya sedikit berbeda: di *al-Dharīʿa* orang ujub lebih buruk karena "buta terhadap keburukan-keburukan dirinya, memandangnya sebagai kebaikan"; di sini karena ia berdusta dalam tiga hal sekaligus, ucapan, perbuatan, dan keyakinan. Hadis "dua pakaian palsu" tidak dikutip di sana. Dalam konteks risalah ini, uraian tentang ujub agaknya ditujukan kepada syekh yang menganggap ilmu kalam puncak segala ilmu.

[^p104]: CP: Sesudah doa penutup ini naskah memuat kolofon penyalin (tanggal penyalinan dan nama penyalin), yang tidak diterjemahkan karena bukan bagian dari risalah.

# Risalah Keempat {.kitab-ke}

# Uraian tentang Lafal *al-Wāḥid* dan *al-Aḥad* {.judul-kitab}

[Dengan nama Allah Yang Maha Pengasih, Maha Penyayang]{.basmalah}

Ya Tuhanku, mudahkanlah dan jangan Engkau persulit; dan hanya kepada-Nya kami memohon pertolongan.

Kami telah membicarakan bersama Syekh yang utama, semoga Allah memanjangkan umurnya dan melanggengkan pertolongan-Nya kepadanya, tentang lafal *al-wāḥid* dan *al-aḥad* serta pemastian makna keduanya. Beliau meminta agar aku menuliskan hal itu, dan aku melakukannya untuk memenuhi permintaannya.[^s13] Hendaklah beliau menyerahkan kepadaku (kembali tulisan ini melalui) orang yang membacakannya kepadanya, dan berkenan mengingatkanku akan kelupaan atau kekeliruan yang ia temukan di dalamnya; dan pendapatnya dalam hal itu, insya Allah, mendapat taufik.

### Lafal *al-Wāḥid* {.judul-pasal}

Ringkasnya, apa yang dikatakan para peneliti tentang lafal *wāḥid* ialah bahwa ia pada asalnya diletakkan untuk sesuatu yang darinya bilangan tersusun. Tentang definisinya atau deskripsinya mereka berkata: "Ia adalah sesuatu yang sama sekali tidak memiliki bagian." Inilah asal peletakannya.

Kemudian ia dipakai untuk setiap maujud, baik yang kadim maupun yang baru, yang sederhana maupun yang tersusun. Karena itu tidak ada sesuatu pun yang disifati dengan wujud kecuali ia juga disifati dengan kesatuan (*waḥda*). Karena itu seorang bijak berkata: "Kesatuan adalah wujud khusus yang dengannya setiap maujud terbedakan." Karena tidak ada maujud kecuali sah disifati dengan *wāḥid*, sah pula setiap bilangan disifati dengannya; maka dikatakan: sepuluh yang satu, dan seribu yang satu.[^m-wahid]

*Wāḥid* adalah lafal musytarak yang dipakai dalam enam cara.[^p105]

**Pertama**: yang satu dalam genus atau dalam spesies, seperti ucapan kita: manusia dan kuda satu dalam genus, dan Zaid dan Amr satu dalam spesies.

**Kedua**: yang satu karena bersambung, baik dari segi ciptaan, seperti ucapanmu: satu pribadi; maupun dari segi buatan, seperti ucapanmu: satu ikat.

**Ketiga**: yang satu karena tidak ada bandingannya, baik dalam ciptaan, seperti ucapanmu: matahari itu satu; maupun dalam klaim keutamaan, seperti ucapanmu: si fulan satu-satunya di zamannya, yakni ia tenunan tersendiri (tiada tandingnya).

**Keempat**: yang satu karena tidak mungkin dibagi, baik karena kecilnya, seperti debu yang beterbangan, maupun karena kerasnya, seperti intan.

**Kelima**: untuk permulaan, baik permulaan bilangan, seperti ucapan kita: satu, dua; maupun permulaan garis, seperti ucapan kita: satu titik.

Inilah lima cara; kesatuan dalam semuanya bersifat aksidental, dan tidak sah sesuatu pun darinya dipakai untuk Allah, karena Dia suci dari adanya kebanyakan pada-Nya, sedang kebanyakan terdapat pada masing-masing darinya. Genus, meskipun satu dari satu segi, banyak dengan spesies-spesiesnya; spesies banyak dengan individu-individunya; yang bersambung, segi-segi kebanyakannya jelas; matahari, meskipun satu secara individu dan zat, tubuhnya memiliki bagian-bagian; demikian pula orang yang disifati satu-satunya di zamannya; demikian pula yang tidak dapat dibagi karena kecil atau karena kerasnya; dan demikian pula titik dan satu dalam bilangan: meskipun keduanya tidak dapat dibagi, keduanya dapat dikenai kebanyakan. Tidakkah engkau lihat bahwa seluruh bilangan adalah bilangan yang berlipat-lipat, dan garis adalah titik-titik yang berturut-turut?

Yang dimaksud dengan *wāḥid* bila Sang Pencipta, Mahasuci dan Mahatinggi Dia, disifati dengannya ialah bahwa Dialah yang tidak dapat dikenai pembagian dan tidak pula kebanyakan; yakni Dia bukan satu yang darinya sesuatu dapat tersusun, dan bukan pula tersusun dari sesuatu.

Seorang bijak berkata: kesatuan yang paling dekat kepada Allah Ta'ala, bila diteliti dan direnungkan, ialah satu yang merupakan asal bilangan. Sebab segala sesuatu selain Dia yang disebut dengan lafal *wāḥid* dapat dikenai pembagian dan pelipatan, kecuali satu yang dipakai dalam bilangan: ia, meskipun dapat dilipatkan, tidak dapat dibagi; sedang Sang Pencipta Ta'ala tidak dapat dikenai pembagian dan tidak pula pelipatan.

Lagi pula, satu adalah asal bilangan, tetapi tidak termasuk dalam bilangan; ia ada sesudah setiap bilangan (sebagai unsurnya), tetapi tidak ada bilangan sesudahnya (yang menjadi unsurnya); darinya bilangan tumbuh dan kepadanya bilangan terurai; dan ia menguasai segala yang terbilang. Sebagaimana satu bukanlah bilangan, padahal darinya bilangan tumbuh dan kepadanya ia kembali, demikian pula Sang Pencipta Ta'ala bukanlah sesuatu dari segala sesuatu ini, padahal dari-Nya permulaan segala maujud dan kepada-Nya kembalinya, sebagaimana firman-Nya: *"Dialah Yang Awal, Yang Akhir"* (al-Hadid: 3). Mahatinggi Allah dari penyerupaan.[^p106]

Inilah cara-cara pemakaian lafal *wāḥid*.

### Lafal *al-Aḥad* {.judul-pasal}

Adapun *aḥad*, ia dipakai dalam dua macam.[^m-ahad]

Pertama, dalam penafian saja. Ia diletakkan untuk mencakup seluruh jenis makhluk yang bertutur (*al-nāṭiqūn*), dan meliputi yang sedikit dan yang banyak, baik berkumpul maupun terpisah. Seperti ucapan mereka: "Tidak ada seorang pun (*aḥad*) di rumah," yakni tidak ada satu, tidak dua, tidak pula tiga atau lebih, baik berkumpul maupun terpisah.

Keadaannya yang diletakkan dengan cara ini menuntut bahwa ia tidak dipakai kecuali dalam penafian. Sebab menafikan dua hal yang berlawanan itu sah, tetapi menetapkan keduanya tidak sah. Bila kita berkata, "Tidak ada seorang pun di rumah," kita menafikan satu dan banyak, berkumpul maupun terpisah. Seandainya kita berkata, "Ada *aḥad* di rumah," tentu di dalamnya terkandung penetapan satu yang tersendiri sekaligus penetapan yang lebih dari satu, berkumpul maupun terpisah; dan kemustahilan hal itu jelas. Karena ia mencakup satu dan yang lebih dari itu, sah dikatakan: "Tidak ada seorang pun yang utama" (*mā min aḥadin fāḍil*), dan "Tidak ada seorang pun yang utama-utama" (*mā min aḥadin fāḍilīn*), seperti firman-Nya: *"Maka tidak seorang pun dari kamu yang dapat menghalangi (Kami untuk menghukumnya)"* (al-Haqqah: 47).[^p107]

Adapun yang dipakai dalam penetapan, ada tiga cara.

**Pertama**: pada satu yang digabungkan dengan puluhan, seperti *aḥad ʿashar* (sebelas) dan *aḥad wa-ʿishrūn* (dua puluh satu).

**Kedua**: dipakai sebagai yang disandarkan atau yang disandari, dalam arti "yang pertama", seperti firman-Nya: *"Salah seorang di antara kamu, akan bertugas menyediakan minuman khamar bagi tuannya"* (Yusuf: 41), dan ucapan mereka *yawm al-aḥad* (hari Ahad), yang maknanya hari pertama, dengan bukti ucapan mereka *yawm al-ithnayn* (hari Senin, hari kedua).

**Ketiga**: dipakai dalam penetapan secara mutlak sebagai sifat, dan itu hanya dalam menyifati Allah Ta'ala, seperti firman-Nya: *"Dialah Allah, Yang Maha Esa (aḥad)"* (al-Ikhlas: 1).

### Perbedaan antara *al-Wāḥid* dan *al-Aḥad* {.judul-pasal}

Perbedaan antara *wāḥid* dan *aḥad* dalam menyifati Allah Ta'ala ialah bahwa keduanya, meskipun dimaksudkan dengan satu makna dalam menyifati Allah Ta'ala, berbeda peletakannya pada asal bahasa.

*Wāḥid* berbentuk *fāʿil* (pelaku), sehingga dari segi peletakannya ia menunjuk dua hal: zat dan kesatuan; sebagaimana *aswad* (yang hitam) menunjuk dua hal: zat dan kehitaman. *Wāḥid* satu karena kesatuan, sebagaimana *aswad* hitam karena kehitaman. Maka bila dikatakan *wāḥid*, tampak darinya dua hal, sebagaimana tampak pada ucapan mereka *aswad*, *abyaḍ*, dan yang semisalnya.

Adapun *aḥad* menunjuk kesatuan yang murni, sebab ia masdar. Asalnya *waḥad*; huruf *wāw* diganti dengan hamzah, dan sesudah penggantian itu ia dikhususkan pemakaiannya untuk menyifati Allah Ta'ala.[^k-ahad] Adapun *waḥad* kadang dipakai untuk menyifati selain-Nya, dan maknanya "yang sendiri", seperti kata penyair:[^p108]

> (Seekor banteng liar) dari satwa liar Wajrah, berbintik-bintik kakinya,
> ramping perutnya, berkilau seperti pedang tunggal buatan pandai besi.

*Aḥad* tidak dipakai untuk selain Allah kecuali dengan dibatasi oleh apa yang disandarkan kepadanya atau apa yang digabungkan dengannya, sebagaimana telah dikemukakan.

Jika seseorang berkata: penyair telah berkata:

> Engkau telah bersinar terang, maka tak tersembunyi dari seorang pun,
> kecuali dari seseorang yang tidak mengenal bulan.

Ucapannya "kecuali dari seseorang" adalah penetapan, dan ia memakainya bukan untuk menyifati Allah Ta'ala. Dijawab: pemakaiannya sah di tempat ini karena didahului penafian dan datang sesudahnya; seandainya tidak demikian, pemakaiannya tidak sah. Suatu lafal kadang dipakai dengan cara tertentu karena didahului oleh lafal lain; seandainya tidak didahului, pemakaian itu tidak sah. Seperti firman-Nya: *"sebagian berjalan dengan empat kaki"* (an-Nur: 45): Dia memakai *man* (siapa, kata untuk yang berakal) untuk binatang ternak, karena datang sesudah (kata) yang sah memakainya.[^p109]

Jika dikatakan: seandainya tidak sah memakai *aḥad* untuk manusia, tentu penyair tidak berkata:

> Sesungguhnya Bani al-Adram tidak termasuk seorang pun,

dan tidak akan dikatakan: "Si fulan bukan seorang pun" (*laysa bi-aḥad*). Dijawab: *aḥad* di sini adalah yang dipakai dalam penafian, dan itu khusus untuk manusia, sebagaimana telah dikemukakan; maknanya: ia bukan manusia. Ia termasuk dalam keumuman ucapan mereka: "Tidak ada seorang pun yang melakukan anu," dan "Tidak seorang pun berkata anu," seperti ucapan penyair:

> engkau keliru bila menanyakan mereka dengan "siapa".[^p110]

Dan seperti ucapan mereka: "Si fulan bukan manusia," dan "Ia *al-fulān*, bukan *fulān*," sebagai peringatan bahwa ia binatang, bukan manusia; sebab *fulān* dan *fulāna* dipakai untuk manusia, sedang *al-fulān* dan *al-fulāna* untuk hewan.

Adapun firman Allah Ta'ala: *"Apakah dia mengira bahwa tidak ada sesuatu pun (aḥad) yang melihatnya?"* (al-Balad: 7), dan firman-Nya: *"Apakah dia (manusia) itu mengira bahwa tidak ada sesuatu pun (aḥad) yang berkuasa atasnya?"* (al-Balad: 5), dalam tafsirnya disebutkan dua pendapat.

Pertama, *aḥad* di sini adalah yang disebut dalam firman-Nya: *"Dialah Allah, Yang Maha Esa (aḥad)"*, dan maknanya: apakah ia mengira bahwa Allah Ta'ala tidak melihatnya? Isyarat maknanya kepada firman-Nya seperti: *"Tidak ada pembicaraan rahasia antara tiga orang, melainkan Dialah yang keempatnya"* (al-Mujadilah: 7).

Kedua, *aḥad* di sini adalah yang dipakai dalam penafian, dan maknanya: manusia tidak mampu (membuat) apa yang ia sembunyikan tidak diketahui oleh seorang pun, sebab Allah Ta'ala dan para malaikat pencatat yang mulia mengetahuinya; isyarat kepada firman-Nya seperti: *"Tidak ada suatu kata yang diucapkannya melainkan ada di sisinya malaikat pengawas yang selalu siap (mencatat)"* (Qaf: 18).

### Penutup {.judul-pasal}

Kadar ini cukup untuk apa yang dimaksud, yaitu menjelaskan lafal *wāḥid* dan *aḥad*; meskipun dalam pemastian makna kesatuan dan keadaannya sebagai salah satu limpahan pertama Sang Pencipta atas segala maujud terdapat hikmah yang mendalam dan keajaiban-keajaiban yang banyak. Sebab Allah Ta'ala menjadikan kesatuan sebab kesepakatan dan keakraban, dan kebanyakan sebab perpecahan dan perselisihan. Karena itu seorang bijak berkata: "Kebaikan adalah wujud dalam kesatuan, dan keburukan adalah ketiadaan dalam kebanyakan." Dikatakan pula: "Tidak ada kebaikan dalam banyaknya pemimpin." Maka setiap kerukunan adalah bayangan kesatuan, dan setiap perselisihan adalah perbuatan kebanyakan.[^p111]

Seandainya Syekh yang utama itu bukan orang yang sangat menguasai pengetahuan dan hikmah, tentu aku menahan diri dari menyinggung perkara seperti ini. Meski demikian, aku telah menahan tali kekang pembicaraan ketika sampai kepadanya, karena khawatir tulisan ini jatuh ke tangan orang yang mata hatinya kabur dari mengidraknya lalu ia tersesat karenanya. Tidak semestinya dilupakan riwayat dari Nabi, semoga salam atasnya: *"Tidaklah seseorang menyampaikan kepada suatu kaum pembicaraan yang tidak dijangkau pemahaman mereka kecuali hal itu menjadi fitnah bagi sebagian mereka."*[^p112][^d55]

Aku memohon kepada Allah Ta'ala agar menyelamatkan kami. Siapa yang mengenal kadar dirinya, dan mengenal kekurangan dan kelemahannya, tidak akan meninggalkan firman Allah Ta'ala: *"sedangkan kamu tidak diberi pengetahuan melainkan sedikit"* (al-Isra': 85), demi memuji dan membenarkan dirinya sendiri.[^p113]

[^s13]: CM: Syekh yang dimaksud mungkin sama dengan tokoh yang dituju risalah-risalah sebelumnya, yaitu wazir Aḥmad bin Ibrāhīm al-Ḍabbī (w. 399 H); lihat catatan s1.

[^m-wahid]: **Satu, esa** (*wāḥid*, *waḥda*). Dalam *al-Mufradāt*: *waḥda* ialah kesendirian (*infirād*); *wāḥid* pada hakikatnya ialah sesuatu yang sama sekali tidak memiliki bagian, kemudian dipakai untuk setiap maujud, sehingga tidak ada bilangan kecuali sah disifati dengannya, seperti "sepuluh yang satu, seratus yang satu, seribu yang satu". Kemudian disebutkan cara-cara pemakaiannya, persis seperti dalam risalah ini, dengan penutup: "Kesatuan dalam semuanya bersifat aksidental; bila Allah Ta'ala disifati dengan *wāḥid*, maknanya ialah Dia yang tidak dapat dikenai pembagian dan tidak pula kebanyakan." Di sana ditambahkan: "Karena sulitnya kesatuan ini, Allah Ta'ala berfirman: *'Dan apabila yang disebut hanya nama Allah, kesal sekali hati orang-orang yang tidak beriman kepada akhirat'* (az-Zumar: 45)." (*al-Mufradāt*, s.v. *w-ḥ-d*.) *Kashshāf*: *waḥda* adalah lawan *kathra* (kebanyakan), dan keduanya termasuk makna yang jelas dengan sendirinya; para teolog mendefinisikannya sebagai keadaan sesuatu yang tidak terbagi kepada hal-hal yang sama dalam esensinya, dan membedakan kesatuan hakiki (seperti Yang Wajib Ada dan titik) dari kesatuan relatif (seperti Zaid yang terbagi kepada anggota-anggotanya). (*Kashshāf*, s.v. *al-waḥda*.) Seluruh bagian pertama risalah ini adalah uraian yang lebih luas dari entri *al-Mufradāt* tersebut.

[^p105]: CP: Seperti dalam *al-Mufradāt*, s.v. *w-ḥ-d*, disebut "enam cara" tetapi yang diuraikan hanya lima, dan sesudahnya dikatakan "Inilah lima cara". Para penyunting *al-Mufradāt* mencatat hal yang sama. Penyunting risalah ini menduga cara keenam adalah pemakaian *wāḥid* untuk Allah, yang dijelaskan sesudah kelima cara itu; dugaan itu masuk akal, sebab paragraf-paragraf sesudahnya memang menguraikan makna *wāḥid* bagi Allah sebagai kebalikan dari kelima cara tersebut. Kata *nasīj waḥdihi* (dalam teks tahkik: *shaykh*) dibetulkan oleh penyunting.

[^p106]: CP: Perbandingan antara satu dalam bilangan dan keesaan Allah adalah gagasan yang lazim dalam filsafat Neo-Platonis dan dalam tradisi Pythagoras, yang dikenal dalam dunia Islam antara lain melalui *Rasāʾil Ikhwān al-Ṣafāʾ*: satu adalah asal bilangan tetapi bukan bilangan, sebagaimana Allah adalah asal segala yang ada tetapi bukan salah satu dari yang ada. Al-Rāghib menukilnya dari "seorang bijak" dan menutupnya dengan penyucian: "Mahatinggi Allah dari penyerupaan", sebab perbandingan ini hanya berlaku pada segi kesatuan, bukan pada zat. Kalimat "ia ada sesudah setiap bilangan, tetapi tidak ada bilangan sesudahnya" agaknya berarti bahwa satu terkandung dalam setiap bilangan, sedang ia sendiri tidak mengandung bilangan apa pun. Kata *al-amdād* dibetulkan penyunting menjadi *al-aʿdād*.

[^m-ahad]: **Esa** (*aḥad*). Dalam *al-Mufradāt*: *aḥad* dipakai dalam dua macam: dalam penafian saja, dan dalam penetapan. Yang khusus dalam penafian ialah untuk mencakup jenis makhluk yang bertutur, meliputi yang sedikit dan yang banyak, berkumpul maupun terpisah, seperti "Tidak ada seorang pun di rumah"; karena itu ia tidak sah dipakai dalam penetapan, "sebab menafikan dua hal yang berlawanan itu sah, sedang menetapkan keduanya tidak sah". Yang dipakai dalam penetapan ada tiga cara: satu yang digabungkan dengan puluhan, yang disandarkan dalam arti "yang pertama", dan yang dipakai secara mutlak sebagai sifat, yang hanya untuk Allah Ta'ala, seperti al-Ikhlas: 1; "asalnya *waḥad*". (*al-Mufradāt*, s.v. *a-ḥ-d*.) Bagian kedua risalah ini sama persis dengan entri tersebut, dengan tambahan pembahasan tentang perbedaan *wāḥid* dan *aḥad* dan jawaban atas keberatan-keberatan.

[^p107]: CP: Edisi tahkik mencetak ayat ini dengan tambahan kata *aḥad* (*fa-mā aḥad minkum min aḥad*), dan penyunting mencatatnya sebagai bunyi naskah. Ayat dikutip menurut bunyinya dalam mushaf. Kalimat "karena ia mencakup satu dan yang lebih dari itu" juga terdapat dalam *al-Mufradāt*.

[^k-ahad]: **Esa** (*aḥad*). *Kashshāf*: asalnya *waḥad*; dalam *al-Itqān* disebutkan bahwa *aḥad* adalah nama yang lebih sempurna daripada *wāḥid*: bila dikatakan "tidak ada *wāḥid* yang sanggup menghadapinya", maknanya bisa saja dua orang atau lebih sanggup, berbeda dengan "tidak ada *aḥad*"; *aḥad* juga khusus untuk manusia, sama untuk laki-laki dan perempuan, dan tidak masuk ke dalam perkalian, pembagian, bilangan, dan hitungan; sedang Abū ʿUbayd berpendapat bahwa keduanya bermakna sama. (*Kashshāf*, s.v. *al-aḥad*.) Pembedaan al-Rāghib di sini lain: *wāḥid* sebagai bentuk pelaku menunjuk zat dan sifat, sedang *aḥad* sebagai masdar menunjuk kesatuan yang murni.

[^p108]: CP: Terjemahan Turki mengusulkan bahwa kata yang dimaksud adalah *fard* ("tunggal"), karena kata itulah yang terdapat dalam bait yang dikutip. Tetapi *al-Mufradāt*, s.v. *w-ḥ-d*, menunjukkan bahwa kata yang dibahas memang *waḥad*: "*Waḥad* ialah yang sendiri, dan ia dipakai untuk menyifati selain Allah Ta'ala, seperti kata penyair: *ʿalā mustaʾnisin waḥadi*." Kata itu terdapat pada bait al-Nābigha al-Dhubyānī sebelumnya ("seakan pelanaku, ketika siang telah condong, di Dhū al-Jalīl, berada di atas (seekor banteng) yang waspada dan sendirian"); risalah ini, atau penyalinnya, mengutip bait sesudahnya, yang berakhir dengan *al-fard*. Penyunting juga mencatat bahwa kutipan dalam *al-Mufradāt* lebih tepat. Wajrah adalah padang di antara Makkah dan Bashrah yang terkenal dengan satwa liarnya.

[^p109]: CP: Maksudnya ayat an-Nur: 45 lengkapnya: "di antaranya ada yang berjalan di atas perutnya, sebagian berjalan dengan dua kaki, sedang sebagian (yang lain) berjalan dengan empat kaki". Kata *man*, yang biasanya dipakai untuk makhluk berakal, dipakai untuk hewan yang berjalan dengan empat kaki karena didahului oleh kata *man* untuk yang berjalan dengan dua kaki, yang mencakup manusia. Penyair bait tentang bulan tidak diketahui; penyunting tidak menemukannya.

[^p110]: CP: Larik ini milik al-Mutanabbi; larik pertamanya: "Di sekelilingku di setiap tempat ada makhluk-makhluk dari mereka". Maksudnya: mereka seperti binatang, sehingga keliru menanyakan mereka dengan "siapa", kata tanya untuk makhluk berakal. Penyunting mengutip pula bait-bait tentang Bani al-Adram, yang menafikan mereka dari kabilah-kabilah Arab.

[^p111]: CP: Ungkapan "limpahan pertama Sang Pencipta atas segala maujud" (*awāʾil fayḍ al-bārī ʿalā al-mawjūdāt*) memakai istilah para filsuf tentang limpahan (*fayḍ*). Di sini al-Rāghib berhenti pada isyarat, dan menjelaskan dalam paragraf berikutnya mengapa ia tidak melanjutkannya. Kata *al-waḥda* dan *al-mawjūdāt* mengikuti pembetulan penyunting (teks: *al-wāḥida*, *al-wujūdāt*).

[^p112]: CP: Edisi tahkik membaca *mutaʾadhdhiyan* ("merasa terganggu"), yang oleh penyunting dibetulkan dari *mutaʾaddiban* ("karena sopan santun"); kami memahaminya "karena khawatir". Kata *fa-aṣlahu* yang tidak jelas kami baca *fa-yuḍilluhu* ("lalu menyesatkannya"), sesuai pemahaman terjemahan Turki. Penerjemah Turki mencatat bahwa ucapan ini diriwayatkan sebagai ucapan Abdullah bin Mas'ud dalam mukadimah *Ṣaḥīḥ Muslim*, bukan sebagai hadis marfu'.

[^d55]: CD: Hadis yang sama dan sikap yang sama terdapat dalam *al-Dharīʿa*, Pasal Kedua, "Wajibnya Mencegah Orang-Orang Bodoh dari Hakikat Ilmu dan Membatasi Mereka Sesuai Kadar Pemahaman Mereka": "Tidaklah seseorang menyampaikan kepada suatu kaum pembicaraan yang tidak dijangkau akal mereka kecuali hal itu menjadi fitnah bagi sebagian mereka." Terjemahan di atas mengikuti redaksi itu. Di sana pula dikutip ucapan Ali kepada Kumail bin Ziyad tentang ilmu yang tidak ia dapati orang yang sanggup memikulnya.

[^p113]: CP: Kalimat penutup ini ringkas dan kurang jelas dalam edisi tahkik (*fa-mā taraka qawl Allāh … tamadduḥan wa-muṣaḥḥiḥan*). Terjemahan Turki memahaminya: orang yang mengenal kadar dirinya menanamkan ayat ini dalam kalbunya, bukan terpesona oleh pujian dan pembenaran orang lain. Terjemahan di atas mengikuti makna itu.
