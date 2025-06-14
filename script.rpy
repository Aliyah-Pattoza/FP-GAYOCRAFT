# =============================================================================
# CHARACTER DEFINITIONS
# =============================================================================

define a = Character("Ara", color="#c8ffc8")
define k = Character("Kakek Ibrahim", color="#ffc8c8")
define m = Character("Pak Mahmud", color="#c8c8ff")
define s = Character("Bu Sari", color="#ffc8ff")
define d = Character("Kepala Desa", color="#ffff88")
define n = Character("Narrator", color="#ffffff")

# =============================================================================
# IMAGES
# =============================================================================

image bg mountain_sunrise = "images/mountain_sunrise.png"
image bg coffee_plantation_old = "images/coffee_plantation_old.png"
image bg jakarta_office = "images/jakarta_office.jpg"
image bg ara_apart = "images/ara_apart.png"
image bg village_entrance = "images/village_entrance.png"
image bg coffee_plantation_abandoned = "images/coffee_plantation_abandoned.png"
image bg village_center = "images/village_center.png"
image bg ara_room_night = "images/ara_room_night.png"
image bg coffee_plantation_clean = "images/coffee_plantation_clean.png"
image bg coffee_plantation_good = "images/coffee_plantation_good.png"
image bg village_center_evening = "images/village_center_evening.png"
image bg coffee_plantation_prepared = "images/coffee_plantation_prepared.png"
image bg nursery = "images/nursery.png"
image bg coffee_plantation_rain = "images/coffee_plantation_rain.png"
image bg coffee_plantation_growing = "images/coffee_plantation_growing.png"
image bg coffee_plantation_month1 = "images/coffee_plantation_month1.png"
image bg coffee_plantation_problem = "images/coffee_plantation_problem.png"
image bg coffee_plantation_old = "images/coffee_plantation_old.png"

# =============================================================================
# VARIABLES
# =============================================================================

default player_name = "Ara"
default money = 50000
default energy = 100
default knowledge = 0
default reputation = 0
default day = 0
default current_season = "dry"
default coffee_plants = 0
default harvested_beans = 0

# =============================================================================
# INTRO STATE - CHILDHOOD FLASHBACK
# =============================================================================

label start:
    scene bg mountain_sunrise
    with fade
    # play music "audio/gayo_traditional.ogg" fadeout 1.0 fadein 2.0
    
    n "Dataran tinggi Aceh Tengah, 15 tahun yang lalu..."
    
    scene bg coffee_plantation_old
    with dissolve
    
    show kakek_young at left
    show ara_child at right
    with easeinleft
    
    k "Ara, cucu kakek... lihat ke sekeliling kita."
    k "Semua yang terlihat mata ini adalah warisan nenek moyang kita."
    
    show ara_child happy
    a "Wah, Kek! Pohon kopi ini tinggi sekali!"
    
    k "Hehe, iya nak. Ini bukan pohon kopi biasa."
    k "Ini adalah kopi Gayo Arabica, yang terkenal di seluruh dunia."
    k "Rasanya unik, aromanya khas, dan cara menanamnya turun temurun."
    
    show ara_child curious
    a "Kenapa rasanya bisa unik, Kek?"
    
    k "Karena tanah di sini istimewa, nak."
    k "Dataran tinggi dengan ketinggian 1.200 meter di atas permukaan laut."
    k "Udaranya sejuk, tanahnya subur vulkanis, dan curah hujannya pas."
    
    show ara_child excited
    a "Wah! Aku juga mau jadi petani kopi seperti Kakek!"
    
    k "Hahaha... mungkin suatu hari nanti, nak."
    k "Tapi ingat, menjadi petani kopi itu tidak mudah."
    k "Butuh kesabaran, ketekunan, dan ilmu yang mendalam."
    
    k "Ingat baik-baik pelajaran hari ini, Ara."
    k "Siapa tahu suatu hari kamu harus melanjutkan warisan ini..."
    
    scene black
    with fade
    
    n "Tapi takdir berkata lain..."
    n "Setelah lulus SMA, Ara merantau ke Jakarta untuk kuliah dan bekerja..."
    n "15 tahun berlalu..."

# =============================================================================
# INTRO STATE - CITY LIFE & RETURN DECISION  
# =============================================================================

label city_life:
    scene bg jakarta_office
    with fade
    #play music "audio/city_ambience.ogg"
    
    show ara_adult tired at center
    with easeinbottom
    
    n "Jakarta, 2025. Ara kini sudah 28 tahun, bekerja sebagai marketing executive di sebuah perusahaan multinasional."
    
    a "Huh... hari ini meeting lagi, deadline lagi..."
    a "Kapan ya aku bisa istirahat dengan tenang?"
    
    scene bg ara_apart
    
    # Phone rings
    play sound "audio/phone_ring.ogg"
    
    show ara_adult surprised
    a "Halo?"
    
    s "Ara? Ini Bu Sari, tetangga kakek di kampung."
    s "Kabar kurang baik, nak..."
    
    show ara_adult worried
    a "Ada apa, Bu? Kakek kenapa?"
    
    s "Kakek Ibrahim... sudah dipanggil Yang Kuasa minggu lalu."
    s "Kami sudah coba hubungi kamu berkali-kali..."
    
    show ara_adult shocked
    a "APAA?! Kakek... kenapa bisa..."
    
    s "Maaf ya nak, sinyal di sini susah. Prosesi sudah selesai."
    s "Tapi ada yang perlu kamu ketahui..."
    s "Kebun kopi kakek... kondisinya memprihatinkan."
    
    show ara_adult sad
    a "Maksud Ibu bagaimana?"
    
    s "Sudah 5 tahun kakek sakit-sakitan, jadi kebunnya terbengkalai."
    s "Sekarang rumput liar sudah tinggi, pohon kopinya banyak yang mati."
    s "Kalau tidak ada yang urus, takutnya tanah warisan itu dijual orang."
    
    # Decision point
    menu:
        "Aku harus pulang dan menyelamatkan warisan kakek":
            $ reputation += 10
            $ knowledge += 5
            jump return_to_village
            
        "Tapi pekerjaanku di Jakarta...":
            a "Bu Sari, aku masih ada kewajiban di Jakarta..."
            s "Iya nak, Ibu paham. Tapi pikirkan baik-baik."
            s "Ini warisan nenek moyang kita. Kalau hilang, tidak akan kembali lagi."
            jump return_decision_2

label return_decision_2:
    show ara_adult thinking
    a "..."
    a "Aku ingat dulu kakek pernah bilang..."
    a "'Siapa tahu suatu hari kamu harus melanjutkan warisan ini...'"
    
    show ara_adult determined
    a "Bu Sari, aku akan pulang!"
    a "Beri aku waktu dua minggu untuk urus resign dan urusan di Jakarta."
    
    s "Alhamdulillah... kakek pasti senang di alam sana."
    s "Kami tunggu kedatanganmu, nak."

# =============================================================================
# INTRO STATE - ARRIVAL AT VILLAGE
# =============================================================================

