# al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī: Terjemahan Indonesia

**Karya:** Fakhr al-Dīn al-Rāzī (w. 606/1210), *al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī*
**Naskah dasar (Turki):** Fahreddin er-Râzî, *el-Metâlibü'l-Âliye mine'l-İlmi'l-İlâhî: Metafizik*, jilid 1 sampai 3, ed. Ekrem Demirli, terj. Ekrem Demirli, Eşref Altaş, Hayrettin Gödekli, Osman Demir, Istanbul: Fikriyat, 2022 (berkas `6659d7ee-matalib.docx`, hasil OCR)
**Naskah pembanding (Arab):** *al-Maṭālib al-ʿĀliya min al-ʿIlm al-Ilāhī*, ed. Aḥmad Ḥijāzī al-Saqqā, Beirut: Dār al-Kitāb al-ʿArabī, 1407/1987 (berkas `e51348c0-matalib_arab.docx`, hasil OCR; urutan jilid dalam berkas acak)
**Rujukan istilah:** Glosarium v2.0 dan catatan Kashshāf dalam `terjemahan-asas-al-taqdis.md`; Muḥammad ʿAlī al-Tahānawī, *Kashshāf Iṣṭilāḥāt al-Funūn wa-l-ʿUlūm*, ed. Rafīq al-ʿAjam dan ʿAlī Daḥrūj, Beirut: Maktabat Lubnān Nāshirūn, 1996

---

## 0. Status Proyek dan Penanda Posisi

| Butir | Keterangan |
|---|---|
| Tahap | Penerjemahan berjalan: Kitab Pertama, Bagian Pertama |
| Sudah diterjemahkan | Pembuka; Mukadimah (Pasal 1 sampai 4); Kitab Pertama: Persiapan, Bagian Pertama Pengantar, Pasal 1 sampai 3, Pasal 4 (Syubhat 1 sampai 9) |
| Posisi berikutnya | Kitab Pertama, Bagian Pertama, Pasal Keempat, Syubhat Kesepuluh (berkas Turki baris 821; berkas Arab baris 10331) |
| Nomor catatan terakhir | CT: t9 · CA: a205 · CP: p10 |
| Catatan Kashshāf baru | istiqra, tasdiq, basira, riyada, maad, iqnai, tali |

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
3. **Catatan kaki:** semua catatan edisi Turki diterjemahkan (awalan **CT:**), dan semua catatan edisi Arab al-Saqqā diterjemahkan (awalan **CA:**), termasuk catatan perbedaan naskah. Siglum naskah edisi Arab ditulis dengan huruf Latin padanannya: س = S, ن = N, ز = Z, ط = Ṭ, ل = L, م = M. Bacaan varian dikutip dalam transliterasi. Catatan yang teksnya rusak dalam berkas OCR ditandai "(sebagian tidak terbaca)". Letak catatan CA di badan teks mengikuti letak kata yang dirujuknya; bila penanda aslinya hilang dalam OCR, letaknya ditentukan dari isi catatan.
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
| يقيني / إقناعي | yaqīnī / iqnāʿī | - / rhetoric proof | **meyakinkan** / **persuasif** † | Catatan Kashshāf pada *iqnāʿī*. |
| مقدم / تالي | muqaddam / tālī | - / the next, the predicate | **anteseden** / **konsekuen** † | Bagian proposisi kondisional. Catatan Kashshāf pada *tālī*. |
| الفطرة الأصلية | al-fiṭra al-aṣliyya | - | **fitrah asali** | |
| لزوم / التزام | luzūm / iltizām | - | **konsekuensi suatu pendapat** / **berpegang pada suatu pendapat** | |
| ظن غالب | ẓann ghālib | - | **dugaan yang kuat** | |
| أولوية | awlawiyya | - | **kelayakan** (lebih layak untuk ada) | |
| مجعول / جاعل | majʿūl / jāʿil | - | **yang diadakan** / **yang mengadakan** | |
| موصوفية الماهية بالوجود | mawṣūfiyyat al-māhiyya bi-l-wujūd | - | **keadaan esensi disifati dengan wujud** | |
| محض الاتفاق | maḥḍ al-ittifāq | agreement, concord (*ittifāq*) | **kebetulan semata** | |
| مدة | mudda | - | **rentang masa** | Mengikuti Glosarium *Asās*. |
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

# Kitab Pertama {.kitab-ke}

# Dalil-Dalil yang Menunjukkan Adanya Tuhan Alam dan bahwa Dia Wajib Ada karena Zat-Nya {.judul-kitab}

[Tr. h. 31]{.penanda}

#### Persiapan {.subpasal}

Ketahuilah, kitab ini disusun dalam tiga bagian.[^a79]

[^a79]: CA: Dalam naskah pokok tertulis "dua bagian".

**Bagian pertama**: uraian dalil-dalil yang pasti dan meyakinkan (*yaqīnī*).

**Bagian kedua**: uraian dalil-dalil persuasif (*iqnāʿī*)[^k-iqnai] yang kuat.

**Bagian ketiga**: pembahasan tentang keniscayaan, wujud, keazalian, ketertentuan, esensi, dan tuntutan serta pembahasan lain yang serupa.[^a80]

[^k-iqnai]: **Persuasif** (*iqnāʿī*; Ing. *rhetoric proof*). *Iqnāʿī* dipakai untuk silogisme retoris (*qiyās khiṭābī*), yaitu dalil yang tersusun dari premis-premis yang masyhur dan yang diduga benar. Terkadang istilah ini dipakai pula untuk dalil yang meyakinkan pada pandangan pertama, meskipun sebenarnya tidak memuaskan. (*Kashshāf*, s.v. *al-iqnāʿī*.)

[^a80]: CA: Uraian bagian ketiga ini ditambahkan oleh penyunting. Dalam naskah, bagian ini disebut sesudah pasal ketiga dari bagian kedua.

## Bagian Pertama {.bagian-ke}

## Uraian Dalil-Dalil Pasti yang Tidak Mengandung Keraguan {.judul-bagian}

[Tr. h. 33]{.penanda}

#### Pengantar: Penjelasan tentang Hal-Hal yang Pelik dalam Bagian Ini {.subpasal}

Ketahuilah, bila kita hendak menetapkan suatu maujud yang wujudnya tidak diputuskan oleh indra kita dan tidak pula oleh fitrah jiwa dan akal kita,[^a81] tidak ada jalan untuk itu kecuali satu jalan: akal kita yang jernih memutuskan bahwa maujud-maujud yang wujudnya kita putuskan dengan indra dan akal kita ini membutuhkan, entah dalam wujudnya sendiri entah dalam wujud salah satu sifatnya, adanya suatu maujud yang gaib dari indra dan daya waham kita. Dengan jalan inilah akal mampu menetapkan maujud yang gaib itu.[^p5]

[^a81]: CA: Naskah S: "fitrah kita dan akal kita".

[^p5]: CP: Terjemahan Turki berbunyi "bisa ada suatu jalan yang mengantar kita kepada penetapan itu". Terjemahan Indonesia mengikuti teks Arab yang lebih tegas: *mimmā lā sabīla ilayhi illā bi-ṭarīq wāḥid* (tidak ada jalan kepadanya kecuali satu jalan). Paragraf pengantar ini tercetak dua kali dalam berkas Turki dan hanya diterjemahkan sekali.

Bila engkau telah memahami hal ini, kami katakan: sumber kebutuhan itu adakalanya kemungkinan, adakalanya kebaharuan, dan adakalanya gabungan keduanya. Ketiga keadaan ini adakalanya dipandang pada zat-zat, adakalanya pada sifat-sifat. Maka semuanya ada enam jalan:

- (a) kemungkinan zat-zat;
- (b) kemungkinan sifat-sifat;
- (c) kebaharuan zat-zat;
- (d) kebaharuan sifat-sifat;
- (e) gabungan kemungkinan dan kebaharuan pada zat-zat;
- (f) gabungan kemungkinan dan kebaharuan pada sifat-sifat.

Inilah jalan-jalan yang dapat dipakai untuk berdalil atas penetapan maujud yang wajib ada karena zatnya. Cukuplah sekian untuk pengantar ini.

### Pasal Pertama {.pasal-ke}

### Penyusunan Premis-Premis Dalil Ini menurut Cara yang Dikenal di Kalangan Para Filsuf[^t7] {.judul-pasal}

[^t7]: CT: Diterjemahkan sesuai bacaan *tarkīb* (penyusunan) dalam naskah Perpustakaan Süleymaniye, koleksi M. Ragıp Paşa no. 810.

[Tr. h. 35]{.penanda}

Kami katakan: tidak diragukan adanya suatu maujud. Setiap maujud, hakikatnya adakalanya menolak menerima ketiadaan, adakalanya tidak. Yang pertama adalah yang wajib karena zatnya, dan yang kedua adalah yang mungkin karena zatnya.[^a82] Maka tetaplah bahwa adanya suatu maujud harus diakui, dan tetap pula bahwa setiap maujud adakalanya wajib karena zatnya, adakalanya mungkin karena zatnya.[^a83] Premis-premis ini menghasilkan kesimpulan: dalam wujud adakalanya ada maujud yang wajib ada karena zatnya,[^a84] adakalanya ada maujud yang mungkin karena zatnya. Jika yang pertama, itulah yang dituju. Jika yang kedua, kami katakan: yang mungkin karena zatnya, salah satu dari kedua sisinya (ada dan tiada) tidak menjadi lebih unggul daripada yang lain kecuali karena penentu keunggulan.[^a85] Penentu keunggulan itu, jika wajib karena zatnya, itulah yang dituju; jika mungkin karena zatnya, pembagian pertama kembali berlaku padanya. Maka adakalanya terjadi regresi tak berhingga atau lingkaran, dan keduanya mustahil, atau berujung pada maujud yang wajib ada karena zatnya, dan itulah yang dituju.

[^a82]: CA: Kata "karena zatnya" pada "yang mungkin" ditambahkan dari naskah N. Catatan lain pada judul pasal ini dalam naskah S sebagian tidak terbaca.

[^a83]: CA: Frasa "adakalanya mungkin karena zatnya" ditambahkan dari naskah S.

[^a84]: CA: Tambahan dari salah satu naskah (siglumnya tidak terbaca).

[^a85]: CA: Frasa "kecuali karena penentu keunggulan" ditambahkan dari naskah N.

Ketahuilah, dalil ini dibangun di atas beberapa premis:

- (a) yang mungkin, salah satu sisinya tidak menjadi lebih unggul daripada yang lain kecuali karena penentu keunggulan;
- (b) penjelasan[^a86] apakah kebutuhan ini terjadi ketika ia mulai ada (*ḥudūth*) ataukah ketika ia bertahan (*baqāʾ*);
- (c) penentu keunggulan itu harus maujud;
- (d) ia harus[^a87] maujud ketika pengaruhnya terjadi;
- (e) lingkaran itu batil;
- (f) regresi tak berhingga itu batil.

[^a86]: CA: Naskah S: "bahwa dikatakan" (*an yuqāl*) sebagai ganti "penjelasan" (*bayān*).

[^a87]: CA: Kata "harus" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

Bila penjelasan keenam premis ini telah tuntas, tercapailah kepastian bahwa adanya maujud[^a88] yang wajib ada karena zatnya harus diakui. Kemudian, bila sesudah itu kami jelaskan bahwa alam indrawi ini mustahil wajib ada karena zatnya,[^a89] kita pun mengetahui bahwa alam indrawi ini, dalam wujudnya, membutuhkan adanya maujud yang wajib ada karena zatnya. Itulah yang dituju. Maka hendaklah kita khususkan satu pasal untuk menjelaskan masing-masing premis ini.

[^a88]: CA: Kata "maujud" ditambahkan dari naskah S.

[^a89]: CA: Kalimat "Kemudian, bila sesudah itu … karena zatnya" ditambahkan dari naskah N.

### Pasal Kedua {.pasal-ke}

### Penjelasan bahwa Salah Satu Sisi yang Mungkin Tidak Menjadi Lebih Unggul daripada yang Lain kecuali karena Penentu Keunggulan {.judul-pasal}

[Tr. h. 36]{.penanda}

Ketahuilah, dalam hal ini orang-orang berakal memiliki dua pendapat. Pertama, premis ini swabukti (*badīhī*). Kedua, premis ini membutuhkan burhan (*burhānī*).

Para penganut pendapat pertama berhujah atas kebenaran mazhab mereka dengan berkata: kita lihat mayoritas orang berakal sepakat bahwa bila mereka merasakan terjadinya suatu peristiwa baru, mereka mencari sebabnya; bila mereka mendengar suara manusia, mereka terdorong untuk mengetahui secara niscaya kehadiran manusia itu; dan bila mereka melihat sebuah bangunan berdiri, mereka memastikan adanya pembangun.

Bahkan kami tambahkan: pengetahuan ini ada pula dalam jiwa anak-anak yang akalnya belum sempurna. Sebab, bila seorang anak memiliki tempat khusus yang ia kuasai, lalu ia mendapati di sana makanan yang tidak ia letakkan, atau sesuatu yang telah ia letakkan[^a90] hilang dari sana, ia berteriak, "Siapa yang mengambilnya? Siapa yang meletakkannya?" Ini menunjukkan bahwa fitrah anak itu bersaksi bahwa yang mungkin pasti memiliki penentu keunggulan dan bahwa yang baharu pasti memiliki yang membaharukan.[^a91] Bila pengetahuan ini tertanam dalam naluri[^a92] jiwa anak itu, kita pun tahu bahwa ia adalah pengetahuan swabukti yang paling kuat.

[^a90]: CA: Kata "yang telah ia letakkan" ditambahkan dari naskah N.

[^a91]: CA: Frasa "dan bahwa yang baharu pasti memiliki yang membaharukan" ditambahkan dari naskah N.

[^a92]: CA: Kata "naluri" (*gharīza*) ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

Bahkan kami katakan: jenis pencerapan ini tertanam pula dalam jiwa hewan. Sebab, bila seekor hewan mendengar suara ular, ia lari; dan larinya tidak lain karena pencerapannya akan suara ular menuntut pencerapannya akan adanya ular. Ini menunjukkan bahwa perpindahan fitrah dan jiwa dari pengaruh kepada pemberi pengaruh ada pada jiwa anak-anak,[^a93] bahkan juga pada jiwa hewan.

[^a93]: CA: Naskah S: "pada jiwa anak-anak dan hewan". Kata "bahkan hal itu" (*bal huwa amr*) ditambahkan dari salah satu naskah.

Jika dikatakan, pembahasan kalian dapat disanggah dari beberapa segi.

