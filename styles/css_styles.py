# ===== FICHIER : styles/css_styles.py =====
import streamlit as st

def load_custom_css():
    """Chargement des styles CSS personnalisés modernes avec animations"""
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Variables CSS */
        :root {
            --primary-color: #2563eb;
            --secondary-color: #3b82f6;
            --accent-color: #06b6d4;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            --dark-color: #1f2937;
            --light-color: #f8fafc;
            --gray-color: #6b7280;
            --border-radius: 12px;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Reset et base */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
            padding: 3rem 2rem;
            border-radius: var(--border-radius);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/></pattern></defs><rect width="100" height="20" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            text-align: center;
            color: white;
        }
        
        .hero-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            animation: fadeInUp 0.8s ease-out;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            font-weight: 400;
            opacity: 0.9;
            animation: fadeInUp 0.8s ease-out 0.2s both;
        }
        
        /* Section Container */
        .section-container {
            margin-bottom: 2rem;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: linear-gradient(135deg, var(--dark-color) 0%, var(--gray-color) 100%);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
        }
        
        .section-header:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .section-icon {
            font-size: 2rem;
            opacity: 0.9;
        }
        
        .section-header h2 {
            margin: 0;
            font-size: 1.5rem;
            font-weight: 600;
        }
        
        /* Profile Card */
        .profile-card {
            background: white;
            border-radius: var(--border-radius);
            padding: 2rem;
            box-shadow: var(--shadow-md);
            border: 1px solid #e5e7eb;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }
        
        .profile-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, var(--primary-color), var(--accent-color));
        }
        
        .profile-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        .profile-content {
            margin-bottom: 1.5rem;
        }
        
        .profile-text {
            font-size: 1.1rem;
            line-height: 1.7;
            color: var(--dark-color);
            margin: 0;
        }
        
        .profile-highlight {
            background: linear-gradient(135deg, #ecfdf5, #d1fae5);
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid var(--success-color);
        }
        
        .highlight-text {
            color: var(--success-color);
            font-weight: 600;
            font-size: 1rem;
        }
        
        /* Social Cards */
        .social-container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        .social-card {
            background: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            border: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            gap: 1rem;
            transition: var(--transition);
            cursor: pointer;
        }
        
        .social-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .social-card.linkedin {
            border-left: 4px solid #0077b5;
        }
        
        .social-card.youtube {
            border-left: 4px solid #ff0000;
        }
        
        .social-card.website {
            border-left: 4px solid #00ab6c;
        }
        
        .social-card.github {
            border-left: 4px solid #333333;
        }
        
        .social-icon {
            font-size: 1.5rem;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8fafc;
            border-radius: 50%;
        }
        
        .social-content h4 {
            margin: 0 0 0.5rem 0;
            font-size: 1rem;
            font-weight: 600;
            color: var(--dark-color);
        }
        
        .social-link {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
            transition: var(--transition);
        }
        
        .social-link:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }
        
        .github-links {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .separator {
            color: var(--gray-color);
            font-weight: 300;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 2rem;
            border-radius: var(--border-radius);
            text-align: center;
            margin-top: 2rem;
            border: 1px solid #e2e8f0;
        }
        
        .cta-content h3 {
            color: var(--dark-color);
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .cta-content p {
            color: var(--gray-color);
            font-size: 1rem;
            margin: 0;
        }
        
        /* Utility Classes */
        .spacer {
            height: 1rem;
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .hero-subtitle {
                font-size: 1rem;
            }
            
            .section-header {
                flex-direction: column;
                text-align: center;
                gap: 0.5rem;
            }
            
            .social-card {
                flex-direction: column;
                text-align: center;
            }
            
            .github-links {
                justify-content: center;
            }
        }
        
        /* Skill badges améliorés */
        .skill-badge {
            display: inline-block;
            background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
            color: var(--primary-color);
            padding: 0.5rem 1rem;
            margin: 0.25rem;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid #bae6fd;
            transition: var(--transition);
            cursor: default;
        }
        
        .skill-badge:hover {
            background: linear-gradient(135deg, #e0f2fe, #bae6fd);
            transform: translateY(-1px);
            box-shadow: var(--shadow-sm);
        }
        
        /* Cards génériques améliorées */
        .experience-card, .project-card {
            background: white;
            padding: 2rem;
            border-radius: var(--border-radius);
            margin: 1.5rem 0;
            box-shadow: var(--shadow-md);
            border: 1px solid #e5e7eb;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }
        
        .experience-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--primary-color);
        }
        
        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--warning-color);
        }
        
        .experience-card:hover, .project-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        /* Contact info amélioré */
        .contact-info {
            background: linear-gradient(135deg, #f0fdf4, #dcfce7);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            margin: 1rem 0;
            border: 1px solid #bbf7d0;
            border-left: 4px solid var(--success-color);
        }
        
        /* Metric cards */
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            border: 1px solid #e5e7eb;
            border-left: 4px solid var(--success-color);
            transition: var(--transition);
        }
        
        .metric-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
    </style>
    """, unsafe_allow_html=True)

