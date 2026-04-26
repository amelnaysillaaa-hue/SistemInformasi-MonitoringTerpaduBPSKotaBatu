import streamlit as st
import base64
from pathlib import Path

# ================= KONFIGURASI =================
st.set_page_config(
    page_title="Portal BPS Kota Batu",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/e/e0/Logo_BPS.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= FUNGSI LOGO =================
def get_base64_of_bin_file(bin_file):
    path = Path(bin_file)
    if path.exists():
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_base64 = get_base64_of_bin_file("Logo-Badan-Pusat-Statistik-BPS.png")
logo_src = f"data:image/png;base64,{logo_base64}" if logo_base64 else "https://upload.wikimedia.org/wikipedia/commons/e/e0/Logo_BPS.png"

# ================= CSS YANG SUDAH DIPERBAIKI =================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

    * {{
        font-family: 'Inter', sans-serif;
    }}

    /* BACKGROUND MESH GRADIENT - BIRU, ORANGE, HIJAU */
    .stApp {{
        background: #071426;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(66,165,245,0.35) 0%, rgba(66,165,245,0) 55%),
            radial-gradient(circle at 90% 30%, rgba(255,167,38,0.35) 0%, rgba(255,167,38,0) 55%),
            radial-gradient(circle at 50% 80%, rgba(102,187,106,0.35) 0%, rgba(102,187,106,0) 55%);
        background-attachment: fixed;
    }}

    /* HEADER - LOGO BESAR & JARAK RAPAT */
    .header-box {{
        text-align: center;
        padding: 2rem 1rem 1rem;
        animation: fadeIn 0.7s ease;
    }}
    .bps-logo {{
        width: 160px;
        filter: drop-shadow(0 8px 20px rgba(0,0,0,0.25));
        margin-bottom: 0.25rem;
        transition: transform 0.2s;
    }}
    .bps-logo:hover {{
        transform: scale(1.02);
    }}
    .main-title {{
        font-size: 3.8rem;
        font-weight: 800;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #64B5F6, #FFB74D, #81C784);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        line-height: 1.2;
        text-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .sub-title {{
        font-size: 1.2rem;
        color: #E2E8F0;
        font-weight: 500;
        margin-top: 0.2rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }}
    .badge {{
        display: inline-block;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(12px);
        padding: 0.3rem 1.2rem;
        border-radius: 40px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #F1F5F9;
        margin-top: 0.8rem;
        border: 1px solid rgba(255,255,255,0.2);
    }}

    /* CARD GLASSMORPHISM */
    .card-modern {{
        background: rgba(10, 25, 47, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 2rem;
        padding: 2rem 1.8rem;
        box-shadow: 0 20px 35px -10px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.12);
        transition: all 0.35s cubic-bezier(0.2, 0.9, 0.4, 1.1);
        height: 100%;
    }}
    .card-modern:hover {{
        transform: translateY(-8px);
        background: rgba(15, 35, 60, 0.8);
        border-color: rgba(255,255,255,0.25);
        box-shadow: 0 30px 45px -12px rgba(0,0,0,0.5);
    }}
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2));
    }}
    .card-title {{
        font-size: 1.9rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0.75rem;
    }}
    .title-stat {{
        background: linear-gradient(135deg, #64B5F6, #2196F3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .title-iph {{
        background: linear-gradient(135deg, #FFB74D, #FF9800);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .card-desc {{
        color: #CBD5E1;
        line-height: 1.5;
        font-size: 0.95rem;
        margin-bottom: 1.8rem;
    }}

    /* TOMBOL */
    .stLinkButton > a {{
        width: 100% !important;
        padding: 0.85rem 0 !important;
        border-radius: 3rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        border: none !important;
        cursor: pointer !important;
        letter-spacing: 0.5px;
        color: white !important;
        box-shadow: 0 6px 14px rgba(0,0,0,0.35) !important;
    }}
    div[data-testid="column"]:first-child .stLinkButton > a {{
        background: linear-gradient(95deg, #0D47A1, #1565C0) !important;
        border-bottom: 2px solid #42A5F5 !important;
    }}
    div[data-testid="column"]:first-child .stLinkButton > a:hover {{
        background: linear-gradient(95deg, #1565C0, #1E88E5) !important;
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 12px 22px rgba(33,150,243,0.5) !important;
    }}
    div[data-testid="column"]:last-child .stLinkButton > a {{
        background: linear-gradient(95deg, #BF360C, #E65100) !important;
        border-bottom: 2px solid #FFB74D !important;
    }}
    div[data-testid="column"]:last-child .stLinkButton > a:hover {{
        background: linear-gradient(95deg, #E65100, #FB8C00) !important;
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 12px 22px rgba(255,152,0,0.5) !important;
    }}

    /* FOOTER */
    .footer {{
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: #94A3B8;
        font-size: 0.8rem;
        border-top: 1px solid rgba(255,255,255,0.08);
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(15px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* HIDE DEFAULT STREAMLIT */
    #MainMenu, footer, .stDeployButton {{
        visibility: hidden;
    }}
    header {{
        background: transparent !important;
    }}
    .stApp header {{
        background-color: transparent !important;
    }}
    p, h1, h2, h3, h4, h5, h6, span, div {{
        color: #F1F5F9;
    }}
</style>
""", unsafe_allow_html=True)

# ================= KONTEN =================
st.markdown(f"""
<div class="header-box">
    <img src="{logo_src}" class="bps-logo">
    <h1 class="main-title">BPS KOTA BATU</h1>
    <p class="sub-title">Sistem Informasi & Monitoring Terpadu</p>
    <div class="badge">⚡ Integrasi • Digitalisasi • Analisis ⚡</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="card-modern">
        <div class="card-icon">📊</div>
        <div class="card-title title-stat">Dashboard Statistik</div>
        <div class="card-desc">
            Visualisasi data statistik Kota Batu secara otomatis.<br>
            Grafik interaktif, filter dinamis, dan unduh laporan.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Buka Dashboard Statistik", 
                   "https://dashboardbatu-ka64nijfnekqtwwmpq4qgd.streamlit.app/", 
                   use_container_width=True)

with col2:
    st.markdown("""
    <div class="card-modern">
        <div class="card-icon">📈</div>
        <div class="card-title title-iph">Monitoring IPH</div>
        <div class="card-desc">
            Pantau Indeks Perkembangan Harga (IPH) secara real-time.<br>
            Analisis inflasi untuk kebijakan TPID Kota Batu.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Buka Dashboard IPH", 
                   "https://dashboard-iph-kota-batu-cwg5au63betgavnrt2lmpk.streamlit.app/", 
                   use_container_width=True)

st.markdown("""
<div class="footer">
    © 2026 BPS Kota Batu - Intern Project | Membangun Data, Mencerdaskan Bangsa
</div>
""", unsafe_allow_html=True)