label return_to_village:
    scene bg village_entrance
    with fade
    play music "audio/village_ambience.ogg"
    
    show ara_adult at center
    with easeinright
    
    n "Dua minggu kemudian, Ara tiba di Takengon, Aceh Tengah."
    n "Udara sejuk dataran tinggi menyambut kepulangannya setelah 15 tahun merantau."
    
    a "Wah... udaranya masih sejuk seperti dulu."
    a "Tapi kok rasanya asing ya? Banyak yang berubah..."
    
    scene bg kakek_house_exterior
    with dissolve
    
    show ara_adult sad
    a "Ini dia... rumah kakek."
    a "Ya Ampun, kondisinya..."
    
    # Meet Bu Sari
    show sari at left
    show ara_adult at right
    with easeinleft
    
    s "Ara! Alhamdulillah kamu sudah sampai."
    s "Selamat datang kembali ke kampung halaman."
    
    show ara_adult grateful
    a "Terima kasih Bu Sari sudah menghubungi aku."
    a "Maaf ya, aku baru bisa datang sekarang."
    
    s "Tidak apa-apa nak. Yang penting kamu sudah di sini."
    s "Ayo, Ibu antar lihat kondisi kebun dan rumah kakek."
    
    scene bg coffee_plantation_abandoned
    with dissolve
    
    show ara_adult shocked
    a "Ya ampun... ini benar-benar parah."
    a "Rumput liar di mana-mana, pohon kopi banyak yang mati..."
    
    show sari concerned
    s "Iya nak. Sudah 5 tahun tidak terurus dengan baik."
    s "Kakek sudah tua, tidak kuat lagi kerja berat."
    s "Kami tetangga sudah bantu semampu kami, tapi..."
    
    show ara_adult determined
    a "Bu Sari, aku akan menghidupkan kembali kebun ini!"
    a "Aku tidak akan membiarkan warisan kakek hilang begitu saja!"
    
    s "Tapi nak, kamu kan sudah lama di kota..."
    s "Bertani kopi itu tidak mudah, apalagi kamu mulai dari nol..."
    
    a "Aku tahu Bu. Tapi aku harus coba."
    a "Dulu kakek pernah bilang, 'Butuh kesabaran, ketekunan, dan ilmu yang mendalam.'"
    a "Nah, sekarang saatnya aku belajar ilmu itu!"

# =============================================================================
# TUTORIAL STATE - MEET THE MENTOR
# =============================================================================

label meet_mentor:
    $ day = 1
    scene bg village_center
    with fade
    
    show sari at left
    show ara_adult at center
    
    s "Ara, Ibu mau kenalkan kamu dengan Pak Mahmud."
    s "Beliau petani kopi terbaik di desa ini, dan sahabat baik kakek kamu."
    
    show mahmud at right
    with easeinright
    
    m "Halo. Jadi ini Ara, cucu Ibrahim yang sering diceritakan?"
    
    show ara_adult respectful
    a "Halo, Pak. Saya Ara."
    a "Mohon bimbingannya, Pak Mahmud."
    
    m "Hmm... Sari sudah cerita, kamu mau menghidupkan kebun kakek?"
    m "Itu bagus. Tapi apa kamu yakin?"
    m "Bertani kopi bukan main-main, nak."
    
    menu:
        "Saya yakin, Pak. Saya akan belajar dengan sungguh-sungguh.":
            $ knowledge += 10
            $ reputation += 5
            m "Bagus! Sikap seperti itu yang dibutuhkan."
            jump mentor_accepts
            
        "Sejujurnya saya masih ragu, tapi saya harus coba.":
            $ knowledge += 5
            m "Kejujuran itu baik. Setidaknya kamu realistis."
            jump mentor_accepts

label mentor_accepts:
    m "Baiklah, Bapak akan bantu kamu."
    m "Tapi ingat, Bapak hanya bisa bimbing. Yang kerja tetap kamu."
    m "Kamu siap?"
    
    show ara_adult determined
    a "Siap, Pak!"
    
    m "Oke. Mulai besok, kamu ikut Bapak ke kebun."
    m "Kita mulai dari dasar: mengenal tanah, bibit, dan peralatan."
    m "Jam 6 pagi, kamu sudah harus di rumah Bapak."
    
    a "Baik, Pak! Terima kasih!"
    
    # Tutorial preparation
    scene bg ara_room_night
    with fade
    play music "audio/night_ambience.ogg"
    
    show ara_adult thinking
    n "Malam itu, Ara menyiapkan diri untuk hari pertamanya belajar bertani."
    
    a "Oke Ara, besok hari pertama."
    a "Kamu pasti bisa! Demi kakek, demi warisan keluarga!"

# =============================================================================
# TUTORIAL STATE - FIRST DAY LEARNING
# =============================================================================

label first_day_learning:
    $ day = 2
    $ energy = 100
    
    scene bg mahmud_house
    with fade
    play music "audio/morning_birds.ogg"
    
    show mahmud at center
    with easeinleft
    
    m "Pagi, Ara! Tepat waktu. Bagus!"
    
    show ara_adult energetic at right
    with easeinright
    
    a "Selamat pagi, Pak Mahmud!"
    a "Saya sudah siap belajar!"
    
    m "Haha, semangat sekali. Ayo ikut Bapak."
    m "Hari ini kita mulai dengan yang paling dasar: mengenal tanah."
    
    scene bg coffee_plantation_good
    with dissolve
    
    m "Lihat kebun Bapak ini. Sudah 20 tahun Bapak rawat."
    m "Bandingkan dengan kebun kakek kamu yang terbengkalai."
    m "Apa yang kamu lihat?"
    
    show ara_adult observing
    a "Kebun Bapak lebih rapi, pohon kopinya sehat..."
    a "Tanah di sini juga terlihat lebih subur."
    
    m "Benar! Sekarang coba ambil segenggam tanah ini."

    m "Tanah untuk kopi Gayo harus:"
    m "pH antara 6.0-6.5, drainase baik, kaya humus."
    m "Ketinggian ideal 1.200-1.700 meter di atas permukaan laut."
    
    $ knowledge += 15
    
    show ara_adult excited
    a "Wah, ternyata banyak sekali yang harus diperhatikan!"
    
    m "Ini baru permulaan, nak."
    m "Sekarang kita lihat berbagai varietas kopi Gayo."
    
    # Varietas introduction
    m "Ada beberapa varietas utama:"
    m "Gayo 1: Tahan penyakit, produktivitas tinggi."
    m "Gayo 2: Kualitas cup terbaik, aroma kuat."
    m "Bourbon: Tradisional, rasa kompleks."
    m "Catimor: Tahan hama, cocok untuk pemula."
    
    menu:
        "Untuk pemula seperti saya, sebaiknya pilih varietas apa, Pak?":
            m "Bagus, kamu bertanya yang tepat!"
            m "Untuk pemula, Bapak sarankan Catimor dan Gayo 1."
            m "Mudah dirawat dan tahan penyakit."
            $ knowledge += 10
            
        "Saya mau langsung coba yang kualitas terbaik!":
            m "Semangat yang bagus, tapi..."
            m "Gayo 2 membutuhkan keahlian tinggi."
            m "Sebaiknya kamu mulai dari yang mudah dulu."
            $ knowledge += 5
    
    # Tools introduction
    m "Sekarang kita lihat peralatan yang dibutuhkan."
    
    m "Hari ini cukup sampai di sini."
    m "Besok kita praktik langsung di kebun kakek kamu."
    m "Istirahat yang cukup, karena besok akan lebih berat."
    
    $ energy -= 30
    
    show ara_adult tired but happy
    a "Baik, Pak! Terima kasih untuk pelajaran hari ini."
    a "Banyak sekali yang saya pelajari!"
    
    # Evening reflection
    scene bg ara_room_night
    with fade
    
    show ara_adult thinking
    n "Malam itu, Ara merefleksikan pelajaran hari pertamanya."
    
    a "Wah, ternyata bertani kopi tidak sesederhana yang kukira."
    a "Tapi ini menarik! Aku mulai paham kenapa kakek sangat mencintai pekerjaannya."

# =============================================================================
# FARMING CYCLE STATE - LAND PREPARATION
# =============================================================================

