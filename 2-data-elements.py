import streamlit as st
import pandas as pd             # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np              # untuk membuat data numerik acak
import altair as alt            # untuk membuat chart interaktif

st.title("Praktikum-1")
st.caption("Bagian 2: Data Elements")

# st.markdown digunakan untuk menampilkan teks dengan format Markdown (bullet list, bold, italic, dll.)
st.markdown("""
        - Jasrino Maulana Putra - 0110122297
        - Febrianscah - 0110122242
        - Syaffa Mufidah - 0110122188
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan dataframe
st.dataframe(df)

st.subheader("DataFrame 1000")

df = pd.DataFrame(
    np.random.randn(1000,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan dataframe
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

# highlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# Highlight Nilai Maximum
st.subheader("Highlight Maximum Value di DataFrame")

# highlight nilai terbesar disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_max(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(70,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") # kenaikan 1.2 °C

# Metrics sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default): naik -> hijau, turun -> merah
# - "inverse": kebalikannya (naik -> merah)
# - "off": tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") # netral (tidak baik, tidak buruk)

# Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong # naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") # penurunan