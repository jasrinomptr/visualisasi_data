import streamlit as st
import datetime

# Judul Aplikasi
st.title("🚀 Formulir Pendaftaran Acara: Versi Kompleks")
st.write("Menggunakan validasi input, logika kondisional, dan layout tab.")

# 1. Membuat Form
# Menggunakan 'with st.form' untuk mengelompokkan elemen
with st.form(key="formulir_kompleks"):
    
    # 2. Kreasi Layout: Menggunakan Tab
    tab1, tab2 = st.tabs(["Data Diri", "Preferensi & Lain-lain"])

    with tab1:
        st.header("1. Data Diri Peserta")
        
        # st.text_input (Text Box)
        nama = st.text_input(label="Nama Lengkap Anda *")
        
        # st.radio (Radio Buttons) [cite: 250-257]
        pekerjaan = st.radio(
            "Pekerjaan Saat Ini *",
            ('Pelajar/Mahasiswa', 'Pegawai Swasta', 'Wiraswasta', 'Lainnya'),
            horizontal=True
        )
        
        # LOGIKA KONDISIONAL
        # Elemen ini hanya muncul jika 'Lainnya' dipilih
        pekerjaan_lainnya = "" # Inisialisasi variabel
        if pekerjaan == 'Lainnya':
            pekerjaan_lainnya = st.text_input("Sebutkan Pekerjaan Anda *") [cite: 336]
        
        # st.date_input (Date Input)
        tgl_lahir = st.date_input(
            "Tanggal Lahir",
            value=datetime.date(2000, 1, 1),
            max_value=datetime.date.today()
        )
        
        # st.number_input (Number Input)
        usia = st.number_input(
            "Usia", 
            min_value=17, 
            max_value=100, 
            value=25, 
            help="Usia minimal pendaftar adalah 17 tahun."
        )

    with tab2:
        st.header("2. Preferensi & Lain-lain")
        
        # st.multiselect (Multiselects)
        hobi = st.multiselect(
            "Apa hobi Anda? (Bisa pilih lebih dari satu)",
            ["Membaca", "Olahraga", "Musik", "Gaming", "Jalan-jalan", "Memasak"],
            default=["Membaca"]
        )
        
        # st.time_input (Time Input)
        waktu_preferensi = st.time_input("Waktu Sesi yang Diinginkan")
        
        # st.color_picker (Color Input)
        warna_tema = st.color_picker("Pilih Warna Tema Kartu Peserta Anda", "#0d6efd")
        
        # st.text_area (Text Area)
        alasan_bergabung = st.text_area(
            "Apa motivasi Anda bergabung acara ini?",
            max_chars=500,
            placeholder="Tuliskan alasan Anda..."
        )
        
        # st.file_uploader (Dataset Upload)
        file_cv = st.file_uploader(
            "Upload CV (Opsional, .pdf)", 
            type=["pdf"]
        )

    # 3. Tombol Submit
    # st.form_submit_button
    # Diletakkan di luar tab, tapi masih di dalam form
    st.markdown("---")
    st.caption("Pastikan data yang bertanda (*) sudah terisi dengan benar.")
    submitted = st.form_submit_button(label="Kirim Pendaftaran")

# 4. Logika Setelah Form di-Submit
if submitted:
    # VALIDASI INPUT
    valid = True
    if not nama:
        st.error("Error: Nama Lengkap wajib diisi!")
        valid = False
        
    if pekerjaan == 'Lainnya' and not pekerjaan_lainnya:
        st.error("Error: Harap sebutkan pekerjaan Anda!")
        valid = False
    
    # JIKA LOLOS VALIDASI
    if valid:
        st.success(f"Pendaftaran Berhasil! Terima kasih, **{nama}**!")
        st.balloons()
        
        st.subheader("Ringkasan Pendaftaran Anda:")
        
        # Menentukan nilai 'pekerjaan' yang akan ditampilkan
        pekerjaan_final = pekerjaan_lainnya if pekerjaan == 'Lainnya' else pekerjaan
        
        # Menampilkan data gabungan dari kedua tab
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Nama:** {nama}")
            st.write(f"**Pekerjaan:** {pekerjaan_final}")
            st.write(f"**Usia:** {usia} tahun")
            st.write(f"**Tanggal Lahir:** {tgl_lahir.strftime('%d %B %Y')}")
            
        with col2:
            st.write(f"**Sesi Pilihan:** {waktu_preferensi}")
            st.write(f"**Hobi:** {', '.join(hobi) if hobi else '-'}")
            st.markdown(f"**Warna Tema:** `{warna_tema}` <div style='width:20px; height:20px; display:inline-block; background-color:{warna_tema}; border: 1px solid #000;'></div>", unsafe_allow_html=True)
            if file_cv is not None:
                st.write(f"**CV Terupload:** {file_cv.name}")
        
        st.write(f"**Alasan Bergabung:** \n> {alasan_bergabung}")