**Pertanyaan pertama**: pertimbangan-pertimbangan yang kalian sebutkan ini, seandainya benar, hanya menunjukkan bahwa pengetahuan tentang kebutuhan yang baharu (*muḥdath*) kepada pemberi pengaruh adalah pengetahuan niscaya; ia tidak menunjukkan bahwa pengetahuan tentang kebutuhan yang mungkin kepada pemberi pengaruh adalah pengetahuan niscaya. Betapa jauh jarak antara keduanya!

Jika seseorang berkata, "Kita mendapati secara swabukti bahwa bila wujud dan ketiadaan setara, mustahil salah satunya lebih unggul daripada yang lain kecuali karena penentu keunggulan. Maka kita tahu bahwa sebagaimana pengetahuan swabukti ada tentang kebutuhan yang baharu kepada pemberi pengaruh, pengetahuan swabukti itu ada pula tentang kebutuhan yang mungkin kepada penentu keunggulan", maka dalam menjawab hal ini kami katakan: akal memang memastikan ucapan kalian bahwa bila wujud dan ketiadaan setara baginya, salah satunya tidak menjadi lebih unggul kecuali karena penentu keunggulan. Namun akal memastikannya karena ucapan kalian "salah satu sisi menjadi lebih unggul daripada yang lain" menimbulkan kesan bahwa keunggulan itu[^a94] baharu, yakni sesuatu yang terjadi setelah sebelumnya tidak ada. Jadi kepastian ini muncul dari segi makna[^a95] kebaharuan, bukan dari kemungkinan semata. Dalilnya: bila kesan kebaharuan kita hilangkan sama sekali dan kita pandang makna kemungkinan terlepas dari kesan kebaharuan, yaitu pada hal mungkin yang bertahan dalam keadaan bertahannya,[^a96] kita tidak mendapati dalam akal kepastian bahwa yang mungkin, dalam keadaan bertahannya, membutuhkan pemberi pengaruh. Yang justru dominan dalam daya waham adalah bahwa yang bertahan itu, dalam keadaan bertahannya, tidak membutuhkan pemberi pengaruh, dan bahwa ia bertahan dengan sendirinya sampai datang hal yang menghilangkan dan meniadakannya. Maka kita tahu bahwa kepastian itu hanya muncul ketika ada kebaharuan atau ketika makna kebaharuan dibayangkan.[^a97] Adapun kemungkinan, bila terlepas dari bayangan kebaharuan, akal yang jernih tidak memutuskan bahwa ia menjadi sebab kebutuhannya kepada yang lain.

[^a94]: CA: Kata "itu" (*dhālika*) ditambahkan dari naskah N.

[^a95]: CA: Kata "makna" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

[^a96]: CA: Frasa "dalam keadaan bertahannya" ditambahkan dari naskah S.

[^a97]: CA: Naskah S: "bayangan" dengan bentuk kata *jāl* (sebagian tidak terbaca).

**Pertanyaan kedua** terhadap pokok pembahasan: kami tidak menerima bahwa orang-orang berakal memastikan kebutuhan yang mungkin kepada penentu keunggulan. Hal ini ditunjukkan oleh beberapa segi.

Pertama, para penganut[^a98] kebaharuan alam lebih banyak jumlahnya daripada penganut keqadimannya. Dengan jumlah yang banyak itu mereka berpegang bahwa Allah Ta'ala menjadi pelaku alam setelah sebelumnya bukan pelakunya, lalu mereka sepakat bahwa pembaruan kepelakuan ini tidak terjadi karena suatu sebab. Jadi mereka sepakat bahwa makna kebaharuan dan pembaruan terjadi dalam kasus ini tanpa sebab. Seandainya kemustahilan hal itu diketahui secara niscaya, mustahil orang-orang berakal bersepakat atasnya.

[^a98]: CA: Naskah S: "orang yang berpendapat" (bentuk tunggal).

Kedua, mereka berkata: orang yang lari dari binatang buas, bila di hadapannya terbentang dua jalan yang setara dari segala segi, memilih salah satunya tanpa penentu keunggulan. Demikian pula orang yang diberi pilihan untuk minum dari salah satu dari dua gelas air yang setara, memilih salah satunya tanpa penentu keunggulan.[^a99] Contoh-contoh dalam hal ini banyak dan masyhur. Di sini mayoritas sepakat bahwa keunggulan terjadi tanpa penentu keunggulan. Seandainya kemustahilan premis ini diketahui secara swabukti, tentu segolongan besar orang berakal tidak akan berpendapat bahwa hal itu benar.

[^a99]: CA: Kalimat tentang dua gelas air ditambahkan dari naskah S.

Ketiga, segolongan besar mutakalim[^p6] berpendapat bahwa zat-zat setara dalam hal keberadaannya sebagai zat. Mereka berkata:[^a100] hal ini ditunjukkan oleh dua segi.

[^p6]: CP: Edisi Turki menambahkan keterangan dalam kurung "[yakni Muktazilah]". Pendapat bahwa zat-zat setara dalam kezatannya (*tamāthul al-dhawāt*) memang masyhur di kalangan Muktazilah.

[^a100]: CA: Kata "mereka berkata" ditambahkan dari naskah N.

- (a) Zat dapat dibagi menjadi yang wajib dan yang mungkin, yang abstrak dan yang material, dan pokok yang dibagi itu sama-sama dimiliki oleh bagian-bagiannya.
- (b) Bila kita memahami zat-zat, kemudian kita meyakini bahwa suatu zat wajib karena zatnya, keyakinan pertama tetap. Bila kemudian kita meyakini bahwa zat itu mungkin karena zatnya, keyakinan bahwa ia wajib karena zatnya hilang, tetapi keyakinan bahwa ia zat tidak hilang. Maka tetaplah bahwa keberadaannya sebagai zat[^a101] adalah kadar yang sama-sama dimiliki oleh yang wajib, yang mungkin, yang material,[^a102] dan yang abstrak.

[^a101]: CA: Frasa "maka tetaplah bahwa keberadaannya sebagai zat" ditambahkan dari naskah S.

[^a102]: CA: Naskah M: "yang terpisah (dari materi)" (*al-mufāriq*) sebagai ganti "yang material".

Bila hal ini telah tetap, kami katakan: tidak diragukan bahwa Zat Yang Wajib Ada[^a103] berbeda dari zat-zat lainnya karena suatu batasan; demikian pula zat akal berbeda dari zat jisim karena suatu batasan.[^a104] Sebab, seandainya tidak ada sesuatu yang dengannya pembedaan terjadi, niscaya pembedaan sama sekali tidak terjadi. Bila hal ini telah tetap, kami katakan: telah tetap bahwa zat-zat, sejauh ia zat, adalah hal-hal yang setara; kemudian masing-masing zat itu terkhusus dengan sesuatu yang karenanya ia berbeda dari yang lain. Jika kekhususan masing-masing dengan pembeda itu terjadi karena sesuatu yang lain, niscaya terjadi lingkaran atau regresi tak berhingga, dan keduanya mustahil. Maka kekhususan itu pasti terjadi bukan karena sesuatu dan bukan karena penentu keunggulan. Dengan dalil ini tetaplah terjadinya yang mungkin tanpa penentu keunggulan. Lagi pula, pendapat ini dianut oleh segolongan besar orang berakal. Semua ini membatalkan pendapat bahwa kebutuhan yang mungkin kepada penentu keunggulan adalah premis yang diketahui secara swabukti.

[^a103]: CA: Naskah S: "bahwa zat yang wajib" (tanpa kata "ada").

[^a104]: CA: Kalimat "demikian pula zat akal … suatu batasan" ditambahkan dari naskah S.

**Pertanyaan ketiga**: sebagaimana kita lihat mayoritas orang berakal sepakat bahwa yang baharu pasti memiliki yang membaharukan dan bangunan pasti memiliki pembangun, kita lihat pula mereka sepakat atas premis-premis lain, padahal para mutakalim menganggapnya tidak[^a105] benar.

[^a105]: CA: Kata "tidak" ditambahkan dari naskah N.

Pertama, sebagaimana mereka menganggap mustahil terjadinya bangunan tanpa pembangun, mereka pun menganggap mustahil terjadinya bangunan tanpa materi yang mendahuluinya, misalnya bangunan terjadi tanpa didahului tanah, batu, dan kayu. Seandainya kepastian orang-orang berakal bahwa bangunan membutuhkan pelaku menjadi hujah[^a106] atas kebenaran premis itu, niscaya kepastian mereka bahwa bangunan membutuhkan materi yang mendahuluinya juga menjadi hujah atas kebenaran premis ini. Padahal para mutakalim menganggap bahwa terjadinya sesuatu tidak membutuhkan materi yang mendahuluinya. Ini menunjukkan bahwa kesepakatan mayoritas orang berakal atas suatu hukum berdasarkan fitrah asali tidak menunjukkan bahwa hukum itu benar.

[^a106]: CA: Naskah S: "menjadi hujah, niscaya kepastian mereka … dst." dengan susunan berbeda.

Jika mereka berkata, "Berdasarkan fitrah asali, mereka sepakat bahwa bangunan membutuhkan pembangun, tetapi mereka tidak sepakat bahwa bangunan membutuhkan materi yang mendahuluinya, dengan bukti bahwa para mutakalim menyelisihi mereka dalam kebenaran premis ini", kami jawab: bila kita hendak membedakan proposisi-proposisi fitri yang asali[^a107] dari selainnya, yang dijadikan patokan dalam pembedaan itu adalah hukum fitrah asali[^a108] yang belum terbiasa dengan perbantahan dan perdebatan dan belum akrab dengan sikap keras kepala. Sudah dimaklumi bahwa hukum mayoritas makhluk tentang salah satu dari kedua proposisi ini sama dengan hukum mereka tentang proposisi yang lain. Tinggal dikatakan: segolongan mutakalim menyelisihi bahwa bangunan membutuhkan materi yang mendahuluinya. Maka dapat pula dikatakan: segolongan lain menyelisihi bahwa bangunan membutuhkan pembangun. Jika tampaknya[^a109] penyelisihan dari kelompok kecil merusak keswabuktian suatu proposisi, makna ini ada pada kedua sisi. Dan jika persetujuan dan penyelisihan kaum ahli debat dan perbantahan tidak diperhitungkan, dan yang diperhitungkan hanyalah hukum fitrah asali dan jiwa-jiwa yang bersih dari coretan-coretan batil, makna ini pun ada pada kedua bab. Maka tampaklah bahwa tidak ada jalan untuk membedakan keduanya.

[^a107]: CA: Naskah S: "proposisi-proposisi swabukti" (*al-badīhiyya*) sebagai ganti "proposisi-proposisi fitri yang asali".

[^a108]: CA: Naskah S: "maka yang kami maksud dalam hal itu adalah pembedaan fitrah asali".

[^a109]: CA: Naskah S: "jalan" (*ṭarīq*) sebagai ganti "tampaknya" (*ẓuhūr*).

Kedua, kita lihat orang-orang berakal sepakat bahwa sesuatu hanya terjadi pada waktu tertentu dan tempat tertentu.[^a110] Kemudian para mutakalim menganggap bahwa terjadinya sesuatu tidak bergantung pada didahului oleh waktu tertentu dan tempat tertentu; jika tidak demikian, niscaya mereka harus berpendapat bahwa waktu dan tempat itu qadim. Bila hal ini telah tetap, kami katakan: menurut akal, kesepakatan orang-orang berakal bahwa yang baharu membutuhkan pelaku tidak lebih kuat daripada kesepakatan mereka bahwa yang baharu[^a111] membutuhkan waktu dan tempat. Jika boleh mendustakan salah satu dari kedua bab, boleh pula mendustakan bab yang kedua;[^a112] dan jika wajib membenarkan salah satunya, wajib pula membenarkan bab yang kedua. Maka tetaplah bahwa pembedaan itu batil.

[^a110]: CA: Frasa "dan tempat tertentu" ditambahkan dari naskah S.

[^a111]: CA: Frasa "membutuhkan pelaku tidak lebih kuat … bahwa yang baharu" ditambahkan dari naskah N.

[^a112]: CA: Naskah S: "bab yang lain" (*al-ākhar*). Kata "kedua" pada kalimat berikutnya ditambahkan dari naskah N.

Ketiga, orang-orang berakal memastikan bahwa bangunan tertentu di sebuah rumah atau madrasah hanya terjadi melalui manusia yang mengurus perbaikan bangunan itu. Adapun terjadinya bangunan itu[^a113] tanpa diurus oleh seorang manusia pun dianggap mustahil oleh semua orang. Bahkan, seandainya seseorang mengaku bahwa kemarin ia meninggalkan sebuah padang pasir, lalu keesokan harinya ia kembali dan mendapati rumah-rumah dan kebun-kebun telah berdiri di sana tanpa seorang manusia pun hadir untuk mengurusnya, mayoritas orang berakal akan mendustakan ucapan itu. Kepastian ini ada dalam akal mayoritas, padahal menurut para mutakalim kepastian ini batil. Sebab mereka membolehkan Allah Ta'ala menciptakan bangunan itu secara langsung tanpa perantaraan manusia, dan membolehkan pula salah satu malaikat, atau salah satu jin dan setan, yang mengurus perbaikannya. Maka tetaplah bahwa para mutakalim sepakat bahwa tidak setiap hukum yang diputuskan mayoritas makhluk berdasarkan fitrah asali dan naluri yang sehat pasti benar. Bila hal ini telah tetap, dan tetap pula bahwa kalian tidak memiliki sandaran bagi kebenaran ucapan kalian "yang baharu pasti memiliki yang membaharukan" selain bahwa mayoritas makhluk menghukumi kebenaran premis ini berdasarkan fitrah asali, maka tetaplah bahwa premis ini lemah.

[^a113]: CA: Kalimat "Adapun terjadinya bangunan itu" ditambahkan dari naskah S.

**Pertanyaan keempat**: kami katakan, jika uraian kalian menunjukkan bahwa pengetahuan tentang kebutuhan yang mungkin dan yang baharu kepada pemberi pengaruh adalah pengetahuan niscaya, di sini ada beberapa segi yang menunjukkan bahwa pengetahuan ini tidak niscaya. Penjelasannya dari beberapa segi.

**Sanggahan pertama**: bila kita hadapkan kepada akal kita bahwa satu adalah separuh dari dua, dan kita hadapkan pula bahwa yang mungkin pasti memiliki penentu keunggulan, kita dapati hukum akal atas proposisi pertama lebih jelas daripada hukumnya atas proposisi kedua. Perbedaan kekuatan antara kedua hukum ini menunjukkan bahwa kemungkinan sebaliknya ada pada proposisi yang kalah kuat, dan ini menunjukkan bahwa proposisi yang kalah kuat itu bersifat dugaan, bukan kepastian.

