import streamlit as st

st.set_page_config(page_title="Visualisasi Data - Kelompok 17", page_icon="📊", layout="wide")

st.title("Visualisasi Data — Kelompok 17")
st.markdown("Pilih halaman lewat menu Pages (kiri atas) atau link cepat di bawah.")

cols = st.columns(3)
with cols[0]:
    # link ke file di folder pages/
    st.page_link("pages/01_Columns.py", label="Columns Demo", icon="🧱")
with cols[1]:
    st.page_link("pages/02_Navigation.py", label="Navigation Demo", icon="🧭")
with cols[2]:
    st.write("")  # ruang

st.markdown("---")
st.write("Kelompok 17 - Visualisasi Data")
st.write("- Jasrino Maulana Putra - 0110122297")
st.write("- Febrianscah - 0110122242")
st.write("- Syaffa Mufidah - 0110122188")