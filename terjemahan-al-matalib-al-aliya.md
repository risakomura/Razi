# al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī: Terjemahan Indonesia

**Karya:** Fakhr al-Dīn al-Rāzī (w. 606/1210), *al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī*
**Naskah dasar (Turki):** Fahreddin er-Râzî, *el-Metâlibü'l-Âliye mine'l-İlmi'l-İlâhî: Metafizik*, jilid 1 sampai 3, ed. Ekrem Demirli, terj. Ekrem Demirli, Eşref Altaş, Hayrettin Gödekli, Osman Demir, Istanbul: Fikriyat, 2022 (berkas `6659d7ee-matalib.docx`, hasil OCR)
**Naskah pembanding (Arab):** *al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī*, ed. Aḥmad Ḥijāzī al-Saqqā, Beirut: Dār al-Kitāb al-ʿArabī, 1407/1987 (berkas `e51348c0-matalib_arab.docx`, hasil OCR; urutan jilid dalam berkas acak)
**Rujukan istilah:** Glosarium v2.0 dan catatan Kashshāf dalam `terjemahan-asas-al-taqdis.md`; Muḥammad ʿAlī al-Tahānawī, *Kashshāf Iṣṭilāḥāt al-Funūn wa-l-ʿUlūm*, ed. Rafīq al-ʿAjam dan ʿAlī Daḥrūj, Beirut: Maktabat Lubnān Nāshirūn, 1996

---

## 0. Status Proyek dan Penanda Posisi

| Butir | Keterangan |
|---|---|
| Tahap | Penerjemahan berjalan: Mukadimah selesai, masuk Kitab Pertama |
| Sudah diterjemahkan | Pembuka; Mukadimah (Pasal 1 sampai 4) |
| Posisi berikutnya | Kitab Pertama, Persiapan (Tr. h. 31; berkas Turki baris 548; berkas Arab baris 10056) |
| Nomor catatan terakhir | CT: t6 · CA: a78 · CP: p4 |
| Catatan Kashshāf baru | istiqra, tasdiq, basira, riyada, maad |

---

## 1. Konvensi Markup (untuk Pembentukan DOCX)

Markup berikut dipakai secara ketat agar berkas ini dapat diubah langsung menjadi DOCX dengan gaya paragraf bernama (untuk InDesign). Setiap baris hanya memuat satu unsur.

| Markup MD | Unsur | Gaya DOCX |
|---|---|---|
| `# Teks {.kitab-ke}` | Nomor kitab (Kitab Pertama, dst.) | Kitab Ke |
| `# Teks {.judul-kitab}` | Judul kitab atau Mukadimah | Judul Kitab |
| `## Teks {.bagian-ke}` / `## Teks {.bab-ke}` | Nomor bagian (*kısım*/*qism*) atau bab (*bâb*) | Bagian Ke / Bab Ke |
| `## Teks {.judul-bagian}` / `## Teks {.judul-bab}` | Judul bagian atau bab | Judul Bagian / Judul Bab |
| `### Teks {.pasal-ke}` | Nomor pasal (*fasıl*/*faṣl*) | Pasal Ke |
| `### Teks {.judul-pasal}` | Judul pasal | Judul Pasal |
| `#### Teks {.subpasal}` | Subjudul di dalam pasal (Pengantar, Persiapan, dsb.) | Subpasal |
| `[Teks]{.basmalah}` (satu paragraf) | Basmalah pembuka | Basmalah |
| `[Teks]{.penanda}` (satu paragraf) | Penanda halaman edisi Turki/Arab | Penanda Sumber |
| Paragraf biasa | Teks isi (paragraf pertama sesudah judul otomatis menjadi Teks Isi Pertama) | Teks Isi / Teks Isi Pertama |
| `- (a) teks` | Butir berhuruf | Butir |
| `1. teks` | Butir bernomor | Butir Bernomor |
| `> teks` (satu larik per baris) | Syair | Syair |
| `**Label**:` di awal paragraf | Label argumen (Dalil Pertama, Premis Kedua, dst.) | Label Argumen (gaya karakter) |
| `*"kutipan"* (Surah: ayat)` | Kutipan ayat beserta rujukannya | Kutipan Ayat + Rujukan Ayat |
| `*"kutipan"*` tanpa rujukan ayat | Kutipan hadis atau ucapan | Kutipan Riwayat |
| `*kata*` lainnya | Transliterasi dan judul karya | Transliterasi |
| `[^tN]` | Catatan edisi Turki (awalan **CT:**) | Catatan Kaki |
| `[^aN]` | Catatan edisi Arab al-Saqqā (awalan **CA:**) | Catatan Kaki |
| `[^pN]` | Catatan penerjemah Indonesia (awalan **CP:**) | Catatan Kaki |
| `[^k-…]` | Catatan istilah *Kashshāf* | Catatan Kaki |

Definisi catatan kaki (`[^id]: …`) diletakkan tepat sesudah paragraf yang merujuknya.

---

## 2. Keputusan Kerja

1. **Teks dasar:** terjemahan Turki edisi Fikriyat. Teks Arab edisi al-Saqqā dipakai untuk memverifikasi makna, memulihkan istilah teknis, dan membetulkan bagian yang kacau dalam terjemahan Turki. Penyimpangan yang berarti dicatat dalam catatan **CP**.
2. **Bagian yang tidak diterjemahkan:** pengantar editor (*Sunuş*), biografi ar-Razi oleh Eşref Altaş, dan daftar isi edisi Turki, karena bukan bagian dari karya ar-Razi.
3. **Catatan kaki:** semua catatan edisi Turki diterjemahkan (awalan **CT:**), dan semua catatan edisi Arab al-Saqqā diterjemahkan (awalan **CA:**), termasuk catatan perbedaan naskah. Siglum naskah edisi Arab ditulis dengan huruf Latin padanannya: س = S, ن = N, ز = Z, ط = Ṭ, ل = L. Bacaan varian dikutip dalam transliterasi. Catatan yang teksnya rusak dalam berkas OCR ditandai "(sebagian tidak terbaca)". Letak catatan CA di badan teks mengikuti letak kata yang dirujuknya; bila penanda aslinya hilang dalam OCR, letaknya ditentukan dari isi catatan.
4. **Rujukan Al-Qur'an** dari kedua edisi tidak dijadikan catatan kaki, tetapi dicantumkan di badan teks sesudah kutipan dengan format (Nama Surah: ayat). Rujukan yang keliru dalam salah satu edisi dibetulkan tanpa catatan.
5. **Kutipan Al-Qur'an** mengikuti gaya Terjemahan Kemenag RI.
6. **Tanpa aksara Arab:** badan teks dan catatan kaki tidak memuat aksara Arab. Istilah konseptual diberi transliterasi IJMES pada kemunculan pertama, misalnya: akal dan abstrak (*maʿqūl mujarrad*).
7. **Glosarium:** Glosarium v2.0 *Asās al-Taqdīs* berlaku sepenuhnya. Istilah baru dicatat di bagian 3 berkas ini.
8. **Catatan Kashshāf:** istilah yang sudah diberi catatan Kashshāf dalam *Asās al-Taqdīs* (lihat daftar di 3.2) tidak diberi catatan lagi. Istilah falsafah dan kalam yang baru diberi catatan Kashshāf pada kemunculan pertamanya, dengan format yang sama.
9. **Nama tokoh dan aliran** ditulis dalam bentuk lazim Indonesia (Ibnu Sina, al-Ghazali, Aristoteles, Euklides). Judul karya ditulis dalam transliterasi IJMES.
10. **Tanpa tanda pisah panjang** (em dash) dan tanpa tanda pisah menengah (en dash).

---

## 3. Glosarium Tambahan *al-Maṭālib*

Kolom dan sumber padanan Inggris mengikuti Glosarium v2.0 *Asās al-Taqdīs*. Tanda † menandai istilah yang diberi catatan Kashshāf di berkas ini.

### 3.1 Istilah Baru

| Bentuk Arab | Transliterasi | Padanan Inggris (*Kashshāf*) | Padanan Indonesia | Catatan |
|---|---|---|---|---|
| العلم الإلهي | al-ʿilm al-ilāhī | - | **ilmu ilahi** (metafisika) | Edisi Turki: *metafizik*. Pada kemunculan pertama diberi keterangan "metafisika". |
| الأولى والأخلق | al-awlā wa-l-akhlaq | - | **yang lebih utama dan lebih layak** | Tingkat kepastian di bawah keyakinan pasti. |
| الجزم المانع من النقيض | al-jazm al-māniʿ min al-naqīḍ | - | **kepastian yang menutup kemungkinan sebaliknya** | |
| استقراء | istiqrāʾ | induction | **induksi** † | |
| حدس | ḥads | - | **intuisi** | |
| تصور / تصديق | taṣawwur / taṣdīq | - / assent | **konsepsi** / **pembenaran** † | Pasangan dalam logika. Catatan Kashshāf pada *taṣdīq*. |
| كسبي | kasbī | - | **perolehan** (pengetahuan hasil usaha) | Lawan *badīhī*. |
| بصيرة | baṣīra | perspicacity, sagacity | **mata batin** † | |
| رياضة / مجاهدة | riyāḍa / mujāhada | practice of piety, asceticism | **latihan rohani** / **perjuangan batin** † | |
| مكاشفة | mukāshafa | - | **penyingkapan** | |
| المبدأ الأول | al-mabdaʾ al-awwal | - | **Prinsip Pertama** | |
| المبدأ والمعاد | al-mabdaʾ wa-l-maʿād | hereafter, resurrection, afterworld (*maʿād*) | **asal-mula dan tempat kembali** † | Catatan Kashshāf pada *maʿād*. |
| سعادة / شقاوة | saʿāda / shaqāwa | happiness | **kebahagiaan** / **kesengsaraan** | |
| الحكماء الإلهيون | al-ḥukamāʾ al-ilāhiyyūn | - | **para filsuf ketuhanan** | |
| مرجح | murajjiḥ | - | **penentu keunggulan** | Mengikuti Glosarium *Asās*. |
| مؤثر | muʾaththir | - | **pemberi pengaruh** | Mengikuti Glosarium *Asās*. |

### 3.2 Istilah yang Sudah Bercatatan Kashshāf di *Asās al-Taqdīs* (tidak diberi catatan lagi)

sifat, penyerupaan, penafian, kuasa, maujud/wujud, indra, ruang, alam, dalil, niscaya, swabukti, nazari, daya waham, daya khayal, abstrak, terpahami oleh akal, esensi, posisi, hakikat, wadah, ukuran, bentuk, bentangan, hakikat terdalam, zat, regresi tak berhingga, kemungkinan, kebaharuan, bertempat di dalam, mustahil, qadim, kaum Dahriyah, tauhid, kaum Musyabbihah, Muktazilah, akal, hayula, para filsuf (hikmah), dugaan, Karramiyah, jisim, makna, mutasyabih, substansi, aksiden, atom, yang menempati ruang, burhan, ketertentuan, pengkhusus, ketiadaan, padanan (keserupaan), kelaziman, tara, global, genus, jiwa rasional, relasi, sofisme, lingkaran (daur), keserupaan lafaz, makna lahiriah, takwil, para mutakalim, kinayah, majaz, mutawatir, metafora, petunjuk (qarinah), Hasywiyah, wajib.

---

# TERJEMAHAN

[Dengan nama Allah Yang Maha Pengasih, Maha Penyayang.]{.basmalah}

Junjungan kami, sang imam yang menyeru kepada Allah, Abu Abdillah Muhammad bin Umar bin al-Husain ar-Razi, semoga Allah meridainya, berkata:

Bagian *al-Maṭālib al-ʿĀliya* ini membahas ilmu ilahi (*al-ʿilm al-ilāhī*), yakni metafisika, yang dalam bahasa Yunani disebut *uthūlūjiyā* (teologi). Bagian ini tersusun atas satu mukadimah dan beberapa kitab.[^a1]

[^a1]: CA: Dalam salah satu naskah (siglumnya tidak terbaca), setiap kitab disebut *juzʾ* (bagian).

# Mukadimah {.judul-kitab}

[Tr. h. 3]{.penanda}

Mukadimah ini terdiri atas empat pasal.

**Pasal Pertama**: penjelasan bahwa ilmu ilahi adalah ilmu yang paling mulia dari segala segi.

**Pasal Kedua**: dapatkah akal manusia mencapai keputusan dan kepastian dalam ilmu ilahi, ataukah dalam sebagian bidang dan masalahnya akal hanya dapat berpegang pada yang lebih utama dan lebih layak?

**Pasal Ketiga**: apakah jalan menuju pengetahuan-pengetahuan yang mulia ini satu, ataukah lebih dari satu?

**Pasal Keempat**: apa saja masalah-masalah pokok ilmu ini?

### Pasal Pertama {.pasal-ke}

### Ilmu Ilahi adalah Ilmu yang Paling Mulia dari Segala Segi {.judul-pasal}

[Tr. h. 4]{.penanda}

Ketahuilah, kemuliaan suatu ilmu tampak dari beberapa segi.

**Segi pertama**: kemuliaan suatu ilmu ditentukan oleh kemuliaan hal yang dikajinya. Dalam ilmu ilahi yang dikaji adalah Zat Allah Yang Mahatinggi dan sifat-sifat-Nya, sedangkan Allah secara mutlak adalah maujud yang paling mulia. Bahwa Allah adalah maujud yang paling mulia dapat ditunjukkan dari beberapa segi.

1. Allah tidak membutuhkan pelaku (*fāʿil*) yang mengadakan-Nya dan tidak pula penerima (*qābil*) yang menanggung wujud-Nya, sedangkan segala sesuatu selain-Nya membutuhkan-Nya.
2. Allah Esa secara mutlak dari segala segi, sehingga Dia tidak membutuhkan bagian yang menegakkan-Nya.
3. Hanya Allah yang wajib karena zat-Nya. Segala sesuatu selain-Nya adalah mungkin karena zatnya dan membutuhkan pemberi pengaruh (*muʾaththir*). Karena itu, segala sesuatu selain-Nya membutuhkan Allah, sedangkan Allah tidak membutuhkan apa pun. Maka Allah pasti maujud yang paling mulia.
4. Yang mungkin membutuhkan pemberi pengaruh, baik ketika ia mulai ada maupun ketika wujudnya berlangsung. Segala sesuatu selain-Nya, baik ketika mulai ada maupun ketika bertahan, selalu membutuhkan-Nya. Bahkan, sebagaimana yang mungkin membutuhkan-Nya dari sisi wujud, ia pun membutuhkan-Nya dari sisi ketiadaan. Sebab, yang mungkin tidaklah tiada karena dirinya sendiri; ketiadaannya bergantung pada kaidah "sebab ketiadaan adalah ketiadaan sebab". Dengan uraian ini tetaplah bahwa Allah Yang Mahabenar lebih mulia daripada selain-Nya dari segi-segi tersebut.
5. Wujud lebih mulia daripada ketiadaan. Yang wajib karena zatnya sama sekali tidak menerima ketiadaan. Maka Allah maujud karena Zat-Nya, dan dengan wujud-Nya setiap maujud memperoleh wujud; bahkan wujud-Nya seakan-akan penafian terhadap ketiadaan. Adapun segala sesuatu selain-Nya adalah mungkin karena zatnya, dan yang mungkin karena zatnya, bila dipandang dari segi dirinya sendiri, tidak maujud. Jadi, segala sesuatu selain-Nya, bila dipandang dari segi dirinya sendiri, tidak maujud, sedangkan Allah, bila dipandang dari segi Diri-Nya sendiri, maujud. Dalam pengertian inilah kami katakan: Dialah Yang Mahabenar (*al-Ḥaqq*), dan selain-Nya batil. Bahkan yang benar, kata "benar" hanya layak bagi-Nya, dan suatu keyakinan hanya layak disifati benar bila ia adalah keyakinan akan wujud-Nya[^a2] dan akan kefanaan murni serta kebinasaan mutlak segala sesuatu selain-Nya. Sebagaimana difirmankan dalam Kitab Ilahi, *"Segala sesuatu pasti binasa, kecuali Zat-Nya"* (al-Qashash: 88).

[^a2]: CA: Naskah S: *bi-iʿtiqādih* (dengan keyakinannya).

Dengan dalil-dalil ini tetaplah bahwa Allah Ta'ala adalah maujud yang paling mulia dan paling sempurna; bahkan Dia terlalu mulia dan terlalu sempurna untuk dibandingkan dengan selain-Nya.[^a3] Jika hal ini telah tetap, kami katakan: kemuliaan pengetahuan mengikuti kemuliaan yang diketahui. Bila yang diketahui adalah yang paling mulia, pengetahuan tentangnya pun pengetahuan yang paling mulia. Karena Allah Ta'ala adalah yang paling mulia di antara segala yang diketahui, ilmu tentang-Nya pastilah ilmu yang paling mulia.

[^a3]: CA: Naskah S: "dan lebih sempurna untuk dibandingkan dengan selain-Nya, sebab Dia lebih mulia dan lebih sempurna daripadanya. Jika telah tetap …, dst."

**Segi kedua**: keutamaan ilmu ilahi juga dapat dijelaskan dari segi kebutuhan manusia kepadanya dan kesempurnaan manfaatnya. Dari segi kebutuhan manusia dan kesempurnaan manfaat yang diperolehnya, ilmu yang paling mulia tidak lain adalah ilmu ilahi. Sebab, tujuan pokok menuntut ilmu adalah meraih kebahagiaan (*saʿāda*) dan terbebas dari kesengsaraan (*shaqāwa*). Kebahagiaan itu adakalanya jasmani, adakalanya rohani. Dalil-dalil falsafah dan tanda-tanda yang benar menunjukkan bahwa kebahagiaan jasmani itu rendah. Di antara dalil-dalil itu:

- (a) Dalil yang paling sederhana dalam hal ini ialah bahwa hewan-hewan yang hina pun turut serta dengan manusia dalam kenikmatan jasmani. Bahkan induksi (*istiqrāʾ*)[^k-istiqra] menunjukkan bahwa dalam kenikmatan-kenikmatan itu hewan-hewan hina tersebut lebih kuat dan lebih sempurna daripada manusia.
- (b) Intuisi (*ḥads*) dan induksi menunjukkan bahwa tenggelam dalam mengejar kenikmatan-kenikmatan itu menarik jiwa dari puncak alam arwah yang suci ke dasar alam kebinatangan.
- (c) Kenikmatan-kenikmatan itu cepat berlalu dan segera habis, sedangkan kenikmatan rohani terpelihara dari kelenyapan dan kebinasaan.
- (d) Banyak mengejar kenikmatan jasmani adalah perbuatan rendah, sebagaimana disaksikan oleh tabiat seluruh makhluk. Setiap orang sepakat bahwa manusia yang menghabiskan seluruh waktunya untuk makan dan bersetubuh adalah orang yang buruk akhlaknya, rendah cita-citanya, dan tak ubahnya binatang. Sebaliknya, bila seseorang diyakini sedikit mengejar kenikmatan jasmani seperti makan dan bersetubuh, tabiat setiap orang berakal akan mendorongnya untuk menghormati orang itu dan mengakui ketinggian derajat serta kesempurnaan keutamaannya. Karena itu, orang awam, bila mengira seseorang sedikit perhatiannya pada makan, minum, dan persetubuhan, meyakini bahwa ia layak dihormati dan dilayani, dan di hadapannya mereka menempatkan diri seperti pelayan di hadapan tuannya. Semua ini menunjukkan bahwa kebahagiaan jasmani itu rendah dan hina.

[^k-istiqra]: **Induksi** (*istiqrāʾ*; Ing. *induction*). Secara bahasa, *istiqrāʾ* berarti menelusuri. Menurut para ahli logika, induksi adalah argumen yang tersusun dari proposisi-proposisi yang memuat hukum atas hal-hal partikular untuk menetapkan suatu hukum universal. Induksi ada dua: induksi sempurna, yang disebut juga silogisme pembagian (*qiyās muqassim*), yaitu berdalil dengan seluruh partikular lalu menghukumi keseluruhannya, dan ini menghasilkan keyakinan; serta induksi tidak sempurna, yaitu berdalil dengan sebagian besar partikular saja, dan ini hanya menghasilkan dugaan, seperti menyimpulkan bahwa setiap hewan menggerakkan rahang bawahnya ketika mengunyah, padahal buaya tidak demikian. (*Kashshāf*, s.v. *al-istiqrāʾ*.)

Adapun kebahagiaan rohani bersifat kekal, abadi, luhur, dan mulia. Ia menarik jiwa manusia dari dasar kebinatangan ke puncak kemalaikatan, dan dari kegelapan alam jisim ke martabat tinggi alam-alam suci yang murni. Sebagaimana difirmankan dalam Kitab Ilahi, *"Amal kebajikan yang kekal itu lebih baik pahalanya di sisi Tuhanmu serta lebih baik untuk menjadi harapan"* (al-Kahf: 46). Pemilik wahyu dan syariat, Nabi shallallahu 'alaihi wasallam, bersabda dalam hadis qudsi yang beliau riwayatkan dari Tuhan Yang Mahaperkasa, *"Aku adalah teman duduk orang yang mengingat-Ku."*[^t1]

[^t1]: CT: al-Bayhaqī, *al-Jāmiʿ li-Shuʿab al-Īmān*, ed. ʿAbd al-ʿAlī ʿAbd al-Ḥamīd Ḥāmid (Riyad: Maktabat al-Rushd, 2003), no. 670.

Dari uraian ini tampak bahwa kebahagiaan rohani lebih utama daripada kebahagiaan jasmani. Kebahagiaan rohani yang paling depan, yang menjadi pemimpin, inti, dan sarinya, adalah mengenal Prinsip Pertama (*al-mabdaʾ al-awwal*), sifat-sifat-Nya yang luhur, dan sifat-sifat kesempurnaan serta keagungan-Nya. Dalil-dalil kenabian dan pengetahuan-pengetahuan falsafah menunjukkan bahwa tidak mengenal Prinsip Pertama mengakibatkan azab yang terus-menerus dan kerugian dari segala segi, sedangkan mengenal-Nya mendatangkan kebahagiaan abadi dan kemuliaan yang tak terputus. Maka ilmu ilahi pastilah pemuka dan pemimpin segala ilmu, serta pengetahuan yang paling mulia dan paling utama.

