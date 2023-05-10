import streamlit as st
from PIL import Image

st.set_page_config(page_title="About us", page_icon=":nerd_face:")
st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>About Us</h1>", unsafe_allow_html=True)

st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Kami dari kelompok 6 kelas 1E Penjaminan Mutu Industri Pangan Politeknik AKA Bogor. Kalkulator BMI kami dirancang untuk membantu Anda menghitung berat badan ideal Anda dan memberikan saran tentang cara mencapainya. Kami memahami bahwa setiap orang memiliki kebutuhan yang berbeda, dan itulah mengapa kami menyediakan sumber daya yang dapat disesuaikan dengan kebutuhan Anda. Jangan ragu untuk menghubungi kami jika Anda memerlukan bantuan atau saran. </p>"
         , unsafe_allow_html=True)
font_size = "20px"

#image
ismi = Image.open('ismi.jpg')
silmi = Image.open('silmi.jpeg')
eka = Image.open('eka.jpeg')
talitha = Image.open('talitha.jpeg')
raja = Image.open('raja.jpeg')

# display the images in a row
col1, col2, col3, col4, col5= st.columns(5)

with col1:
    st.image(ismi, use_column_width=True)
    st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Ismi Maharani (2220459)</span>",
    unsafe_allow_html=True)

with col2:
    st.image(raja, use_column_width=True)
    st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Raja Nur Falah (2220483)</span>",
    unsafe_allow_html=True)

with col3:
    st.image(silmi, use_column_width=True)
    st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Silmi Arijah (2220488)</span>",
    unsafe_allow_html=True)

with col4:
    st.image(eka, use_column_width=True)
    st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Sri Rizka Nurwahidah (2220490)</span>",
    unsafe_allow_html=True)

with col5:
    st.image(talitha, use_column_width=True)
    st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Talitha Dias Azzahra (2220492)</span>",
    unsafe_allow_html=True)