label land_preparation:
    $ day = 3
    $ energy = 100
    
    scene bg coffee_plantation_abandoned
    with fade
    play music "audio/working_music.ogg"
    
    show mahmud at left
    show ara_adult at right
    
    m "Nah, ini dia kebun kakek kamu."
    m "Kondisinya memang parah, tapi masih bisa diselamatkan."
    m "Apa rencana kamu?"
    
    show ara_adult determined
    a "Saya ingin membersihkan semua rumput liar ini dulu, Pak."
    a "Terus lihat pohon kopi mana yang masih bisa diselamatkan."
    
    m "Bagus! Itu langkah yang tepat."
    m "Tapi hati-hati, jangan sembarangan memotong."
    m "Beberapa yang kelihatan mati mungkin masih bisa hidup kembali."
    
    # After 2 hours of work
    $ energy -= 40
    $ money -= 5000  # Cost of tools
    
    scene bg coffee_plantation_clean
    show ara_adult tired
    a "Hah... hah... capek juga ya, Pak."
    a "Baru sebagian kecil, tapi sudah mulai keliatan bedanya."
    
    m "Haha, kamu sudah bagus untuk hari pertama."
    m "Ingat, bertani itu butuh fisik yang kuat."
    m "Makanya petani bangun subuh dan tidur lebih awal."
    
    # Soil testing sequence
    m "Sekarang kita tes tanah di beberapa titik."
    m "Ini penting untuk tahu kondisi pH dan nutrisi."
    
    m "Hmm... pH-nya 5.5. Agak asam."
    m "Perlu diberi kapur dolomit untuk menetralkan."
    m "Kandungan nitrogen juga kurang."
    
    a "Berarti perlu pupuk ya, Pak?"
    
    m "Iya, tapi tidak sembarangan."
    m "Pupuk organik lebih baik untuk jangka panjang."
    m "Kompos, pupuk kandang, atau pupuk dari kulit kopi."
    
    # Resource management decision
    menu:
        "Beli pupuk kimia (cepat tapi mahal - 50.000)":
            if money >= 50000:
                $ money -= 50000
                $ knowledge += 5
                m "Boleh juga, tapi jangan terlalu sering."
                m "Pupuk kimia cepat, tapi bisa merusak tanah kalau berlebihan."
            else:
                m "Uang kamu tidak cukup, nak."
                m "Bapak sarankan kamu membuat pupuk organik saja terlebih dulu."
                a "Baik pak. Kalau begitu saya akan mencoba menggunakan pupuk organik terlebih dahulu."
                jump organic_fertilizer
                
        "Buat pupuk organik sendiri (murah tapi butuh waktu - 10.000)":
            label organic_fertilizer:
            $ money -= 10000
            $ knowledge += 15
            $ reputation += 5
            m "Pilihan yang bijak!"
            m "Pupuk organik lebih sehat untuk tanah dan lingkungan."
            m "Plus, kopi organik harganya lebih tinggi di pasar."

    # Irrigation planning
    m "Yang terakhir hari ini, kita rencanakan sistem pengairan."
    m "Kopi butuh air yang cukup, tapi tidak boleh tergenang."
    
    m "Besok kita mulai menanam bibit."
    m "Hari ini sudah cukup. Pulang dan istirahat."
    
    $ knowledge += 20
    $ day += 1
    
    # Evening village interaction
    scene bg village_center_evening
    with fade
    
    show villager1 at left
    show ara_adult at center
    show villager2 at right
    
    "Warga 1" "Ara, dengar-dengar kamu mau hidupin kebun kakek?"
    
    a "Iya, Pak. Saya sedang belajar dengan Pak Mahmud."
    
    "Warga 2" "Wah, bagus tuh! Desa kita butuh petani muda seperti kamu."
    "Warga 2" "Kebanyakan anak muda sekarang pada ke kota."
    
    "Warga 1" "Betul! Kalau ada yang perlu dibantu, bilang aja ya."
    "Warga 1" "Kita kan tetangga, harus saling bantu."
    
    $ reputation += 10
    
    show ara_adult grateful
    a "Terima kasih, Bapak-bapak!"
    a "Saya sangat terbantu dengan dukungan kalian."

# =============================================================================
# FARMING CYCLE STATE - PLANTING
# =============================================================================

label planting_phase:
    $ day = 5
    $ energy = 100
    
    scene bg nursery
    with fade
    
    show mahmud at left
    show ara_adult at center
    
    m "Hari ini kita mulai dengan bibit."
    m "Bibit yang baik adalah kunci sukses bertani kopi."
 
    m "Ciri-ciri bibit yang baik:"
    m "Daun hijau segar, batang kokoh, akar putih bersih."
    m "Umur bibit 4-6 bulan, tinggi 15-20 cm."
    
    $ knowledge += 15
    
    # Transplanting sequence
    scene bg coffee_plantation_prepared
    with dissolve
    
    m "Sekarang kita pindahkan bibit ke kebun."
    m "Jarak tanam yang ideal adalah 2.5 x 2.5 meter."
    m "Kenapa harus segitu?"
    
    menu:
        "Supaya pohon dapat sinar matahari yang cukup?":
            $ knowledge += 10
            m "Benar! Dan juga sirkulasi udara yang baik."
            
        "Supaya mudah dipanen nanti?":
            $ knowledge += 5
            m "Itu juga benar, tapi ada alasan yang lebih penting."
            m "Jarak yang tepat membuat pohon dapat nutrisi optimal."
            
        "Saya tidak tahu, Pak...":
            m "Tidak apa-apa. Ini memang harus dipelajari."
            m "Jarak tanam mempengaruhi pertumbuhan dan produksi."
    
    $ coffee_plants += 50
    $ energy -= 50
    $ money -= 25000  # Cost of seedlings
    
    # Weather concern
    play sound "audio/thunder.ogg"
    
    show ara_adult worried
    a "Pak, kok langit mendung ya? Jangan-jangan hujan?"
    
    m "Iya, sepertinya memang akan hujan."
    m "Tapi ini bagus! Bibit yang baru ditanam butuh air."
    m "Hujan alami lebih baik daripada siram manual."
    
    # Rain sequence
    scene bg coffee_plantation_rain
    with fade
    play sound "audio/rain.ogg" loop
    
    n "Hujan turun dengan deras..."
    
    show ara_adult happy
    a "Alhamdulillah... semoga bibit-bibit kita tumbuh dengan baik."
    
    # One week later - growth check
    $ day += 7
    $ energy = 100
    
    scene bg coffee_plantation_growing
    with fade
    stop sound
    play music "audio/morning_birds.ogg"
    
    show mahmud at left
    show ara_adult excited at right
    
    a "Pak Mahmud! Lihat! Bibit-bibit kita mulai tumbuh!"
    a "Ada tunas-tunas baru yang keluar!"
    
    m "Haha, kamu lebih excited daripada anakku dulu."
    m "Iya, mereka tumbuh dengan baik."
    m "Tapi ini baru permulaan. Pohon kopi baru berbuah setelah 3-4 tahun."
    
    show ara_adult surprised
    a "Lama sekali ya, Pak?"
    
    m "Makanya bertani kopi butuh kesabaran."
    m "Tapi tenang, sementara menunggu, kita bisa tanam tanaman sela."
    m "Jagung, kacang tanah, atau sayuran."
    m "Biar ada penghasilan sambil menunggu kopi berbuah."
    
    # Intercropping decision
    menu:
        "Mau tanam jagung (penghasilan 3 bulan, untung sedang)":
            $ money += 30000
            $ knowledge += 10
            
        "Mau tanam sayuran (penghasilan 1 bulan, untung kecil tapi cepat)":
            $ money += 15000  
            $ knowledge += 5
            
        "Fokus ke kopi saja (tidak ada penghasilan tambahan)":
            $ knowledge += 20
            m "Pilihan yang fokus. Tapi pastikan kamu punya cukup uang untuk hidup."

# =============================================================================
# FARMING CYCLE STATE - MAINTENANCE & GROWTH
# =============================================================================

label maintenance_phase:
    $ day = 30
    $ energy = 100
    
    scene bg coffee_plantation_month1
    with fade
    
    show mahmud at left
    show ara_adult at center
    
    m "Sudah sebulan sejak kita tanam."
    m "Sekarang masuk fase perawatan intensif."
    m "Ini periode paling krusial untuk menentukan keberhasilan."
    
    # Daily routine introduction
    m "Dari sekarang, kamu harus punya rutinitas harian:"
    m "Pagi: cek kondisi tanaman, siram kalau perlu."
    m "Siang: bersihkan gulma, cek hama penyakit."
    m "Sore: pupuk, pangkas kalau perlu."
    
    $ energy -= 20
    
    # Disease detection event
    $ day += 15
    
    scene bg coffee_plantation_problem
    with fade
    
    show ara_adult worried
    a "Pak Mahmud! Ada yang aneh dengan beberapa pohon kopi saya!"
    a "Daunnya menguning dan ada bercak-bercak coklat!"
    
    show mahmud concerned at right
    with easeinright
    
    m "Hmm... ini terlihat seperti penyakit karat daun."
    m "Penyakit jamur yang sering menyerang kopi."
    m "Kalau tidak ditangani cepat, bisa menyebar ke seluruh kebun."

    m "Sekarang kita harus bertindak cepat."
    
    # Treatment options
    menu:
        "Gunakan fungisida kimia (cepat sembuh, 75.000 rupiah)":
            if money >= 75000:
                $ money -= 75000
                $ knowledge += 5
                call chemical_treatment
            else:
                m "Uang tidak cukup. Kita coba cara alami saja."
                jump organic_treatment
                
        "Pakai obat tradisional dari bahan alami (murah tapi lambat, 15.000 rupiah)":
            label organic_treatment:
            $ money -= 15000
            $ knowledge += 15
            $ reputation += 10
            call organic_treatment_sequence
            
        "Pangkas daun yang sakit saja (gratis tapi berisiko)":
            $ knowledge += 10
            call pruning_treatment

