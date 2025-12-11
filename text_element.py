import streamlit as st 

# Identitas pengguna
st.markdown("## 👤 Identitas")
st.write("**Kelompok : 17**")
st.write("**Nama:** Febrianscah")
st.write("**NIM:** 0110122242")
st.write("**Nama:** Jasrino Maulana Putra")
st.write("**NIM:** 0110122297")
st.write("**Nama:** Syaffa Mufidah")
st.write("**NIM:** 0110122188")
st.divider()

# Bagian awal tampilan
st.write("Hello")
st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""this is our sub-header""")
st.caption("""this is our caption""")

# displaying plain text
st.text("hi, \nPeople\t")
st.text('welcome to')
st.text("""streamlit's world""")

# displaying markdown
st.markdown("# hi, \n# ***People*** \t!!!!!")
st.markdown('## welcome to')
st.markdown("""### streamlit's world""")

# displaying latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("Python Code")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# Displaying Java Code
st.subheader("Java Code")
st.code("""
public class GFG {
    public static void main(String args[]) {
        System.out.println("Hello World");
    }
}
""", language='java')

# Displaying JavaScript Code
st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    adddlert("Welcome guest!");
} catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>
""", language='javascript')
