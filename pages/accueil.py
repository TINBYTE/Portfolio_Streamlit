# ===== FICHIER : pages/accueil.py =====
import streamlit as st
from data.personal_data import profil_professionnel, reseaux_sociaux

def render():
    """Page d'accueil avec design moderne et responsive"""
    
    # Hero section avec animation
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Bienvenue sur mon Portfolio</h1>
            <p class="hero-subtitle">Découvrez mon parcours professionnel et mes réalisations</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Espacement
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    # Layout principal
    col1, col2 = st.columns([3, 2], gap="large")
    
    with col1:
        # Section profil professionnel
        st.markdown("""
        <div class="section-container">
            <div class="section-header">
                <div class="section-icon">👨‍💻</div>
                <h2>Profil Professionnel</h2>
            </div>
            <div class="profile-card">
                <div class="profile-content">
                    <p class="profile-text">{}</p>
                </div>
                <div class="profile-highlight">
                    <span class="highlight-text">🚀 Prêt pour de nouveaux défis</span>
                </div>
            </div>
        </div>
        """.format(profil_professionnel), unsafe_allow_html=True)
    
    with col2:
        # Section réseaux sociaux
        st.markdown("""
        <div class="section-container">
            <div class="section-header">
                <div class="section-icon">🌐</div>
                <h2>Mes Réseaux</h2>
            </div>
            <div class="social-container">
        """, unsafe_allow_html=True)
        
        # LinkedIn
        st.markdown(f"""
        <div class="social-card linkedin">
            <div class="social-icon">💼</div>
            <div class="social-content">
                <h4>LinkedIn</h4>
                <a href="{reseaux_sociaux['linkedin']}" target="_blank" class="social-link">
                    Profil Professionnel
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # YouTube
        st.markdown(f"""
        <div class="social-card youtube">
            <div class="social-icon">📺</div>
            <div class="social-content">
                <h4>YouTube</h4>
                <a href="{reseaux_sociaux['youtube']}" target="_blank" class="social-link">
                    @BYDEVMAR
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Website
        st.markdown(f"""
        <div class="social-card website">
            <div class="social-icon">📝</div>
            <div class="social-content">
                <h4>Blog</h4>
                <a href="{reseaux_sociaux['website']}" target="_blank" class="social-link">
                    Articles Medium
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # GitHub
        st.markdown(f"""
        <div class="social-card github">
            <div class="social-icon">💻</div>
            <div class="social-content">
                <h4>GitHub</h4>
                <div class="github-links">
                    <a href="https://github.com/BYDEVMAR" target="_blank" class="social-link">
                        {reseaux_sociaux['github'][0]}
                    </a>
                    <span class="separator">|</span>
                    <a href="https://github.com/TINBYTE" target="_blank" class="social-link">
                        {reseaux_sociaux['github'][1]}
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Call to action section
    st.markdown("""
    <div class="cta-section">
        <div class="cta-content">
            <h3>Intéressé par une collaboration ?</h3>
            <p>N'hésitez pas à me contacter pour discuter de vos projets</p>
        </div>
    </div>
    """, unsafe_allow_html=True)