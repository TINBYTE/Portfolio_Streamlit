# ===== FICHIER : pages/contact.py =====
import streamlit as st
from data.personal_data import personal_info, reseaux_sociaux

def render():
    """Page contact"""
    st.markdown('<div class="section-header"><h2>📞 Informations de Contact</h2></div>', unsafe_allow_html=true)