label chemical_treatment:
    m "Fungisida memang cepat, tapi hati-hati penggunaannya."
    m "Kalau berlebihan bisa merusak lingkungan."
    m "Dan kopi kita tidak bisa dapat sertifikat organik."
    
    $ day += 3
    n "Tiga hari kemudian, penyakit sudah mulai terkendali."
    jump maintenance_continue

label organic_treatment_sequence:
    m "Bagus! Cara organik memang lebih lambat tapi lebih aman."
    m "Kita pakai campuran bawang putih, cabai, dan sabun."
    m "Plus mikroorganisme lokal dari bambu."
    
    $ day += 7
    n "Seminggu kemudian, penyakit mulai reda dengan perlahan."
    m "Pohon yang diobati organik biasanya lebih tahan penyakit."
    jump maintenance_continue

label pruning_treatment:
    m "Pemangkasan memang bisa membantu."
    m "Tapi kalau tidak tepat, malah bisa melemahkan pohon."
    
    $ day += 5
    # Random chance of success/failure
    if renpy.random.randint(1, 10) > 4:
        n "Beruntung! Pemangkasan berhasil menghentikan penyebaran."
        $ knowledge += 15
    else:
        n "Sayangnya, penyakit malah menyebar lebih luas..."
        $ coffee_plants -= 10
        $ money -= 20000  # Loss from dead plants
        m "Sayang sekali. Ini risiko dari cara manual."
        m "Lain kali sebaiknya pakai cara yang lebih pasti."

label maintenance_continue:
    # Fertilizing sequence
    $ day += 30
    scene bg coffee_plantation_month2
    with fade
    
    show mahmud at left
    show ara_adult at center
    
    m "Sudah 2 bulan sejak penanaman."
    m "Sekarang saatnya pemupukan yang lebih intensif."
    m "Pohon kopi mulai membentuk sistem akar yang kuat."
    
    # Fertilizer education
    m "Ada 3 jenis nutrisi utama yang dibutuhkan kopi:"
    m "Nitrogen (N) untuk pertumbuhan daun dan batang."
    m "Fosfor (P) untuk perkembangan akar dan bunga."
    m "Kalium (K) untuk kekuatan pohon dan kualitas buah."
    
    $ money -= 40000
    $ knowledge += 20
    $ energy -= 30
    
    # Pruning education
    m "Sekarang kita belajar teknik pemangkasan yang benar."
    m "Pemangkasan penting untuk:"
    m "Membentuk pohon yang produktif."
    m "Memudahkan panen nanti."
    m "Menjaga kesehatan pohon."
    
    # Pest management event
    $ day += 20
    
    scene bg coffee_plantation_pest
    with fade
    play sound "audio/insects.ogg"
    
    show ara_adult alarmed
    a "Pak Mahmud! Ada serangan hama!"
    a "Banyak sekali serangga kecil di daun-daun kopi!"
    
    show mahmud examining at right
    m "Hmm... ini kutu daun hijau."
    m "Hama yang cukup umum menyerang kopi muda."
    m "Untung kamu cepat mendeteksi."
    
    m "Untuk kutu daun, ada beberapa cara pengendalian:"
    m "Biologis: lepas predator alami seperti kepik."
    m "Mekanis: semprot air atau bersihkan manual."
    m "Organik: spray sabun atau minyak neem."
    
    menu:
        "Pakai predator alami (ramah lingkungan, 30.000)":
            $ money -= 30000
            $ knowledge += 20
            $ reputation += 15
            call biological_control
            
        "Semprot air saja (gratis tapi butuh tenaga)":
            $ energy -= 40
            $ knowledge += 10
            call mechanical_control
            
        "Buat spray organik sendiri (murah, 10.000)":
            $ money -= 10000
            $ knowledge += 15
            call organic_spray

label biological_control:
    m "Pilihan yang sangat baik!"
    m "Kepik dan predator alami akan jaga keseimbangan ekosistem."
    m "Ini investasi jangka panjang untuk kebun yang sehat."
    
    $ day += 10
    n "Sepuluh hari kemudian, populasi kutu daun berkurang drastis."
    n "Kepik-kepik bekerja dengan efektif."
    jump maintenance_success

label mechanical_control:
    m "Cara yang paling aman untuk lingkungan."
    m "Tapi memang butuh tenaga ekstra dan harus rajin."
    
    $ day += 7
    n "Dengan penyemprotan rutin, kutu daun terkendali."
    n "Meski capek, tapi hasilnya memuaskan."
    jump maintenance_success

label organic_spray:
    m "Spray organik juga efektif."
    m "Kita pakai sabun cuci piring yang ramah lingkungan."
    m "Campur dengan minyak goreng sedikit."
    
    $ day += 5
    n "Lima hari kemudian, kutu daun mulai berkurang."
    n "Cara yang ekonomis dan cukup efektif."

label maintenance_success:
    # Growth milestone
    $ day += 60
    $ coffee_plants += 10  # Some plants recovered/grew well
    
    scene bg coffee_plantation_healthy
    with fade
    play music "audio/success_theme.ogg"
    
    show ara_adult proud at center
    
    n "4 bulan sejak penanaman..."
    n "Kebun kopi Ara sudah mulai menampakkan hasil yang menggembirakan."
    
    a "Alhamdulillah... Pohon-pohon kopi sudah tumbuh tinggi dan sehat!"
    a "Daun-daunnya hijau segar, batangnya kokoh."
    
    show mahmud proud at right
    with easeinright
    
    m "Wahh... Kamu sudah berhasil, Ara!"
    m "Kebun ini sudah jauh berbeda dari 4 bulan lalu."
    m "Kakek Ibrahim pasti bangga melihat cucunya."
    
    $ reputation += 25
    $ knowledge += 30
    
    # Community recognition
    show villager1 at left
    with easeinleft
    
    "Warga 1" "Ara! Dengar-dengar kebun kamu sudah bagus?"
    "Warga 1" "Boleh kami lihat-lihat?"
    
    show ara_adult humble
    a "Silakan, Pak. Masih belajar kok."
    
    "Warga 1" "Wah, ini mah sudah bagus banget!"
    "Warga 1" "Anak muda jaman sekarang jarang yang mau bertani."
    "Warga 1" "Kamu jadi inspirasi buat yang lain!"
    
    $ reputation += 15

# =============================================================================
# FARMING CYCLE STATE - FIRST FLOWERING & FRUIT SET
# =============================================================================

label first_flowering:
    $ day += 365  # 1 year after planting
    
    scene bg coffee_plantation_flowering
    with fade
    play music "audio/gentle_wind.ogg"
    
    show ara_adult amazed at center
    
    n "Setahun kemudian..."
    n "Keajaiban pertama terjadi di kebun Ara."
    
    a "Wahhh... bunga-bunga putih kecil bermunculan!"
    a "Wanginya harum sekali... seperti melati!"
    
    show mahmud excited at right
    with easeinright
    
    m "Alhamdulillah! Pohon kopi kamu mulai berbunga!"
    m "Ini pertanda bahwa akar dan batangnya sudah kuat."
    m "Sebentar lagi akan ada buah kopi pertama!"
    
    # Flowering education
    m "Bunga kopi itu unik, Ara."
    m "Mereka bisa menyerbuki sendiri, tidak butuh bantuan serangga."
    m "Tapi tetap lebih baik kalau ada lebah untuk membantu."
    
    $ knowledge += 25
    
    # Bee keeping suggestion
    m "Ngomong-ngomong soal lebah..."
    m "Mau tidak kamu coba ternak lebah?"
    m "Selain bantu penyerbukan, bisa dapat madu juga."
    
    menu:
        "Tertarik! Bagaimana caranya? (investasi 100.000)":
            if money >= 100000:
                $ money -= 100000
                $ knowledge += 30
                $ reputation += 20
                call beekeeping_start
            else:
                m "Uang belum cukup. Nanti saja kalau sudah ada modal."
                jump flowering_continue
                
        "Fokus ke kopi dulu saja":
            $ knowledge += 10
            m "Oke, tidak masalah. Satu-satu dulu."
            jump flowering_continue

