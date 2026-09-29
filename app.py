import streamlit as st

# 1. Pengaturan tampilan awal halaman web
st.set_page_config(page_title="Kejutan Spesial Untukmu ❤️", page_icon="💖", layout="centered")

# Efek balon otomatis berhamburan saat website dibuka pacarmu!
st.balloons()

# 2. Judul Utama
st.title("Halo Sayang! Welcome to Our Dynamic Place 🥰")
st.write("Website mini ini aku rakit khusus pakai Python buat nemenin hari LDR kita.")

# 3. Galeri Foto-Foto Bersama
st.subheader("📸 Memori Indah Kita")

# Pastikan nama 'foto1.jpg' dan 'foto2.jpg' sesuai dengan yang ada di foldermu
try:
    st.image("foto1.jpg", caption="Saat kita pertama kali jalan-jalan ✨", use_container_width=True)
    st.image("foto2.jpg", caption="Momen favorit yang selalu bikin kangen 💖", use_container_width=True)
except Exception as e:
    st.warning("Foto belum terbaca. Pastikan file foto sudah ditaruh di dalam folder yang sama dengan app.py ya!")

# 4. Surat Cinta Romantis
st.subheader("💌 Surat Kecil LDR")
st.info(
    "Meskipun jarak memisahkan kita untuk sementara waktu, perasaan aku nggak akan pernah berubah. "
    "Semoga website kecil ini bisa bikin kamu tersenyum hari ini. I love you so much! 💖✨"
)

# 5. Tombol Interaktif
if st.button("Klik kalau kamu kangen aku! 😘"):
    st.success("Yeeay! Aku juga kangen kamu bangeeet! Langsung kabari aku via WhatsApp ya! 📲❤️")
    st.snow() # Efek salju turun di layar
