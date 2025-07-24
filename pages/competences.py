# ===== pages/competences.py =====
import streamlit as st
import pandas as pd
from data.competences_data import (
    competences_categories, 
    competences_niveaux, 
    tech_utilisation,
    certifications,
    skills_stats,
    domaines_application
)
from utils.charts import create_competences_chart, create_tech_pie_chart

def render():
    """Page compétences améliorée avec design moderne"""
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">🛠️ Compétences Techniques</h1>
            <p class="hero-subtitle">Un aperçu complet de mes expertises en développement et technologies</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistiques générales
    render_skills_stats()
    
    # Graphiques de performance
    render_charts_section()
    
    # Compétences détaillées par catégorie
    render_detailed_skills()
    
    # Certifications
    render_certifications()
    
    # Domaines d'application
    render_application_domains()

def render_skills_stats():
    """Affichage des statistiques générales"""
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-icon">📈</span>
            <h2>Statistiques Générales</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Métriques en colonnes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--primary-color); margin-bottom: 0.5rem;">💻</div>
                <div style="font-size: 2rem; font-weight: 700; color: var(--dark-color); margin-bottom: 0.5rem;">{skills_stats['total_langages']}</div>
                <div style="color: var(--gray-color); font-size: 0.9rem;">Langages</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--success-color); margin-bottom: 0.5rem;">🔧</div>
                <div style="font-size: 2rem; font-weight: 700; color: var(--dark-color); margin-bottom: 0.5rem;">{skills_stats['total_frameworks']}</div>
                <div style="color: var(--gray-color); font-size: 0.9rem;">Frameworks</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--warning-color); margin-bottom: 0.5rem;">📅</div>
                <div style="font-size: 2rem; font-weight: 700; color: var(--dark-color); margin-bottom: 0.5rem;">{skills_stats['annees_experience']}</div>
                <div style="color: var(--gray-color); font-size: 0.9rem;">Années d'expérience</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--accent-color); margin-bottom: 0.5rem;">🏆</div>
                <div style="font-size: 2rem; font-weight: 700; color: var(--dark-color); margin-bottom: 0.5rem;">{skills_stats['projets_realises']}</div>
                <div style="color: var(--gray-color); font-size: 0.9rem;">Projets réalisés</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_charts_section():
    """Section des graphiques"""
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-icon">📊</span>
            <h2>Analyse des Compétences</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig1 = create_competences_chart(competences_niveaux)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig2 = create_tech_pie_chart(tech_utilisation)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_detailed_skills():
    """Affichage détaillé des compétences par catégorie"""
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-icon">🎯</span>
            <h2>Compétences Détaillées</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Création de tabs pour une meilleure organisation
    tab_names = list(competences_categories.keys())
    tab_titles = [competences_categories[key]["title"] for key in tab_names]
    
    tabs = st.tabs([f"{competences_categories[key]['icon']} {competences_categories[key]['title']}" 
                    for key in tab_names])
    
    for i, (tab, category_key) in enumerate(zip(tabs, tab_names)):
        with tab:
            render_skill_category(category_key, competences_categories[category_key])

