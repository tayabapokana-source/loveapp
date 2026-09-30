import streamlit as st

# 1. Konfigurasi Awal Halaman
st.set_page_config(page_title="HALLO CACA SURYANI ❤️", page_icon="💝", layout="centered")

# Inisialisasi nomor slide menggunakan Session State agar posisi halaman tersimpan saat diklik
if "slide" not in st.session_state:
    st.session_state.slide = 1

# ==============================================================================
# STRUKTUR KONTEN SLIDE (Silakan sesuaikan nama file foto & teks ucapanmu)
# ==============================================================================
if st.session_state.slide == 1:
    st.balloons() # Efek balon berhamburan khusus di slide pembuka!
    st.title("Halo Sayang! 🥰")
    
    # Membungkus teks panjang menggunakan kutip tiga agar rapi dan aman dari error
    pesan_romantis = """
    Melalui halaman kecil yang aku rakit , aku cuma ingin meluangkan waktu sejenak untuk menuliskan apa yang sering kali sulit aku ucapkan langsung lewat kata-kata. Aku ingin kamu tahu betapa beruntung dan bersyukurnya aku karena memiliki kamu di dalam hidupku. Terima kasih ya, sudah menjadi sosok yang luar biasa, yang selalu sabar menghadapi segala kurangku, dan selalu menjadi alasan di balik senyum paling tulus yang aku miliki sampai detik ini.

    Dunia kadang terasa sangat bising, melelahkan, dan penuh dengan hal-hal yang membuat kepala jadi pusing. Tapi, setiap kali aku melihat kamu, mengobrol denganmu, atau sekadar memikirkan bahwa aku punya kamu di sisiku, semua rasa lelah itu rasanya menguap begitu saja. Kehadiranmu itu seperti tempat bernaung paling nyaman buatku. Bersamamu, aku tidak pernah merasa perlu berpura-pura menjadi orang lain. Aku bisa menjadi diriku yang seutuhnya, karena aku tahu aku dicintai oleh orang yang tepat.

    Terima kasih sudah memilih untuk tinggal, ya. Terima kasih untuk setiap tawa kecil yang kita bagi bersama, untuk dukungan-dukungan sederhana yang selalu menguatkan aku saat dunia sedang tidak berjalan baik, dan untuk kasih sayang hangat yang selalu kamu berikan. Menghabiskan waktu bersamamu adalah momen-momen favoritku yang tidak akan pernah bosan untuk aku ulangi. 

    Aku tidak tahu apa yang akan terjadi di masa depan nanti, tapi satu hal yang aku tahu pasti: aku ingin terus berjalan bersamamu, melewati hari demi hari, merajut lebih banyak cerita indah, dan merayakan setiap kebahagiaan-kebahagiaan kecil di hidup ini berdua denganmu. Tetap jadi pacar hebatku yang menggemaskan ya. I love you so much, hari ini, esok, dan seterusnya! ❤️✨
    """
    
    # Menampilkan teks ke dalam kotak info yang estetik
    st.info(pesan_romantis)
    
    st.write("---")
    st.info("Klik tombol 'Slide Selanjutnya' ya! 👇")

elif st.session_state.slide == 2:
    st.title("Slide 2: Setiap Detik Berharga ✨")
    
    # Membungkus kata-kata romantis yang panjang menggunakan tanda kutip tiga (""")
    pesan_slide_2 = """
    Katanya, sebuah foto bisa menyimpan ribuan kenangan indah yang tidak akan pernah pudar oleh waktu. Dan setiap kali aku melihat foto di bawah ini, aku selalu diingatkan tentang betapa indahnya momen-momen yang sudah kita laluin bersama selama ini. Kadang aku suka tersenyum sendiri waktu mengingat betapa serunya setiap obrolan kita, tawa lepas kita, dan bagaimana semua hal yang awalnya biasa saja berubah menjadi jauh lebih menyenangkan kalau aku sedang berada di dekat kamu.

    Bersamamu, waktu rasanya berjalan begitu cepat, sampai-sampai aku selalu berharap bisa memutar balik waktu atau menghentikan detiknya sebentar saja, hanya untuk menikmati kehadiranmu lebih lama lagi. Foto ini bukan cuma sekadar gambar digital di layar buatku, tapi ini adalah bukti nyata dari salah satu hari terbaik dalam hidupku, hari di mana aku sadar bahwa bahagia itu ternyata sangat sederhana: cukup dengan melihat kamu bahagia dan ada di sisiku. Terima kasih ya sudah mengizinkan aku menjadi bagian dari memori indah ini.
    """
    
    # Menampilkan teks narasi romantis di atas foto
    st.write(pesan_slide_2)
    st.write("") # Memberi jarak kosong/spasi agar tidak terlalu rapat
    
    # Menampilkan Foto Pertama yang sudah diganti namanya di GitHub kamu
    try:
        st.image("foto1.jpg", caption="THANKS FOR MOMENT", use_container_width=True)
    except Exception as e:
        st.warning("Foto 'foto1.jpg' belum terbaca. Pastikan format nama file di GitHub sudah huruf kecil semua ya!")

elif st.session_state.slide == 3:
    st.title("Slide 3: Menatap Masa Depan 💖")
    st.write("Terima kasih ya sudah selalu sabar dan ada buat aku sampai detik ini.")
    
    # Menampilkan Foto Kedua
    try:
        st.image("foto2.jpg", caption="SEMOGA YA SEMOGA 🥰", use_container_width=True)
    except Exception as e:
        st.warning("Foto 'foto2.jpg' belum terbaca di GitHub.")

elif st.session_state.slide == 4:
    st.snow() # Efek salju turun di slide terakhir!
    st.title("Slide 4: MWEHEHEHE 💌")
    
    st.success(
        "TUNGGU AKU SUKSES NANTI YA 💖✨"
    )
    
    # Fitur Interaktif Tombol Kangen
    if st.button("KLIK JIKA KAMU SAYANG AKU! 😘"):
        st.success("Yeeay! Aku juga SAMA WLEEEE 📲❤️")

# ==============================================================================
# SISTEM NAVIGASI TOMBOL SLIDE (Pindah Halaman)
# ==============================================================================
st.write("---") # Garis pembatas teks
kolom1, kolom2 = st.columns(2)

with kolom1:
    # Tombol untuk kembali ke slide sebelumnya
    if st.session_state.slide > 1:
        if st.button("⬅️ Slide Sebelumnya"):
            st.session_state.slide -= 1
            st.rerun() # Refresh halaman untuk memuat slide baru

with kolom2:
    # Tombol untuk maju ke slide berikutnya
    if st.session_state.slide < 4:  # Angka 4 adalah total jumlah slide kamu
        if st.button("Slide Selanjutnya ➡️"):
            st.session_state.slide += 1
            st.rerun()

# ==============================================================================
# BONUS: BACKSOUND MUSIK ROMANTIS (Berjalan di semua slide)
# ==============================================================================
st.write("---")
st.subheader("🎵 Lagu untuk Kamu")
# Kamu bisa mengganti URL di bawah ini dengan link file .mp3 lagu kesukaan kalian asli
LINK_LAGU = "https://22832-sleeping-with-sirens.mp3.pm/song/10315886-if-i-m-james-dean-you-re-audrey-hepburn-acoustic-version/"
st.audio(LINK_LAGU, format="audio/mp3")
