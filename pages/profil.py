# ===== FICHIER : pages/profil.py =====
import streamlit as st
from data.personal_data import soft_skills

def render():
    """Page profil"""
    st.markdown('<div class="section-header"><h2>👤 Profil Détaillé</h2></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>🎂 Âge</h4>
            <h2>25 ans</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📍 Localisation</h4>
            <h3>Tinghir, Maroc</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>🎓 Niveau</h4>
            <h3>Master en cours</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h4>💼 Statut</h4>
            <h3>Junior</h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Soft Skills")
    for skill in soft_skills:
        st.markdown(f'<span class="skill-badge">✨ {skill}</span>', unsafe_allow_html=True)