def render_skill_category(category_key, category_data):
    """Rendu d'une catégorie de compétences"""
    
    # En-tête de catégorie avec niveau global
    st.markdown(f"""
    <div class="category-header">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0; color: var(--dark-color);">{category_data['icon']} {category_data['title']}</h3>
                <p style="margin: 0.5rem 0 0 0; color: var(--gray-color); font-size: 0.9rem;">{category_data['description']}</p>
            </div>
            <div class="level-indicator">
                <div style="font-size: 1.5rem; font-weight: 700; color: var(--primary-color);">{category_data['level']}%</div>
                <div style="font-size: 0.8rem; color: var(--gray-color);">Niveau global</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Barre de progression pour le niveau global
    render_progress_bar(category_data['level'])
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    # Liste des compétences avec détails
    for skill in category_data['skills']:
        render_skill_item(skill)

def render_skill_item(skill):
    """Rendu d'une compétence individuelle"""
    
    # Couleur basée sur le niveau
    level_colors = {
        "Expert": "var(--success-color)",
        "Avancé": "var(--primary-color)", 
        "Intermédiaire": "var(--warning-color)",
        "Débutant": "var(--gray-color)"
    }
    
    color = level_colors.get(skill['level'], "var(--gray-color)")
    rating_stars = "⭐" * skill['rating']
    
    st.markdown(f"""
    <div class="skill-item">
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: white; border-radius: 8px; border: 1px solid #e5e7eb; margin: 0.5rem 0; transition: var(--transition);">
            <div style="flex-grow: 1;">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;">
                    <span style="font-weight: 600; color: var(--dark-color); font-size: 1rem;">{skill['name']}</span>
                    <span style="background: {color}; color: white; padding: 0.2rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: 500;">{skill['level']}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; font-size: 0.9rem; color: var(--gray-color);">
                    <span>📅 {skill['years']} années</span>
                    <span>{rating_stars}</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_progress_bar(level):
    """Barre de progression pour le niveau"""
    st.markdown(f"""
    <div style="background: #f1f5f9; border-radius: 10px; height: 8px; margin: 1rem 0; overflow: hidden;">
        <div style="background: linear-gradient(90deg, var(--primary-color), var(--accent-color)); height: 100%; width: {level}%; border-radius: 10px; transition: var(--transition);"></div>
    </div>
    """, unsafe_allow_html=True)

def render_certifications():
    """Section des certifications"""
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-icon">🏆</span>
            <h2>Certifications & Formations</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage des certifications en grid
    cols = st.columns(2)
    
    for i, cert in enumerate(certifications):
        with cols[i % 2]:
            render_certification_card(cert)

def render_certification_card(cert):
    """Carte de certification"""
    
    status_colors = {
        "obtenu": "var(--success-color)",
        "en_cours": "var(--warning-color)", 
        "planifie": "var(--gray-color)"
    }
    
    status_labels = {
        "obtenu": "✅ Obtenu",
        "en_cours": "🔄 En cours",
        "planifie": "📅 Planifié"
    }
    
    color = status_colors.get(cert['status'], "var(--gray-color)")
    label = status_labels.get(cert['status'], cert['status'])
    
    st.markdown(f"""
    <div class="certification-card">
        <div style="background: white; padding: 1.5rem; border-radius: var(--border-radius); border: 1px solid #e5e7eb; margin: 1rem 0; border-left: 4px solid {color}; transition: var(--transition);">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">{cert['icon']}</span>
                <div>
                    <h4 style="margin: 0; color: var(--dark-color); font-size: 1.1rem; font-weight: 600;">{cert['name']}</h4>
                    <p style="margin: 0.5rem 0 0 0; color: var(--gray-color); font-size: 0.9rem;">{cert['issuer']} • {cert['date']}</p>
                </div>
            </div>
            <div style="display: flex; justify-content: flex-end;">
                <span style="background: {color}; color: white; padding: 0.3rem 1rem; border-radius: 15px; font-size: 0.8rem; font-weight: 500;">{label}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_application_domains():
    """Section des domaines d'application"""
    st.markdown("""
    <div class="section-container">
        <div class="section-header">
            <span class="section-icon">🚀</span>
            <h2>Domaines d'Application</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage des domaines en grid
    cols = st.columns(2)
    
    domain_keys = list(domaines_application.keys())
    for i, domain_key in enumerate(domain_keys):
        with cols[i % 2]:
            render_domain_card(domain_key, domaines_application[domain_key])

def render_domain_card(domain_key, domain_data):
    """Carte de domaine d'application"""
    
    st.markdown(f"""
    <div class="domain-card">
        <div style="background: white; padding: 2rem; border-radius: var(--border-radius); border: 1px solid #e5e7eb; margin: 1rem 0; transition: var(--transition); height: 100%;">
            <div style="margin-bottom: 1.5rem;">
                <h4 style="margin: 0 0 0.5rem 0; color: var(--dark-color); font-size: 1.2rem; font-weight: 600;">{domain_data['title']}</h4>
                <div style="background: linear-gradient(90deg, var(--primary-color), var(--accent-color)); height: 4px; width: 40px; border-radius: 2px; margin-bottom: 1rem;"></div>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.9rem; color: var(--gray-color);">Niveau de maîtrise</span>
                    <span style="font-weight: 600; color: var(--primary-color);">{domain_data['niveau']}%</span>
                </div>
                <div style="background: #f1f5f9; border-radius: 10px; height: 6px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, var(--primary-color), var(--accent-color)); height: 100%; width: {domain_data['niveau']}%; border-radius: 10px;"></div>
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <p style="font-size: 0.9rem; color: var(--gray-color); margin: 0 0 0.5rem 0;">Technologies principales:</p>
                <div>
                    {"".join([f'<span style="display: inline-block; background: #f0f9ff; color: var(--primary-color); padding: 0.3rem 0.8rem; margin: 0.2rem; border-radius: 15px; font-size: 0.8rem; border: 1px solid #bae6fd;">{tech}</span>' for tech in domain_data['technologies'][:4]])}
                </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
                <span style="font-size: 0.9rem; color: var(--gray-color);">📊 {domain_data['projets']} projets réalisés</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)