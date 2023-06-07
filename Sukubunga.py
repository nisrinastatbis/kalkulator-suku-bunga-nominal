

import streamlit as st


#HALAMAN HITUNG SUKU BUNGA NOMINAL

st.title('Kalkulator Suku Bunga Nominal')

p= st.number_input ("masukkan pokok pinjaman",0)
i= st.number_input ("masukkan suku bunga per rate")
n= st.number_input ("masukkan periode waktu",0)
Suku_Bunga_Nominal= st.button("Hitung nilai akhir Suku Bunga Nominal")


if Suku_Bunga_Nominal:
    Suku_Bunga = p*i*n
    st.write("nilai suku bunga nominal adalah = ", Suku_Bunga)