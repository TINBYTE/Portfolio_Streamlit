import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="CV - Abdelfattah BOUHLALI",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 1rem 0;
    }
    
    .skill-badge {
        display: inline-block;
        background: #e1f5fe;
        color: #01579b;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        border: 1px solid #b3e5fc;
    }
    
    .experience-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .project-card {
        background: #fff3e0;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .contact-info {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

# Données du CV
personal_info = {
    "nom": "Abdelfattah BOUHLALI",
    "titre": "SOFTWARE ENGINEER - JUNIOR DATA SCIENTIST",
    "email": "bouhlali2407@gmail.com",
    "telephone": "0680483608",
    "age": "25 ans",
    "ville": "TINGHIR, MAROC"
}

# Header principal
st.markdown(f"""
<div class="main-header">
    <h1>👨‍💻 {personal_info['nom']}</h1>
    <h3>{personal_info['titre']}</h3>
    <p>📧 {personal_info['email']} | 📱 {personal_info['telephone']} | 🎂 {personal_info['age']} | 📍 {personal_info['ville']}</p>
</div>
""", unsafe_allow_html=True)

# Sidebar avec navigation
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

# Métriques rapides dans la sidebar
st.sidebar.markdown("### 📊 Aperçu rapide")
st.sidebar.metric("Années d'expérience", "2+")
st.sidebar.metric("Projets réalisés", "4+")
st.sidebar.metric("Technologies maîtrisées", "20+")
st.sidebar.metric("Langues parlées", "5")

# Section Accueil
if selected_section == "🏠 Accueil":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="section-header"><h2>🎯 Profil Professionnel</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="experience-card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
        Ingénieur en logiciel et data scientist junior alliant expertise en développement full-stack et science des données. 
        Spécialisé dans la création de solutions innovantes basées sur l'IA et le machine learning, avec une solide formation 
        en mathématiques appliquées. Passionné par la transformation de défis complexes en solutions concrètes et évolutives.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header"><h2>🔗 Réseaux Sociaux</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="contact-info">
        <p><strong>🔗 LinkedIn:</strong><br>
        <a href="https://www.linkedin.com/in/bouhlaliabdelfattah/" target="_blank">linkedin.com/in/bouhlaliabdelfattah</a></p>
        
        <p><strong>📺 YouTube:</strong><br>
        <a href="https://www.youtube.com/@BYDEVMAR" target="_blank">@BYDEVMAR</a></p>
        
        <p><strong>📝 Website:</strong><br>
        <a href="https://medium.com/@bouhlali99abdelfattah" target="_blank">medium.com/@bouhlali99abdelfattah</a></p>
        
        <p><strong>💻 GitHub:</strong><br>
        <a href="https://github.com/BYDEVMAR" target="_blank">@BYDEVMAR</a> | 
        <a href="https://github.com/TINBYTE" target="_blank">@TINBYTE</a></p>
        </div>
        """, unsafe_allow_html=True)

# Section Profil
elif selected_section == "👤 Profil":
    st.markdown('<div class="section-header"><h2>👤 Profil Détaillé</h2></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>🎂 Âge</h4>
            <h2>25 ans</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📍 Localisation</h4>
            <h3>Tinghir, Maroc</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>🎓 Niveau</h4>
            <h3>Master en cours</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h4>💼 Statut</h4>
            <h3>Junior</h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Soft Skills")
    soft_skills = [
        "Communication efficace", "Résolution de problèmes complexes", 
        "Collaboration et travail en équipe", "Pensée critique et analytique",
        "Gestion efficace du temps", "Apprentissage continu et adaptabilité"
    ]
    
    for skill in soft_skills:
        st.markdown(f'<span class="skill-badge">✨ {skill}</span>', unsafe_allow_html=True)

# Section Expériences
elif selected_section == "💼 Expériences":
    st.markdown('<div class="section-header"><h2>💼 Expériences Professionnelles</h2></div>', unsafe_allow_html=True)
    
    # Expérience 1
    st.markdown("""
    <div class="experience-card">
        <h3>🏢 Développeur Full Stack & Analyste Financier</h3>
        <h4>AUDIT ÉTOILE EXPERTISE | Avril 2023 - Mai 2023</h4>
        <h5>📍 MARRAKECH, MAROC</h5>
        
        <h4>🎯 Missions réalisées :</h4>
        <ul>
            <li><strong>Conception UML :</strong> Modélisation du système de soumission de factures pour garantir une architecture logicielle robuste</li>
            <li><strong>Développement Web Full-Stack :</strong> Création d'une application web utilisant React.js, HTML5, CSS3, Bootstrap4, ExpressJS, et MySQL</li>
            <li><strong>Traitement Comptable :</strong> Analyse et gestion des données financières pour assurer leur conformité aux normes comptables</li>
            <li><strong>Gestion Bancaire :</strong> Saisie et suivi des relevés bancaires pour maintenir des registres précis et à jour</li>
        </ul>
        
        <h4>🛠️ Technologies utilisées :</h4>
        <span class="skill-badge">React.js</span>
        <span class="skill-badge">HTML5</span>
        <span class="skill-badge">CSS3</span>
        <span class="skill-badge">Bootstrap4</span>
        <span class="skill-badge">Express.js</span>
        <span class="skill-badge">MySQL</span>
        <span class="skill-badge">UML</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Expérience 2
    st.markdown("""
    <div class="experience-card">
        <h3>📧 Agent Mailer</h3>
        <h4>CLOUD MARKETING HUB | Mars 2022 - Juin 2022</h4>
        <h5>📍 TANGER, MAROC</h5>
        
        <h4>🎯 Missions réalisées :</h4>
        <ul>
            <li><strong>Création de Campagnes Emailing :</strong> Conception et intégration de templates email en utilisant HTML5, CSS3, et JavaScript</li>
            <li><strong>Tests et Validation :</strong> Réalisation de tests A/B pour optimiser les taux d'ouverture et de clics des campagnes marketing</li>
            <li><strong>Automatisation :</strong> Développement de scripts en Batch Script et iMacros Scripts pour automatiser les processus répétitifs</li>
        </ul>
        
        <h4>🛠️ Technologies utilisées :</h4>
        <span class="skill-badge">HTML5</span>
        <span class="skill-badge">CSS3</span>
        <span class="skill-badge">JavaScript</span>
        <span class="skill-badge">Batch Script</span>
        <span class="skill-badge">iMacros</span>
    </div>
    """, unsafe_allow_html=True)

# Section Formation
elif selected_section == "🎓 Formation":
    st.markdown('<div class="section-header"><h2>🎓 Formation Académique</h2></div>', unsafe_allow_html=True)
    
    formations = [
        {
            "periode": "2023 - En cours",
            "diplome": "Master en Mathématiques Appliquées pour la Science des Données",
            "etablissement": "UNIVERSITÉ IBN ZOHR | FACULTÉ POLYDISCIPLINAIRE",
            "lieu": "OUARZAZATE, MAROC"
        },
        {
            "periode": "2022 - 2023",
            "diplome": "Licence Professionnelle en Informatique et Gestion des Entreprises",
            "etablissement": "UNIVERSITÉ IBN ZOHR | FACULTÉ POLYDISCIPLINAIRE",
            "lieu": "OUARZAZATE, MAROC"
        },
        {
            "periode": "2021 - 2022",
            "diplome": "DEUP en Informatique et Gestion des Entreprises",
            "etablissement": "UNIVERSITÉ IBN ZOHR | FACULTÉ POLYDISCIPLINAIRE",
            "lieu": "OUARZAZATE, MAROC"
        },
        {
            "periode": "2018 - 2020",
            "diplome": "Diplôme Technicien Spécialisé en développement informatique",
            "etablissement": "INSTITUT SPÉCIALISÉ DE TECHNOLOGIE APPLIQUÉE",
            "lieu": "TINGHIR, MAROC"
        },
        {
            "periode": "2018",
            "diplome": "Baccalauréat scientifique option science physique",
            "etablissement": "LYCÉE ALMORABITIN",
            "lieu": "TINGHIR, MAROC"
        }
    ]
    
    for formation in formations:
        st.markdown(f"""
        <div class="experience-card">
            <h3>📚 {formation['diplome']}</h3>
            <h4>🏫 {formation['etablissement']}</h4>
            <p><strong>📅 Période :</strong> {formation['periode']}</p>
            <p><strong>📍 Lieu :</strong> {formation['lieu']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header"><h2>🏆 Cours et Certifications</h2></div>', unsafe_allow_html=True)
    
    certifications = [
        {
            "nom": "PCAP – Certified Associate in Python Programming",
            "organisme": "Python Institute",
            "date": "Avril 2021"
        },
        {
            "nom": "PCEP – Certified Entry-Level Python Programmer",
            "organisme": "Python Institute",
            "date": "Juillet 2020"
        },
        {
            "nom": "Advanced Search Strategies in Scopus and Scopus AI",
            "organisme": "ELSEVIER",
            "date": "Décembre 2024"
        }
    ]
    
    for cert in certifications:
        st.markdown(f"""
        <div class="project-card">
            <h4>🏅 {cert['nom']}</h4>
            <p><strong>🏢 Organisme :</strong> {cert['organisme']}</p>
            <p><strong>📅 Date :</strong> {cert['date']}</p>
        </div>
        """, unsafe_allow_html=True)

# Section Projets
elif selected_section == "💻 Projets":
    st.markdown('<div class="section-header"><h2>💻 Projets Réalisés</h2></div>', unsafe_allow_html=True)
    
    projets = [
        {
            "nom": "ASK.BASE",
            "technologies": "Next.js, IA (RAG, FAISS, Llama 3.2)",
            "description": "Développement d'une application web intelligente pour la génération automatisée d'examens SQL.",
            "fonctionnalites": [
                "Création dynamique de quiz",
                "Retours en temps réel",
                "Interface utilisateur interactive",
                "Architecture évolutive"
            ]
        },
        {
            "nom": "Sentiment Analysis with NLP",
            "technologies": "RoBERTa, Python",
            "description": "Système d'analyse des sentiments appliqué aux avis sur les produits alimentaires d'Amazon.",
            "fonctionnalites": [
                "Prédiction automatisée des sentiments (positif, neutre, négatif)",
                "Traitement avancé des données textuelles",
                "Visualisation via nuages de mots",
                "Statistiques exploitables"
            ]
        },
        {
            "nom": "Gestion Absence API",
            "technologies": "Express.js, MongoDB",
            "description": "Développement d'une API RESTful pour la gestion des absences (2023).",
            "fonctionnalites": [
                "Gestion complète des absences (CRUD)",
                "Authentification des utilisateurs",
                "Endpoints RESTful",
                "Configuration simple de MongoDB",
                "Architecture évolutive"
            ]
        },
        {
            "nom": "COVID19APK",
            "technologies": "Android, Java",
            "description": "Application mobile multilingue pour suivre les mises à jour sur la COVID-19.",
            "fonctionnalites": [
                "Affichage en temps réel des statistiques COVID-19",
                "Support multilingue (français, espagnol, anglais, arabe)",
                "Interface adaptative selon la langue",
                "Statistiques détaillées (cas, guérisons, décès)"
            ]
        }
    ]
    
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

# Section Compétences
elif selected_section == "🛠️ Compétences":
    st.markdown('<div class="section-header"><h2>🛠️ Compétences Techniques</h2></div>', unsafe_allow_html=True)
    
    # Graphique des compétences
    col1, col2 = st.columns(2)
    
    with col1:
        competences_data = {
            'Catégorie': ['Frontend', 'Backend', 'Data Science', 'Bases de données', 'DevOps'],
            'Niveau': [85, 90, 80, 85, 70]
        }
        
        fig = px.bar(
            competences_data, 
            x='Niveau', 
            y='Catégorie',
            orientation='h',
            title="Niveau de Compétences par Catégorie",
            color='Niveau',
            color_continuous_scale='viridis'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Graphique en secteurs des technologies
        tech_data = {
            'Technologie': ['Python', 'JavaScript', 'Java', 'React', 'Node.js', 'Autres'],
            'Utilisation': [30, 25, 15, 15, 10, 5]
        }
        
        fig2 = px.pie(
            tech_data,
            values='Utilisation',
            names='Technologie',
            title="Répartition d'utilisation des technologies"
        )
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Détail des compétences
    st.markdown("### 💻 Langages de programmation & Développement logiciel")
    langages = ["Python", "Java", "C", "C#", "PHP8", "JavaScript", "SQL", "Kotlin", "TypeScript", "HTML5", "CSS3"]
    for lang in langages:
        st.markdown(f'<span class="skill-badge">{lang}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🎨 Développement Front-End")
    frontend = ["React.js", "Vue.js", "Bootstrap4", "jQuery"]
    for tech in frontend:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Développement Back-End")
    backend = ["Node.js", "Express.js", "Next.js", "Laravel", "Django", "ASP.NET"]
    for tech in backend:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Data Science & Analyse de Données")
    datascience = ["Statistiques", "Machine Learning", "Deep Learning", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras"]
    for tech in datascience:
        st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🗄️ Bases de données")
    databases = ["MySQL", "Oracle DB", "SQL Server", "MongoDB"]
    for db in databases:
        st.markdown(f'<span class="skill-badge">{db}</span>', unsafe_allow_html=True)
    
    st.markdown("### 🔧 Outils & Autres")
    outils = ["Git", "Batch Script", "iMacros Scripts", "Microsoft Office", "Canva", "Figma", "Adobe XD", "UML", "MERISE", "Windows", "Linux (Kali Linux)"]
    for outil in outils:
        st.markdown(f'<span class="skill-badge">{outil}</span>', unsafe_allow_html=True)

# Section Langues
elif selected_section == "🌍 Langues":
    st.markdown('<div class="section-header"><h2>🌍 Compétences Linguistiques</h2></div>', unsafe_allow_html=True)
    
    # Graphique des langues
    langues_data = {
        'Langue': ['Arabe', 'Tamazight', 'Français', 'Anglais', 'Espagnol'],
        'Niveau': [100, 100, 85, 80, 75],
        'Type': ['Langue maternelle', 'Langue maternelle', 'Compétence professionnelle', 'Compétence professionnelle', 'Compétence professionnelle']
    }
    
    fig = px.bar(
        langues_data,
        x='Langue',
        y='Niveau',
        color='Type',
        title="Niveau de maîtrise des langues (%)",
        text='Niveau'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=500)
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

# Section Contact
elif selected_section == "📞 Contact":
    st.markdown('<div class="section-header"><h2>📞 Informations de Contact</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>📧 Contact Direct</h3>
            <p><strong>Email :</strong> bouhlali2407@gmail.com</p>
            <p><strong>Téléphone :</strong> 0680483608</p>
            <p><strong>Localisation :</strong> Tinghir, Maroc</p>
            <p><strong>Âge :</strong> 25 ans</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Formulaire de contact simulé
        st.markdown("### 💌 Envoyer un message")
        with st.form("contact_form"):
            nom = st.text_input("Votre nom")
            email = st.text_input("Votre email")
            sujet = st.text_input("Sujet")
            message = st.text_area("Message", height=100)
            
            if st.form_submit_button("Envoyer le message"):
                st.success("Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.")
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h3>🌐 Réseaux Sociaux</h3>
            <p><strong>🔗 LinkedIn :</strong><br>
            <a href="https://www.linkedin.com/in/bouhlaliabdelfattah/" target="_blank">linkedin.com/in/bouhlaliabdelfattah</a></p>
            
            <p><strong>📺 YouTube :</strong><br>
            <a href="https://www.youtube.com/@BYDEVMAR" target="_blank">youtube.com/@BYDEVMAR</a></p>
            
            <p><strong>📝 Blog Medium :</strong><br>
            <a href="https://medium.com/@bouhlali99abdelfattah" target="_blank">medium.com/@bouhlali99abdelfattah</a></p>
            
            <p><strong>💻 GitHub :</strong><br>
            <a href="https://github.com/BYDEVMAR" target="_blank">github.com/BYDEVMAR</a><br>
            <a href="https://github.com/TINBYTE" target="_blank">github.com/TINBYTE</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Carte de disponibilité
        st.markdown("### 📅 Disponibilité")
        disponibilite = st.select_slider(
            "Actuellement disponible pour :",
            options=["Projets freelance", "Stages", "CDI", "Missions courtes", "Collaborations"],
            value="CDI"
        )
        st.info(f"Je suis actuellement ouvert aux opportunités de : **{disponibilite}**")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
    <p><strong>💼 Abdelfattah BOUHLALI</strong> - Software Engineer & Junior Data Scientist</p>
    <p>🚀 Transformant les défis complexes en solutions innovantes | 📧 bouhlali2407@gmail.com</p>
    <p><em>Créé avec ❤️ en utilisant Streamlit</em></p>
</div>
""", unsafe_allow_html=True)