# ===== FICHIER : pages/formation.py =====
import streamlit as st
from data.formations_data import formations, certifications

def render():
    """Page formation"""
    st.markdown('<div class="section-header"><h2>🎓 Formation Académique</h2></div>', unsafe_allow_html=True)
    
    for formation in formations:
        st.markdown(f"""
        <div class="experience-card">
            <h3>📚 {formation['diplome']}</h3>
            <h4>🏫 {formation['etablissement']}</h4>
            <p><strong>📅 Période :</strong> {formation['periode']}</p>
            <p><strong>📍 Lieu :</strong> {formation['lieu']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header"><h2>🏆 Cours et Certifications</h2></div>', unsafe_allow_html=True)
    
    for cert in certifications:
        st.markdown(f"""
        <div class="project-card">
            <h4>🏅 {cert['nom']}</h4>
            <p><strong>🏢 Organisme :</strong> {cert['organisme']}</p>
            <p><strong>📅 Date :</strong> {cert['date']}</p>
        </div>
        """, unsafe_allow_html=True)