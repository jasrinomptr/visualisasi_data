import streamlit as st
import graphviz as graphviz

st.title("Area Chart")
st.write("Kelompok 17 - Visualisasi Data")
st.markdown("""
    - Jasrino Maulana Putra - 0110122297
    - Febrianscah - 0110122242
    - Syaffa Mufidah - 0110122188
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model" 
    }
""")