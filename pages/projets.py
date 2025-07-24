# ===== FICHIER : pages/projets.py =====
import streamlit as st
from data.projets_data import projets

def render():
    """Page projets"""
    st.markdown('<div class="section-header"><h2>💻 Projets Réalisés</h2></div>', unsafe_allow_html=True)
    
    for projet in projets:
        st.markdown(f"""
        <div class="project-card">
            <h3>🚀 {projet['nom']}</h3>
            <p><strong>🛠️ Technologies :</strong> {projet['technologies']}</p>
            <p><strong>📝 Description :</strong> {projet['description']}</p>
            
            <h4>⭐ Fonctionnalités :</h4>
            <ul>
        """, unsafe_allow_html=True)
        
        for fonc in projet['fonctionnalites']:
            st.markdown(f"<li>{fonc}</li>", unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
