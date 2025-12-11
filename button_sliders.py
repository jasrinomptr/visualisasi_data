import streamlit as st
import time


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

# =====================================================
# MODUL 1: STREAMLIT – INTERACTIVE ELEMENTS
# =====================================================
st.title("🎯 Modul 1: Streamlit Interactive Elements")

# -----------------------------------------------------
# 1️⃣ BUTTON
# -----------------------------------------------------
st.header("1️⃣ Button")
st.write("Tombol digunakan untuk menjalankan aksi tertentu ketika diklik.")

button = st.button("Click Here")

if button:
    st.success("✅ You have clicked the Button.")
else:
    st.warning("❌ You have not clicked the Button.")

# -----------------------------------------------------
# 2️⃣ RADIO BUTTONS
# -----------------------------------------------------
st.header("2️⃣ Radio Buttons")
st.write("Radio button digunakan untuk memilih satu opsi dari beberapa pilihan yang tersedia.")

gender = st.radio(
    "Select your Gender:",
    ("Male", "Female", "Others")
)

if gender == "Male":
    st.info("You have selected Male.")
elif gender == "Female":
    st.info("You have selected Female.")
else:
    st.info("You have selected Others.")

# -----------------------------------------------------
# 3️⃣ CHECK BOXES
# -----------------------------------------------------
st.header("3️⃣ Check Boxes")
st.write("Checkbox digunakan untuk memilih satu atau lebih opsi dari daftar.")

check_1 = st.checkbox("Books")
check_2 = st.checkbox("Movies")
check_3 = st.checkbox("Sports")

st.subheader("📚 Your Selected Hobbies:")
if check_1:
    st.write("- Books")
if check_2:
    st.write("- Movies")
if check_3:
    st.write("- Sports")
if not any([check_1, check_2, check_3]):
    st.write("Belum memilih hobi apa pun.")

# -----------------------------------------------------
# 4️⃣ DROP-DOWNS (SELECTBOX)
# -----------------------------------------------------
st.header("4️⃣ Drop-Downs (Select Box)")
st.write("Dropdown memungkinkan pengguna memilih satu opsi dari daftar pilihan yang tersedia.")

hobby = st.selectbox(
    "Choose your hobby:",
    ("Books", "Movies", "Sports")
)
st.success(f"You selected: {hobby}")

# -----------------------------------------------------
# 5️⃣ MULTISELECTS
# -----------------------------------------------------
st.header("5️⃣ Multiselects")
st.write("Multiselect memungkinkan pengguna memilih beberapa opsi dari daftar pilihan.")

hobbies = st.multiselect(
    "What are your Hobbies?",
    [
        "Reading", "Cooking", "Watching Movies/TV Series",
        "Playing", "Drawing", "Hiking"
    ],
    ["Reading", "Playing"]  # nilai default
)

st.subheader("🎨 Your Selected Hobbies:")
if hobbies:
    for h in hobbies:
        st.write(f"- {h}")
else:
    st.write("Kamu belum memilih hobi apa pun.")

# -----------------------------------------------------
# 6️⃣ DOWNLOAD BUTTONS
# -----------------------------------------------------
st.header("6️⃣ Download Buttons")
st.write("""
Download button memungkinkan pengguna mengunduh file langsung dari aplikasi.
Fungsi yang digunakan: `st.download_button()`.
""")

# Tombol download untuk file gambar
try:
    with open("C:\\xampp\\visdat\\praktikum01\\landak.jpg", "rb") as img_file:
        st.download_button(
            label="📷 Download Image",
            data=img_file,
            file_name="landak.jpg",
            mime="image/jpg"
        )
except FileNotFoundError:
    st.warning("⚠️ File 'D:/animal1.jpg' tidak ditemukan. Ganti path sesuai lokasi file kamu.")

# Tombol download untuk file CSV
try:
    with open("./files/avocado.csv", "rb") as csv_file:
        st.download_button(
            label="📊 Download CSV",
            data=csv_file,
            file_name="data.csv",
            mime="text/csv"
        )
except FileNotFoundError:
    st.warning("⚠️ File './files/avocado.csv' tidak ditemukan. Ganti path sesuai file kamu.")

# -----------------------------------------------------
# 7️⃣ PROGRESS BARS
# -----------------------------------------------------
st.header("7️⃣ Progress Bars")
st.write("Progress bar digunakan untuk menampilkan proses berjalan atau loading task.")

progress_bar = st.progress(0)
for percentage in range(100):
    time.sleep(0.02)
    progress_bar.progress(percentage + 1)
st.success("✅ Download Complete!")

# -----------------------------------------------------
# 8️⃣ SPINNERS
# -----------------------------------------------------
st.header("8️⃣ Spinners")
st.write("""
Spinner digunakan untuk memberikan indikasi bahwa suatu proses sedang berlangsung.  
Biasanya dipakai ketika proses memerlukan waktu agak lama.
""")

with st.spinner("⏳ Loading..."):
    time.sleep(5)
st.success("👋 Hello Data Scientists!")
