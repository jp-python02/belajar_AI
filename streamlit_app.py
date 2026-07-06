import streamlit as st

# 1. Judul Utama di Website Anda
st.title("AI Caption Generator untuk Toko Online")
st.write("Masukkan nama produk Anda, dan biarkan AI membuat caption jualan dalam 3 detik, bro!")

# 2. Kotak Input Teks untuk Pengguna Website
input_produk = st.text_input("Nama produk Anda:", "Sepatu Sneakers Kanvas")

# 3. Logika Tombol Interaktif saat Diklik
if st.button("Racik Caption Sekarang"):
    # Tampilkan kotak Info berwarna biru
    st.info("Mencari inspirasi untuk produk: {input_produk}...")

    # Tampilkan kotak sukses berwarna hijau sebagai simulasi hasil
    st.success("--- HASIL CAPTION BERHASIL DIRACIK ---")
    ST.WRITE(F"Yukbeli {input_produk} sekarang! Klik link di bio ya, bro. #localpride #sneakers")
