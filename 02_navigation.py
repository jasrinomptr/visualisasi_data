import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Navigation", page_icon="🧭", layout="wide")

# Sidebar: Identitas Kelompok
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

st.title("Navigasi — Pola Umum")
st.caption("Tabs, sidebar switch, dan query params.")

# Contoh data
np.random.seed(7)
hari = pd.date_range(end=pd.Timestamp.today().normalize(), periods=14)
df = pd.DataFrame({
    "tanggal": hari,
    "order": np.random.randint(20, 80, len(hari)),
    "revenue": np.random.randint(1_000_000, 5_000_000, len(hari))
})

# Tabs
st.subheader("1) Tabs")
tab_overview, tab_detail, tab_faq = st.tabs(["Overview", "Detail", "FAQ"])
with tab_overview:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Trend Order 14 hari:")
        st.line_chart(df.set_index("tanggal")[["order"]], height=220)
    with col2:
        st.write("Ringkasan")
        st.metric("Total Order", int(df["order"].sum()))
        st.metric("Avg/Hari", round(df["order"].mean(), 1))
with tab_detail:
    st.write("Detail Transaksi (contoh)")
    st.bar_chart(df.set_index("tanggal")[["revenue"]], height=220)
    st.dataframe(df, use_container_width=True)
with tab_faq:
    st.write("Q: Bagaimana cara pindah tab via URL?")
    st.write("A: Gunakan Query Params di bagian 3) di bawah.")

# Sidebar Section Switch
st.subheader("2) Sidebar Section Switch")
section = st.sidebar.radio("Pilih Section:", ["Dashboard", "Laporan", "Pengaturan"], index=0, key="section_radio")
if section == "Dashboard":
    st.info("Section: Dashboard — tampilkan ringkasan metrik & grafik kecil.")
    st.line_chart(df.set_index("tanggal")[["order"]], height=160)
elif section == "Laporan":
    st.info("Section: Laporan — tabel & unduhan CSV.")
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Unduh CSV", data=csv, file_name="laporan.csv", mime="text/csv")
else:
    st.info("Section: Pengaturan — tempat kontrol dan preferensi.")
    dark = st.sidebar.checkbox("Mode gelap (dummy)")
    st.write("Nilai toggle/checkbox:", dark)

# Query Params
st.subheader("3) Query Params")
# baca param
page = st.query_params.get("page", ["dashboard"])
# normalize
page_val = page[0] if isinstance(page, list) else page

col1, col2, col3 = st.columns(3)
if col1.button("Goto ?page=dashboard"):
    st.query_params["page"] = "dashboard"
if col2.button("Goto ?page=report"):
    st.query_params["page"] = "report"
if col3.button("Goto ?page=settings"):
    st.query_params["page"] = "settings"

st.write("Query param aktif:", page_val)
if page_val == "dashboard":
    st.success("Anda berada di halaman virtual: dashboard")
elif page_val == "report":
    st.warning("Anda berada di halaman virtual: report")
else:
    st.error("Anda berada di halaman virtual: settings")