Jika dikatakan:

- (a) Kami tidak menerima adanya perbedaan dalam kepastian akal atas kedua proposisi ini. Apa dalilnya?
- (b) Anggaplah perbedaan antara kedua hukum ini terjadi pada sebagian waktu; namun pada sebagian waktu lain kekuatan keduanya bisa setara. Orang yang mendengar suara manusia mengetahui secara niscaya kehadiran manusia itu, dan pengetahuan ini setara kekuatannya dengan pengetahuan bahwa satu adalah separuh dari dua.
- (c) Anggaplah perbedaan itu terjadi secara mutlak; namun kami tidak menerima bahwa perbedaan itu kembali kepada pembenaran; ia kembali kepada konsepsi. Penjelasannya: pembenaran bergantung pada konsepsi kedua ujung proposisi. Konsepsi-konsepsi dalam ucapan kita "satu adalah separuh dari dua" adalah konsepsi yang terang dan tidak membutuhkan definisi, sebab di dalamnya hanya ada konsepsi satu, dua, dan separuh,[^a114] dan konsepsi-konsepsi ini terang dan tidak membutuhkan definisi. Berbeda dengan ucapan kita "yang mungkin membutuhkan pemberi pengaruh", sebab pembenaran ini bergantung pada konsepsi esensi yang mungkin, esensi kebutuhan, dan esensi[^a115] pemberi pengaruh, dan konsepsi ketiga hal ini samar dan tersembunyi. Jadi perbedaan yang terdapat dalam akal makhluk antara kedua hukum ini terjadi karena perbedaan antara konsepsi-konsepsinya. Adapun anggapan bahwa perbedaan itu terjadi pada pembenaran-pembenaran itu sendiri tidak dapat diterima. Apa dalilnya?
- (d) Anggaplah perbedaan itu terjadi di antara pembenaran-pembenaran. Mengapa kalian katakan bahwa bila salah satu pembenaran lebih kuat daripada yang lain, pembenaran yang kalah kuat pasti bersifat dugaan dan mustahil bersifat yakin? Apa dalil bahwa perkaranya demikian?

[^a114]: CA: Kalimat "sebab di dalamnya hanya ada … tidak membutuhkan definisi" ditambahkan dari naskah N.

[^a115]: CA: Kata "esensi" ditambahkan dari naskah S.

Jawabannya:

- (a) Tentang ucapannya, "Kami tidak menerima adanya perbedaan antara hukum kita bahwa satu adalah separuh dari dua dan hukum kita bahwa salah satu sisi yang mungkin tidak menjadi lebih unggul kecuali karena penentu keunggulan", kami katakan: perbedaan ini diketahui dengan akal secara swabukti, sehingga mengingkarinya berarti mengingkari yang swabukti. Seandainya kalian boleh bersikeras dalam pengingkaran ini secara keras kepala, orang lain pun boleh berkata, "Aku tidak mendapati dalam diriku kepastian akal bahwa yang baharu pasti memiliki yang membaharukan." Walhasil, pokok yang diperhitungkan dalam membedakan hal-hal swabukti dari yang lain adalah apa yang didapati orang-orang berakal dalam jiwa dan akal mereka secara nyata dan terang. Jika kalian membuka pintu pengingkaran secara keras kepala, pintu-pintu itu terbuka bagi semua hal, dan ketika itu segalanya menjadi rusak.
- (b) Tentang pertanyaan kedua, yaitu bahwa akal, meskipun memutuskan adanya perbedaan pada sebagian waktu, bisa memutuskan kesetaraan keduanya pada waktu-waktu lain, kami katakan: terjadinya perbedaan pada sebagian kasus sudah cukup untuk menggugat, sedangkan kesetaraan pada banyak kasus tidak menghasilkan kebenaran. Penjelasannya: proposisi swabukti adalah proposisi yang semata-mata[^a116] konsepsi subjek dan predikatnya sudah cukup bagi pikiran untuk memastikan nisbah salah satunya kepada yang lain, baik dengan negasi maupun afirmasi. Seandainya proposisi ini swabukti, niscaya konsepsi subjek dan predikatnya cukup untuk menghasilkan pembenaran itu. Jika demikian, mustahil kedua konsepsi itu terlepas dari terjadinya kepastian dalam pembenaran. Bila kedua konsepsi itu terlepas dari kepastian dalam pembenaran, walaupun hanya dalam satu kasus, hal itu sudah cukup untuk mengetahui bahwa kedua konsepsi itu tidak mengharuskan pembenaran tersebut, sebab mengecualikan kebalikan konsekuen (*tālī*)[^k-tali] menghasilkan kebalikan anteseden (*muqaddam*). Adapun seandainya kepastian itu terjadi dalam sejuta kasus, hal itu sama sekali tidak menghasilkan apa pun, sebab mengecualikan konsekuen itu sendiri sama sekali tidak menghasilkan apa pun.
- (c) Jawaban atas pertanyaan ketiga dari dua segi. Pertama, kami tidak menerima bahwa konsepsi apa pun dapat bersifat perolehan (*kasbī*); pokok ini telah ditetapkan pada awal ilmu logika. Kedua, anggaplah konsepsi dapat bersifat perolehan; namun kita menghadirkan esensi yang mungkin, esensi kebutuhan, dan esensi pemberi pengaruh dalam akal dan pikiran kita dengan cara yang paling sempurna. Sebab yang mungkin tidak memiliki penjelasan selain "yang menerima wujud dan ketiadaan sejauh ia adalah dirinya", atau "yang pengandaian wujudnya dan pengandaian ketiadaannya, sejauh ia adalah dirinya, tidak meniscayakan kemustahilan". Kebutuhan tidak memiliki penjelasan selain keperluan dan ketergantungan. Pemberi pengaruh tidak memiliki penjelasan selain hal yang dengannya dan karenanya sesuatu itu terjadi. Bila engkau telah mengetahui hal ini, kami katakan: setelah kita menghadirkan ketiga konsepsi ini dalam akal kita dengan cara yang paling sempurna, bila kita memandang kepastian akal atas kebenaran ucapan kita "salah satu sisi yang mungkin tidak menjadi lebih unggul daripada yang lain kecuali karena penentu keunggulan", lalu kita memandang kepastian akal bahwa satu adalah separuh dari dua, kita tahu secara niscaya bahwa kepastian yang pertama jauh lebih lemah daripada kepastian yang kedua. Perbedaan ini bukan karena perbedaan dalam konsepsi-konsepsi, sebab dalam keadaan ini kita telah menghadirkan konsepsi-konsepsi itu dengan cara yang paling sempurna. Maka kita tahu bahwa perbedaan ini hanya terjadi pada hukum dan pembenaran.[^a117]
- (d) Tentang pertanyaan keempat, yaitu ucapannya, "Apa dalil bahwa bila salah satu dari kedua kepastian lebih kuat daripada yang lain, yang kalah kuat bersifat dugaan dan bukan yakin?", kami katakan: dalil bahwa proposisi yang kalah kuat pasti bersifat dugaan dan bukan yakin ialah bahwa kepastian akal atas proposisi yang kalah kuat ini adakalanya disertai penolakan menyeluruh terhadap kebalikannya, adakalanya penolakan tegas terhadap kebalikannya tidak ada. Jika penolakan tegas terhadap kebalikannya ada, mustahil terjadi perbedaan. Jika penolakan tegas terhadap kebalikannya tidak ada, melainkan kemungkinan kebalikannya ada dari sebagian segi,[^a118] baik kemungkinan itu dekat maupun jauh, maka pembenaran itu adalah dugaan yang kuat (*ẓann ghālib*), sebab kemungkinan kebalikan menuntut makna ini. Dan ketika itu kepastian tersebut bukan kepastian dan keyakinan, melainkan dugaan. Inilah seluruh pembahasan tentang jawaban atas pertanyaan-pertanyaan yang mereka ajukan terhadap dalil ini.

[^a116]: CA: Kata "semata-mata" (*mujarrad*) ditambahkan dari naskah N.

[^k-tali]: **Konsekuen** (*tālī*; Ing. *the next, the predicate*). Menurut para ahli logika, *tālī* adalah bagian kedua dari proposisi kondisional (*qaḍiyya sharṭiyya*), dinamai demikian karena ia mengikuti bagian pertama, yang disebut anteseden (*muqaddam*) karena mendahuluinya. Dalam ucapan "Jika matahari terbit, maka siang ada", "jika matahari terbit" adalah anteseden dan "maka siang ada" adalah konsekuen. (*Kashshāf*, s.v. *al-tālī*.)

[^a117]: CA: Kalimat "jauh lebih lemah … hukum dan pembenaran" ditambahkan dari naskah S.

[^a118]: CA: Kalimat "mustahil terjadi perbedaan … kemungkinan kebalikannya ada" ditambahkan dari naskah Z (sebagian tidak terbaca).

**Sanggahan kedua**, untuk menjelaskan bahwa kebutuhan yang mungkin kepada penentu keunggulan bukanlah premis swabukti: telah kami sebutkan bahwa segolongan besar orang berakal berpendapat bahwa salah satu sisi yang mungkin boleh menjadi lebih unggul daripada yang lain tanpa penentu keunggulan. Seandainya proposisi ini swabukti, mustahil golongan-golongan besar bersepakat mengingkarinya.

**Sanggahan ketiga**: seandainya premis ini swabukti, niscaya pengetahuan bahwa yang mungkin yang bertahan, dalam keadaan bertahannya, membutuhkan pemberi pengaruh adalah pengetahuan swabukti, sebab kemungkinan ada padanya. Namun perkaranya tidak demikian, sebab kebanyakan orang berakal menyatakan kebatilannya dan berkata: mengadakan yang sudah ada adalah mustahil menurut akal secara swabukti. Maka kita tahu bahwa pengetahuan[^a119] tentang kebutuhan yang mungkin kepada pemberi pengaruh bukanlah hukum swabukti. Inilah akhir pembahasan tentang jalan-jalan pertanyaan dan sanggahan.

[^a119]: CA: Naskah S: "hukum" (*al-ḥukm*) sebagai ganti "pengetahuan" (*al-ʿilm*).

**Jawaban**. Tentang ucapannya pada pertanyaan pertama, "Syubhat-syubhat yang kalian sebutkan hanya menunjukkan bahwa pengetahuan tentang kebutuhan yang baharu kepada pemberi pengaruh adalah pengetahuan niscaya, dan tidak menunjukkan bahwa pengetahuan tentang kebutuhan yang mungkin kepada pemberi pengaruh[^a120] dan penentu keunggulan adalah pengetahuan niscaya", kami katakan:[^a121] untuk menjawabnya ada dua jalan.

[^a120]: CA: Kata "pemberi pengaruh" ditambahkan dari naskah M.

[^a121]: CA: Naskah M: "kami katakan: kami memiliki (dua jalan) terhadapnya".

Jalan pertama: kami katakan, karena telah tetap dengan segi-segi yang disebutkan tadi bahwa pengetahuan tentang kebutuhan yang baharu[^a122] kepada pemberi pengaruh adalah pengetahuan niscaya dan swabukti,[^a123] maka hal itu mengharuskan kemungkinan pun menjadi sebab kebutuhan kepada pemberi pengaruh. Dalilnya: bila kita mengandaikan sesuatu qadim dan azali, lalu bersamaan dengan itu kita mengandaikannya wajib ada karena zatnya, maka di sini ada keyakinan bahwa ia azali dan ada pula keyakinan bahwa ia wajib ada karena zatnya.[^a124] Bersamaan dengan kedua keyakinan ini, mustahil kita meyakini bahwa dalam wujudnya ia membutuhkan penentu keunggulan dan pemberi pengaruh. Ini menunjukkan bahwa sumber kebutuhan adakalanya kebaharuan, adakalanya kemungkinan, sebab ketika kita mengandaikan hilangnya kedua pengertian ini, mustahil kita menghukumi adanya kebutuhan. Maka tetaplah bahwa yang menuntut kebutuhan adalah gabungan kedua batasan ini atau salah satunya. Bila hal ini telah tetap, kami katakan: kebaharuan mustahil menjadi sebab kebutuhan, bagian dari sebabnya, atau syarat sebabnya. Bila kebaharuan gugur dari pertimbangan, tinggallah bahwa yang berpengaruh dalam kebutuhan ini hanyalah kemungkinan. Dengan jalan ini tampak bagi kita bahwa kemungkinan adalah sebab kebutuhan kepada pemberi pengaruh. Adapun penjelasan bahwa kebaharuan mustahil diperhitungkan dalam hal ini akan datang dalam satu pasal tersendiri.[^a125]

[^a122]: CA: Naskah S: *al-muḥdath* (yang baharu) dengan bentuk berbeda.

[^a123]: CA: Naskah S: "pengetahuan swabukti" sebagai ganti "perkara yang niscaya lagi swabukti".

[^a124]: CA: Kalimat "maka di sini ada keyakinan … wajib ada karena zatnya" ditambahkan dari naskah Z.

[^a125]: CA: Kalimat "Adapun penjelasan … satu pasal tersendiri" ditambahkan dari naskah S.

Jalan kedua: kami tinggalkan segi yang telah kami sebutkan, lalu kami katakan: yang mungkin adalah sesuatu yang nisbah wujud kepadanya sama dengan nisbah ketiadaan. Bila kita meyakini bahwa nisbah wujud dan nisbah ketiadaan kepadanya setara, akal yang jernih memutuskan bahwa mustahil salah satu sisi menjadi lebih unggul daripada yang lain kecuali karena sesuatu yang terpisah. Pengetahuan bahwa perkaranya demikian adalah pengetahuan swabukti dan niscaya. Siapa yang mengingkarinya, ia telah meninggalkan tuntutan akalnya[^a126] dengan lisannya, tetapi hati nuraninya kembali kepadanya. Bila kita berpegang pada jalan ini, kita tidak perlu menyebutkan syubhat-syubhat itu dan menguraikan contoh-contoh tersebut. Inilah jawaban atas pertanyaan pertama.

[^a126]: CA: Naskah S: "meninggalkan pengetahuannya" (*fāraqa ʿilmah*).