label beekeeping_start:
    m "Bagus! Lebah Trigona cocok untuk daerah sini."
    m "Mereka tidak menyengat dan mudah dirawat."
    m "Plus madunya punya kualitas premium."
    
    n "Beberapa minggu kemudian..."
    n "Suara lebah mulai ramai di kebun Ara."
    n "Bunga-bunga kopi lebih sering dikunjungi lebah."
    
    $ money += 20000  # Monthly honey income
    
    show ara_adult happy
    a "Wah, ternyata lebah benar-benar membantu ya!"
    a "Dan madunya enak sekali!"

label flowering_continue:
    # Fruit development
    $ day += 60
    
    scene bg coffee_plantation_young_fruits
    with fade
    
    show ara_adult excited
    a "Pak Mahmud! Lihat! Bunga-bunga sudah berubah jadi buah kecil!"
    a "Hijau kecil-kecil, lucu sekali!"
    
    show mahmud at right
    m "Iya, ini yang disebut 'pin head stage'."
    m "Buah kopi masih kecil seperti kepala peniti."
    m "Dari sini butuh 6-8 bulan lagi sampai matang."
    
    # Fruit development education
    m "Selama periode ini, pohon butuh perhatian ekstra:"
    m "Air yang cukup tapi tidak berlebihan."
    m "Nutrisi yang seimbang."  
    m "Perlindungan dari hama burung dan tupai."
    
    $ money -= 25000  # Investment in bird nets
    $ knowledge += 20
    
    # Weather challenge
    $ day += 90
    
    scene bg coffee_plantation_dry_season
    with fade
    play sound "audio/strong_wind.ogg"
    
    show ara_adult worried
    a "Pak, kemarau tahun ini lebih panjang dari biasanya."
    a "Daun-daun mulai layu, buah-buah kecil banyak yang gugur."
    
    show mahmud concerned at right
    m "Iya, ini tantangan serius."
    m "Kalau tidak ditangani, bisa gagal panen total."
    m "Kita perlu sistem irigasi darurat."
    
    # Drought management decision
    menu:
        "Pasang sistem irigasi tetes (mahal tapi efisien - 200.000)":
            if money >= 200000:
                $ money -= 200000
                $ knowledge += 25
                call drip_irrigation_system
            else:
                m "Modal tidak cukup. Coba cara lain."
                jump manual_watering
                
        "Siram manual setiap hari (murah tapi capek)":
            label manual_watering:
            $ energy -= 60
            $ knowledge += 15
            call manual_watering_sequence
            
        "Pasrah dan berharap hujan turun":
            $ knowledge += 5
            call prayer_for_rain

label drip_irrigation_system:
    m "Keputusan yang bijak untuk investasi jangka panjang!"
    m "Sistem tetes menghemat air 60 persen dibanding siram manual."
    m "Dan airnya tepat ke akar, tidak ada yang terbuang."
    
    $ day += 14
    n "Dua minggu kemudian, sistem irigasi mulai beroperasi."
    n "Pohon-pohon kopi terlihat segar kembali."
    n "Buah-buah yang sempat stress mulai pulih."
    
    $ coffee_plants += 5  # Some plants recovered
    jump first_harvest_prep

label manual_watering_sequence:
    m "Tidak apa-apa. Yang penting konsisten."
    m "Siram pagi dan sore, jangan siang hari."
    m "Air yang panas bisa merusak akar."
    
    $ day += 30
    n "Sebulan dengan penyiraman manual yang rajin..."
    n "Meski capek, tapi hasilnya lumayan baik."
    n "Sebagian besar tanaman berhasil bertahan."
    
    jump first_harvest_prep

label prayer_for_rain:
    m "Doa memang penting, tapi ikhtiar juga harus maksimal."
    m "Yuk kita coba usaha yang bisa kita lakukan."
    
    # Random weather event
    if renpy.random.randint(1, 10) > 7:
        n "Wahh! Hujan turun setelah seminggu!"
        n "Sepertinya doa dan ikhtiar dikabulkan!"
        $ reputation += 10
        jump first_harvest_prep
    else:
        n "Sayangnya cuaca tetap kering..."
        n "Banyak buah muda yang gugur karena stress air."
        $ coffee_plants -= 15
        $ money -= 30000  # Loss from failed fruits
        m "Ini pelajaran penting tentang manajemen risiko."

# =============================================================================
# FARMING CYCLE STATE - FIRST HARVEST
# =============================================================================

label first_harvest_prep:
    $ day += 120  # 4 months later
    
    scene bg coffee_plantation_ripe_fruits  
    with fade
    play music "audio/harvest_celebration.ogg"
    
    show ara_adult amazed at center
    
    n "Akhirnya... setelah 2 tahun menunggu..."
    n "Buah kopi pertama di kebun Ara mulai matang!"
    
    a "Wahh! Buah-buahnya sudah merah seperti ceri!"
    a "Cantik sekali! Ini hasil kerja keras selama 2 tahun!"
    
    show mahmud proud at right
    with easeinright
    
    m "Alhamdulillah, Ara! Kamu berhasil!"
    m "Panen pertama adalah momen yang sangat spesial."
    m "Kakek Ibrahim pasti tersenyum di alam sana."
    
    # Harvest timing education
    m "Sekarang kita harus hati-hati dengan timing panen."
    m "Buah yang bagus itu merah matang sempurna."
    m "Kalau masih hijau, rasanya asam."
    m "Kalau terlalu matang, bisa fermentasi di pohon."
    
    $ knowledge += 30
    
    # Selective picking education
    m "Petik kopi itu harus selektif."
    m "Hanya ambil yang merah matang."
    m "Sistem 'petik merah' ini yang bikin kopi Gayo berkualitas."

    $ harvested_beans += 50
    $ energy -= 40
    $ money += 75000  # Income from first harvest
    
    show ara_adult emotional
    a "Pak... saya hampir menangis..."
    a "Ini buah kopi pertama yang saya panen sendiri!"
    a "Rasanya seperti anak sendiri yang sudah besar!"
    
    m "Haha! Semua petani merasakan hal yang sama."
    m "Makanya petani kopi itu sangat menyayangi tanamannya."
    m "Sekarang kita proses hasil panen ini."

# =============================================================================
# FARMING CYCLE STATE - POST HARVEST PROCESSING
# =============================================================================

label post_harvest_processing:
    scene bg processing_facility
    with fade
    
    show mahmud at left
    show ara_adult at center
    
    m "Sekarang masuk tahap yang menentukan kualitas akhir."
    m "Post harvest processing atau pengolahan pasca panen."
    m "Di sini kita tentukan profil rasa kopi kita."
    
    # Processing method education
    m "Ada 3 metode utama pengolahan kopi:"
    m "Natural/kering: buah dikeringkan langsung."
    m "Washed/basah: kulit buah dikupas, difermentasi, dicuci."
    m "Honey/semi-washed: kombinasi keduanya."
    
    menu:
        "Coba metode natural (mudah, rasa fruity)":
            $ knowledge += 15
            call natural_processing
            
        "Coba metode washed (lebih sulit, rasa clean)":
            $ knowledge += 25
            call washed_processing
            
        "Coba metode honey (paling sulit, rasa kompleks)":
            $ knowledge += 35
            call honey_processing

label natural_processing:
    m "Natural processing adalah metode tertua."
    m "Buah kopi dikeringkan langsung tanpa dikupas."
    m "Hasilnya rasa lebih fruity dan sweet."
    
    $ day += 21  # 3 weeks drying
    $ money += 10000  # Premium for natural process
    jump processing_complete

