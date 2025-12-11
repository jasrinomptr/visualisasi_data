import streamlit as st
import pandas as pd

# Bagian 1: Text Element
st.header("Ini header")
st.subheader("Ini subheader")
st.text("Ini untuk teks biasa tanpa format")
st.markdown("**Ini untuk teks bold** dan *ini untuk italic*")
st.caption("ini untuk caption")
st.title("Ini untuk judul")

## 1. judul praktikum pakai judul
## 2. bagian praktikum pakai subheader
## 3. nama lengkap anggota - nim pakai mark

# Bagian 2: Displaying LaTeX
st.header("Displaying LaTeX")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominal

# Bagian 3: Menampilkan Kode program
st.header ("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!)
'''

# st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello World!);
        }
    }
""", language='java')
# fungsi st.code() bisa digunakan untuk bahasa pemrograman lain 
# seperti Java, Javascript, C++, HTML, dll

st.subheader("CSS Code")
st.code("""
div{
    width: 700px;
    height: 600px;
    /* border-radius: 20px; */
    margin: auto;
    margin-left: 20px;
}

.container{
    display: flex;
    position: absolute;
    left: 20%;
}

.container img{
    width: 154px;
    height: 154px;
}

.kotak1{
    background-color: red;
}

.kotak2{
    background-color: yellow;
}

.kotak3{
    background-color: green;
}

.kotak4{
    background-color: blue;
}
""", language='css')

st.subheader("Javascript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest!); // kesalahan ketik (addalert)
    sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
}
""", language='javascript')
# Kode ini menunjukkan contoh bagaimana menangani error (expection)
# di Javascript.
# Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai
# contoh kode.

# latihan 1 text elements
st.title("Praktikum-1")
st.subheader("Bagian 1")
st.markdown("""
        - Jasrino Maulana Putra (0110122297)
        - Febrianscah (0110122242)
        - Syaffa Mufidah (0110122188)
""")