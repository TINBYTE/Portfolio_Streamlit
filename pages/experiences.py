# ===== FICHIER : pages/experiences.py =====
import streamlit as st
from data.experiences_data import experiences

def render():
    """Page expériences"""
    st.markdown('<div class="section-header"><h2>💼 Expériences Professionnelles</h2></div>', unsafe_allow_html=True)
    
    for exp in experiences:
        st.markdown(f"""
        <div class="experience-card">
            <h3>🏢 {exp['titre']}</h3>
            <h4>{exp['entreprise']} | {exp['periode']}</h4>
            <h5>📍 {exp['lieu']}</h5>
            
            <h4>🎯 Missions réalisées :</h4>
            <ul>
        """, unsafe_allow_html=True)
        
        for mission in exp['missions']:
            st.markdown(f"<li>{mission}</li>", unsafe_allow_html=True)
        
        st.markdown("<h4>🛠️ Technologies utilisées :</h4>", unsafe_allow_html=True)
        for tech in exp['technologies']:
            st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