**Segi ketiga**: manusia yang sempurna mendapati dari dirinya sendiri bahwa semakin sempurna ruhnya tenggelam dalam pengetahuan-pengetahuan ini, semakin dalam ia menyelaminya, dan semakin kuat ia tertarik kepadanya dengan memutuskan diri dari selainnya,[^a4] semakin sempurna pula kegembiraannya akan dirinya, semakin sempurna kekuatan ruhnya, dan semakin besar sukacitanya. Bila keadaannya sebaliknya, keadaan-keadaan rohani dan pengaruh-pengaruh kejiwaan pun menjadi kebalikan dari yang kami sebutkan.[^a5] Semua ini menunjukkan bahwa segala kebahagiaan terikat pada sebab ini, dan bahwa segala kesempurnaan dan kebaikan terbit dari ufuk ini. Sebagaimana difirmankan dalam Kitab Ilahi, *"Ingatlah, hanya dengan mengingat Allah hati menjadi tenteram"* (ar-Ra'd: 28).

[^a4]: CA: Naskah S: "tenggelamnya dalam pengetahuan-pengetahuan ini" (*istighrāquhu fī hādhihi al-maʿārif*).

[^a5]: CA: Kata "kebalikan" (*bi-l-ʿaks*) dalam kalimat ini ditambahkan dari naskah N (sebagian tidak terbaca).

**Segi keempat**: kemaslahatan yang diperhitungkan manusia adakalanya kemaslahatan kehidupan dunia, adakalanya kemaslahatan tempat kembali. Kemaslahatan kehidupan dunia hanya tertata dengan mengenal asal-mula dan tempat kembali (*al-mabdaʾ wa-l-maʿād*). Sebab, seandainya syariat-syariat yang benar tidak tegak, niscaya tatanan akan lenyap, kemaslahatan akan kacau, kekacauan akan merajalela, dan tak seorang pun merasa aman atas nyawanya dan orang yang dicintainya. Adapun kemaslahatan tempat kembali, tak satu pun darinya sempurna kecuali dengan mengenal Allah Ta'ala, para malaikat-Nya, kitab-kitab-Nya, rasul-rasul-Nya, dan hari akhir; dan semua itu hanya diperoleh melalui ilmu ilahi.

Maka tampaklah dari pembahasan yang telah kami tetapkan ini bahwa asal segala kebaikan, tempat terbitnya kebahagiaan, dan sumber keutamaan adalah ilmu ini. Barang siapa menguasainya sebagaimana mestinya, ia berada pada martabat terakhir kemanusiaan dan martabat pertama kemalaikatan.

### Pasal Kedua {.pasal-ke}

### Dapatkah Akal Mencapai Keputusan dan Kepastian dalam Ilmu Ilahi, ataukah dalam Sebagian Bidang dan Masalahnya Akal Hanya Dapat Berpegang pada yang Lebih Utama dan Lebih Layak? {.judul-pasal}

[Tr. h. 9]{.penanda}

Dalam sebuah kitab aku membaca ucapan yang dinukil dari para tokoh hikmah dan pilar-pilar falsafah: puncak yang dapat dicapai dalam bidang ini adalah berpegang pada yang lebih utama dan lebih layak (*al-awlā wa-l-akhlaq*),[^a6] serta memilih sisi yang lebih utama dan lebih sempurna; adapun kepastian yang menutup kemungkinan sebaliknya (*al-jazm al-māniʿ min al-naqīḍ*), dalam sebagian pembahasan boleh jadi mustahil diperoleh.

[^a6]: CA: Frasa "yang lebih utama dan lebih layak" ditambahkan dari naskah S.

Para penganut pendapat ini[^a7] berhujah dengan beberapa segi.

[^a7]: CA: Naskah S: "orang yang berpendapat" (bentuk tunggal).

**Hujah pertama**: di antara segala yang diketahui, yang paling jelas bagi semua orang berakal adalah pengetahuan manusia tentang zat dirinya yang khusus[^a8] dan jiwanya yang khusus. Namun pengetahuan ini, meskipun merupakan pengetahuan yang paling jelas dan paling terang, telah mencapai tingkat kesulitan dan ketersembunyian yang membuat akal tak sanggup mencapainya. Jika demikian keadaan hal yang paling jelas diketahui, lalu bagaimana keadaan Zat yang paling jauh dari keserupaan dengan hal-hal yang diketahui makhluk? Hujah ini hanya tuntas dengan menetapkan beberapa premis.

[^a8]: CA: Naskah S: "tentang dirinya dengan zatnya" (*bi-dhātih*).

**Premis pertama**: yang paling jelas diketahui oleh setiap orang adalah zat dirinya yang khusus. Dalilnya: siapa pun yang mengetahui sesuatu pasti mengetahui bahwa dirinya mengetahui sesuatu itu; karena itu ia berkata, "Aku telah mencerap dan mengetahui hal ini." Namun pengetahuannya bahwa ia mengetahui sesuatu itu didahului oleh pengetahuannya tentang zat dirinya yang khusus. Sebab, bagaimana mungkin orang yang tidak mengenal zat dirinya menghukumi dirinya sebagai yang mengetahui hal itu?[^a9] Mereka juga berkata: setiap pembenaran (*taṣdīq*)[^k-tasdiq] didahului[^a10] oleh konsepsi (*taṣawwur*), dan jelas bahwa syarat mendahului yang disyarati dalam urutan martabat. Ini menunjukkan bahwa pengetahuan setiap orang tentang apa pun yang diketahuinya disyarati oleh pengetahuannya tentang zat dirinya yang khusus[^a11] dan didahului olehnya. Maka tetaplah bahwa pengetahuan setiap orang tentang dirinya mendahului pengetahuannya tentang segala sesuatu selain dirinya, baik pengetahuan itu termasuk hal-hal swabukti yang terang[^a12] maupun pengetahuan perolehan (*kasbī*). Dan sesuatu yang mendahului seluruh pengetahuan swabukti tentu lebih layak lagi untuk menjadi swabukti. Maka dengan pembuktian ini tetaplah bahwa pengetahuan manusia tentang zat dirinya yang khusus adalah pengetahuan yang paling jelas, paling terang, dan paling kuat.

[^a9]: CA: Kalimat "Sebab, bagaimana mungkin … hal itu?" ditambahkan dari naskah N.

[^k-tasdiq]: **Pembenaran** (*taṣdīq*; Ing. *assent*). Secara bahasa, *taṣdīq* adalah menisbahkan kebenaran kepada seorang penutur, dengan hati atau lisan; lawannya adalah pengingkaran dan pendustaan. Para ulama berbeda pendapat tentang hubungannya dengan *taṣdīq* dalam logika, yaitu penerimaan akal atas hubungan penuh yang bersifat berita dalam suatu proposisi, yang merupakan pasangan *taṣawwur* (konsepsi). Sebagian, seperti Ṣadr al-Sharīʿa, memandang pembenaran menurut bahasa lebih khusus daripada pembenaran menurut logika, karena yang pertama menuntut kepatuhan dan penerimaan yang disengaja. (*Kashshāf*, s.v. *al-taṣdīq*.)

[^a10]: CA: Naskah S: "didahului" dengan kata *muqaddam* sebagai ganti *sābiq*.

[^a11]: CA: Frasa "dan didahului olehnya" (*wa-masbūq bi-ʿilmih bi-dhātih al-makhṣūṣa*) ditambahkan dari naskah N.

[^a12]: CA: Naskah S: *al-badīhiyyāt* (hal-hal swabukti) tanpa kata "yang terang".

**Premis kedua**: menjelaskan bahwa pengetahuan setiap orang tentang zat dirinya yang khusus adalah pengetahuan yang amat sulit dan tersembunyi. Dalilnya: yang ditunjuk setiap orang dengan ucapan "aku" adakalanya tubuh yang tampak ini, adakalanya salah satu jisim yang ada di dalam tubuh ini, adakalanya salah satu sifat tubuh ini, dan adakalanya substansi yang terlepas dari tubuh ini dan dari keterkaitan-keterkaitannya. Mengenai keempat kemungkinan ini akal orang-orang berakal telah kebingungan dan kepala mereka pening dalam menentukannya. Siapa pun yang merenungkan pembahasan tentang jiwa akan mendapati bahwa masalah ini telah mencapai puncak kesulitan. Maka tetaplah bahwa pengetahuan ini sulit dan pelik.

**Premis ketiga**: telah kami jelaskan bahwa yang paling jelas diketahui adalah pengetahuan setiap orang tentang zat dirinya yang khusus dan jiwanya yang tertentu,[^a13] dan telah kami jelaskan pula bahwa pengetahuan itu, meskipun paling jelas, telah mencapai puncak[^a14] kesulitan, ketersembunyian, dan kepelikan.

[^a13]: CA: Kata "yang tertentu" (*al-muʿayyana*) ditambahkan dari naskah N.

[^a14]: CA: Kata "puncak" (*al-quṣwā*) ditambahkan dari naskah S.

Jika hal ini telah tetap, kami katakan: Zat Allah Yang Mahasuci berbeda, dalam esensi dan hakikat-Nya, dari seluruh jenis hal yang mungkin dan yang baharu. Bila pengetahuan tentang hal yang paling jelas diketahui telah mencapai batas ketersembunyian dan kepelikan sebagaimana kami sebutkan, maka pengetahuan tentang sifat-sifat Maujud yang sama sekali tidak menyerupai sesuatu pun dari hal-hal yang mungkin dan tidak memiliki keserupaan dengan apa pun, yang amat jauh dari keserupaan dengan hal-hal terpahami dan dari kemiripan dengan apa pun yang dapat dicapai pikiran, ingatan, daya waham, dan daya khayal, tentu lebih layak lagi untuk menjadi sulit dan pelik. Maka tetaplah bahwa ilmu yang mulia ini terlalu tinggi dan agung untuk diliputi akal secara sempurna, dan bahwa bagi akal manusia tidak ada jalan di dalamnya selain berpegang pada yang lebih utama, lebih layak, lebih sempurna, dan lebih baik.

Hujah ini dapat pula diuraikan dengan cara lain. Induksi menunjukkan bahwa pengetahuan yang paling jelas bagi manusia ada beberapa: pengetahuan setiap orang tentang dirinya, tentang tempat dan waktunya, dan tentang keadaannya sebagai jisim. Namun ketika akal menyelami pengetahuan tentang jiwa, jisim, tempat, dan waktu, ia jatuh ke dalam kebingungan yang tak dapat ia keluar darinya. Jika demikian keadaan akal dalam mengenal hal yang paling jelas, lalu bagaimana keadaannya dalam mengenal hal yang paling tersembunyi? Mari kita jelaskan kebenaran uraian kami.

Pertama, pengetahuan seseorang tentang zat dirinya. Hakikat perkara ini telah kami jelaskan di atas.

Kedua, pengetahuannya tentang tempat dan waktu. Setiap orang, dengan akal sehatnya yang swabukti, memutuskan bahwa ia berada di tempat ini, lalu berpindah darinya ke tempat lain, dan bahwa sebelumnya ia berada di tempat yang pertama itu; dan pengetahuan tentang tempat adalah bagian dari pengetahuan tersebut. Setiap orang pun, dengan akal sehatnya yang swabukti, memutuskan bahwa waktu tertentu ini adalah waktu anu, lalu sesudahnya ia berkata bahwa waktu itu telah berlalu dan datang waktu yang lain; dan pengetahuan tentang hakikat waktu dan rentang masa adalah bagian dari pengetahuan bahwa waktu pertama telah berlalu dan waktu kedua telah datang. Namun dalam mengenal hakikat tempat dan waktu, kepala orang-orang berakal pening dan akal mereka kebingungan. Mengenai tempat, para pengikut Plato dan semua filsuf terkemuka sebelumnya[^a15] sepakat bahwa tempat adalah bentangan dimensi, sedangkan para pengikut Aristoteles sepakat bahwa tempat tidak lain adalah permukaan yang melingkupi, dan bahwa pendapat yang menyamakan tempat dengan dimensi batil. Kesulitan masalah ini tampak dalam pembahasan tentang tempat. Mengenai waktu, akal pun kebingungan dan kepala pening dalam mengenalnya. Bila engkau merenungkan masalah waktu dan akalmu meliputi rahasia-rahasia yang dalam[^a16] dan titik-titik yang halus dalam masalah-masalahnya, engkau akan tahu bahwa masalah ini telah mencapai batas terjauh dan titik paling ujung dalam kesulitan dan ketersembunyian.[^a17]

[^a15]: CA: Naskah S: "Aristoteles" sebagai ganti "Plato". Catatan lain di tempat ini sebagian tidak terbaca.

[^a16]: CA: Naskah S: "rahasia-rahasia yang dalam pada masalah-masalah itu".

[^a17]: CA: Kata "dan ketersembunyian" ditambahkan dari naskah N.

Ketiga, pengetahuan tentang hakikat jisim. Akal juga kebingungan apakah jisim tersusun dari bagian-bagian yang tak dapat dibagi lagi, ataukah tidak demikian, melainkan dapat dibagi tanpa akhir. Siapa pun yang menyelami masalah ini dan mengetahui kuatnya dalil-dalil kedua belah pihak akan tahu bahwa pada akhirnya akal tidak memperoleh apa-apa selain kebingungan dan keterpanaan, serta berpegang pada yang lebih utama dan lebih layak.

Maka tetaplah dengan induksi ini bahwa yang diperoleh akal dalam mengenal[^a18] hal-hal yang paling jelas diketahui tidak lain adalah kebingungan dan keterpanaan belaka, serta berpegang pada yang lebih utama dan lebih layak. Lalu bagaimana dugaanmu tentang akal ketika ia naik menuju pintu[^a19] keagungan Allah Ta'ala, dan ketika ia berusaha menyelami hakikat terdalam keperkasaan-Nya, kemandirian-Nya dari segala sesuatu, dan sifat-sifat keagungan dan kemuliaan-Nya, seperti ilmu, kuasa, dan hikmah-Nya? Inilah ringkasan pembahasan dalam bab ini.

[^a18]: CA: Kata "mengenal" (*maʿrifa*) ditambahkan dari naskah N.

[^a19]: CA: Kata "pintu" (*bāb*) ditambahkan dari naskah N.

Yang semakin menegaskan uraian ini[^a20] ialah bahwa, menurut kesepakatan mayoritas orang berakal, pembahasan rasional yang paling kokoh adalah pembahasan geometri. Renungkanlah kitab Euklides. Ia berkata bahwa jenis-jenis bangun bersegi banyak dimulai dari segitiga dan berlanjut tanpa akhir. Kemudian Euklides menegakkan hujah untuk menetapkan segitiga dan segi empat pada makalah pertama. Ketika hendak menetapkan segi lima, ia perlu mendahuluinya dengan satu premis, yaitu melukis segitiga yang masing-masing sudut alasnya dua kali sudut puncaknya,[^a21] lalu membagi dua masing-masing sudut alas itu; dengan cara ini ia mampu melukis segi lima.[^t2][^p1] Kemudian, setelah menegakkan burhan[^a22] bahwa jari-jari setiap lingkaran sama dengan tali busur seperenam lingkaran itu, ia pun mampu dengan cara ini melukis segi enam. Sesudah itu ia melompat[^a23] ke bangun bersegi lima belas. Sebab lompatan ini: untuk melukis segi tujuh[^a24] ia perlu terlebih dahulu melukis segitiga yang masing-masing sudut alasnya tiga kali sudut puncaknya, sedangkan lukisan-lukisan dalam kitab Euklides tidak memadai untuk menegakkan burhan atas hal itu; hal itu hanya dapat ditetapkan dengan irisan-irisan kerucut. Euklides tidak mampu melakukannya, lalu meninggalkannya. Demikian pula, ia tidak dapat menetapkan lukisan segi sembilan kecuali dengan salah satu dari dua cara. Pertama, melukis segitiga sama sisi lalu membagi masing-masing dari ketiga sudutnya menjadi tiga bagian yang sama, padahal telah kami jelaskan bahwa hal ini hanya tuntas dengan irisan-irisan kerucut. Kedua, melukis segitiga yang masing-masing sudut alasnya empat kali sudut puncaknya, dan Euklides tidak mampu melakukannya. Adapun bangun yang dilingkupi sebelas sisi hanya dapat dilukis dengan terlebih dahulu melukis segitiga yang masing-masing sudut alasnya lima kali sudut puncaknya, dan ia tidak mampu melakukannya. Begitu pula bangun yang dilingkupi tiga belas sisi, yang hanya dapat dilukis dengan melukis segitiga yang masing-masing sudut alasnya enam kali sudut puncaknya, dan ia tidak mampu melakukannya. Adapun bangun bersegi lima belas, ia mampu melukisnya dengan premis-premis yang telah ia tetapkan dalam kitabnya. Ia melukis segitiga sama sisi di dalam lingkaran sehingga lingkaran terbagi menjadi tiga bagian yang sama; lalu pada salah satu bagian itu ia menempatkan jari-jari lingkaran,[^a25] yaitu tali busur segi enam; kemudian ia membagi dua sisanya. Dengan cara ini ia membagi setiap dua busur[^a26] menjadi lima bagian yang sama, sehingga diperolehlah bangun yang dilingkupi lima belas sisi. Di situlah karyanya berhenti, dan ia tidak mampu menambah lagi.

[^a20]: CA: Naskah S: "yang semakin menegaskan pembahasan ini".

[^a21]: CA: Naskah N: "dua kali sudut puncak" (*ḍiʿfan li-l-zāwiya*), sebagai ganti "condong ke sudut puncak" (*munʿaṭifan ilā al-zāwiya*) dalam naskah lain.

[^t2]: CT: Diterjemahkan dengan memperhatikan bacaan dalam naskah Perpustakaan Naskah Kayseri Raşid Efendi no. 503 (kata yang dikutip tidak terbaca dalam berkas OCR).

[^p1]: CP: Terjemahan Turki pada bagian ini (segitiga yang sudut-sudut alasnya "condong" ke arah sudut puncak) tidak sesuai dengan geometri Euklides. Terjemahan Indonesia mengikuti bacaan naskah N dalam edisi Arab: untuk segi lima diperlukan segitiga sama kaki yang tiap sudut alasnya dua kali sudut puncak (*Elemen* IV.10 dan IV.11), untuk segi tujuh tiga kali, untuk segi sembilan empat kali, dan seterusnya.

[^a22]: CA: Naskah S: "dalil" sebagai ganti "burhan".

[^a23]: CA: Naskah S: "ia melompat ke lukisan bangun".

[^a24]: CA: Naskah S: "segi sembilan" (sebagian tidak terbaca).

[^a25]: CA: Naskah N: "panjang" sebagai ganti "jari-jari".

[^a26]: CA: Naskah S: "setiap tali busur menjadi enam bagian" (sebagian tidak terbaca).

Walhasil, Euklides mampu menegakkan burhan untuk menetapkan lima jenis bangun bersegi: segitiga, segi empat, segi lima, segi enam, dan segi lima belas. Adapun sisa jenis yang tak berhingga banyaknya, kaidah-kaidahnya tak mampu menetapkannya dan premis-premisnya tak memadai untuk menjelaskannya. Para ahli ilmu irisan kerucut telah menempuh suatu cara untuk menetapkan segi tujuh dan segi sembilan, sedangkan sisanya tetap berada pada posisi ketidakmampuan dan kekurangan. Maka tampaklah dari uraian kami bahwa akal manusia terbatas, dan daya pemahaman manusia tidak memadai untuk mencerap hakikat segala sesuatu, kecuali sedikit sekali dari yang amat banyak dalam pengetahuan tentang hal-hal indrawi ini. Lalu bagaimana dugaanmu tentang akal ketika cahaya ketuhanan terbit dan sinar-sinar kemandirian Ilahi memancar?[^a27]

[^a27]: CA: Kata "memancar" (*wa-suṭūʿ*) ditambahkan dari naskah S.

**Hujah kedua**: daya penglihatan (*baṣar*) dan daya mata batin (*baṣīra*)[^k-basira] serupa dan sepadan. Maka hendaklah kita merenungkan keadaan daya penglihatan lebih dahulu, lalu beralih ke keadaan daya mata batin. Kami katakan: daya penglihatan, bila dikaitkan dengan hal-hal yang terlihat, memiliki tiga keadaan.

[^k-basira]: **Mata batin** (*baṣīra*; Ing. *perspicacity, sagacity*). *Baṣīra* adalah daya kalbu yang diterangi cahaya kesucian, yang dengannya kalbu melihat hakikat dan batin segala sesuatu, sebagaimana penglihatan (*baṣar*) bagi jiwa melihat rupa dan lahiriah segala sesuatu. Daya ini disebut para filsuf daya rasional teoretis (*al-quwwa al-ʿāqila al-naẓariyya*); bila ia telah diterangi cahaya kesucian dan hijabnya tersingkap berkat petunjuk Allah, para filsuf menyebutnya daya suci (*al-quwwa al-qudsiyya*). (*Kashshāf*, s.v. *al-baṣīra*.)

Keadaan pertama: hal-hal terlihat yang lemah, hina, dan tersembunyi, seperti partikel dan debu. Sudah dimaklumi bahwa daya penglihatan tidak mampu mencerap hal-hal semacam itu, tidak dapat menangkapnya,[^a28] dan tidak sanggup meliputi tingkatan-tingkatannya.

[^a28]: CA: Naskah N: "dan tidak mampu menangkapnya" (sebagian tidak terbaca). Catatan lain di sini: naskah N menulis "yang tersembunyi" dengan bentuk berbeda.

Keadaan kedua: hal-hal terlihat yang kuat, perkasa, dan mengungguli, seperti bundaran matahari pada puncak kilau dan sinarnya. Daya penglihatan tidak mampu mencerapnya secara utuh dan sempurna. Tidakkah engkau lihat bahwa orang yang memaksakan diri menatap bundaran matahari pada puncak kilau dan sinarnya membayangkan kegelapan dan kehitaman di tengah bundaran itu, seakan-akan cahaya hanya memancar dari tepi-tepinya, laksana sebuah baskom yang cahayanya meluap dari pinggirnya, sedangkan badan bundaran itu sendiri, yang serupa baskom, tampak baginya seperti kegelapan yang hitam? Padahal akal sehat memutuskan bahwa kegelapan itu tidak ada pada substansi matahari, karena matahari adalah sumber cahaya dan tempat munculnya sinar; hanya saja daya penglihatan manusia terkalahkan oleh kesempurnaan cahayanya.

Keadaan ketiga: hal-hal terlihat yang sedang dalam kekuatan dan kelemahan, kesempurnaan dan kekurangan, yaitu sifat-sifat yang melekat pada jisim-jisim alam ini. Daya penglihatan mampu menangkapnya, meliputinya, dan mencerapnya secara sempurna.

Maka tampaklah dari penjelasan ini bahwa daya penglihatan tidak mampu mencerap[^a29] hal-hal terlihat yang amat perkasa, dan tidak mampu pula mencerap hal-hal terlihat yang amat lemah; ia hanya mampu mencerap hal-hal terlihat yang sedang dalam kekuatan dan kelemahan, kesempurnaan dan kekurangan. Bila engkau telah mengetahui ketiga tingkatan dalam daya penglihatan ini, ketahuilah bahwa tingkatan daya mata batin dan akal pun serupa dengannya, sebab hal-hal yang diketahui pun ada tiga tingkatan.

[^a29]: CA: Naskah S: *ibṣār* (melihat) sebagai ganti *idrāk* (mencerap).

Pertama, hal-hal yang diketahui yang lemah dan hina, seperti tingkatan-tingkatan campuran unsur (*amzija*) serta perubahan dan perbedaan yang terjadi pada derajat-derajat perubahan wujud dalam jisim-jisim yang mengalami kejadian dan kerusakan. Akal manusia tidak kuat mencerap tingkatan-tingkatan itu dan memastikan derajat-derajatnya, karena semua itu adalah keadaan yang lemah, cepat hilang, dan segera lenyap dan habis. Karena lemah dan hina, akal manusia tidak kuat mencerapnya secara sempurna dan utuh.

Kedua, hal-hal yang diketahui yang perkasa, luhur, dan suci, yaitu substansi-substansi suci dan esensi-esensi yang terlepas dari keterkaitan dengan jisim. Yang paling mulia dan paling tinggi di antaranya adalah Zat Allah Ta'ala, sifat-sifat keagungan-Nya, dan sifat-sifat kebesaran-Nya.[^a30] Karena kemilau keagungan-Nya mencapai puncaknya, akal tidak mampu mencerap-Nya, dan daya waham serta pemahaman tak kuasa mencapai medan-medan tempat kebesaran-Nya bersinar. Pemilik syariat, semoga selawat Allah tercurah kepadanya,[^a31] mengisyaratkan hal ini dengan sabdanya, *"Sesungguhnya Allah memiliki tujuh puluh hijab dari cahaya. Seandainya Dia menyingkapnya, niscaya kemuliaan wajah-Nya[^t3] membakar segala yang ada di langit dan di bumi."*[^t4] Salah seorang saleh[^a32] berkata, *"Mahasuci Dia yang terhijab dari akal karena dahsyatnya penampakan-Nya, dan tersembunyi darinya karena sempurnanya cahaya-Nya."*

[^a30]: CA: Naskah S: "dan kesempurnaan-Nya" (sebagian tidak terbaca).

[^a31]: CA: Frasa "semoga selawat Allah tercurah kepadanya" ditambahkan dari naskah S.

[^t3]: CT: Diterjemahkan menurut bacaan naskah Perpustakaan Süleymaniye, koleksi Esad Efendi no. 1284.

[^t4]: CT: Hadis yang maknanya "Hijab Allah adalah cahaya; seandainya Dia menyingkap hijab itu, niscaya cahaya-cahaya Zat-Nya membakar seluruh maujud" (Muslim, *Kitāb al-Īmān*, 293; Ibnu Majah, *al-Muqaddima*, 13) dikutip dalam bentuk seperti ini oleh Imam al-Ghazali dalam *Mishkāt al-Anwār*, dan demikian pula di sini.

[^a32]: CA: Naskah S: "salah seorang *ṣiddīq*" sebagai ganti "salah seorang saleh".

Bila engkau telah mengetahui hal ini, engkau pun tahu bahwa akal tidak mampu[^a33] mencerap dan mengenal-Nya justru karena puncak kekuatan, kesempurnaan, dan ketinggian-Nya. Sebagaimana penglihatan tak mampu mencerap bundaran matahari karena kesempurnaan cahayanya, dan hanya membayangkan kehitaman dan kegelapan pada bundaran itu serta membayangkan cahaya memancar dari tepi-tepinya saja, demikian pula akal: bila ia berusaha memandang hakikat terdalam kebesaran-Nya, ia diliputi keadaan serupa keterpanaan dan kebingungan, sehingga ia sama sekali tidak melihat apa pun. Ia hanya dapat melihat cahaya kemurahan-Nya serta limpahan kedermawanan dan rahmat-Nya yang sampai kepada makhluk-Nya, sebagaimana kita melihat cahaya matahari memancar dari tepi dan sisi-sisinya.

[^a33]: CA: Naskah S: "akal lemah" (*qāṣir*) sebagai ganti "tidak mampu" (*ʿājiz*). Catatan lain di sini: kata "bundaran" (*qurṣ*) ditambahkan dari naskah N; naskah S: "menuju kebesaran keagungan-Nya".

Ketiga, hal-hal yang diketahui yang sedang, yang tidak berada pada puncak kekuatan dan keagungan, dan tidak pula pada puncak kelemahan dan kehinaan. Hal-hal inilah yang mampu dicerap dan diliputi oleh akal.

Maka tampaklah dari perbandingan ini bahwa akal-akal terhalang, pikiran-pikiran terkalahkan, dan lintasan hati tertolak. Hakikat Allah Yang Mahabenar tak mungkin dicapai dengan lintasan akal dan pikiran, dan kebesaran ketuhanan mustahil diketahui dengan sayap-sayap kias dan penalaran. Maka tampaklah bahwa yang dapat diperoleh akal hanyalah pengakuan akan kesempurnaan mutlak-Nya dan penyucian-Nya dari seluruh kekurangan secara global. Adapun secara rinci, hal itu bukan urusan daya akal manusia.

**Hujah ketiga**: pengetahuan itu adakalanya berupa konsepsi, adakalanya berupa pembenaran. Mengenai konsepsi, setelah pengujian yang saksama dan induksi yang sempurna kita dapati dalam diri kita, secara swabukti, bahwa dengan akal, daya waham, daya khayal, dan indra kita, kita hanya dapat menunjuk salah satu dari empat jenis konsepsi.

- (a) Esensi-esensi yang kita cerap dengan salah satu dari pancaindra, yaitu hal-hal yang dilihat, didengar, dicium, dikecap, dan diraba.
- (b) Esensi-esensi yang kita cerap dari dalam diri kita secara niscaya, seperti rasa sakit, kenikmatan, lapar, kenyang, gembira, marah, dan semacamnya.
- (c) Esensi-esensi yang kita cerap berdasarkan fitrah akal kita, seperti konsepsi kita tentang makna wujud dan ketiadaan, kesatuan dan kejamakan, keniscayaan, kemungkinan, dan kemustahilan.
- (d) Esensi-esensi yang disusun oleh akal dan daya khayal dari unsur-unsur sederhana ini.

Contoh penyusunan oleh daya khayal ialah ketika kita membayangkan lautan air raksa atau manusia berkepala seribu. Dengan indra penglihatan kita mencerap lautan dan air raksa, lalu daya khayal menyusun rupa lautan dengan rupa air raksa. Demikian pula contoh-contoh lainnya.

Adapun penyusunan oleh akal ialah seperti ketika kita berkata, "Sekutu Tuhan mustahil ada." Selama akal belum mengonsepsikan makna "sekutu Tuhan", mustahil ia menghukuminya sebagai mustahil. Akal dapat mengonsepsikan makna sekutu Tuhan karena di beberapa tempat ia telah mengonsepsikan makna "sekutu", dan telah pula mengonsepsikan makna "Tuhan" secara global. Ketika kedua pengertian itu ada padanya, akal menyusun keduanya sehingga ia memperoleh konsepsi tentang sekutu Tuhan, lalu ia mampu menghukuminya sebagai mustahil. Maka kami katakan: ketika kita memahami makna sekutu dalam kaitannya dengan diri kita, makna yang kita pahami dalam kaitannya dengan diri kita itu kita sandarkan kepada Allah Ta'ala, lalu kita berkata: adanya sesuatu bagi Allah Ta'ala yang nisbahnya kepada-Nya seperti nisbah sekutu kita kepada kita adalah mustahil.

Dengan penjelasan ini tetaplah bahwa konsepsi-konsepsi akal manusia tidak keluar dari keempat jenis ini. Bila konsepsi-konsepsi kita terbatas pada jenis-jenis ini, pembenaran-pembenaran kita pun terbatas padanya, karena telah tetap bahwa pembenaran disyarati oleh konsepsi. Maka tetaplah bahwa konsepsi dan pembenaran makhluk terbatas pada keempat jenis ini.

Bila premis ini telah jelas, kami katakan: telah tetap dengan burhan bahwa hakikat Allah Yang Mahabenar berbeda dari seluruh esensi yang terindra oleh kita dan hadir dalam akal kita secara terperinci. Dia tidak menyerupai satu pun darinya, dan berbeda dari semuanya dari segala segi. Sebab, seandainya Dia sama dengannya dalam sebagian segi dan berbeda dalam segi-segi lainnya, maka segi kesamaan berlainan dengan segi perbedaan, sehingga hakikat-Nya tersusun, dan itu mustahil. Karena itu, hakikat-Nya tidak mungkin dikonsepsikan oleh makhluk dari segi mana pun. Dan bila hakikat-Nya tidak dapat dikonsepsikan oleh makhluk, sedangkan pembenaran bergantung pada konsepsi, maka menghukumi-Nya dengan afirmasi dan negasi, baik yang sederhana maupun yang tersusun, adalah mustahil. Jadi akal tak mampu mengenal-Nya, dan pencerapan manusia tidak sampai kepada-Nya. Puncak yang dapat dicapai dalam hal ini ialah: bila kita mengonsepsikan makna kesempurnaan dan kekurangan pada diri kita, sesuai dengan apa yang layak dan sepadan dengan kita, kita pun memahami makna kesempurnaan dan kekurangan itu secara mutlak, sebab yang mutlak adalah bagian dari esensi yang terbatasi. Dengan jalan ini makna kesempurnaan dan kekurangan[^a34] dapat dikonsepsikan. Bila kita telah mengonsepsikan makna ini, kita mengakui bahwa apa yang dinamai kesempurnaan dapat ditetapkan bagi-Nya, dengan syarat yang dinamai itu disucikan[^a35] dari hal-hal yang melekat padanya karena keberadaannya dalam diri kita. Pengetahuan makhluk tentang keagungan-Nya tidak lebih dari kadar ini.

[^a34]: CA: Naskah S: "kesempurnaan dan kekurangan" dengan bentuk kata *naqḍ* (sebagian tidak terbaca). Dalam naskah S frasa "pada diri kita, sesuai dengan … kesempurnaan dan kekurangan" hilang.

[^a35]: CA: Naskah S: "dengan syarat terbebasnya" (*barāʾa*) sebagai ganti "disucikannya" (*tanazzuh*).

Maka jelaslah dengan penjelasan ini bahwa akal manusia hanya memperoleh pengetahuan-pengetahuan ilahi yang global, yang diisyaratkan tadi, dengan cara yang lebih utama dan lebih layak, bukan secara terperinci.

**Hujah keempat**: perpindahan dari yang diketahui kepada yang tidak diketahui hanya dapat terjadi dengan salah satu dari tiga cara. Pertama, berdalil dengan sebab atas akibat. Kedua, berdalil dengan yang sepadan atas yang sepadan. Ketiga, berdalil dengan akibat atas sebab. Dua cara yang pertama tidak berlaku bagi Allah Yang Mahabenar, sehingga tinggallah cara ketiga, yaitu naik dari pengaruh kepada pemberi pengaruh, dan berpindah dari makhluk kepada Khalik.

Bila engkau telah mengetahui hal ini, kami katakan: jiwa rasional manusia berada pada martabat terakhir di antara maujud-maujud abstrak yang suci. Kebenaran premis ini akan engkau ketahui ketika engkau memahami derajat dan martabat para malaikat. Bila demikian, jiwa manusia naik dari pengetahuannya tentang dirinya kepada pengetahuan tentang sebabnya, lalu dari pengetahuan tentang sebabnya kepada pengetahuan tentang sebab dari sebabnya, dan demikianlah ia naik martabat demi martabat hingga akhirnya sampai ke hadirat Yang Wajib Ada karena Zat-Nya. Sebagaimana difirmankan dalam Kitab Ilahi, *"Dan sesungguhnya kepada Tuhanmulah kesudahannya (segala sesuatu)"* (an-Najm: 42); *"Ingatlah, segala urusan hanya kembali kepada Allah"* (asy-Syura: 53); dan *"Dialah Yang Awal dan Yang Akhir"* (al-Hadid: 3). Jadi, Allah Yang Mahabenar adalah Yang Awal ketika turun dari Yang Mahabenar kepada makhluk, dan Yang Akhir ketika naik dari makhluk kepada Yang Mahabenar.[^a36]

[^a36]: CA: Naskah S: "ketika naik dari makhluk kepada Yang Mahabenar" dengan susunan kata berbeda.

Karena derajat-derajat perantara antara Yang Awal dan Yang Akhir itu banyak dan martabat-martabatnya tersembunyi dari akal manusia, karena keadaan perantara-perantara itu berbeda-beda dan tingkat cahaya, keperkasaan, serta kekuatannya pun berlainan, dan karena daya jiwa rasional manusia lemah untuk naik melalui martabat-martabat itu, maka sebagian besar jiwa manusia tertahan pada salah satu derajat[^a37] perantara-perantara tersebut. Bahkan kami katakan: kebanyakan makhluk tetap berada di dasar alam-alam indrawi; hanya sedikit sekali dari mereka yang lolos dari alam indra dan naik dari alam hal-hal indrawi ke alam khayali; dan hanya sedikit[^a38] dari penghuni alam khayali yang berpindah ke alam hal-hal terpahami. Di alam hal-hal terpahami pun martabat ruh-ruh suci amat banyak. Maka tak pelak, sebagian besar akal yang utama, ketika sampai[^a39] ke alam-alam cahaya hal-hal terpahami, lenyap, fana, dan sirna dalam cahaya ruh-ruh suci itu. Kecuali orang yang dikuatkan dengan daya yang perkasa dan jiwa ilahi, yang naik dari jahe Mars ke salsabil Yupiter, lalu dari sana ke kapur barus Saturnus, kemudian mengatasi semuanya dan naik melampaui semuanya,[^a40] lalu sampai ke hadirat yang suci dari segala yang melekat pada alam kemungkinan dan dari debu kebaharuan, dan berbahagia dengan firman-Nya, *"Dan Tuhan memberikan kepada mereka minuman yang bersih (dan suci)"* (al-Insan: 21), yakni minuman suci yang menyucikannya dari keterkaitan-keterkaitan kemungkinan dan kebaharuan serta menampakkannya di ambang keniscayaan karena zat.[^p2]

[^a37]: CA: Frasa "salah satu derajat" (*darajatin min*) ditambahkan dari naskah N.

[^a38]: CA: Kata "sedikit" (*al-qalīl*) ditambahkan dari naskah Z.

[^a39]: CA: Kata "ketika sampai" (*lammā waṣalat*) ditambahkan dari naskah Z. Catatan lain di sini: naskah S: "cahaya-cahaya" (*al-anwār*) sebagai ganti "ruh-ruh" (*al-arwāḥ*).

[^a40]: CA: Sebagai ganti kalimat ini, naskah S berbunyi: "kemudian berpindah kepada semuanya".

[^p2]: CP: Terjemahan Turki menambahkan "falak Atlas" dan "falak terjauh" (*felek-i aksâ*) sesudah Saturnus, yang tidak terdapat dalam teks Arab edisi al-Saqqā. Terjemahan Indonesia mengikuti teks Arab. Jahe (*zanjabīl*), salsabil, dan kapur barus (*kāfūr*) adalah nama-nama minuman surga dalam surah al-Insan yang di sini dikaitkan dengan planet-planet.

Bila engkau telah mengetahui hal ini, tampaklah bahwa hanya sedikit ruh manusia yang memiliki kesiapan untuk menerima satu kilatan dari cahaya-cahaya alam keagungan. Ini adalah isyarat dan peringatan yang kami sebutkan pada pembukaan ilmu ini, agar orang mengetahui bahwa sedikit saja dari pembahasan pengetahuan-pengetahuan mulia ini sudah amat banyak bagi ruh-ruh manusia. Karena itu, dalam Kitab Ilahi Allah Yang Mahabenar berfirman, *"Dan sedikit sekali dari hamba-hamba-Ku yang bersyukur"* (Saba': 13), dan berfirman mengisahkan Iblis, *"dan Engkau tidak akan mendapati kebanyakan mereka bersyukur"* (al-A'raf: 17). Cukuplah uraian sekadar ini pada kesempatan ini, sebab ilmu ini adalah lautan yang tak bertepi.

### Pasal Ketiga {.pasal-ke}

### Apakah Jalan Menuju Pengetahuan-Pengetahuan Ilahi Itu Satu, ataukah Lebih dari Satu? {.judul-pasal}

[Tr. h. 19]{.penanda}

Ketahuilah, telah tersingkap bagi para pemilik mata batin bahwa jalan menuju pengetahuan-pengetahuan ini ada dua. Pertama, jalan para ahli penalaran dan pendalilan (*aṣḥāb al-naẓar wa-l-istidlāl*). Kedua, jalan para ahli latihan rohani dan perjuangan batin (*aṣḥāb al-riyāḍa wa-l-mujāhada*).[^k-riyada]

[^k-riyada]: **Latihan rohani** (*riyāḍa*; Ing. *practice of piety, asceticism*). Menurut ahli bahasa, *riyāḍa* adalah mengganti keadaan yang tercela dengan keadaan yang terpuji. Sebagian filsuf berkata: *riyāḍa* adalah berpaling dari tujuan-tujuan syahwat. Ada pula yang mendefinisikannya dengan menjaga diri, berpuasa, menahan diri dari celaan, dan menjauh dari pergaulan dengan orang banyak. (*Kashshāf*, s.v. *al-riyāḍa*.)

Jalan pertama, yaitu jalan penalaran dan pendalilan, adalah jalan para filsuf ketuhanan (*al-ḥukamāʾ al-ilāhiyyūn*). Jalan ini berdalil dengan keadaan[^a41] hal-hal yang mungkin untuk menetapkan maujud yang wajib ada karena zatnya.[^a42] Sebab:

- (a) telah tetap bahwa maujud-maujud indrawi ini mungkin dan baharu;
- (b) telah tetap bahwa yang mungkin membutuhkan penentu keunggulan (*murajjiḥ*);
- (c) telah tetap bahwa yang baharu membutuhkan yang membaharukan (*muḥdith*);
- (d) telah tetap bahwa regresi tak berhingga dan lingkaran (*dawr*) mustahil.

Maka maujud-maujud ini pasti berujung pada maujud yang qadim, azali,[^a43] dan wajib ada karena zatnya.

[^a41]: CA: Naskah S: "dengan hukum-hukum" (*bi-aḥkām*) sebagai ganti "dengan keadaan" (*bi-aḥwāl*).

[^a42]: CA: Naskah S: "untuk menetapkan wujud yang wajib karena zatnya".

[^a43]: CA: Kata "azali" ditambahkan dari naskah N.

Syekh ar-Ra'is Abu Ali Ibnu Sina[^a44] dalam kitab *al-Ishārāt* menyebutkan bahwa di sini ada jalan lain yang mengantar kepada penetapan Yang Wajib Ada karena Zat-Nya, yaitu dengan merenungkan keadaan wujud sejauh ia wujud. Ia berkata, "Dalam jalan ini tidak diperlukan perenungan atas keadaan selain wujud. Sebab kami katakan: tidak diragukan bahwa dalam wujud ada suatu maujud. Maujud itu, jika wajib karena zatnya, itulah yang dituju; jika mungkin karena zatnya, ia pasti membutuhkan yang wajib karena zatnya. Maka tetaplah bahwa merenungkan keadaan maujud sejauh ia maujud memberi kesaksian atas adanya maujud yang wajib ada karena zatnya." Itulah perkataannya. Kemudian ia mengunggulkan jalan ini atas jalan[^a45] yang berdalil dengan kemungkinan selain-Nya atas wujud-Nya.

[^a44]: CA: Nama "Abu Ali Ibnu Sina" ditambahkan dari naskah S (sebagian tidak terbaca).

[^a45]: CA: Frasa "atas jalan" ditambahkan dari naskah N.

Ketahuilah, pembahasan yang tuntas menunjukkan[^a46] bahwa perkataan ini tidak kuat.[^a47] Sebab, bila kita berkata, "Maujud itu adakalanya wajib karena zatnya, adakalanya mungkin karena zatnya", maka jika ia mungkin karena zatnya, mustahil wujudnya lebih unggul daripada ketiadaannya kecuali karena penentu keunggulan. Ini tidak lain adalah berdalil dengan wujud yang mungkin atas wujud yang wajib. Maka tetaplah bahwa tidak ada jalan untuk menetapkan Yang Wajib Ada kecuali melalui premis ini. Lagi pula, anggaplah jalan yang ia sebutkan memang menunjukkan adanya maujud yang wajib ada karena zatnya; namun masih tersisa[^a48] keraguan: apakah maujud yang wajib karena zatnya itu jisim-jisim ini ataukah selainnya? Selama burhan belum ditegakkan bahwa jisim-jisim ini mungkin karena zatnya, tidak dapat diputuskan bahwa dalam wujudnya ia membutuhkan[^a49] pemberi pengaruh dan penentu keunggulan.

[^a46]: CA: Kata "menunjukkan" (*yadullu*) ditambahkan dari naskah N.

[^a47]: CA: Naskah S: "tidak kuat bagi dalil itu" (sebagian tidak terbaca).

[^a48]: CA: Kata "masih tersisa" (*yabqā*) ditambahkan dari naskah S.

[^a49]: CA: Naskah S: *taḥtāju* (bentuk feminin dari "membutuhkan").

Maka tetaplah dengan uraian kami bahwa pengetahuan tentang Yang Wajib Ada karena Zat-Nya hanya dapat diperoleh bila kita merenungkan keadaan wujud hal-hal indrawi ini. Bila kita telah menjelaskan bahwa hal-hal itu mungkin karena zatnya, lalu menjelaskan bahwa yang mungkin karena zatnya pasti membutuhkan penentu keunggulan, lalu menjelaskan bahwa regresi tak berhingga dan lingkaran itu batil, barulah kita dapat memastikan adanya maujud yang wajib ada karena zatnya. Inilah ringkasan pembahasan tentang berdalil dengan wujud selain Allah atas wujud Allah Ta'ala.

Adapun jalan kedua, yaitu jalan para ahli latihan rohani, adalah jalan yang menakjubkan,[^a50] kokoh, dan perkasa. Sebab, bila manusia sibuk menyucikan kalbunya dari mengingat selain Allah, dan terus-menerus mengingat Allah dengan lisan jasad dan lisan ruhnya, jatuhlah ke dalam kalbunya cahaya, sinar, keadaan yang perkasa, dan daya yang luhur. Pada substansi jiwanya tersingkap cahaya-cahaya tinggi dan rahasia-rahasia ilahi. Semua itu adalah maqam-maqam yang tak mungkin diketahui secara rinci selama manusia belum sampai kepadanya. Namun aku akan mengingatkan beberapa maqam yang harus diketahui, agar peringatan ini[^a51] menjadi sebab untuk berhati-hati terhadap kekeliruan yang terjadi di dalamnya.

[^a50]: CA: Naskah N: "jalan yang menakjubkan, lezat, kuat, dan perkasa". Catatan lain di tempat ini sebagian tidak terbaca.

[^a51]: CA: Naskah Z: "agar persoalan ini" (*li-taṣīra tilka al-qaḍiyya*).

**Maqam pertama** di antara maqam-maqam yang diperhitungkan dalam bab ini: telah tetap menurut kami bahwa jiwa-jiwa rasional manusia berbeda-beda dalam esensi dan substansinya. Sebagiannya bercahaya, ilahi, dan luhur; sebagian lainnya gelap, keruh, dan rendah. Kami telah menguraikan makna-makna ini secara mendalam dalam kitab *al-Nafs*.

Bila hal ini telah tetap, kami katakan: di antara jiwa-jiwa itu ada yang pada asal substansi dan esensinya adalah jiwa ilahi yang condong kepada hadirat kesucian, amat mencintainya, dan tenggelam dalam derajat-derajat pengenalannya. Ada pula yang memperoleh sesuatu dari keadaan-keadaan ini, tetapi lemah. Dan ada jiwa-jiwa keruh dan gelap yang kosong dari tarikan-tarikan ilahi dan dorongan-dorongan rohani ini, tenggelam dalam lautan hawa nafsu[^a52] serta kegelapan alam indra dan khayal.

[^a52]: CA: Kata "hawa nafsu" (*al-hawā*) dalam naskah S ditulis dengan bentuk lain (sebagian tidak terbaca).

Untuk memperjelas makna-makna ini, aku buat satu perumpamaan. Gunung dan bukit di bumi ada dua macam: ada yang di dalamnya terbentuk sesuatu dari barang tambang, dan ada yang tidak. Induksi menunjukkan[^a53] bahwa gunung yang kosong dari barang tambang jauh lebih banyak daripada gunung yang di dalamnya terbentuk barang tambang. Selanjutnya kami katakan: di antara gunung yang di dalamnya terbentuk barang tambang, ada yang menghasilkan tambang rendah, seperti minyak bumi, belerang, kapur, dan garam, dan ada yang menghasilkan tambang mulia, seperti emas, perak, yakut, dan lal. Induksi menunjukkan bahwa gunung yang mengandung tambang mulia dan berharga ini jauh lebih sedikit daripada gunung yang mengandung tambang rendah. Kemudian kami katakan: bahkan di antara gunung-gunung yang mengandung tambang mulia ini, yaitu tujuh logam esensial (*al-ajsād al-sabʿa al-dhātiyya*),[^a54] kita lihat bahwa logam yang lebih rendah lebih banyak tambangnya, sedangkan logam yang lebih mulia lebih sedikit tambangnya. Sebab induksi menyaksikan bahwa tambang besi, tembaga, timah putih, dan timah hitam jauh lebih banyak daripada tambang emas dan perak.

[^a53]: CA: Dalam naskah S, kalimat "Gunung dan bukit … Induksi menunjukkan" memiliki susunan yang didahulukan dan diakhirkan.

[^a54]: CA: Frasa "yaitu tujuh logam esensial" ditambahkan dari naskah N. Catatan berikutnya: tambahan dari naskah S (sebagian tidak terbaca).

Tambang emas dan perak[^a55] pun berbeda-beda. Ada gunung yang menuntut kerja keras dan berat untuk menghasilkan sedikit emas, dan ada yang tidak demikian, bahkan kerja yang sedikit dan ringan kadang mengantar kepada harta yang banyak. Di antara kedua ujung ini terdapat tingkatan-tingkatan pertengahan yang berbeda-beda dalam sedikit dan banyaknya. Kebaikan dan kesempurnaan terus bertambah, hingga bisa jadi perkaranya berujung pada sebuah gunung yang di dalamnya manusia menemukan gua penuh berisi emas dan perak.[^a56] Bila engkau telah mengetahui tingkatan-tingkatan ini, tampaklah bagimu bahwa gunung yang memuat gua semacam itu amat langka, dan sampai kepadanya serta meraihnya hanya terjadi secara kebetulan dalam kurun-kurun yang berjauhan.[^a57]

[^a55]: CA: Kata "dan perak" ditambahkan dari naskah S.

[^a56]: CA: Kata "dan perak" ditambahkan dari naskah N.

[^a57]: CA: Kalimat "Bila engkau telah mengetahui … kurun-kurun yang berjauhan" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

Bila engkau telah mengetahui hal ini, kami katakan: anggaplah ruh-ruh manusia seperti gunung dan bukit, dan cahaya pengenalan serta kecintaan kepada Allah seperti emas murni. Sebagaimana kebanyakan gunung dan bukit di dunia kosong dari barang tambang, demikian pula ruh kebanyakan makhluk kosong dari kecenderungan kepada alam rohani. Golongan ini, sekalipun berlebih-lebihan dalam latihan jasmani, hanya sedikit memperoleh manfaat darinya; sebagaimana gunung yang kosong dari tambang, andaikan manusia bersusah payah menggarapnya, ia sama sekali tidak akan menemukan apa pun di dalamnya.

Adapun golongan kedua, yaitu ruh-ruh yang di dalamnya terdapat barang-barang tambang itu: sebagaimana gunung-gunung yang mengandung tambang emas dan perak berbeda-beda, sebagian menuntut kerja yang banyak untuk memperoleh manfaat yang sedikit, demikian pula golongan ruh ini; ada yang membutuhkan latihan rohani yang berat dan banyak untuk memperoleh sedikit dari penyingkapan-penyingkapan (*mukāshafāt*) ini, dan ada yang tidak demikian, bahkan amal yang sedikit mengantarnya meraih nikmat-nikmat yang besar. Sebagaimana tingkatan gunung-gunung yang mengandung barang tambang[^a58] berbeda-beda dalam sedikit dan banyaknya dengan perbedaan yang tak dapat dipastikan, demikian pula tingkatan derajat ruh-ruh berbeda dalam kuat dan lemahnya, sedikit dan banyaknya, dengan perbedaan yang tak dapat dipastikan. Dan sebagaimana tidak mustahil, meski jarang, ditemukan gunung yang memuat gua penuh emas,[^a59] demikian pula tidak mustahil ditemukan, dalam kurun-kurun yang berjauhan, seorang manusia yang gua ruhnya penuh dengan cahaya keagungan Allah.

[^a58]: CA: Frasa "yang mengandung barang tambang" ditambahkan dari naskah N.

[^a59]: CA: Naskah S: "emas murni" (*dhahaban ibrīzan*).

Bila engkau memahami perumpamaan ini, engkau tahu bahwa tidak setiap orang yang menempuh latihan rohani, sekalipun dengan cara yang paling berat, pasti sampai kepada sesuatu. Dan tidak setiap orang yang sampai kepada sesuatu telah sampai ke puncak; bahkan puncak di jalan ini mustahil. Sebab, sebagaimana keagungan Allah dan ketinggian kebesaran-Nya tidak berujung, demikian pula martabat-martabat kebahagiaan dalam bab ini tidak berujung. Maka jadikanlah perumpamaan ini di pelupuk matamu dan tetap hadir dalam khayalmu, agar engkau tidak tertipu lalu mengira bahwa setiap orang yang menempuh jalan pasti sampai, dan setiap orang yang mencari pasti menemukan.

Kami tidak mengingkari bahwa latihan-latihan itu membuahkan pengaruh dari sebagian segi, sebab orang yang tekun beramal tentu mendapat bekas dari sebagian segi. Namun jelas bahwa bercelak mata tidak sama dengan mata yang memang hitam sejak lahir.[^p3] Alangkah bagus ucapan sang bijak di antara para penyair, al-Mutanabbi:

> Hati diminta untuk melupakan kalian,
> namun tabiat menolak siapa pun yang hendak mengubahnya.[^t5]

[^p3]: CP: Peribahasa Arab *laysa al-takaḥḥul fī al-ʿaynayn ka-l-kaḥal* membedakan mata yang diberi celak (*takaḥḥul*) dari mata yang hitam alami (*kaḥal*): yang diusahakan tidak sama dengan yang menjadi pembawaan.

[^t5]: CT: Maksudnya: aku meminta hatiku untuk melupakanmu, tetapi engkau telah seperti tabiatku sendiri, dan tabiat tidak mungkin berpindah dari satu keadaan ke keadaan lain.

Aristoteles berkata, "Barang siapa hendak memasuki[^a60] pencarian pengetahuan-pengetahuan ilahi ini, hendaklah ia menciptakan bagi dirinya fitrah yang lain." Maksudnya, manusia hendaknya bersungguh-sungguh menanggalkan akalnya dari keterkaitan dengan indra, daya waham,[^a61] dan daya khayal. Inilah yang dapat dikatakan tentang maqam ini.

[^a60]: CA: Naskah S: "hendak memulai" (*al-shurūʿ*).

[^a61]: CA: Kata "daya waham" ditambahkan dari naskah N.

**Maqam kedua**: inti jalan ini adalah mengosongkan kalbu dari mengingat selain Allah. Sebab substansi jiwa, dengan tabiat asal dan naluri fitrinya, merindukan[^a62] hadirat keagungan Allah. Hanya saja, ketika ia terikat pada badan ini dan sibuk dengan kenikmatan jasmani serta kelezatan-kelezatan rendah, tenggelamnya di sisi ini menjadi[^a63] penghalang baginya untuk tertarik ke tanah air[^a64] asalnya dan pusat zatinya. Bila manusia bersungguh-sungguh menghilangkan hal-hal yang datang kemudian ini, substansi jiwa tetap bersama kelaziman-kelaziman aslinya, debu yang menghijab dan tabir yang menghalangi pun terangkat, dan ketika itu tampaklah padanya cahaya[^a65] keagungan Allah. Maka hendaklah manusia bersungguh-sungguh dalam hal ini sekurang-kurangnya sampai ia merasakan kelezatan mengetahui satu zarah dari cahaya ilmu itu. Sebab, bila kebahagiaan itu telah diperoleh, kelezatan menguat dan kegembiraan membesar, dan hal itu menjadi tarikan terbesar yang membawanya berpaling kepada Allah Yang Mahabenar dan menghadap kepada-Nya.

[^a62]: CA: Naskah S: "sepadan dengan hadirat" (*munāsiba li-ḥaḍra*) sebagai ganti "merindukan" (*ʿāshiqa*).

[^a63]: CA: Naskah S: *ṣāra* (menjadi) dengan bentuk berbeda.

[^a64]: CA: Naskah S: *al-quṭr* (negeri) sebagai ganti *al-waṭan* (tanah air).

[^a65]: CA: Naskah S: "sifat" (sebagian tidak terbaca) sebagai ganti "cahaya".

**Maqam ketiga**: orang yang menempuh latihan rohani, bila kosong dari jalan penalaran dan pendalilan, bisa jadi pada derajat-derajat[^a66] latihannya tampak baginya penyingkapan-penyingkapan yang kuat dan keadaan-keadaan[^a67] yang luhur dan perkasa, lalu ia meyakini bahwa itulah keadaan penyingkapan yang terakhir dan derajat yang tertinggi. Hal itu pun menjadi penghalang baginya untuk sampai kepada tujuan. Adapun bila ia telah terlatih dalam jalan penalaran dan pendalilan, dan dapat membedakan maqam yang mustahil dicapai dari maqam yang tidak mustahil, ia akan aman dari kekeliruan ini. Dan bila seseorang telah sempurna dalam jalan pendalilan rasional, kemudian dikaruniai kesempurnaan dalam jalan penyucian dan latihan rohani, sedangkan jiwanya sejak awal fitrahnya memiliki kesiapan yang besar untuk keadaan-keadaan ini, maka orang itu dapat sampai ke puncak tertinggi dalam jenjang dan tangga pendakian ini.

[^a66]: CA: Naskah S: "gerakan-gerakan" (*ḥarakāt*) sebagai ganti "derajat-derajat" (*darajāt*).

[^a67]: CA: Kata "keadaan-keadaan" ditambahkan dari naskah S.

Dinukil dari Aristoteles bahwa ia berkata, "Dahulu aku minum dan tak juga puas. Ketika aku minum dari lautan ini, aku puas dengan kepuasan yang tak akan pernah haus lagi sesudahnya." Keadaan-keadaan ini tak dapat diuraikan dengan kata-kata dan tak terjangkau oleh ucapan. Siapa yang tidak merasakan tidak akan mengenal, dan siapa yang tidak menyaksikan tidak akan membenarkan. Allah lebih mengetahui hal-hal yang gaib.

### Pasal Keempat {.pasal-ke}

### Penetapan Masalah-Masalah Pokok Ilmu Ini {.judul-pasal}

[Tr. h. 24]{.penanda}

Ketahuilah, manusia memiliki tiga keadaan: masa lalu, masa kini, dan masa depan.

Tentang masa lalu, manusia ingin mengetahui bagaimana keadaan-keadaan yang dialaminya ini pada masa lalu. Hal itu hanya dapat diperoleh dengan mengenal Prinsip Pertama, mengenal sifat-sifat-Nya, dan mengetahui bagaimana keadaan-keadaan ini muncul dari-Nya. Inilah tiga hal yang harus diketahui lebih dahulu, dan pada jalan masing-masing terdapat simpul yang menakutkan.

**Pengetahuan tentang zat**: bila kita memutuskan bahwa Zat-Nya sama dengan sesuatu dari hal-hal yang kita cerap dengan indra kita, yang kita dapati dalam jiwa kita, atau yang kita dapati dengan akal kita, niscaya Zat-Nya mungkin karena zatnya, dan itu mustahil. Bila kita memutuskan bahwa Zat yang khusus itu berbeda dari semua maujud yang kita pahami dan kita ketahui, akal tetap bingung dan terpana, tidak mendapat petunjuk kepada apa pun. Walhasil, bila akal menetapkan hakikat itu dengan cara yang dapat dicapai oleh pencerapannya, berarti ia sama sekali tidak mengenal-Nya, sebab segala yang demikian adalah mungkin ada, bukan wajib ada. Dan bila akal menetapkan-Nya sebagai berbeda dari seluruh hakikat ini, ia tak mampu mengenal-Nya sebagaimana Dia adanya. Bila ia tak mampu mengenal dan mengonsepsikan-Nya, bagaimana mungkin ia menyifati-Nya dengan sifat-sifat keagungan, kebesaran, dan kesucian? Inilah perhentian yang menggentarkan dalam pengetahuan tentang zat.

**Pengetahuan tentang sifat**: di sini ada dua maqam yang amat menggentarkan.

Maqam pertama: jika sifat-sifat itu berlainan dengan zat, hakikat Tuhan tersusun dari banyak esensi,[^a68] sedangkan setiap yang tersusun adalah mungkin; maka Yang Wajib karena Zat-Nya menjadi mungkin karena zatnya, dan itu mustahil. Jika sifat-sifat itu identik dengan zat, hal itu pun bermasalah dari dua segi. Pertama, esensi masing-masing sifat ini dapat diketahui tanpa memperhatikan hakikat zat yang khusus; seandainya zat[^a69] identik dengan sifat, niscaya hal itu mustahil. Kedua, setiap sifat memiliki esensi yang berlainan dengan esensi sifat yang lain; seandainya sifat-sifat itu identik dengan zat yang satu, niscaya sesuatu yang satu tidak lagi satu, melainkan esensi-esensi yang berbeda-beda, dan itu mustahil.

[^a68]: CA: Naskah S: "maka hakikat Tuhan adalah makna-makna yang tersusun dari banyak esensi". Catatan-catatan berikutnya di halaman ini menandai tambahan dari naskah N (sebagian tidak terbaca).

[^a69]: CA: Kata "zat" ditambahkan dari naskah N.

Maqam kedua: ilmu Allah Ta'ala pasti meliputi hal-hal universal dan partikular yang tak berhingga, dan kuasa Allah Ta'ala pasti berlaku atas seluruh hal yang mungkin. Padahal satu sifat yang meliputi hal-hal tak berhingga secara terperinci, tanpa satu urusan menyibukkan-Nya dari urusan lain, adalah sesuatu yang tidak pernah kita dapati dalam jiwa dan akal kita. Karena itu, sulit bagi akal manusia untuk mengonsepsikan pencerapan makna-makna ini.

**Pengetahuan tentang perbuatan**: di sini ada perhentian yang membuat akal kebingungan dan pemahaman tersesat, yaitu: bagaimana dapat dipahami[^a70] penyandaran pengaruh yang tertentu kepada pemberi pengaruh yang sama sekali tidak mengalami penentuan? Sebab, selama tidak terjadi pada-Nya suatu kehendak, perubahan waktu,[^a71] munculnya suatu maslahat, atau hilangnya suatu penghalang, mustahil Dia menjadi pelaku setelah sebelumnya tidak demikian. Para penganut kebaharuan alam harus membuka simpul ini. Adapun para penganut keqadiman alam mengira bahwa mereka telah lolos dari simpul ini, padahal tidak demikian. Sebab, tidak diragukan bahwa bentuk-bentuk dan aksiden-aksiden di alam ini baharu, bahwa keadaan-keadaan ini ada setelah tiada dan tiada setelah ada. Bila setiap yang baharu kita sandarkan kepada yang baharu lainnya tanpa berujung pada maujud yang qadim, itu mustahil. Dan bila ia pasti berujung dan bersandar pada akhirnya kepada maujud yang wajib ada karena zatnya dan suci dari segala segi perubahan, kesulitan itu pun kembali.

[^a70]: CA: Frasa "bagaimana dapat dipahami" (*kayfa yuʿqal*) ditambahkan dari naskah S.

[^a71]: CA: Frasa "perubahan waktu" ditambahkan dari naskah S.

Ketahuilah, tujuan kami menyebutkan kesulitan-kesulitan ini di sini adalah untuk mengingatkannya. Adapun penjelasan[^a72] masing-masing secara tuntas dan sempurna akan datang di tempatnya dalam kitab ini, insya Allah Ta'ala. Inilah isyarat kepada pengetahuan tentang masa lalu.

[^a72]: CA: Naskah S: "definisi" (*taʿrīf*) sebagai ganti "penjelasan" (*taqrīr*).

Adapun kajian tentang keadaan masa kini: manusia perlu mengetahui keyakinan dan amal mana yang membawanya meraih kebahagiaan terbesar dan derajat tertinggi, dan keyakinan serta amal mana yang sebaliknya.

Adapun kajian tentang masa depan: manusia perlu mengetahui bahwa ia memiliki tempat kembali (*maʿād*).[^k-maad] Tempat kembali itu mungkin hanya rohani, atau hanya jasmani,[^a73] atau keduanya sekaligus. Ia juga perlu mengetahui keadaan kebahagiaan dan kesengsaraannya di tempat kembali itu.

[^k-maad]: **Tempat kembali** (*maʿād*; Ing. *hereafter, resurrection, afterworld*). Di kalangan ahli balagah, *maʿād* adalah nama salah satu gaya bait. Adapun menurut ahli kalam, *maʿād* disebut juga *ḥashr* (kebangkitan), dan terbagi dua: jasmani dan rohani. (*Kashshāf*, s.v. *al-maʿād*.)

[^a73]: CA: Frasa "atau hanya jasmani" ditambahkan dari naskah S.

Inilah pembatasan bab-bab ilmu ilahi. Dengan demikian tampaklah, melalui induksi, bahwa ilmu ini mencakup sepuluh bagian.

**Bagian pertama**: penetapan dalil-dalil[^a74] yang menunjukkan adanya maujud yang wajib ada karena zatnya.

[^a74]: CA: Kata "yang menunjukkan" ditambahkan dari salah satu naskah (sebagian tidak terbaca).

**Bagian kedua**: pembahasan tentang sifat-sifat negatif-Nya, yaitu sifat-sifat keagungan (*jalāl*). Termasuk di dalamnya bahwa Dia Esa secara mutlak, suci[^a75] dari segala segi[^a76] kejamakan (dan inilah sifat-sifat negatif-Nya), dan konsekuensinya Dia suci dari lawan dan tandingan, serta suci dari kejisiman, ruang, dan tempat.

[^a75]: CA: Naskah S: *munazzah* (suci) sebagai ganti *mubarraʾ* (terbebas). Catatan lain di sini: naskah S: *khālin* (kosong).

[^a76]: CA: Naskah S: "dari" (*ʿan*) dengan susunan berbeda.

**Bagian ketiga**: pembahasan tentang sifat-sifat kemuliaan (*ikrām*), yaitu ilmu, kuasa, kehendak, dan rahmat.

**Bagian keempat**: pembahasan tentang perbuatan-perbuatan-Nya, yang terbagi menjadi beberapa bagian. Pertama, apakah Dia senantiasa menjadi pelaku dan pemberi limpahan? Kedua, pembahasan tentang cara perbuatan-perbuatan muncul dari-Nya; termasuk di dalamnya pemetaan mazhab-mazhab manusia, serta pemaparan dalil-dalil yang kurang memadai dan syubhat-syubhat yang menggugat dalam setiap mazhab. Ketiga, pembahasan tentang qada dan qadar.

**Bagian kelima**: pembahasan tentang uraian firman-Nya dalam penciptaan alam atas dan alam bawah, sebatas kemampuan akal manusia, disertai peringatan bahwa sampai kepada hakikat terdalam bab ini termasuk hal yang tak dapat dicapai makhluk. Termasuk di dalamnya penjelasan apakah alam jasmani itu satu atau lebih.

**Bagian keenam**: pembahasan tentang martabat ruh-ruh suci serta penjelasan derajat-derajat para malaikat rohani dan malaikat karubiyun dengan segala perbedaan derajat mereka.[^p4]

[^p4]: CP: Terjemahan Turki berbunyi "derajat para malaikat dan empat malaikat besar". Terjemahan Indonesia mengikuti teks Arab: *al-malāʾika al-rūḥāniyyīn wa-l-karūbiyyīn* (malaikat rohani dan malaikat karubiyun).

**Bagian ketujuh**: pembahasan tentang hakikat tempat dan waktu, beserta perincian pendapat-pendapat tentang keduanya.

**Bagian kedelapan**: pembahasan tentang kenabian dan uraian hakikatnya, perbedaan mazhab-mazhab manusia tentangnya, serta pemaparan segi-segi yang menguatkan dan segi-segi yang menggugat dalam setiap mazhab.

**Bagian kesembilan**: pembahasan[^a77] tentang cara memperoleh sifat-sifat utama yang menjadikan jiwa termasuk golongan orang-orang berbahagia lagi saleh, bukan golongan orang-orang sengsara lagi durhaka.

[^a77]: CA: Kata "pembahasan" ditambahkan dari naskah N.

**Bagian kesepuluh**: pembahasan tentang tempat kembali yang rohani dan jasmani, serta uraian sifat-sifat masing-masing dari kedua bagian itu.[^t6][^a78]

[^t6]: CT: Susunan yang disebut ar-Razi pada pembukaan ini berbeda dari susunan kitab yang sampai kepada kita dalam edisi cetak. Ada tiga sebabnya. Pertama, naskah cetak tidak memuat sebagian bagian kitab. Kedua, pengarang wafat sebelum menulis dua bagian terakhir. Ketiga, naskah-naskah tulisan tangan memuat bagian-bagian kitab dengan urutan yang berbeda.

[^a78]: CA: Ketahuilah, bagian kesembilan membahas ilmu akhlak, dan bagian kesepuluh membahas tempat kembali yang rohani dan jasmani. Pengarang telah berpulang ke rahmat Allah Ta'ala sebelum menulis tentang akhlak dan tentang tempat kembali.

Di sinilah akhir uraian tentang pembagian ilmu ilahi. Kami memohon pertolongan dan taufik kepada Allah untuk sampai kepada tujuan-tujuan yang luhur dan maksud-maksud yang suci ini, sesuai dengan daya manusia dan kemampuan insani. Inilah akhir pembahasan tentang Mukadimah.