Adapun pertanyaan kedua,[^p7] yaitu ucapan mereka, "Sebagaimana akal memastikan bahwa yang baharu pasti memiliki pelaku, akal pun memastikan bahwa yang baharu pasti didahului oleh materi, rentang masa, dan tempat", kami katakan: pertanyaan ini tidak berlaku bagi para filsuf, sebab mereka berpegang bahwa yang baharu,[^a127] sebagaimana ia pasti memiliki pelaku yang mendahuluinya,[^a128] ia pun pasti memiliki materi yang mendahuluinya dan rentang masa yang mendahuluinya. Dengan jalan ini,[^a129] pertanyaan ini tidak berlaku bagi mereka.

[^p7]: CP: Menurut urutan pertanyaan di atas, isi pertanyaan ini adalah pertanyaan ketiga. Edisi Turki menyebutnya "pertanyaan ketiga", sedangkan teks Arab menyebutnya "pertanyaan kedua".

[^a127]: CA: Frasa "bahwa yang baharu" ditambahkan dari naskah N. Kata sebelumnya dalam kalimat pertanyaan ("materi") juga ditambahkan dari naskah N.

[^a128]: CA: Kata "yang mendahuluinya" ditambahkan dari naskah N.

[^a129]: CA: Frasa "dengan jalan ini" ditambahkan dari naskah N.

Adapun para penganut kebaharuan materi dan rentang masa, mereka berkata: perbedaan antara kedua bab itu jelas. Mengenai materi, tidak ada perselisihan bahwa bentuk-bentuk dan aksiden-aksiden terjadi dari ketiadaan murni. Bila kita memahami terjadinya sebagian hal dari ketiadaan murni,[^a130] mengapa terjadinya zat-zat dari ketiadaan murni mustahil menurut akal pada tingkat pertamanya?[^a131] Mengenai rentang masa, mereka berkata: tidak diragukan bahwa sebagian bagiannya mendahului sebagian yang lain, tetapi bukan karena rentang masa yang lain; jika tidak demikian, niscaya rentang masa berada di dalam rentang masa yang lain, dan terjadilah regresi tak berhingga, dan itu mustahil. Maka tetaplah bahwa didahuluinya bagian yang belakangan dari rentang masa oleh bagian yang lebih dahulu[^p8] bukan karena rentang masa yang lain. Bila hal ini dapat dipahami, mengapa tidak dapat dipahami bahwa ketiadaan yang baharu mendahului wujudnya tanpa rentang masa? Maka tetaplah dengan kedua jalan ini bahwa akal yang jernih tidak menuntut yang baharu, dalam kebaharuannya, didahului oleh materi dan rentang masa, sebab dalam kedua kasus ini akal menghukumi adanya kebaharuan tanpa didahului materi dan rentang masa. Adapun mengenai pelaku, akal yang jernih menghukumi adanya kebutuhan kepada pelaku, dan tidak ada sesuatu yang baharu pun yang terjadi tanpa pelaku. Maka tampaklah perbedaannya.

[^a130]: CA: Kalimat "Bila kita memahami … ketiadaan murni" ditambahkan dari naskah S.

[^a131]: CA: Frasa "pada tingkat pertamanya" (*fī awwal al-ʿaql*) ditambahkan dari naskah S.

[^p8]: CP: Naskah S dalam edisi Arab membaca "bagian yang lebih dahulu" (*juzʾ al-mutaqaddam*); teks yang dicetak dalam berkas OCR rusak di tempat ini. Terjemahan mengikuti maksudnya.

Adapun ucapannya dalam sanggahan pertama, "Kepastian akal atas ucapan kita 'satu adalah separuh dari dua' lebih kuat daripada kepastiannya bahwa salah satu sisi yang mungkin tidak menjadi lebih unggul daripada yang lain kecuali karena penentu keunggulan", jawaban yang benar adalah bahwa perbedaan ini tidak diterima. Sebab, orang yang menghilangkan dari akalnya kebiasaan berdebat dan berbantah dalam segala hal, lalu menghadirkan dalam akalnya bahwa nisbah wujud kepadanya sama dengan nisbah ketiadaan kepadanya, dan bahwa sama sekali tidak ada keunggulan salah satu sisi atas yang lain, niscaya memastikan secara swabukti bahwa selama kesetaraan ini tetap berlangsung, mustahil terjadi keunggulan. Bila keunggulan terjadi, kesetaraan itu telah hilang dan sesuatu yang lain telah bergabung ke sisi yang unggul. Bila akal memandang proposisi ini dengan cara demikian, tidak tersisa perbedaan antara proposisi ini dan ucapan "satu adalah separuh dari dua".

Adapun sanggahan kedua, yaitu ucapannya, "Sekelompok orang berakal membolehkan salah satu sisi yang mungkin menjadi lebih unggul daripada yang lain tanpa penentu keunggulan; seandainya proposisi ini swabukti, mereka tidak akan berselisih tentangnya", kami katakan: kami tidak menerima bahwa mereka berpegang pada keunggulan yang mungkin tanpa penentu keunggulan.[^a132] Memang, bisa jadi hal itu merupakan konsekuensi dari sebagian pendapat mereka; namun perbedaan antara konsekuensi suatu pendapat (*luzūm*) dan berpegang padanya (*iltizām*) sudah dimaklumi.[^p9]

[^a132]: CA: Naskah S: "tanpa pemberi pengaruh" (*muʾaththir*). Catatan lain di tempat ini sebagian tidak terbaca.

[^p9]: CP: Kalimat sesudah "Memang, bisa jadi" terpotong dalam berkas OCR teks Arab; terjemahan melengkapinya menurut edisi Turki.

Adapun sanggahan ketiga, yaitu ucapan mereka, "Seandainya proposisi ini swabukti, niscaya pengetahuan bahwa yang mungkin yang bertahan membutuhkan pemberi pengaruh adalah pengetahuan swabukti, padahal tidak demikian", kami katakan: setiap orang yang mengonsepsikan bahwa maujud yang bertahan itu setara (antara wujud dan ketiadaannya) terdorong secara niscaya kepada pengetahuan bahwa ia membutuhkan pemberi pengaruh. Memang, kadang orang tidak menghukumi bahwa ia membutuhkan pemberi pengaruh[^a133] karena meyakini bahwa, karena ia bertahan, ia menjadi lebih layak untuk ada. Namun bila ia menghilangkan syubhat ini dari hatinya dan mengetahui bahwa dalam keadaan bertahan pun kedua sisinya tetap setara sebagaimana dalam keadaan mulai ada, ia terdorong secara niscaya kepada pengetahuan bahwa ia membutuhkan pemberi pengaruh.

[^a133]: CA: Kalimat "Memang, kadang orang tidak menghukumi … pemberi pengaruh" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

Inilah seluruh pembahasan tentang penetapan[^a134] pendapat kami bahwa pengetahuan tentang kebutuhan yang mungkin kepada pemberi pengaruh adalah pengetahuan swabukti. Dan hanya Allah yang memberi hidayah dan bimbingan.[^a135]

[^a134]: CA: Kata "penetapan" (*taqrīr*) dalam salah satu naskah ditulis berbeda (sebagian tidak terbaca).

[^a135]: CA: Kalimat penutup ini ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

### Pasal Ketiga {.pasal-ke}

### Pendapat Orang-Orang yang Menyatakan bahwa Premis "Salah Satu Sisi yang Mungkin Menjadi Lebih Unggul daripada yang Lain Hanya karena Penentu Keunggulan" Harus Dibuktikan {.judul-pasal}

[Tr. h. 38]{.penanda}

Ketahuilah, dalam masalah ini perkataan Syekh ar-Ra'is Abu Ali Ibnu Sina[^a136] goyah. Sebab, di mana pun ia menyebut premis ini dalam kitab-kitabnya, yang panjang maupun yang ringkas, ia mengaku hendak menegakkan burhan atas kebenarannya, lalu ia menyebutkan pembagian-pembagian panjang yang keluar dari maksud. Kemudian, ketika ia sampai pada bagian yang menjadi tujuan dan maksud itu, ia mengklaim bahwa premis itu swabukti. Siapa pun yang menelaah kitab-kitabnya dengan perenungan yang sempurna akan tahu bahwa perkaranya seperti yang kami sebutkan. Pada awalnya ia mengklaim bahwa premis itu bersifat pendalilan (*istidlālī*), dan pada akhirnya, ketika pembahasan menyempit baginya, ia mengklaim bahwa premis itu swabukti.

[^a136]: CA: Nama "Ibnu Sina" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

Aku melihat Abu al-Husain Muhammad bin Ali al-Bashri, salah seorang yang cerdas di kalangan Muktazilah, berhujah atas kebenaran premis ini dalam kitabnya yang ia namai *al-Taṣaffuḥ*. Ia berkata: yang mungkin adalah sesuatu yang kedua sisinya setara. Seandainya keunggulan terjadi tanpa penentu keunggulan, niscaya keunggulan terjadi pada saat kesetaraan ada, dan itu berarti menghimpun dua hal yang saling berlawanan, dan itu mustahil.

Namun orang dapat berkata: kontradiksi ini tidak niscaya. Sebab, yang mungkin adalah sesuatu yang esensinya tidak menuntut keunggulan salah satu sisi atas yang lain; dan kebalikan dari proposisi ini adalah: esensi itu menuntut keunggulan salah satu sisi atas yang lain.[^a137] Adapun bila dikatakan bahwa hakikatnya tidak menuntut keunggulan, kemudian keunggulan terjadi bukan karena zatnya dan bukan pula karena yang lain, maka dengan pengandaian ini kontradiksi itu tidak niscaya.

[^a137]: CA: Kalimat "dan kebalikan dari proposisi ini … atas yang lain" ditambahkan dari naskah N.

Orang ini mengira bahwa karena keunggulan itu tidak disebabkan oleh sesuatu yang lain, ia pasti disebabkan oleh zatnya sendiri, sehingga zatnya menuntut keunggulan itu, dan ini bertentangan dengan ucapan kita bahwa zat itu tidak menuntut keunggulan. Namun perkataan ini hanya benar bila telah tetap bahwa terjadinya keunggulan, bila tidak disebabkan oleh yang lain, pasti disebabkan oleh zatnya sendiri; dan ini hanya benar bila telah tetap bahwa terjadinya keunggulan[^a138] bukan karena zatnya dan bukan karena yang lain adalah mustahil. Jika ia mengklaim pengetahuan swabukti atas premis ini, itu berarti meninggalkan pendalilan. Jika ia mengklaim menetapkannya dengan dalil, kami katakan: telah tetap bahwa kebenaran dalil yang mereka sebutkan[^a139] bergantung pada kebenaran tuntutan ini; seandainya kebenaran tuntutan ini kita gantungkan pada dalil itu, niscaya terjadi lingkaran, dan lingkaran itu batil.

[^a138]: CA: Kalimat "bila tidak disebabkan oleh yang lain … terjadinya keunggulan" ditambahkan dari naskah S.

[^a139]: CA: Frasa "yang mereka sebutkan" ditambahkan dari naskah S.

Bila engkau telah mengetahui hal ini, kami katakan: yang dapat diandalkan untuk menetapkan tuntutan ini ada beberapa segi.

**Hujah pertama**: telah kami jelaskan bahwa pengetahuan swabukti ada tentang kebutuhan yang baharu kepada pemberi pengaruh. Telah kami jelaskan pula bahwa sebab kebutuhan itu adakalanya kebaharuan, adakalanya kemungkinan, dan adakalanya gabungan keduanya; dan telah kami jelaskan bahwa kebaharuan bukan sebab yang sempurna, bukan bagian dari sebab, dan bukan pula syaratnya, sehingga ia gugur sama sekali dari pertimbangan. Bila kebaharuan gugur dari pertimbangan, tidak tersisa selain kemungkinan. Ini menunjukkan bahwa sebab kebutuhan adalah kemungkinan.

**Hujah kedua** untuk menetapkan tuntutan ini: tidak diragukan bahwa yang mungkin adalah sesuatu yang nisbah wujud kepadanya sama dengan nisbah ketiadaan kepadanya. Selama kesetaraan ini tetap berlangsung, mustahil terjadi keunggulan, sebab kesetaraan yang sempurna bertentangan dengan terjadinya[^a140] keunggulan. Maka tetaplah bahwa masuknya yang mungkin ke dalam wujud bergantung pada terjadinya keunggulan. Keunggulan ini, karena terjadi setelah sebelumnya tidak ada, adalah sesuatu yang eksistensial dan positif; dan sifat eksistensial yang tetap pasti memiliki yang disifati yang maujud. Mustahil yang disifati dengan sifat eksistensial ini adalah wujud sesuatu itu sendiri,[^a141] karena telah kami jelaskan bahwa terjadinya keunggulan ini mendahului wujud yang mungkin dalam urutan martabat, sedangkan wadah mendahului apa yang bertempat di dalamnya dalam urutan martabat.[^a142] Seandainya kita katakan bahwa wadah keunggulan ini adalah zat itu ketika ia menjadi maujud, niscaya keunggulan ini mendahului keunggulan itu sendiri, sebagaimana wadah mendahului yang bertempat di dalamnya; dan itu lingkaran, sedangkan lingkaran batil. Maka tetaplah bahwa wadah keunggulan ini bukanlah hal mungkin yang merupakan akibat itu sendiri. Jadi pasti ada sesuatu lain yang berlainan dengannya, yang menjadi wadah bagi keunggulan ini, dan yang keadaannya sedemikian rupa sehingga terjadinya keunggulan padanya meniscayakan terjadinya wujud akibat ini. Yang kami maksud dengan pelaku dan pemberi pengaruh tidak lain adalah maujud yang memiliki keadaan dan sifat seperti yang kami sebutkan. Maka tetaplah bahwa yang mungkin tidak dapat masuk ke dalam wujud kecuali karena pemberi pengaruh yang terpisah darinya. Itulah yang dituju.

[^a140]: CA: Kata "terjadinya" (*ḥuṣūl*) ditambahkan dari naskah S.

[^a141]: CA: Kalimat "yang disifati dengan sifat eksistensial … sesuatu itu sendiri, karena telah kami jelaskan bahwa terjadinya" ditambahkan dari naskah S.

[^a142]: CA: Kalimat "sedangkan wadah mendahului … urutan martabat" ditambahkan dari salah satu naskah (siglumnya tidak terbaca). Catatan lain di tempat ini: naskah S membaca "pada" (*fī*).

