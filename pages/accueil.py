# ===== FICHIER : pages/accueil.py =====
import streamlit as st
from data.personal_data import profil_professionnel, reseaux_sociaux

def render():
    """Page d'accueil"""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="section-header"><h2>🎯 Profil Professionnel</h2></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="experience-card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
        {profil_professionnel}
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header"><h2>🔗 Réseaux Sociaux</h2></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="contact-info">
        <p><strong>🔗 LinkedIn:</strong><br>
        <a href="{reseaux_sociaux['linkedin']}" target="_blank">linkedin.com/in/bouhlaliabdelfattah</a></p>
        
        <p><strong>📺 YouTube:</strong><br>
        <a href="{reseaux_sociaux['youtube']}" target="_blank">@BYDEVMAR</a></p>
        
        <p><strong>📝 Website:</strong><br>
        <a href="{reseaux_sociaux['website']}" target="_blank">medium.com/@bouhlali99abdelfattah</a></p>
        
        <p><strong>💻 GitHub:</strong><br>
        <a href="https://github.com/BYDEVMAR" target="_blank">{reseaux_sociaux['github'][0]}</a> | 
        <a href="https://github.com/TINBYTE" target="_blank">{reseaux_sociaux['github'][1]}</a></p>
        </div>
        """, unsafe_allow_html=True)