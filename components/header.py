# ===== FICHIER : components/header.py =====
import streamlit as st

def render_header(personal_info):
    """Rendu du header principal"""
    st.markdown(f"""
    <div class="main-header">
        <h1>👨‍💻 {personal_info['nom']}</h1>
        <h3>{personal_info['titre']}</h3>
        <p>📧 {personal_info['email']} | 📱 {personal_info['telephone']} | 🎂 {personal_info['age']} | 📍 {personal_info['ville']}</p>
    </div>
    """, unsafe_allow_html=True)