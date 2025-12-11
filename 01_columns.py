import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(page_title="Columns", page_icon="🧱", layout="wide")

# Sidebar: Identitas Kelompok (tetap)
st.sidebar.header("Data Kelompok")
st.sidebar.markdown("""
<div style="padding: 14px 18px; border-radius: 12px; border: 1px solid rgba(49,51,63,0.12);
     background: linear-gradient(180deg, rgba(240,241,246,0.6), rgba(240,241,246,0.3));">
  <div style="font-size: 16px; font-weight: 700;">Kelompok 17 - Visualisasi Data</div>
  <div style="margin-top:6px; line-height: 1.5;">
    - Jasrino Maulana Putra - 0110122297<br>
    - Febrianscah - 0110122242<br>
    - Syaffa Mufidah - 0110122188
  </div>
</div>
""", unsafe_allow_html=True)

st.title("Columns — Variasi & Pola")
st.caption("Contoh lengkap: rasio kolom, spacer, padding, grid, kartu, dashboard mini, container & empty.")

# Dashboard Mini
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Order (bulan ini)", 312, delta=+12)
with m2: st.metric("Revenue", "Rp 128 jt", delta="+8%")
with m3: st.metric("Customer Baru", 57, delta="+6")
with m4: st.metric("Retensi", "72%", delta="-2%")

# Chart dan Tabel berdampingan
left, right = st.columns([2, 1])
with left:
    st.write("Trend Harian (7 hari):")
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=7)
    df = pd.DataFrame({"tanggal": dates, "order": np.random.randint(20, 70, size=7)}).set_index("tanggal")
    st.line_chart(df, height=220)
with right:
    st.write("Top Produk")
    top = pd.DataFrame({
        "Produk": ["Kopi Susu", "Boba Latte", "Americano", "Cappuccino", "Matcha"],
        "Terjual": np.random.randint(40, 120, 5)
    }).sort_values("Terjual", ascending=False)
    st.dataframe(top, use_container_width=True)

st.markdown("---")

# Columns dengan rasio
st.subheader("1) Columns dengan Rasio")
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    st.write("Kolom 1 (rasio 2) — cocok untuk konten utama.")
    st.text_area("Catatan Utama", height=120, placeholder="Tulis catatan penting di sini...")
with c2:
    st.write("Kolom 2 (rasio 1)")
    st.checkbox("Checklist A")
    st.checkbox("Checklist B")
with c3:
    st.write("Kolom 3 (rasio 1)")
    st.selectbox("Pilih Opsi", ["A", "B", "C"])

# Spaced-out (spacer)
st.subheader("2) Spaced-Out Columns")
colA, spacer1, colB = st.columns([1, 0.15, 1])
with colA:
    st.write("Kolom A")
    st.code("colA, spacer, colB = st.columns([1, 0.15, 1])")
with spacer1:
    st.write(" ")
with colB:
    st.write("Kolom B")
    st.code("with spacer: st.write(' ')")
st.caption("Teknik spacer membantu beri jarak tanpa CSS.")

# Padding
st.subheader("3) Columns dengan Padding")
pad_left, pad_right = st.columns(2)
with pad_left:
    st.markdown(
        '<div style="padding:16px; border:1px dashed rgba(49,51,63,0.12); border-radius:12px;">'
        '<b>Konten ber-padding</b><br>Tambahkan ruang agar rapi dan nyaman dilihat.'
        '</div>', unsafe_allow_html=True
    )
with pad_right:
    st.markdown(
        '<div style="padding:28px; border:1px dashed rgba(49,51,63,0.12); border-radius:12px;">'
        'Padding lebih tebal untuk menekankan konten tertentu.'
        '</div>', unsafe_allow_html=True
    )

# Grid kartu
st.subheader("4) Grid Kartu (Katalog)")
for r in range(2):
    g1, g2, g3 = st.columns(3)
    for idx, col in enumerate([g1, g2, g3], start=1):
        with col:
            st.markdown(
                f'<div style="padding:12px; border-radius:10px; border:1px solid rgba(49,51,63,0.08);">'
                f'<div style="font-weight:700; margin-bottom:6px;">Item {r*3+idx}</div>'
                f'<div style="font-size:13px; opacity:0.8;">Deskripsi singkat item.</div>'
                f'<div style="margin-top:8px;"><a href="#" style="text-decoration:none;">Detail →</a></div>'
                f'</div>', unsafe_allow_html=True)

# Expander
st.subheader("5) Expander / Accordion")
with st.expander("Lihat penjelasan gabungan teknik kolom"):
    st.markdown(
        "- **Rasio** untuk menonjolkan area penting\n"
        "- **Spacer** untuk memberi jarak antar elemen\n"
        "- **Padding** untuk kenyamanan baca\n"
        "- **Grid** untuk pola berulang (kartu/katalog)"
    )

# Container & Empty
st.subheader("6) Container & Empty (dinamis)")
slot = st.empty()
with st.container():
    st.write("Container ini menampung elemen secara berurutan.")
    st.write("Kita juga bisa update elemen di tempat lain menggunakan `st.empty()`.")
col_run, col_clear = st.columns(2)
with col_run:
    if st.button("▶ Jalankan demo update"):
        for i in range(5, -1, -1):
            slot.info(f"Mengupdate elemen (countdown): {i}")
            time.sleep(0.4)
        slot.success("Selesai! Ini hasil update terakhir.")
with col_clear:
    if st.button("⟲ Bersihkan"):
        slot.empty()

st.markdown("---")
st.success("Semua variasi kolom di atas responsive mengikuti lebar layar.")