**Hujah ketiga**:[^p10] seandainya keunggulan salah satu sisi yang mungkin atas yang lain tidak membutuhkan pemberi pengaruh dan penentu keunggulan, niscaya mustahil keunggulan itu, dalam kasus mana pun, bergantung pada adanya pemberi pengaruh dan penentu keunggulan.[^a143] Konsekuen ini batil, maka anteseden itu pun batil.[^a144] Penjelasan kelaziman (antara keduanya): bila keunggulan itu tidak membutuhkan pemberi pengaruh, mustahil ia membutuhkan pemberi pengaruh dalam kasus mana pun, sebab tuntutan hakikat dan esensi sama sekali tidak berubah. Bila keunggulan salah satu sisi yang mungkin atas yang lain, sejauh ia adalah dirinya, tidak membutuhkan pemberi pengaruh, ketidakbutuhan ini berlaku dalam semua kasus; dan sesuatu yang karena zatnya tidak membutuhkan sesuatu mustahil membutuhkannya. Adapun penjelasan bahwa keunggulan salah satu sisi yang mungkin atas yang lain kadang bergantung pada adanya pemberi pengaruh: pengetahuan swabukti menyatakan bahwa adanya[^a145] tulisan pada kertas ini bergantung pada adanya penulis dan pada adanya segala hal yang diperlukan agar ia menjadi penulis. Demikian pula halnya dengan memotong, memukul, memecahkan, dan perbuatan-perbuatan semacamnya.

[^p10]: CP: Teks Arab menyebut hujah ini "hujah kedua" untuk kedua kalinya; terjemahan mengikuti urutan dalam edisi Turki.

[^a143]: CA: Kalimat "niscaya mustahil keunggulan itu … penentu keunggulan" ditambahkan dari naskah N.

[^a144]: CA: Kata "batil" pada anteseden ditambahkan dari naskah N.

[^a145]: CA: Kata "adanya" (*ḥuṣūl*) ditambahkan dari salah satu naskah (sebagian tidak terbaca).

**Hujah keempat**: hujah ini hanya tuntas menurut pendapat para penganut keqadiman rentang masa (*mudda*). Uraiannya: pendapat tentang keqadiman rentang masa tak terhindarkan, dan bila demikian, rentang masa dalam wujudnya pasti membutuhkan pemberi pengaruh. Penjelasan bahwa pendapat tentang keqadiman rentang masa tak terhindarkan: setiap bagian dari rentang masa adalah baharu, dan ketiadaan setiap yang baharu mendahului wujudnya. Kedahuluan ini adalah sesuatu yang melebihi ketiadaan semata, sebab ketiadaan yang belakangan sama dengan ketiadaan yang terdahulu dalam pengertiannya sebagai ketiadaan, tetapi berbeda darinya dalam hal yang satu terdahulu dan yang lain belakangan; dan segi perbedaan berlainan dengan segi kesamaan. Maka kedahuluan dan keterdahuluan ini adalah sesuatu yang melebihi ketiadaan semata, sehingga ia adalah sifat yang maujud. Kemudian kesebelumannya (*qabliyya*) itu pun baharu, sehingga ia didahului oleh kesebeluman yang lain, dan pembahasan tentangnya sama seperti tentang yang pertama. Ini mengharuskan setiap "sebelum" didahului oleh "sebelum" yang lain tanpa titik awal. Maka tetaplah dengan uraian ini bahwa rentang masa tidak memiliki awal.

Kemudian kami katakan: rentang masa tersusun dari bagian-bagian yang silih berganti dan berurutan ini, dan masing-masing bagian itu baharu, dan setiap yang baharu adalah mungkin. Jadi waktu tersusun[^a146] dari bagian-bagian yang masing-masing mungkin karena zatnya, sedangkan keseluruhan membutuhkan bagian-bagian itu, dan yang membutuhkan hal yang mungkin lebih layak lagi untuk menjadi mungkin. Maka keseluruhan rentang masa adalah sesuatu yang mungkin karena zatnya.[^a147] Keunggulan wujudnya atas ketiadaannya adakalanya karena sebab yang terpisah, adakalanya bukan karena sebab yang terpisah, melainkan karena kebetulan semata (*maḥḍ al-ittifāq*). Jika karena kebetulan semata tanpa sebab sama sekali,[^a148] maka segala yang terjadi karena kebetulan semata tanpa sebab sama sekali tidaklah mustahil menurut akal untuk sama sekali tidak ada; dan dengan pengandaian ini keterputusan rentang masa menjadi mungkin. Padahal telah kami jelaskan bahwa keterputusan dan permulaan rentang masa mustahil. Maka harus dikatakan bahwa rentang masa itu wajib ada karena keniscayaan sebabnya dan keniscayaan penyebabnya. Ini menunjukkan bahwa rentang masa mungkin karena zatnya dan wajib karena keniscayaan pemberi pengaruhnya. Bila perkaranya demikian dalam kasus ini, pasti demikian pula dalam kasus-kasus lainnya, sebab akal yang jernih secara niscaya memutuskan bahwa seluruh hal yang mungkin setara dalam pengertian ini. Dan Allah-lah yang memberi petunjuk kepada hakikat-hakikat.[^a149]

[^a146]: CA: Kalimat "dari bagian-bagian yang silih berganti … Jadi waktu tersusun" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

[^a147]: CA: Kata "karena zatnya" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

[^a148]: CA: Frasa "Jika karena kebetulan semata" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

[^a149]: CA: Kalimat penutup ini ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

### Pasal Keempat {.pasal-ke}

### Syubhat-Syubhat Orang yang Berpendapat bahwa Keunggulan Salah Satu Sisi yang Mungkin Tidak Bergantung pada Penentu Keunggulan {.judul-pasal}

[Tr. h. 49]{.penanda}

**Syubhat pertama**: seandainya yang mungkin membutuhkan pemberi pengaruh, niscaya yang bertahan, dalam keadaan bertahannya, juga membutuhkan pemberi pengaruh. Konsekuen ini batil, maka anteseden itu pun batil.

Penjelasan proposisi kondisional ini: yang mungkin adalah mungkin karena zatnya, sehingga sesuatu dalam keadaan bertahannya pasti tetap mungkin. Seandainya kemungkinan adalah sebab kebutuhan kepada pemberi pengaruh, niscaya kebutuhan kepada pemberi pengaruh terjadi pula dalam keadaan bertahan. Jangan dikatakan, "Mengapa tidak boleh dikatakan[^a150] bahwa dalam keadaan bertahan, wujud menjadi lebih layak baginya, dan karena adanya kelayakan (*awlawiyya*) ini ia tidak membutuhkan pemberi pengaruh?" Sebab kami katakan: dalih ini batil. Kelayakan yang membuatnya tidak membutuhkan pemberi pengaruh itu adakalanya sudah ada ketika ia mulai ada, adakalanya belum ada.[^a151] Jika yang pertama, niscaya ia tidak membutuhkan pemberi pengaruh ketika mulai ada, dan itu mustahil. Jika yang kedua, kelayakan itu terjadi kemudian; dan hal baharu yang dinamai kelayakan ini menjadi sebab wujud yang bertahan dalam keadaan bertahannya. Maka yang bertahan, dalam keadaan bertahannya, membutuhkan sesuatu yang dinamai kelayakan ini; dan kelayakan ini, karena[^a152] ia sesuatu yang baharu, membutuhkan sebab yang terpisah. Yang membutuhkan sesuatu yang membutuhkan hal lain, membutuhkan pula hal lain itu. Maka yang bertahan, dalam keadaan bertahannya, pasti membutuhkan sebab yang terpisah.

[^a150]: CA: Frasa "boleh dikatakan" ditambahkan dari naskah N.

[^a151]: CA: Frasa "adakalanya belum ada" ditambahkan dari naskah N. Catatan lain di tempat ini sebagian tidak terbaca.

[^a152]: CA: Naskah S membaca kata ini secara berbeda (sebagian tidak terbaca).

Maka tetaplah dengan uraian kami bahwa seandainya yang mungkin membutuhkan pemberi pengaruh, niscaya yang bertahan, dalam keadaan bertahannya, juga membutuhkan pemberi pengaruh. Kami katakan bahwa yang bertahan, dalam keadaan bertahannya, tidak membutuhkan pemberi pengaruh, sebab seandainya kita mengandaikan suatu pemberi pengaruh yang memberi pengaruh kepadanya dalam keadaan bertahannya, pemberi pengaruh itu adakalanya memiliki pengaruh, adakalanya tidak. Jika ia tidak memiliki pengaruh, mustahil ia disifati sebagai pemberi pengaruh. Jika ia memiliki pengaruh, pengaruh itu adakalanya sesuatu yang benar dikatakan bahwa ia sudah ada sebelum pemberian pengaruh ini, adakalanya sesuatu yang benar dikatakan bahwa ia belum ada sebelumnya. Jika yang pertama, niscaya terjadi pengadaan yang sudah ada, dan itu mustahil. Jika yang kedua, pengaruh itu adalah sesuatu yang benar dikatakan bahwa ia belum ada sebelum waktu itu, dan segala yang demikian adalah baharu. Jadi pemberi pengaruh ini hanya berpengaruh pada yang baharu, dan tidak memiliki pengaruh pada yang bertahan; padahal kita telah mengandaikannya berpengaruh pada yang bertahan. Ini kontradiksi.

Jangan dikatakan, "Mengapa tidak boleh dikatakan bahwa pengaruhnya[^a153] adalah bertahannya sesuatu yang sudah maujud itu?" Sebab kami katakan: bertahannya sesuatu itu adakalanya dirinya sendiri, adakalanya selainnya. Jika bertahannya adalah dirinya sendiri, sedangkan dirinya sudah ada sebelum waktu ini, maka pengaruh pemberi pengaruh ini adalah mengadakan yang sudah ada, dan itu mustahil. Jika bertahannya adalah selain dirinya, maka yang disandarkan kepada pemberi pengaruh adalah keadaan tambahan yang baharu ini; jadi dari pemberi pengaruh tidak muncul kecuali yang baharu, sehingga pemberi pengaruh ini tidak memiliki pengaruh pada yang bertahan, padahal kita telah mengandaikannya demikian. Ini kontradiksi.

[^a153]: CA: Naskah S: "bahwa pengaruhnya adalah" (*an yakūna atharuh*).

**Syubhat kedua**: pengaruh pemberi pengaruh pada akibat adakalanya terjadi ketika akibat itu ada, adakalanya ketika akibat itu tiada. Kedua kemungkinan ini batil, maka pendapat tentang adanya pemberian pengaruh batil. Kami katakan bahwa pemberi pengaruh mustahil memberi pengaruh pada akibat ketika akibat itu ada, karena mengadakan yang sudah ada dan menghasilkan yang sudah dihasilkan itu mustahil. Kami katakan pula bahwa pemberi pengaruh mustahil memberi pengaruh pada akibat ketika akibat itu tiada, karena dalam keadaan tiada akibat tetap seperti semula; dan bila akibat tetap berada dalam ketiadaan murni dan penafian mutlak sebagaimana semula, pada waktu itu tidak ada pengaruh apa pun yang muncul dari sesuatu yang dinamai pemberi pengaruh ini.

Maka tetaplah bahwa selama akibat tetap dalam ketiadaannya, pemberi pengaruh mustahil memberi pengaruh padanya; dan bila akibat telah maujud, pemberi pengaruh mustahil memberi pengaruh padanya. Karena tidak ada perantara antara keberadaan akibat dalam keadaan tiada dan keberadaannya dalam keadaan ada, dan telah tetap bahwa pendapat tentang pemberian pengaruh mustahil dalam kedua keadaan itu, maka tetaplah bahwa pendapat tentang pemberian pengaruh itu sendiri mustahil.

Jangan dikatakan, "Mengapa tidak boleh dikatakan bahwa pada saat pertama ia menjadikannya maujud pada saat kedua?" Sebab kami katakan: pada saat pertama, apakah muncul darinya suatu pengaruh atau tidak? Jika sama sekali tidak muncul pengaruh darinya, keadaannya pada saat itu sama seperti sebelumnya; dan sebagaimana sebelum saat itu benar dikatakan bahwa ia tidak memberi pengaruh pada suatu akibat, demikian pula pada saat ini pasti benar dikatakan bahwa ia tidak memberi pengaruh padanya. Adapun jika pada saat pertama muncul darinya suatu pengaruh, pada saat itu ia adalah pemberi pengaruh bagi wujud akibat itu, dan akibat itu maujud pada saat itu. Maka kembalilah keberatan tadi, yaitu keharusan mengadakan yang sudah ada, dan itu mustahil.

**Syubhat ketiga**: seandainya benar dikatakan tentang sesuatu bahwa ia membutuhkan dan memerlukan pemberi pengaruh, kebutuhan dan keperluan itu adakalanya identik dengan sesuatu yang dihukumi membutuhkan dan memerlukan itu, adakalanya berlainan dengannya. Kedua kemungkinan ini batil, maka pendapat tentang adanya kebutuhan dan keperluan batil.

Penjelasan bahwa kebutuhan mustahil identik dengan sesuatu itu sendiri, dari beberapa segi:

- (a) Zat langit dan bumi dapat dipahami oleh orang yang tidak mengetahui[^a154] bahwa keduanya membutuhkan dan memerlukan pemberi pengaruh; dan yang dihukumi sebagai diketahui tidak identik dengan yang dihukumi sebagai tidak diketahui.
- (b) Jisim adalah zat yang berdiri sendiri, yang tidak dipahami dengan membandingkannya dengan yang lain, sedangkan kebutuhan dan keperluan adalah nisbah dan esensi yang dipahami dengan membandingkannya dengan yang lain.[^a155] Ini mengharuskan keberlainan.
- (c) Bila kita berkata, "Jisim membutuhkan yang lain dalam wujudnya", ucapan ini adalah proposisi yang memberi informasi, dan fitrah bersaksi bahwa subjeknya berlainan dengan predikatnya. Bila kita berkata, "Jisim adalah jisim", tidaklah demikian. Ini menunjukkan apa yang dituju.

[^a154]: CA: Naskah S membaca kata ini secara berbeda (sebagian tidak terbaca).

[^a155]: CA: Frasa "sedangkan kebutuhan dan keperluan … dengan yang lain" ditambahkan dari naskah Z.

Adapun penjelasan bahwa kebutuhan dan keperluan mustahil berupa sesuatu yang berlainan dengan zat: hal yang berlainan itu adakalanya pengertian yang bersifat ketiadaan, adakalanya pengertian yang eksistensial, dan kedua kemungkinan ini batil. Kami katakan bahwa ia mustahil bersifat ketiadaan, karena bila kita berkata, "Sesuatu ini tidak membutuhkan dan tidak memerlukan yang lain", akal yang jernih memutuskan bahwa pengertian ini negatif. Bila penafian kebutuhan dan keperluan adalah pengertian yang bersifat ketiadaan, mustahil penetapan kebutuhan dan keperluan juga pengertian yang bersifat ketiadaan, sebab secara niscaya salah satu dari dua sisi yang saling berlawanan pasti positif dan yang lain bersifat ketiadaan.

