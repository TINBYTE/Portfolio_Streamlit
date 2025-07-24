# ===== CORRECTION : pages/langues.py =====
import streamlit as st
import pandas as pd
from data.langues_data import langues_data
from utils.charts import create_langues_chart

def render():
    """Page langues"""
    st.markdown('<div class="section-header"><h2>🌍 Compétences Linguistiques</h2></div>', unsafe_allow_html=True)
    
    # Graphique des langues
    fig = create_langues_chart(langues_data)
    st.plotly_chart(fig, use_container_width=True)
    
    # Détails des langues
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="experience-card">
            <h3>🏠 Langues Maternelles</h3>
            <p><strong>🇲🇦 Arabe :</strong> Langue maternelle</p>
            <p><strong>🏔️ Tamazight :</strong> Langue maternelle</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="experience-card">
            <h3>💼 Langues Professionnelles</h3>
            <p><strong>🇫🇷 Français :</strong> Compétence professionnelle</p>
            <p><strong>🇬🇧 Anglais :</strong> Compétence professionnelle</p>
            <p><strong>🇪🇸 Espagnol :</strong> Compétence professionnelle</p>
        </div>
        """, unsafe_allow_html=True)