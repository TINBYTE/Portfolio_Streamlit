# ===== CORRECTION : main.py =====
import streamlit as st
from config.page_config import setup_page_config
from styles.css_styles import load_custom_css
from data.personal_data import personal_info
from components.header import render_header
from components.sidebar import render_sidebar
from components.footer import render_footer

# Import correct des modules pages
from pages import accueil, profil, experiences, formation, projets, competences, langues, contact

def main():
    # Configuration de la page
    setup_page_config()
    
    # Chargement des styles CSS
    load_custom_css()
    
    # Header principal
    render_header(personal_info)
    
    # Sidebar avec navigation
    selected_section = render_sidebar()
    
    # Navigation vers les différentes pages
    page_mapping = {
        "🏠 Accueil": accueil.render,
        "👤 Profil": profil.render,
        "💼 Expériences": experiences.render,
        "🎓 Formation": formation.render,
        "💻 Projets": projets.render,
        "🛠️ Compétences": competences.render,
        "🌍 Langues": langues.render,
        "📞 Contact": contact.render
    }
    
    # Rendu de la page sélectionnée
    if selected_section in page_mapping:
        page_mapping[selected_section]()
    
    # Footer
    render_footer()

if __name__ == "__main__":
    main()