Kami katakan pula bahwa pengertian kebutuhan dan keperluan mustahil merupakan sesuatu yang positif, dari dua segi.

Pertama, seandainya ia sesuatu yang positif, ia adakalanya wajib karena zatnya, adakalanya mungkin karena zatnya. Yang pertama batil, karena ia adalah sifat bagi maujud yang mungkin karena zatnya,[^a156] sedangkan sifat membutuhkan yang disifati, dan yang membutuhkan hal yang mungkin lebih layak lagi untuk menjadi mungkin. Yang kedua juga batil, karena kebutuhan itu, bila ia maujud yang mungkin karena zatnya,[^a157] membutuhkan[^a158] yang mengadakan, sehingga kebutuhan dari kebutuhan itu menjadi tambahan atasnya, dan terjadilah regresi tak berhingga, dan itu mustahil.

[^a156]: CA: Naskah S: "bagi zat" (*li-l-dhāt*).

[^a157]: CA: Kata "karena zatnya" ditambahkan dari naskah Z.

[^a158]: CA: Kata "membutuhkan" ditambahkan dari naskah S.

Kedua, yang disifati dengan kebutuhan dan keperluan kepada yang mengadakan itu adakalanya maujud, adakalanya tidak. Jika ia maujud, maka yang maujud itu disifati dengan kebutuhan dan keperluan kepada yang mengadakan dan pemberi pengaruh, sehingga terjadi penghasilan yang sudah dihasilkan, dan itu mustahil. Jika ia tiada, niscaya ketiadaan murni dan penafian mutlak disifati dengan sifat yang maujud, dan itu mustahil. Maka tetaplah dengan uraian kami bahwa kebutuhan dan keperluan, seandainya ada, adakalanya identik dengan zat itu, adakalanya berlainan dengannya; dan kedua kemungkinan itu batil. Maka pendapat tentang adanya kebutuhan dan keperluan batil.

**Syubhat keempat**: seandainya benar dikatakan tentang sesuatu bahwa ia membutuhkan yang mengadakan dan pemberi pengaruh, niscaya esensi itu mendahului terjadinya kebutuhan ini dalam urutan martabat, dan sekaligus terkemudian darinya, dan itu mustahil. Maka pendapat tentang adanya kebutuhan pasti mustahil.

Kami katakan bahwa hal itu menuntut kedahuluan, dari dua segi:

- (a) Kebutuhan dan keperluannya kepada pemberi pengaruh adalah salah satu sifatnya[^a159] dan salah satu hukumnya, sedangkan akal yang jernih menuntut bahwa yang disifati mendahului sifat dalam urutan martabat.
- (b) Kebutuhan dan keperluan sesuatu kepada yang lain adalah nisbah khusus antara sesuatu itu dan yang lain itu, dan terwujudnya nisbah antara dua hal bergantung pada terwujudnya kedua hal itu.[^a160] Maka kebutuhan dan keperluan pasti terkemudian dalam urutan martabat dari terwujudnya zat yang dihukumi membutuhkan dan memerlukan.

[^a159]: CA: Naskah S: "(kebutuhannya) kepadanya; sifat-sifatnya tidak membutuhkan …" (sebagian tidak terbaca).

[^a160]: CA: Naskah S: "kedua nisbah" (*al-nisbatayn*) sebagai ganti "kedua hal".

Kami katakan pula bahwa hal itu menuntut keterkemudian, karena kebutuhan kepada pelaku hanya terjadi agar pelaku itu mewujudkan, menghasilkan, dan mengadakannya. Bila demikian, terwujud dan terjadinya akibat pasti terkemudian dari pemberian pengaruh pelaku padanya, padahal pemberian pengaruh pelaku padanya terkemudian dari kebutuhan dan keperluannya kepada pelaku; dan yang terkemudian dari sesuatu yang terkemudian dari hal lain, terkemudian pula dari hal lain itu. Maka tetaplah bahwa terwujudnya hakikat yang dihukumi membutuhkan dan memerlukan pemberi pengaruh itu pasti terkemudian, dalam urutan martabat, dari kebutuhannya kepada pemberi pengaruh. Maka tetaplah dengan uraian kami bahwa seandainya benar dikatakan tentang sesuatu bahwa ia membutuhkan dan memerlukan pemberi pengaruh, niscaya hakikat itu mendahului terjadinya kebutuhan itu dalam urutan martabat dan sekaligus terkemudian darinya; dan sudah dimaklumi bahwa hal itu mustahil. Maka pendapat tentang adanya kebutuhan dan keperluan pasti batil dan mustahil.

Jangan dikatakan, "Mengapa tidak boleh dikatakan bahwa yang disifati dengan kebutuhan dan keperluan kepada pemberi pengaruh adalah esensi, dan esensi itu mendahului terjadinya kebutuhan dan keperluan ini, sedangkan yang terjadi karena pelaku dan pemberi pengaruh adalah wujud, dan wujud terkemudian dalam urutan martabat dari terjadinya kebutuhan ini?"[^a161] Sebab kami katakan: esensi, sejauh ia adalah dirinya, adakalanya membutuhkan pemberi pengaruh, adakalanya tidak. Jika ia membutuhkan pemberi pengaruh, niscaya ia mendahului kebutuhan itu dan sekaligus terkemudian darinya, sebagaimana telah kami jelaskan, sehingga kontradiksi kembali. Jika ia tidak membutuhkan pemberi pengaruh, yang membutuhkan pemberi pengaruh adalah wujud, atau keadaan esensi disifati dengan wujud; dan dengan kedua pengandaian itu, kedahuluan dan keterkemudian itu tetap terjadi, dan itu mustahil.

[^a161]: CA: Kalimat "sedangkan yang terjadi karena pelaku … kebutuhan ini" ditambahkan dari salah satu naskah (siglumnya tidak terbaca).

**Syubhat kelima**: yang membutuhkan pemberi pengaruh mustahil[^a162] berupa esensi, mustahil berupa wujud,[^a163] dan mustahil berupa keadaan esensi disifati dengan wujud. Bila ketiga kemungkinan ini mustahil, mustahil pula esensi membutuhkan pemberi pengaruh. Jadi penetapan uraian ini membutuhkan penetapan empat bagian.[^a164]

[^a162]: CA: Kata "mustahil" (*an yakūna*) ditambahkan dari naskah N.

[^a163]: CA: Frasa "mustahil berupa wujud" ditambahkan dari naskah N.

[^a164]: CA: Dalam naskah pokok tertulis "empat perkara" (*umūr*) sebagai ganti "empat bagian" (*aqsām*).

**Bagian pertama**: ucapan kami bahwa yang membutuhkan pemberi pengaruh mustahil berupa esensi. Penjelasannya dari dua segi.

Pertama, segala sesuatu yang ada karena yang lain pasti lenyap ketika diandaikan ketiadaan yang lain itu.[^a165][^t8] Seandainya esensi, sejauh ia adalah dirinya, membutuhkan pemberi pengaruh, niscaya pengandaian ketiadaan yang lain itu mengharuskan batalnya esensi sejauh ia adalah dirinya. Padahal batalnya esensi sejauh ia adalah dirinya[^a166] mustahil, sebab hitam mustahil berubah menjadi bukan hitam, dan putih mustahil berubah menjadi bukan putih.

[^a165]: CA: Kalimat "segala sesuatu yang ada karena yang lain … yang lain itu. Seandainya esensi … ketiadaan yang lain itu" ditambahkan dari naskah N.

[^t8]: CT: Dalam naskah Perpustakaan Konya Yusuf Ağa no. 692 tertulis *ʿinda farḍ ʿadam dhālika al-ghayr* (ketika diandaikan ketiadaan yang lain itu). Bacaan inilah yang benar, dan terjemahan mengikutinya.

[^a166]: CA: Frasa "padahal batalnya esensi sejauh ia adalah dirinya" ditambahkan dari naskah N dan S.

Kedua, yang membutuhkan pemberi pengaruh adalah yang mungkin, sedangkan kemungkinan adalah keadaan nisbi dan relasional antara esensi dan salah satu sifatnya. Sebab, bila kita berkata, "Anu mungkin menjadi anu", pengertian ini hanya dapat dipahami bila pengertian subjek berlainan dengan predikat. Maka mustahil dikatakan, "Hitam mungkin menjadi hitam", sedangkan tidak mustahil dikatakan, "Hitam mungkin menjadi maujud." Maka tetaplah bahwa yang menyebabkan kebutuhan kepada pemberi pengaruh adalah kemungkinan; tetap pula bahwa kemungkinan adalah keadaan nisbi; dan tetap dalam akal secara swabukti bahwa sesuatu yang satu,[^a167] sejauh ia adalah dirinya semata, tidak dikenai keadaan nisbi dan relasional apa pun. Maka tetaplah bahwa kemungkinan mustahil melekat pada hakikat sejauh ia adalah dirinya. Dan bila yang menuntut kebutuhan tidak lain adalah kemungkinan, sedangkan telah tetap bahwa esensi sejauh ia adalah dirinya mustahil dikenai kemungkinan, maka tetaplah bahwa esensi sejauh ia adalah dirinya mustahil membutuhkan pemberi pengaruh.

[^a167]: CA: Kalimat "adalah kemungkinan; tetap pula bahwa kemungkinan … sesuatu yang satu" ditambahkan dari naskah S.

**Bagian kedua**: pendapat bahwa yang membutuhkan pemberi pengaruh dan yang mengadakan adalah wujud[^a168] juga batil. Sebab wujud, sejauh ia wujud, adalah salah satu esensi dan hakikat; dan kedua dalil yang disebutkan tentang kemustahilan esensi diadakan (*majʿūl*) berlaku sepenuhnya pula tentang kemustahilan wujud diadakan.

[^a168]: CA: Frasa "mustahil berupa" dalam kalimat ini ditambahkan dari naskah N.

**Bagian ketiga**: pendapat bahwa yang membutuhkan pelaku, yang mengadakan, dan pemberi pengaruh adalah keadaan esensi disifati dengan wujud juga batil, dengan dua alasan.[^a169]

[^a169]: CA: Catatan-catatan pada bagian ini: kata "yang melebihi" (*zāʾid*) ditambahkan dari naskah Z; frasa "penjelasan bagian kedua" ditambahkan dari naskah N; naskah S membaca "jelas" (*ẓāhir*) sebagai ganti "batil"; naskah N membaca "ucapan kami" sebagai ganti "ucapannya".

Pertama, keadaan esensi disifati dengan wujud (*mawṣūfiyya*) bukanlah sesuatu yang melebihi esensi dan wujud. Bila demikian, mustahil dihukumi bahwa ia diadakan. Penjelasan bagian pertama kalimat ini: seandainya keadaan esensi disifati dengan wujud berlainan dengan keduanya, niscaya keadaan esensi disifati dengan keadaan disifati itu juga berlainan, dan terjadilah regresi tak berhingga. Penjelasan bagian kedua: karena keadaan disifati ini bukan sesuatu yang positif yang berlainan dengan (yang disifati), mustahil dikatakan bahwa ia adalah akibat dari pelaku dan yang mengadakan. Sebab bagaimana dapat dipahami bahwa sesuatu yang tidak memiliki wujud pada dirinya menjadi akibat dari pemberi pengaruh dan pelaku?

Kedua, alasan kedua bahwa ucapan "pelaku mewujudkan keadaan esensi disifati dengan wujud" itu batil: keadaan disifati ini adakalanya wujud, adakalanya bukan. Jika ia wujud, ia memiliki esensi dan wujud, sehingga pembagian yang disebutkan tentangnya, "pelaku mewujudkan esensinya atau wujudnya", kembali berlaku. Jika ia bukan wujud, mustahil dikatakan bahwa ialah yang terjadi karena pelaku dan yang mengadakan. Maka tampaklah dari uraian kami bahwa mustahil dikatakan pelaku memiliki pengaruh pada esensi, pada wujud, atau pada keadaan esensi disifati dengan wujud.

**Bagian keempat**:[^a170] menjelaskan kebatilan pendapat tentang pemberian pengaruh dan pemberi pengaruh, setelah tampak kebatilan ketiga bagian di atas. Uraiannya: bila akibat tidak membutuhkan pemberi pengaruh dalam esensinya, dalam wujudnya, dan dalam keadaan esensinya disifati dengan wujud, maka esensi yang maujud tidak membutuhkan pemberi pengaruh dan pelaku. Sebab, bila esensi, wujud, dan keadaan esensi disifati dengan wujud telah ada, berarti esensi yang maujud telah menjadi maujud tanpa pemberi pengaruh dan pelaku. Itulah yang dituju.

[^a170]: CA: Naskah N: "bagian keempat" dengan redaksi berbeda.

**Syubhat keenam**: yang dihukumi membutuhkan dan memerlukan itu adakalanya sederhana (*basīṭ*), adakalanya tersusun (*murakkab*). Kedua kemungkinan ini batil, maka pendapat tentang adanya kebutuhan batil. Pembatasannya jelas.

Kami katakan bahwa yang dihukumi membutuhkan dan memerlukan mustahil berupa sesuatu yang sederhana, karena secara niscaya mustahil menghukumi sesuatu bahwa ia mungkin menjadi dirinya sendiri. Maka mustahil dikatakan, "Hitam mungkin menjadi hitam"; yang dapat dikatakan adalah, "Hitam mungkin bertahan dan mungkin terjadi." Namun hal itu hanya benar karena pengertian hitam[^a171] berlainan dengan pengertian keadaannya sebagai yang bertahan dan yang baharu. Adapun ucapan "hitam mungkin menjadi hitam" tidak dapat dipahami. Maka tetaplah bahwa kemungkinan sama sekali tidak melekat pada hakikat-hakikat yang sederhana. Dan karena telah tetap bahwa sebab kebutuhan tidak lain adalah kemungkinan, dan tetap pula bahwa terjadinya kemungkinan pada hal-hal sederhana itu mustahil,[^a172] maka tetaplah bahwa terjadinya kebutuhan pada hal-hal sederhana itu mustahil.

[^a171]: CA: Kata "hitam" ditambahkan dari naskah S.

[^a172]: CA: Kata "karena itu" (*bi-dhālika*) di tempat ini ditambahkan dari naskah S.

