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
| Tahap | Penerjemahan berjalan |
| Sudah diterjemahkan | Risalah Pertama: mukadimah, Bab Pertama s.d. Ketiga |
| Posisi berikutnya | Risalah Pertama, Bab Keempat |
| Nomor catatan terakhir | CM s5 · CP p17 · CD d11 |
| Catatan istilah | lihat 3.3 |

---

## 1. Konvensi Markup (untuk Pembentukan DOCX)

Markup sama dengan terjemahan *al-Dharīʿa* dan *Tafṣīl*. Setiap baris hanya memuat satu unsur.

| Markup MD | Unsur | Gaya DOCX |
|---|---|---|
| `# Teks {.kitab-ke}` | Nomor risalah: Risalah Pertama, dst. | Kitab Ke |
| `# Teks {.judul-kitab}` | Judul risalah | Judul Kitab |
| `## Teks {.judul-bab}` | Bab di dalam risalah | Judul Bab |
| `### Teks {.judul-pasal}` | Subjudul di dalam bab (*faṣl*, "Pasal") | Judul Pasal |
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

(Disusun pada akhir penerjemahan.)

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

Adapun cinta karena keutamaan, yaitu cinta karena Dzat Allah Ta'ala, ia bersih dari semua cela ini.[^p12] Dialah yang dikecualikan dalam firman Allah Ta'ala: *"Teman-teman karib pada hari itu saling bermusuhan satu sama lain, kecuali mereka yang bertakwa"* (az-Zukhruf: 67). Itu pula yang dimaksud Abu al-Atahiyah dengan ucapannya:

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
