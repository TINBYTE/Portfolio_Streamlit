# ===== FICHIER : pages/competences.py =====
import streamlit as st
from data.competences_data import competences, competences_niveaux, tech_utilisation
from utils.charts import create_competences_chart, create_tech_pie_chart

def render():
    """Page compétences"""
    st.markdown('<div class="section-header"><h2>🛠️ Compétences Techniques</h2></div>', unsafe_allow_html=True)
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = create_competences_chart(competences_niveaux)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = create_tech_pie_chart(tech_utilisation)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Détail des compétences
    st.markdown("### 💻 Langages de programmation & Développement logiciel")
    for lang in competences["langages"]:
        st.markdown(f'<span class="skill-badge">{lang}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🎨 Développement Front-End")
    for tech in competences["frontend"]:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Développement Back-End")
    for tech in competences["backend"]:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Data Science & Analyse de Données")
    for tech in competences["datascience"]:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🗄️ Bases de données")
    for db in competences["databases"]:
        st.markdown(f'<span class="skill-badge">{db}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🔧 Outils & Autres")
    for outil in competences["outils"]:
        st.markdown(f'<span class="skill-badge">{outil}</span>', unsafe_allow_html=True)