Kami katakan pula bahwa yang dihukumi membutuhkan dan memerlukan mustahil berupa sesuatu yang tersusun, karena yang tersusun tersusun dari hal-hal sederhana. Bila masing-masing hal sederhana itu tidak membutuhkan pelaku dan pemberi pengaruh, sedangkan menurut tuntutan akal yang swabukti, ketika seluruh unsur tunggal ada, yang tersusun pasti ada, dan ketika semuanya atau salah satunya tidak ada, yang tersusun mustahil ada, maka mustahil pula hal-hal yang tersusun disandarkan kepada pelaku dan yang mengadakan. Jangan dikatakan, "Mengapa tidak boleh dikatakan bahwa yang membutuhkan pemberi pengaruh adalah susunan (*hayʾat al-tarkīb*) itu sendiri?" Sebab kami katakan: susunan itu adalah salah satu bagian dari esensi yang tersusun, sehingga ia pun adakalanya tunggal, adakalanya tersusun, dan pembagian pertama kembali berlaku padanya.

**Syubhat ketujuh**: seandainya sesuatu memberi pengaruh pada sesuatu yang lain, pemberian pengaruh oleh pemberi pengaruh itu pada akibatnya adakalanya identik dengan zat pemberi pengaruh, adakalanya identik dengan zat[^a173] akibat, dan adakalanya pengertian yang berlainan dengan keduanya. Semua kemungkinan ini batil, maka pendapat tentang adanya pemberian pengaruh batil.

[^a173]: CA: Frasa "adakalanya identik dengan zat" ditambahkan dari naskah S.

(a) Kami katakan bahwa pemberian pengaruh oleh pemberi pengaruh pada akibatnya mustahil identik dengan zat pemberi pengaruh atau zat akibat, karena beberapa segi.

Pertama, kita dapat memahami zat pemberi pengaruh dan zat akibat sambil ragu apakah[^a174] zat yang satu memberi pengaruh pada zat yang lain. Misalnya, kita memahami maujud yang wajib ada karena zatnya dan memahami esensi alam indrawi ini, lalu kita ragu apakah alam ini ada karena pengaruh maujud yang wajib karena zatnya itu. Sudah dimaklumi bahwa yang diketahui berlainan dengan yang tidak diketahui. Maka keadaan sebagai pemberi pengaruh (*muʾaththiriyya*) ini pasti berlainan dengan zat pemberi pengaruh dan zat akibat.

[^a174]: CA: Kata "apakah" (*hal hiya*) ditambahkan dari naskah N.

Kedua, keadaan sesuatu sebagai pemberi pengaruh pada sesuatu yang lain adalah nisbah khusus dari yang satu kepada yang lain, sedangkan nisbah antara dua hal bergantung, dalam keterwujudannya, pada terwujudnya zat masing-masing; dan yang bergantung pada dua hal berlainan dengan keduanya. Maka keadaan salah satu dari kedua zat sebagai pemberi pengaruh pada yang lain pasti berlainan dengan zat pemberi pengaruh dan zat akibat.

Ketiga, api, misalnya, memberi pengaruh dalam memanaskan, dan air dalam mendinginkan. Api dan air sama-sama merupakan pemberi pengaruh pada akibat tertentu, dan panas serta dingin sama-sama merupakan akibat dari pemberi pengaruh tertentu. Maka tetaplah bahwa kesamaan terjadi dalam pengertian keadaan sebagai pemberi pengaruh dan keadaan sebagai akibat, sedangkan kesamaan dalam kekhususan zat pemberi pengaruh dan kekhususan zat akibat tidak terjadi, sebab zat api berbeda dari zat air, dan hakikat panas berbeda dari hakikat dingin. Bila hal ini telah tetap, kita harus memastikan bahwa keberadaan api sebagai pemberi pengaruh adalah satu hal dan keberadaannya sebagai api adalah hal lain; demikian pula[^a175] keberadaan panas sebagai akibat dari suatu pemberi pengaruh adalah satu hal dan keberadaannya sebagai panas adalah hal lain.

[^a175]: CA: Kalimat "dingin. Bila hal ini telah tetap … demikian pula" ditambahkan dari naskah Z dan S.

Keempat, bila kita berkata, "Kuasa Allah adalah kuasa Allah", ucapan ini sia-sia dan tidak memberi faedah apa pun. Namun bila kita berkata, "Kuasa Allah memberi pengaruh pada wujud alam", ucapan ini memberi faedah. Seandainya pengertian keberadaan kuasa sebagai kuasa tidak berlainan dengan pengertian keberadaannya sebagai pemberi pengaruh pada wujud alam, niscaya sama sekali tidak tersisa perbedaan antara kedua ucapan itu. Maka tampaklah dengan burhan ini bahwa pemberian pengaruh adalah pengertian yang berlainan dengan zat pemberi pengaruh.

Tinggal kita tegakkan burhan bahwa pemberian pengaruh oleh pemberi pengaruh pada akibat tidak identik dengan zat akibat. Kami katakan: hal ini ditunjukkan oleh beberapa segi.

Pertama, bila kita berkata, "Kuasa Allah memberi pengaruh pada wujud alam", kita telah menyifati kuasa Allah Ta'ala dengan keadaan sebagai pemberi pengaruh ini; dan sudah diketahui secara niscaya bahwa alam bukan sifat bagi kuasa Allah. Dari gabungan kedua premis ini niscaya kita memastikan bahwa (pengaruh) kuasa Allah Ta'ala pada alam bukanlah alam itu sendiri.

Kedua, bila kita ditanya, "Mengapa alam ada?", jawaban kita adalah, "Kuasa Allah Ta'ala menuntut diadakannya alam dalam wujud." Jadi kita menjadikan sebab adanya alam[^a176] bahwa Allah Ta'ala mengadakannya. Seandainya Allah mengadakan alam itu identik dengan alam itu sendiri, niscaya ucapan kita "alam hanya ada karena Allah Ta'ala mengadakannya" berarti "alam hanya ada karena dirinya sendiri"; dan seandainya alam ada karena dirinya sendiri, mustahil dikatakan bahwa ia ada karena Allah Ta'ala mengadakannya. Maka tetaplah bahwa seandainya kita menafsirkan pemberian pengaruh oleh pemberi pengaruh pada akibat sebagai wujud akibat itu sendiri, niscaya pemberi pengaruh dan akibat tertafikan; dan sesuatu yang penetapannya berujung pada penafiannya adalah batil. Maka pendapat bahwa pemberian pengaruh oleh pemberi pengaruh pada akibat adalah akibat itu sendiri[^a177] pasti batil.

[^a176]: CA: Frasa "Jadi kita menjadikan sebab adanya alam" ditambahkan dari naskah S.

[^a177]: CA: Kata "itu sendiri" (*nafs*) ditambahkan dari naskah S.

Ketiga, kita adakalanya menafsirkan Allah Ta'ala mengadakan alam sebagai alam itu sendiri, adakalanya bukan sebagai alam itu sendiri melainkan sebagai munculnya alam dari kuasa Allah Ta'ala. Yang pertama batil, sebab dengan pengandaian bahwa alam ada karena dirinya sendiri, atau ada karena diadakan oleh maujud lain selain Allah, tidaklah benar ucapan bahwa alam terjadi karena Allah Ta'ala mengadakannya. Maka tetaplah bahwa Allah Ta'ala mengadakan alam[^a178] tidak dapat ditafsirkan sebagai alam itu sendiri; ia hanya dapat ditafsirkan sebagai terjadinya alam dari kuasa Allah Ta'ala. Ketika itu kami katakan: tampaklah bahwa keberadaan alam dari kuasa Allah Ta'ala berlainan dengan zat alam dan zat kuasa,[^a179] sehingga ia pasti merupakan pengertian ketiga. Maka tetaplah bahwa pemberian pengaruh oleh pemberi pengaruh pada akibat tidak boleh berupa zat pemberi pengaruh itu sendiri dan tidak boleh berupa zat akibat itu sendiri; ia pasti sesuatu yang berlainan dengan keduanya.

[^a178]: CA: Kata "alam" (*li-l-ʿālam*) ditambahkan dari naskah N.

[^a179]: CA: Kalimat "Ta'ala. Ketika itu … dan zat kuasa" ditambahkan dari naskah Z (sebagian tidak terbaca).

Keempat,[^a180] untuk menjelaskan bahwa pemberian pengaruh sesuatu pada sesuatu mustahil identik dengan zat pemberi pengaruh dan zat akibat: keberadaan pemberi pengaruh sebagai pemberi pengaruh pada akibat, dan keberadaan akibat sebagai akibat dari pemberi pengaruh, termasuk kategori relasi (*maqūlat al-muḍāf*), sedangkan zat pemberi pengaruh dan zat akibat tidak demikian. Sebab, bila kita berkata, "Allah Ta'ala menciptakan alam", zat pemberi pengaruh adalah Zat Yang Wajib Ada, dan zat akibat adalah zat alam.

[^a180]: CA: Dalam naskah pokok tertulis "kelima". Edisi Turki juga menyebutnya "kelima".

Maka tetaplah dengan keempat burhan ini[^a181] bahwa seandainya sesuatu memberi pengaruh pada sesuatu, keadaan yang satu sebagai pemberi pengaruh pada yang lain bukanlah zat pemberi pengaruh itu sendiri dan bukan pula zat akibat itu sendiri, melainkan pengertian ketiga yang berlainan dengan keduanya.

[^a181]: CA: Dalam naskah pokok tertulis "kelima burhan ini".

(b) Adapun bagian kedua, yaitu bahwa pengertian keadaan sebagai pemberi pengaruh adalah pengertian ketiga yang berlainan dengan zat pemberi pengaruh dan zat akibat, kami katakan: ini pun rusak, sebab pengertian yang berlainan itu adakalanya negatif, adakalanya positif, dan kedua kemungkinan ini batil.

Kami katakan bahwa ia mustahil negatif, karena dua segi. Pertama, ucapan kita "sesuatu anu memberi pengaruh pada anu" adalah kebalikan dari ucapan kita "ia tidak memberi pengaruh pada anu". Ucapan "ia tidak memberi pengaruh pada anu" adalah pengertian negatif, sebab dari ucapan kita tentang sesuatu tertentu bahwa ia tidak memberi pengaruh pada anu, tidak berbuat sesuatu, dan tidak mengadakan suatu akibat, kita tidak memahami apa pun selain penafian murni dan ketiadaan mutlak. Bila telah tetap bahwa pengertian ucapan "ia tidak memberi pengaruh pada anu" adalah ketiadaan murni, pengertian ucapan "ia memberi pengaruh pada anu" pasti sesuatu yang tetap dan maujud, sebab secara niscaya, bila salah satu dari dua hal yang saling berlawanan negatif, yang lain pasti positif. Kedua, bila kita katakan bahwa keadaan sebagai pemberi pengaruh adalah pengertian yang bersifat ketiadaan, maknanya ialah bahwa ia tidak memiliki wujud; dan ucapan ini tidak bermakna apa-apa selain menafikan keadaan sebagai pemberi pengaruh dan akibat itu sendiri.

Adapun kemungkinan kedua, yaitu bahwa keadaan sebagai pemberi pengaruh adalah pengertian positif yang berlainan dengan zat pemberi pengaruh dan zat akibat,[^a182] kami katakan: maujud ini adakalanya maujud di alam nyata (*fī al-aʿyān*), adakalanya dikatakan bahwa ia[^a183] tidak memiliki wujud di alam nyata, melainkan termasuk pertimbangan-pertimbangan pikiran (*iʿtibārāt dhihniyya*) yang tidak memiliki wujud di alam nyata. Kemungkinan kedua batil, sebab bila akal menghukumi sesuatu sebagai pemberi pengaruh pada sesuatu yang lain, hukum pikiran[^a184] ini adakalanya sesuai dengan alam nyata, adakalanya tidak. Jika hukum pikiran ini sesuai dengan apa yang ada di alam nyata, maka sesuatu itu di alam nyata memang akibat, pemberi pengaruh, pelaku, dan yang dikenai perbuatan; dan ketika itu batallah ucapan mereka bahwa pengertian-pengertian ini adalah pertimbangan-pertimbangan dalam pikiran yang tidak memiliki wujud di alam nyata. Jika tidak sesuai, hukum pikiran ini adalah kedustaan dan kebodohan, dan ketika itu sesuatu itu pada kenyataannya bukan akibat, bukan pemberi pengaruh, bukan pelaku, dan bukan yang dikenai perbuatan; dan itu mengharuskan penafian pemberian pengaruh dan pemberi pengaruh.

[^a182]: CA: Frasa "yang berlainan dengan zat pemberi pengaruh dan zat akibat" ditambahkan dari naskah N.

[^a183]: CA: Naskah N membaca kata ini secara berbeda (sebagian tidak terbaca).

[^a184]: CA: Kata "pikiran" (*al-dhihnī*) ditambahkan dari salah satu naskah.

Adapun kemungkinan pertama, yaitu bahwa keadaan pemberi pengaruh sebagai pemberi pengaruh dan keadaan akibat sebagai akibat adalah dua pengertian yang berlainan dengan zat dan merupakan hal-hal yang tetap di alam nyata, kami katakan: kemungkinan ini pun batil, sebab hal eksistensial itu adakalanya substansi yang berdiri sendiri, adakalanya sifat yang melekat pada zat pemberi pengaruh dan zat akibat. Yang pertama batil karena beberapa segi:

- (a) keadaan sebagai pemberi pengaruh adalah sifat bagi zat pemberi pengaruh, sedangkan substansi yang berdiri sendiri tidak menjadi sifat bagi zat pemberi pengaruh;
- (b) pemberi pengaruh dan akibat termasuk kategori relasi, sedangkan substansi yang berdiri sendiri tidak demikian;
- (c) substansi yang berdiri sendiri ini, jika tidak memiliki pengaruh pada yang dikenai perbuatan itu, ia asing darinya;[^a185] dan jika memiliki pengaruh padanya, pembagian yang disebutkan tentang keadaan substansi itu sebagai pemberi pengaruh pada akibat itu kembali berlaku.

[^a185]: CA: Naskah Z: "secara tertentu" (*bi-l-taʿyīn*) sebagai ganti "darinya".

