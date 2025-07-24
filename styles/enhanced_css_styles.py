# ===== styles/enhanced_css_styles.py =====
import streamlit as st

def load_enhanced_competences_css():
    """CSS amélioré spécifiquement pour la page compétences"""
    st.markdown("""
    <style>
        /* CSS supplémentaire pour la page compétences */
        
        /* Chart containers */
        .chart-container {
            background: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            border: 1px solid #e5e7eb;
            margin: 1rem 0;
            transition: var(--transition);
        }
        
        .chart-container:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        /* Category headers */
        .category-header {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            border: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }
        
        .level-indicator {
            text-align: center;
            background: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: var(--shadow-sm);
        }
        
        /* Skill items */
        .skill-item {
            margin: 0.5rem 0;
        }
        
        .skill-item > div:hover {
            transform: translateX(4px);
            box-shadow: var(--shadow-md);
            border-color: var(--primary-color);
        }
        
        /* Certification cards */
        .certification-card > div:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        /* Domain cards */
        .domain-card > div:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        /* Améliorations des tabs Streamlit */
        .stTabs [data-baseweb="tab-list"] {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-radius: var(--border-radius);
            padding: 0.5rem;
            margin-bottom: 2rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border: none;
            border-radius: 8px;
            color: var(--gray-color);
            font-weight: 500;
            padding: 0.75rem 1.5rem;
            margin: 0 0.25rem;
            transition: var(--transition);
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(37, 99, 235, 0.1);
            color: var(--primary-color);
        }
        
        .stTabs [aria-selected="true"] {
            background: white !important;
            color: var(--primary-color) !important;
            box-shadow: var(--shadow-sm);
            font-weight: 600;
        }
        
        /* Responsive grid pour les métriques */
        @media (max-width: 768px) {
            .metric-card {
                margin-bottom: 1rem;
            }
            
            .skill-item > div {
                flex-direction: column;
                align-items: flex-start !important;
            }
            
            .skill-item > div > div:first-child > div:first-child {
                flex-direction: column;
                align-items: flex-start !important;
                gap: 0.5rem !important;
            }
        }
        
        /* Animations pour les barres de progression */
        @keyframes progressAnimation {
            from {
                width: 0%;
            }
            to {
                width: var(--target-width);
            }
        }
        
        /* Style pour les badges de compétences améliorés */
        .enhanced-skill-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
            color: var(--primary-color);
            padding: 0.6rem 1.2rem;
            margin: 0.3rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid #bae6fd;
            transition: var(--transition);
            cursor: pointer;
        }
        
        .enhanced-skill-badge:hover {
            background: linear-gradient(135deg, #e0f2fe, #bae6fd);
            transform: translateY(-1px) scale(1.02);
            box-shadow: var(--shadow-md);
        }
        
        .enhanced-skill-badge .badge-level {
            background: var(--primary-color);
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 10px;
            font-size: 0.7rem;
            font-weight: 600;
        }
        
        /* Loading animation pour les éléments */
        .fade-in {
            animation: fadeInUp 0.6s ease-out;
        }
        
        .fade-in-delay-1 {
            animation: fadeInUp 0.6s ease-out 0.1s both;
        }
        
        .fade-in-delay-2 {
            animation: fadeInUp 0.6s ease-out 0.2s both;
        }
        
        .fade-in-delay-3 {
            animation: fadeInUp 0.6s ease-out 0.3s both;
        }
        
        /* Effet de brillance sur les cartes importantes */
        .shine-effect {
            position: relative;
            overflow: hidden;
        }
        
        .shine-effect::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: var(--transition);
            transform: translateX(-100%) translateY(-100%) rotate(45deg);
        }
        
        .shine-effect:hover::after {
            transform: translateX(100%) translateY(100%) rotate(45deg);
        }
        
        /* Indicateurs visuels pour les niveaux */
        .level-indicator-expert {
            background: linear-gradient(135deg, var(--success-color), #059669);
        }
        
        .level-indicator-advanced {
            background: linear-gradient(135deg, var(--primary-color), #1d4ed8);
        }
        
        .level-indicator-intermediate {
            background: linear-gradient(135deg, var(--warning-color), #d97706);
        }
        
        .level-indicator-beginner {
            background: linear-gradient(135deg, var(--gray-color), #4b5563);
        }
    </style>
    """, unsafe_allow_html=True)

# Fonction pour combiner avec les styles existants
def load_all_competences_styles():
    """Charge tous les styles pour la page compétences"""
    from styles.css_styles import load_custom_css
    load_custom_css()
    load_enhanced_competences_css()