label washed_processing:
    m "Washed processing butuh lebih banyak air."
    m "Tapi hasilnya lebih clean dan bright."
    m "Cocok untuk kopi specialty grade."
    
    $ day += 10
    $ money += 25000  # Higher premium for washed
    jump processing_complete

label honey_processing:
    m "Honey processing adalah yang paling rumit."
    m "Buah dikupas tapi lendir tidak dicuci bersih."
    m "Butuh skill tinggi untuk tidak over-fermentasi."
    
    # Success depends on knowledge level
    if knowledge >= 100:
        n "Berhasil! Honey processing berjalan sempurna."
        $ money += 40000  # Highest premium
    else:
        n "Agak over-fermentasi... masih perlu belajar."
        $ money += 15000
        m "Tidak apa-apa, honey processing memang sulit."
        m "Dengan latihan pasti akan lebih baik."
    
    $ day += 14

label processing_complete:
    # Drying completion
    scene bg drying_beds
    with fade
    
    show ara_adult satisfied
    a "Akhirnya selesai juga proses pengeringan!"
    a "Warna biji kopinya bagus, aroma sudah keluar!"
    
    show mahmud examining at right
    m "Bagus! Kadar airnya sudah pas, sekitar 12 persen."
    m "Sekarang kita sortir berdasarkan ukuran dan kualitas."
    
    $ knowledge += 20
    
    # Quality grading
    m "Berdasarkan sortir tadi, kopi kamu bisa dikategorikan:"
    m "Grade 1: 60 persen - kualitas premium"
    m "Grade 2: 30 persen - kualitas standar"  
    m "Grade 3: 10 persen - kualitas rendah"
    
    $ money += 50000  # Additional income from quality grading
    
    show ara_adult proud
    a "Alhamdulillah! Mayoritas grade 1!"
    a "Kerja keras selama ini tidak sia-sia!"

# =============================================================================
# BUSINESS MANAGEMENT STATE - FIRST MARKETING
# =============================================================================

label first_marketing:
    scene bg village_market
    with fade
    play music "audio/market_ambience.ogg"
    
    show ara_adult nervous at center
    
    n "Saatnya Ara menjual hasil panen pertamanya..."
    n "Ini akan menentukan keberlanjutan usaha kebunnya."
    
    a "Deg-degan juga ya... mau jual kopi pertama kali."
    a "Semoga harganya bagus..."
    
    # Meet coffee buyer
    show buyer at right
    with easeinright
    
    "Pembeli" "Permisi, saya dengar ada petani baru yang punya kopi bagus?"
    
    show ara_adult respectful
    a "Iya Pak, saya Ara. Ini kopi Gayo hasil kebun sendiri."
    
    "Pembeli" "Boleh saya cicipi dulu?"
    
    "Pembeli" "Hmm... aromanya bagus, rasanya balance."
    "Pembeli" "Untuk petani pemula, ini sudah bagus sekali."
    "Pembeli" "Saya bisa beli dengan harga 45.000 per kilo."
    
    # Price negotiation
    menu:
        "Terima harga tersebut (aman, langsung dapat uang)":
            $ money += 135000  # 3kg x 45.000
            $ knowledge += 10
            a "Baik Pak, saya setuju."
            jump first_sale_complete
            
        "Coba tawar lebih tinggi (berisiko tapi bisa untung lebih)":
            call price_negotiation_game
            jump negotiation_result
            
        "Tanya harga di tempat lain dulu":
            $ knowledge += 15
            jump find_other_buyer

label price_negotiation_game:
    a "Pak, boleh tidak harganya 50.000 per kilo?"
    a "Kopi saya grade 1, kualitas premium."
    
    "Pembeli" "Hmm... untuk pemula memang berani ya."
    "Pembeli" "Tapi kualitasnya memang bagus..."
    
    # Negotiation success based on reputation and knowledge
    if reputation >= 30 and knowledge >= 80:
        "Pembeli" "Oke, 48.000 per kilo. Final."
        $ money += 144000  # 3kg x 48.000
        $ reputation += 5
        a "Terima kasih Pak!"
        jump first_sale_complete
    else:
        "Pembeli" "Maaf, 45.000 sudah pas untuk pemula."
        "Pembeli" "Kalau tidak mau, silakan cari pembeli lain."
        jump tough_decision

label tough_decision:
    menu:
        "Terima tawaran 45.000 (pragmatis)":
            $ money += 135000
            a "Baik Pak, saya terima."
            jump first_sale_complete
            
        "Cari pembeli lain (berisiko)":
            $ knowledge += 10
            jump find_other_buyer

label find_other_buyer:
    n "Ara memutuskan mencari pembeli lain..."
    
    # Random outcome
    if renpy.random.randint(1, 10) > 6:
        n "Beruntung! Ara menemukan pembeli yang mau bayar 47.000."
        $ money += 141000
        $ reputation += 10
        a "Alhamdulillah, keputusan yang tepat!"
    else:
        n "Sayangnya, tidak ada pembeli lain yang mau bayar lebih tinggi."
        n "Ara akhirnya kembali ke pembeli pertama..."
        "Pembeli" "Harga sekarang 42.000 saja. Take it or leave it."
        $ money += 126000
        a "Huft... lesson learned."

label first_sale_complete:
    show ara_adult happy
    a "Alhamdulillah! Penjualan pertama berhasil!"
    a "Dengan uang ini, bisa buat modal panen berikutnya!"
    
    # Community celebration
    scene bg community_hall
    with fade
    play music "audio/celebration.ogg"
    
    show villager1 at left
    show ara_adult at center  
    show villager2 at right
    
    "Warga 1" "Ara! Dengar-dengar panen pertama kamu berhasil?"
    
    show ara_adult humble
    a "Iya Pak, Alhamdulillah. Masih belajar terus kok."
    
    "Warga 2" "Kamu jadi inspirasi buat anak-anak muda lain!"
    "Warga 2" "Kalau ada yang mau belajar, boleh ke kamu kan?"
    
    $ reputation += 20
    
    a "Tentu saja! Ilmu harus dibagi-bagi."
    a "Saya juga masih banyak belajar dari Pak Mahmud dan tetangga-tetangga."

# =============================================================================
# CULTURAL EVENTS STATE - HARVEST FESTIVAL
# =============================================================================

label harvest_festival:
    $ day += 30
    
    scene bg festival_preparation
    with fade
    play music "audio/traditional_gayo.ogg"
    
    show kepala_desa at left
    show ara_adult at center
    
    d "Ara, sebagai petani muda yang berhasil panen pertama,"
    d "kami ingin mengundang kamu jadi tamu kehormatan di Festival Panen."
    
    show ara_adult surprised
    a "Wah, saya tersanjung Pak Kepala Desa!"
    a "Tapi saya masih pemula..."
    
    d "Justru itu! Kamu bukti bahwa anak muda bisa sukses bertani."
    d "Sharing pengalaman kamu bisa motivasi yang lain."
    
    # Festival preparation
    scene bg festival_day
    with fade
    play music "audio/festival_music.ogg"
    
    n "Hari Festival Panen Kopi Gayo..."
    n "Seluruh desa berkumpul merayakan hasil panen tahun ini."
    
    show ara_adult nervous at center
    a "Grogi juga ya... harus ngomong di depan banyak orang."
    
    show mahmud encouraging at right
    m "Tenang saja. Cerita apa adanya."
    m "Tentang perjuangan kamu dari nol sampai panen pertama."
    
    # Ara's speech
    show ara_adult confident
    a "Assalamu'alaikum, Bapak-Ibu sekalian..."
    a "Dua tahun lalu, saya cuma anak kota yang tidak tahu apa-apa soal bertani."
    a "Tapi berkat bimbingan Pak Mahmud dan dukungan masyarakat..."
    a "Alhamdulillah saya berhasil panen pertama kopi Gayo!"
    
    # Crowd reaction
    play sound "audio/applause.ogg"
    
    show crowd_happy at left
    "Crowd" "Alhamdulillah! Hebat!"
    
    a "Yang ingin saya sampaikan:"
    a "Bertani kopi itu tidak mudah, tapi sangat memuaskan."
    a "Kita menjaga warisan nenek moyang dan alam sekitar."
    a "Untuk teman-teman muda, jangan ragu mencoba!"
    
    $ reputation += 30
    $ knowledge += 20
    
    # Traditional coffee ceremony
    scene bg coffee_ceremony
    with fade
    
    show elder at left
    show ara_adult at center
    
    "Tetua Adat" "Sekarang kita lakukan upacara adat kopi Gayo."
    "Tetua Adat" "Ini tradisi turun temurun untuk menghormati hasil panen."
    
    "Tetua Adat" "Ara, kamu sudah resmi menjadi bagian petani kopi Gayo."
    "Tetua Adat" "Semoga berkah dan sukses selalu menyertai."
    
    $ reputation += 25
    
    # Festival end
    show ara_adult grateful
    a "Terima kasih semuanya!"
    a "Ini momen yang tidak akan pernah saya lupakan!"
    a "Saya berjanji akan terus belajar dan berkontribusi untuk desa!"