Yang kedua, yaitu dikatakan bahwa keadaan sebagai pemberi pengaruh dan keadaan sebagai akibat adalah dua sifat yang melekat pada zat pemberi pengaruh dan zat akibat, juga mustahil. Sebab sifat yang melekat pada yang lain membutuhkan yang lain itu, dan yang membutuhkan yang lain[^a186] adalah mungkin karena zatnya, dan yang mungkin karena zatnya pasti memiliki pemberi pengaruh. Maka keadaan sebagai pemberi pengaruh ini pun membutuhkan pemberi pengaruh yang memberi pengaruh padanya, sehingga pemberian pengaruh oleh pemberi pengaruh itu pada wujud keadaan sebagai pemberi pengaruh ini adalah pengertian tambahan atasnya, dan terjadilah regresi tak berhingga. Regresi ini batil karena dua segi. Pertama, burhan-burhan yang menunjukkan bahwa pendapat tentang regresi tak berhingga itu batil. Kedua, dengan pengandaian bahwa pendapat tentang regresi tak berhingga itu benar, hal yang mustahil tetap terjadi di sini. Sebab yang dapat dipahami dari regresi tak berhingga adalah bahwa sesuatu meniscayakan sesuatu yang lain, yang kedua meniscayakan yang ketiga,[^a187] yang ketiga meniscayakan yang keempat, dan demikian seterusnya tanpa akhir. Namun[^a188] pengertian ini hanya tetap bila ada hal-hal yang saling bersambung, yang masing-masing bersambung dengan yang lain tanpa akhir. Padahal, bila kita katakan bahwa keadaan sesuatu sebagai pemberi pengaruh pada sesuatu adalah sifat tambahan atas keduanya, kita tidak dapat menunjuk dua hal yang salah satunya bersambung dengan yang lain, kecuali keadaan yang satu meniscayakan yang lain merupakan hal ketiga yang menengahi keduanya. Ini menuntut bahwa sama sekali tidak ada sesuatu yang bersambung dengan sesuatu yang lain. Bila ini batal, batal pula[^a189] pendapat tentang regresi tak berhingga. Maka tetaplah bahwa pendapat tentang adanya regresi tak berhingga dalam kasus ini berujung pada ketiadaannya, sehingga pendapat tentang adanya regresi itu pasti batil. Maka tampaklah dari seluruh uraian kami bahwa seandainya sesuatu memberi pengaruh pada sesuatu, pemberian pengaruh oleh pemberi pengaruh pada akibat adakalanya identik dengan zat pemberi pengaruh atau zat akibat, adakalanya pengertian ketiga yang berlainan dengan keduanya; dan telah tetap bahwa kedua bagian itu batil dan rusak. Maka pendapat tentang adanya pemberi pengaruh dan pemberian pengaruh pasti batil.

[^a186]: CA: Frasa "dan yang membutuhkan yang lain" ditambahkan dari naskah S.

[^a187]: CA: Frasa "yang ketiga, yang ketiga meniscayakan" ditambahkan dari naskah N.

[^a188]: CA: Naskah S: "karena ini" (*li-anna hādhā*) sebagai ganti "namun" (*illā anna*).

[^a189]: CA: Frasa "batal pula" ditambahkan dari salah satu naskah.

Jika seseorang berkata, "Pembagian yang kalian sebutkan ini juga berlaku pada hal-hal yang kebenaran dan keberadaannya kita ketahui secara niscaya, sehingga pembagian ini pasti rusak", penjelasannya dari dua segi.

Pertama, dapat dikatakan:[^a190] seandainya rumah ini dan dinding ini ada pada saat ini, keberadaannya pada saat ini adakalanya rumah dan dinding itu sendiri, adakalanya saat itu sendiri, dan adakalanya pengertian ketiga yang berlainan. Ketiga kemungkinan ini batil, maka pendapat tentang adanya sesuatu pada saat ini[^a191] batil. Kami katakan bahwa keberadaan rumah dan dinding ini pada saat ini mustahil identik dengan wujud rumah dan dinding ini, karena pada saat kedua[^a192] keberadaannya pada saat pertama tidak bertahan, padahal zatnya bertahan. Keberadaannya pada saat ini mustahil pula identik dengan saat ini, karena wujud saat ini, di luar pikiran maupun di dalam pikiran, tidak mungkin[^a193] terlepas dari keberadaan sesuatu ini pada saat ini;[^t9] selain itu, keberadaan sesuatu ini pada saat ini termasuk kategori relasi, sedangkan saat ini dan sesuatu ini tidak termasuk kategori relasi. Kami katakan pula bahwa keberadaan sesuatu ini pada saat ini mustahil berupa pengertian tambahan, karena tambahan itu pun ada pada saat itu, sehingga keberadaan pengertian yang berlainan itu pada saat itu adalah hal yang berlainan dengannya, dan terjadilah regresi tak berhingga, dan itu mustahil.

[^a190]: CA: Frasa "dapat dikatakan" ditambahkan dari salah satu naskah.

[^a191]: CA: Kalimat "pada saat ini batil. Kami katakan … mustahil identik dengan" ditambahkan dari naskah N.

[^a192]: CA: Kata "kedua" ditambahkan dari naskah N.

[^a193]: CA: Kata "tidak" ditambahkan dari salah satu naskah.

[^t9]: CT: Sebagian bagian yang memuat kebatilan kemungkinan kedua ini gugur dan kacau dalam teks cetak. Bagian ini diterjemahkan dari naskah Perpustakaan Konya Yusuf Ağa no. 692.

Kedua, untuk menjelaskan bahwa pembagian yang kalian sebutkan[^a194] itu batil, kita tunjuk sebuah jisim yang berada di suatu tempat, lalu kita katakan: ia tidak berada di tempat itu. Sebab, seandainya ia berada di sana, keberadaannya di sana adakalanya identik dengan zatnya, adakalanya tambahan atas zatnya. Yang pertama batil, karena bila ia keluar dari tempat itu zatnya tetap bertahan sedangkan keberadaannya di tempat itu tidak bertahan. Yang kedua juga batil,[^a195] karena tambahan itu adalah sifat bagi jisim itu, dan sifat berada pada yang disifati, sehingga keberadaan sifat itu pada zat yang disifati pasti tambahan atasnya, dan itu mengharuskan regresi tak berhingga,[^a196] dan itu mustahil. Maka tetaplah dengan kedua segi ini bahwa pembagian yang kalian sebutkan berlaku pada hal-hal yang kebenarannya kita ketahui dengan akal secara swabukti, sehingga pembagian yang kalian sebutkan pasti batil.

[^a194]: CA: Frasa "pembagian" ditambahkan dari naskah S.

[^a195]: CA: Kalimat "karena bila ia keluar … juga batil" ditambahkan dari naskah N.

[^a196]: CA: Naskah S: "dan niscaya terjadi regresi tak berhingga".

Jawabannya: pembagian yang kami sebutkan adalah pembagian yang berkisar antara penafian dan penetapan, dan dalil-dalil yang menunjukkan kebatilan masing-masing bagian itu adalah segi-segi yang pasti dan meyakinkan. Bila hal ini telah tetap, kami katakan: pembagian yang kami sebutkan ini adalah burhan yang sahih dari segi bentuk dan dari segi materinya. Jika burhan yang demikian keadaannya masih mungkin rusak, kalian tidak dapat memastikan[^a197] kebenaran dalil dan bukti apa pun, sebab tujuan tertinggi dalam dalil adalah bahwa ia sahih[^a198] dari segi bentuk dan materi. Bila kalian membolehkan, bersamaan dengan kedua syarat ini,[^a199] dalil itu rusak, tidak tersisa lagi kepercayaan pada dalil apa pun, sandaran kepada seluruh dalil gugur sepenuhnya, dan gugur pula sandaran kepada dalil yang kalian kemukakan untuk menetapkan Yang Wajib Ada. Inilah akhir pembahasan tentang uraian syubhat ini, dan sesungguhnya ia adalah syubhat yang paling kuat.

[^a197]: CA: Naskah S: "keseimbangan" (*al-iʿtidāl*) sebagai ganti "memastikan" (*al-qaṭʿ*).

[^a198]: CA: Frasa "bahwa ia" ditambahkan dari salah satu naskah.

[^a199]: CA: Naskah S: "bila kalian telah mewujudkan, bersamaan dengan adanya kedua syarat ini".

**Syubhat kedelapan** dalam menafikan pemberian pengaruh dan pemberi pengaruh: seandainya kemungkinan adalah sebab kebutuhan akibat kepada pemberi pengaruh, niscaya yang tiada, dalam keadaan tiadanya, membutuhkan pemberi pengaruh. Konsekuen ini mustahil, maka anteseden itu pun mustahil. Penjelasan proposisi kondisional ini: yang menyebabkan kebutuhan kepada pemberi pengaruh adalah kemungkinan khusus (*al-imkān al-khāṣṣ*), bukan kemungkinan umum. Namun[^a200] keterkaitan kemungkinan khusus dengan sisi wujud sama dengan keterkaitannya[^a201] dengan sisi ketiadaan, setara tanpa perbedaan sama sekali. Bila nisbah kemungkinan ini kepada kedua sisi setara, maka jika ia adalah sebab kebutuhan pada sisi wujud, ia pasti menjadi sebab kebutuhan pada sisi ketiadaan pula; jika tidak, niscaya salah satu dari kedua sisi yang setara menjadi lebih unggul daripada yang lain tanpa penentu keunggulan, dan itu mustahil; dan dengan pengandaian bahwa hal itu benar, hal itu merusak ucapan kalian bahwa salah satu sisi yang mungkin tidak menjadi lebih unggul daripada yang lain kecuali karena penentu keunggulan. Maka tetaplah bahwa seandainya kemungkinan adalah sebab kebutuhan, niscaya yang tiada, dalam keadaan tiadanya, membutuhkan penentu keunggulan dan pemberi pengaruh.

[^a200]: CA: Naskah S: "demikian pula" (*ka-dhālika*) sebagai ganti "namun" (*lākinna*).

[^a201]: CA: Frasa "dengan sisi wujud sama dengan keterkaitannya" ditambahkan dari naskah S.

Kami katakan bahwa hal ini mustahil, karena ketiadaan yang terus berlangsung menunjuk kepada penafian murni dan negasi mutlak, dan keberadaannya sebagai yang bertahan menunjuk bahwa negasi murni itu terus berlangsung. Masing-masing dari kedua pengertian ini menafikan terjadinya pemberian pengaruh.[^a202] Bahwa keberadaannya sebagai negasi murni menafikan keberadaannya sebagai akibat, karena pemberian pengaruh menuntut terjadinya suatu keadaan dan munculnya sesuatu, sedangkan penafian murni dan negasi mutlak tidak demikian. Adapun bahwa keberadaannya sebagai yang bertahan mencegahnya menjadi akibat dari pemberi pengaruh, karena telah kami jelaskan sebelumnya bahwa pendapat bahwa yang bertahan, dalam keadaan bertahannya, menjadi akibat dari pemberi pengaruh dan perbuatan dari pelaku itu mustahil.[^a203] Maka tetaplah bahwa seandainya kemungkinan menyebabkan kebutuhan kepada pemberi pengaruh, niscaya yang tiada, dalam keadaan bertahannya (dalam ketiadaan), membutuhkan pemberi pengaruh; dan telah tetap bahwa hal ini mustahil. Maka kemungkinan pasti bukan sebab kebutuhan kepada pemberi pengaruh.

[^a202]: CA: Naskah S: "keberlainan" (*al-taghāyur*) sebagai ganti "pemberian pengaruh" (*al-taʾthīr*).

[^a203]: CA: Kalimat "bahwa pendapat bahwa yang bertahan … itu mustahil. Maka tetaplah" ditambahkan dari salah satu naskah.

**Syubhat kesembilan**: seandainya yang mungkin membutuhkan penentu keunggulan, niscaya manusia tidak bebas memilih (*mukhtār*) dalam perbuatan-perbuatannya. Konsekuen ini batil, maka anteseden itu pun batil. Penjelasan proposisi kondisional ini: manusia, ketika ia mampu melakukan perbuatan,[^a204] adakalanya mampu pula meninggalkannya, adakalanya tidak. Jika dalam keadaan berbuat ia tidak mampu meninggalkan, demikian pula ia tidak mampu berbuat;[^a205] dan ketika itu ia sama sekali tidak berkuasa untuk berbuat dan meninggalkan dalam keadaan apa pun, sehingga ia pasti sama sekali bukan pelaku yang bebas memilih. Adapun jika ia mampu meninggalkan, maka keunggulan berbuat atas meninggalkan adakalanya bergantung pada penentu keunggulan, adakalanya tidak. Jika bergantung pada penentu keunggulan, penentu keunggulan itu adakalanya berasal darinya, adakalanya dari selainnya. Jika berasal darinya, pembagian pertama kembali berlaku padanya. Jika berasal dari selainnya, maka ketika penentu keunggulan itu datang dari yang lain, perbuatan itu adakalanya wajib, mungkin, atau mustahil. Jika wajib, ia sama sekali tidak berkuasa untuk berbuat dan meninggalkan, karena sebelum datangnya penentu keunggulan itu, munculnya perbuatan darinya mustahil, dan sesudah datangnya, munculnya perbuatan darinya wajib; dan dengan pengandaian ini, hamba tidak berkuasa dalam keadaan apa pun. Adapun anggapan bahwa ketika penentu keunggulan itu datang, munculnya perbuatan darinya menjadi mungkin dan bukan wajib, hal itu batil karena enam segi yang pasti dan meyakinkan, yang akan kami sebutkan dalam masalah qada dan qadar. Maka tetaplah dengan uraian kami bahwa seandainya keunggulan salah satu sisi yang mungkin atas yang lain bergantung pada bergabungnya penentu keunggulan kepadanya, mustahil makhluk hidup bebas memilih dalam perbuatannya.

[^a204]: CA: Frasa "melakukan perbuatan, adakalanya mampu" ditambahkan dari salah satu naskah (sebagian tidak terbaca).

[^a205]: CA: Naskah S: "demikian pula dalam keadaan meninggalkan ia tidak mampu berbuat".

Kami katakan bahwa adanya pelaku yang bebas memilih pasti diakui, karena kita mengetahui secara swabukti perbedaan antara seorang hamba yang bergerak dengan pilihannya, sesekali ke kanan dan sesekali ke kiri, dan orang yang gemetar yang bergerak karena terpaksa. Demikian pula, orang yang melemparkan batu ke wajah seseorang mengetahui perbedaan antara gerak batu dan gerak tangan pelempar itu, sebab orang-orang berakal dengan akal mereka yang swabukti mengetahui bahwa batu itu tidak boleh dipuji atau dicela karena gerak itu, sedangkan pelemparnya layak dipuji atau dicela karena gerak itu. Seandainya hamba tidak bebas memilih dalam perbuatannya, perbedaan ini tidak akan ada. Maka tetaplah bahwa seandainya keunggulan salah satu sisi yang mungkin atas yang lain bergantung pada penentu keunggulan, niscaya hamba tidak bebas memilih dalam perbuatannya. Dan karena telah tetap bahwa ia bebas memilih dalam perbuatannya, yang mungkin pasti tidak membutuhkan penentu keunggulan.
