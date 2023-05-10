import streamlit as st
import streamlit_themes as stt

# Tambahkan kode untuk memilih tema
theme = st.sidebar.selectbox(
    "Pilih Tema",
    ("light", "dark")
)

# Tambahkan kode untuk memilih tema
if theme == "light":
    stt.set_theme("lumen")
else:
    stt.set_theme("dark")

# Tambahkan kode Streamlit seperti biasa untuk membuat tampilan aplikasi
st.title("Aplikasi dengan Pilihan Tema")

st.write("Ini adalah contoh tampilan Streamlit dengan pilihan tema.")