# =============================================================================
# BUSINESS EXPANSION STATE - SCALING UP
# =============================================================================

label business_expansion:
    $ day += 90  # 3 months later
    
    scene bg coffee_plantation_expanded
    with fade
    
    show ara_adult planning at center
    
    n "Tiga bulan setelah panen pertama..."
    n "Ara mulai merencanakan ekspansi bisnis kopi."
    
    a "Dengan keuntungan dari panen pertama..."
    a "Aku bisa mulai kembangkan usaha ini lebih besar."
    
    show mahmud advisor at right
    with easeinright
    
    m "Bagus! Sekarang kamu sudah siap ke level berikutnya."
    m "Ada beberapa pilihan untuk ekspansi:"
    m "Perluas kebun, buat koperasi, atau olah sendiri sampai siap minum."
    
    # Expansion options
    menu:
        "Perluas kebun (investasi besar, produksi naik)":
            call land_expansion
            
        "Gabung koperasi (risk sharing, akses pasar lebih luas)":
            call join_cooperative
            
        "Buat coffee shop sendiri (value chain lengkap)":
            call coffee_shop_venture
            
        "Fokus kualitas premium (niche market)":
            call premium_quality_focus
 
label land_expansion:
    $ money -= 150000
    $ coffee_plants += 100
    $ knowledge += 25
    
    scene bg coffee_plantation_expanded
    show mahmud advisor at right
    show ara_adult determined at center
    
    m "Pilihan yang bagus! Dengan menambah lahan, produksi kita bisa meningkat drastis."
    m "Tapi ingat, tanaman kopi butuh 3-4 tahun untuk berbuah optimal."
    
    a "Aku sudah siap berinvestasi jangka panjang, Pak Mahmud."
    a "Kakek dulu juga bilang, kesabaran adalah kunci sukses petani kopi."
    
    $ reputation += 15
    $ energy -= 30
    
    n "Dengan ekspansi lahan, Ara kini mengelola kebun kopi seluas 5 hektar."
    n "Ini menjadikannya salah satu petani muda terbesar di desa."
    
    jump cooperative_invitation

label join_cooperative:
    $ knowledge += 20
    $ reputation += 25
    
    scene bg village_hall
    show kepala_desa friendly at left
    show ara_adult confident at center
    show farmers_group at right
    
    d "Selamat datang di Koperasi Kopi Gayo Bersatu, Ara!"
    d "Dengan bergabung bersama kami, akses pasar akan lebih mudah."
    
    a "Terima kasih, Pak Kepala Desa. Aku yakin ini keputusan yang tepat."
    
    # Show cooperative benefits
    n "Keuntungan bergabung koperasi:"
    n "• Harga jual lebih stabil"
    n "• Akses ke pelatihan rutin"
    n "• Bantuan modal dari pemerintah"
    n "• Sertifikasi organik dan fair trade"
    
    $ money += 75000  # Bonus dari koperasi
    
    jump organic_certification

label coffee_shop_venture:
    $ money -= 200000
    $ knowledge += 30
    $ reputation += 20
    
    scene bg coffee_shop_construction
    show ara_adult excited at center
    
    a "Saatnya wujudkan mimpi! Coffee shop dengan kopi hasil kebun sendiri!"
    a "Dari biji sampai cangkir, semua under control!"
    
    scene bg coffee_shop_grand_opening
    with dissolve
    
    show ara_adult proud at center
    show customers_happy at right
    
    a "Selamat datang di 'Warisan Gayo Coffee'!"
    a "Setiap tegukan adalah hasil kerja keras petani lokal."
    
    n "Coffee shop Ara menjadi hits! Wisatawan mulai berdatangan."
    
    $ money += 100000  # Daily revenue
    $ reputation += 30
    
    jump tourism_development

label premium_quality_focus:
    $ knowledge += 35
    $ reputation += 10
    
    scene bg coffee_processing_premium
    show ara_adult focused at center
    show quality_inspector at right
    
    a "Aku akan fokus pada kualitas super premium."
    a "Target pasar kafe specialty dan eksport."
    
    n "Dengan fokus kualitas, harga jual kopi Ara naik 300 persen!"
    n "Tapi volume penjualan lebih sedikit karena pasar terbatas."
    
    $ money += 200000
    
    jump international_recognition

# =============================================================================
# COOPERATIVE AND CERTIFICATION
# =============================================================================

label cooperative_invitation:
    scene bg village_meeting
    show kepala_desa serious at left
    show ara_adult listening at center
    
    d "Ara, dengan ekspansi kebun mu, kami ingin mengundang kamu"
    d "untuk memimpin program sertifikasi organik desa."
    
    show ara_adult surprised
    a "Memimpin? Tapi aku masih belajar, Pak."
    
    d "Justru karena itu! Kamu punya semangat baru dan pengetahuan modern."
    d "Kombinasi dengan tradisi kakek mu akan sempurna."
    
    menu:
        "Terima tantangan memimpin sertifikasi organik":
            $ reputation += 30
            $ knowledge += 20
            jump organic_certification_leader
            
        "Aku masih perlu belajar lebih dulu":
            $ knowledge += 10
            jump organic_certification

label organic_certification_leader:
    scene bg training_session
    show ara_adult teaching at center
    show farmers_learning at right
    
    a "Baik, Bapak-Ibu sekalian. Sertifikasi organik bukan hanya soal label."
    a "Ini soal menjaga kelestarian tanah untuk anak cucu kita."
    
    n "Di bawah kepemimpinan Ara, 20 petani berhasil mendapat sertifikat organik."
    n "Harga jual naik 150 persen, dan pembeli dari luar negeri mulai tertarik."
    
    $ money += 300000
    $ reputation += 50
    
    jump international_buyer

label organic_certification:
    scene bg certification_process
    show ara_adult learning at center
    show organic_inspector at right
    
    n "Proses sertifikasi organik memakan waktu 6 bulan."
    n "Ara harus mengubah cara bertani tanpa pestisida kimia."
    
    n "Berhasil! Kebun Ara mendapat sertifikat organik internasional."
    
    $ money += 150000
    $ knowledge += 25
    $ reputation += 20
    
    jump quality_improvement

# =============================================================================
# INTERNATIONAL RECOGNITION & MARKET ACCESS
# =============================================================================

label international_buyer:
    scene bg video_call_international
    show ara_adult professional at center
    show buyer_international at right
    
    "Buyer International" "Ms. Ara, we're very interested in Gayo coffee from your cooperative."
    "Buyer International" "The quality is exceptional, and the organic certification is perfect."
    
    show ara_adult confident
    a "Thank you! Our coffee represents generations of traditional knowledge."
    a "Combined with modern sustainable practices."
    
    "Buyer International" "We'd like to place an order for 10 tons annually."
    "Buyer International" "Price: $12 per kilogram, FOB Medan port."
    
    show ara_adult excited
    a "That's... that's amazing! Let me discuss with our cooperative."
    
    $ money += 500000
    $ reputation += 40
    
    jump sustainable_future

