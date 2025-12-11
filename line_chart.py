import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok 17 - Visualisasi Data")
st.markdown("""
    - Jasrino Maulana Putra - 0110122297
    - Febrianscah - 0110122242
    - Syaffa Mufidah - 0110122188
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)

df2 = pd.DataFrame(
    np.random.randn(80, 4),
    columns=["D1", "D2", "D3", "D4"]
)

st.line_chart(df2)