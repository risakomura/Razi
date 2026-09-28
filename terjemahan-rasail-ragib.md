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
| Sudah diterjemahkan | Risalah Pertama: mukadimah, Bab Pertama s.d. Keenam |
| Posisi berikutnya | Risalah Pertama, Bab Ketujuh |
| Nomor catatan terakhir | CM s5 · CP p36 · CD d16 · CT t1 |
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

[^d16]: CD: Penjelasan tentang *khalīl* sebagai "yang fakir kepada Allah" sejalan dengan pembagian makna *faqr* dalam *al-Dharīʿa*, Pasal Ketiga, "Kanaah dan Zuhud" (lihat nota kaki *al-Dharīʿa* no. 287). Dalam *al-Mufradāt*, s.v. *kh-l-l*, al-Rāghib memberi dua penjelasan untuk *"Dan Allah telah memilih Ibrahim menjadi kesayangan(-Nya)"* (an-Nisa': 125): Ibrahim dinamai *khalīl* karena kefakirannya kepada Allah dalam setiap keadaan, atau karena *khulla* berarti kasih sayang yang menyusup ke dalam jiwa; dan bila kata itu dipakai untuk Allah, yang dimaksud semata-mata berbuat baik. Di sini hanya penjelasan pertama yang dipakai, sebab penjelasan kedua akan menuntut timbal balik yang ditolak pada akhir bab ini.