label international_recognition:
    scene bg international_coffee_award
    show ara_adult award_ceremony at center
    show judges_panel at right
    
    n "Kopi premium Ara meraih penghargaan di International Coffee Competition!"
    n "'Best Single Origin - Indonesia Category'"
    
    show ara_adult emotional
    a "Kakek... aku berhasil membawa nama Gayo ke pentas dunia..."
    
    # Award ceremony sequence
    n "Media internasional meliput keberhasilan Ara."
    n "Pesanan membludak dari seluruh dunia!"
    
    $ money += 1000000
    $ reputation += 100
    
    jump sustainable_future

# =============================================================================
# TOURISM DEVELOPMENT & AGROWISATA
# =============================================================================

label tourism_development:
    scene bg agrowisata_development
    show ara_adult visionary at center
    show tourists_group at right
    
    a "Dengan coffee shop yang sukses, sekarang saatnya kembangkan agrowisata!"
    a "Wisatawan bisa belajar langsung dari kebun sampai cangkir."
    
    scene bg agrowisata_grand_opening
    with dissolve
    
    show ara_adult guide at center
    show tourists_amazed at right
    
    a "Welcome to Gayo Highland Coffee Experience!"
    a "Here, you'll learn traditional coffee farming from our ancestors."
    
    n "Agrowisata Ara menjadi destinasi wajib di Aceh Tengah."
    n "Pendapatan desa meningkat, lapangan kerja terbuka."
    
    $ money += 400000
    $ reputation += 60
    
    jump community_empowerment

# =============================================================================
# COMMUNITY EMPOWERMENT & SOCIAL IMPACT
# =============================================================================

label community_empowerment:
    scene bg community_meeting
    show ara_adult leader at center
    show community_members at right
    
    a "Kesuksesan ini bukan milik aku sendiri."
    a "Mari kita kembangkan seluruh potensi desa!"
    
    # Community projects
    menu:
        "Bangun sekolah pertanian modern":
            call agricultural_school_project
            
        "Kembangkan koperasi simpan pinjam":
            call cooperative_bank_project
            
        "Buat pusat pengolahan kopi komunal":
            call processing_center_project

label agricultural_school_project:
    $ money -= 300000
    $ reputation += 50
    $ knowledge += 30
    
    scene bg agricultural_school
    show ara_adult teacher at center
    show young_farmers at right
    
    a "Ini 'Sekolah Petani Muda Gayo' - tempat ilmu tradisi bertemu teknologi modern."
    
    n "100 pemuda desa mendapat pelatihan komprehensif."
    n "Mereka siap jadi generasi penerus petani kopi."
    
    jump sustainable_future

label processing_center_project:
    $ money -= 250000
    $ community_income = 150000
    
    scene bg processing_center
    show ara_adult coordinator at center
    show workers_happy at right
    
    a "Dengan pusat pengolahan ini, semua petani bisa produksi kopi berkualitas tinggi."
    a "Nilai tambah tetap di desa, bukan dibawa orang luar."
    
    n "30 keluarga mendapat penghasilan tetap dari pusat pengolahan."
    
    jump sustainable_future

# =============================================================================
# SUSTAINABLE FUTURE & LEGACY
# =============================================================================

label sustainable_future:
    scene bg future_vision
    show ara_adult wise at center
    
    n "5 tahun setelah kepulangan Ara..."
    
    a "Dari gadis kota yang bingung, kini aku jadi bagian dari solusi."
    a "Warisan kakek tidak hanya terselamatkan, tapi berkembang pesat."
    
    # Achievement summary
    call achievement_summary
    
    scene bg coffee_plantation_thriving
    with dissolve
    
    show ara_adult peaceful at center
    show spirit_kakek at left
    
    k "Ara... kakek bangga padamu, nak."
    k "Kamu tidak hanya meneruskan tradisi, tapi membawanya ke masa depan."
    
    show ara_adult emotional
    a "Terima kasih, Kek. Ini semua berkat ajaran dan doa kakek."
    
    jump ending_choice

label ending_choice:
    scene bg sunset_plantation
    show ara_adult contemplative at center
    
    n "Ara kini menghadapi pilihan untuk masa depan..."
    
    menu:
        "Tetap fokus sebagai petani dan pengusaha kopi":
            jump ending_entrepreneur
            
        "Terjun ke politik untuk mengadvokasi petani":
            jump ending_politician
            
        "Jadi konsultan pertanian untuk seluruh Indonesia":
            jump ending_consultant
            
        "Menulis buku dan jadi motivator":
            jump ending_author

# =============================================================================
# MULTIPLE ENDINGS
# =============================================================================

label ending_entrepreneur:
    scene bg successful_business_empire
    show ara_adult ceo at center
    
    n "Ara memilih tetap fokus pada bisnis kopi."
    n "Dalam 10 tahun, dia membangun empire kopi terbesar di Sumatera."
    
    a "Tapi yang terpenting, semua petani mitra kami sejahtera."
    a "Profit with purpose - itulah filosofi bisnis kami."
    
    $ final_score = money + reputation + knowledge
    
    n "ENDING: Coffee Empire Builder"
    n "Score: [final_score]"
    n "Ara berhasil membangun bisnis berkelanjutan yang mengangkat kesejahteraan komunitas."
    
    jump credits

label ending_politician:
    scene bg legislative_building
    show ara_adult politician at center
    
    n "Ara terpilih jadi anggota DPR RI dari daerah pemilihan Aceh."
    n "Dia menjadi suara petani di tingkat nasional."
    
    a "Undang-undang perlindungan petani kecil ini untuk kakek dan seluruh petani Indonesia!"
    
    n "ENDING: People's Representative"
    n "Ara berhasil mengubah kebijakan nasional untuk mendukung petani kecil."
    
    jump credits

label ending_consultant:
    scene bg national_conference
    show ara_adult expert at center
    
    n "Ara menjadi konsultan pertanian terkemuka."
    n "Proyek-proyeknya tersebar dari Sabang sampai Merauke."
    
    a "Setiap daerah punya potensi unik seperti kopi Gayo."
    a "Tugas kita menggalinya dengan cara yang berkelanjutan."
    
    n "ENDING: National Agricultural Consultant"
    n "Ara membawa transformasi pertanian ke seluruh nusantara."
    
    jump credits

label ending_author:
    scene bg book_launch
    show ara_adult author at center
    
    n "Buku 'Pulang ke Akar: Perjalanan Seorang Anak Kota Menjadi Petani' menjadi bestseller."
    
    a "Cerita ini bukan hanya tentang aku."
    a "Ini tentang setiap orang yang berani kembali ke jati dirinya."
    
    n "ENDING: Inspirational Author"
    n "Ara menginspirasi ribuan anak muda untuk kembali ke sektor pertanian."
    
    jump credits

# =============================================================================
# CREDITS & EDUCATIONAL SUMMARY
# =============================================================================

label credits:
    scene black
    with fade
    
    centered "{size=+10}GAYOCRAFT:{/size}\n{size=+5}Journey of Gayo Coffee{/size}"
    
    centered "\n\nGame Edukasi tentang:"
    centered "• Budidaya Kopi Gayo Arabica"
    centered "• Kearifan Lokal Petani Aceh"
    centered "• Kewirausahaan Berbasis Komunitas"
    centered "• Sustainable Agriculture"
    centered "• Agrowisata dan Pemberdayaan Masyarakat"
    
    centered "\n\nFakta tentang Kopi Gayo:"
    centered "• Ditanam di ketinggian 1.200-2.000 mdpl"
    centered "• Varietas Arabica dengan cita rasa unique"
    centered "• Mendapat sertifikasi geografis internasional"
    centered "• Menjadi komoditas ekspor unggulan Aceh"
    centered "• Menghidupi 60,000+ keluarga petani"
    
    centered "\n\n{i}Terima kasih telah bermain GAYOCRAFT!{/i}"
    centered "{i}Mari lestarikan warisan kopi nusantara{/i}"
    
    return

label achievement_summary:
    # Display player achievements
    n "PENCAPAIAN ANDA:"
    n "Uang: Rp [money:,]"
    n "Reputasi: [reputation]/100"
    n "Pengetahuan: [knowledge]/100"
    n "Hari bermain: [day]"
    return
