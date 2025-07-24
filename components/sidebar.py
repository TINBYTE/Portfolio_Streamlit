# ===== FICHIER : components/sidebar.py =====
import streamlit as st

def render_sidebar():
    """Rendu de la sidebar avec navigation et métriques"""
    st.sidebar.title("🧭 Navigation")
    sections = [
        "🏠 Accueil",
        "👤 Profil",
        "💼 Expériences",
        "🎓 Formation",
        "💻 Projets",
        "🛠️ Compétences",
        "🌍 Langues",
        "📞 Contact"
    ]
    
    selected_section = st.sidebar.selectbox("Choisir une section:", sections)
    
    # Métriques rapides
    st.sidebar.markdown("### 📊 Aperçu rapide")
    st.sidebar.metric("Années d'expérience", "2+")
    st.sidebar.metric("Projets réalisés", "4+")
    st.sidebar.metric("Technologies maîtrisées", "20+")
    st.sidebar.metric("Langues parlées", "5")
    
    return selected_section
