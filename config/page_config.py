# ===== FICHIER : config/page_config.py =====
import streamlit as st

def setup_page_config():
    """Configuration de la page Streamlit"""
    st.set_page_config(
        page_title="CV - Abdelfattah BOUHLALI",
        page_icon="👨‍💻",
        layout="wide",
        initial_sidebar_state="expanded"
    )
