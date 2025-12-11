import streamlit as st
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("Kelompok 17 - Visualisasi Data")
st.markdown("""
    - Jasrino Maulana Putra - 0110122297
    - Febrianscah - 0110122242
    - Syaffa Mufidah - 0110122188
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)