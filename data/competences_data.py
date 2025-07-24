# ===== FICHIER : data/competences_data.py =====

# Compétences organisées par catégories avec métadonnées
competences_categories = {
    "langages": {
        "title": "Langages de Programmation",
        "description": "Langages maîtrisés pour le développement d'applications",
        "icon": "💻",
        "level": 90,
        "skills": [
            {"name": "Python", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "JavaScript", "level": "Avancé", "years": "3+", "rating": 4},
            {"name": "Java", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "TypeScript", "level": "Intermédiaire", "years": "2+", "rating": 4},
            {"name": "C#", "level": "Intermédiaire", "years": "2+", "rating": 3},
            {"name": "PHP", "level": "Intermédiaire", "years": "2+", "rating": 3},
            {"name": "C", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Kotlin", "level": "Débutant", "years": "1+", "rating": 2},
            {"name": "SQL", "level": "Avancé", "years": "3+", "rating": 4},
            {"name": "HTML5", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "CSS3", "level": "Avancé", "years": "3+", "rating": 4}
        ]
    },
    "frontend": {
        "title": "Développement Front-End",
        "description": "Technologies pour créer des interfaces utilisateur modernes",
        "icon": "🎨",
        "level": 85,
        "skills": [
            {"name": "React.js", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Vue.js", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Next.js", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Bootstrap", "level": "Avancé", "years": "3+", "rating": 4},
            {"name": "Tailwind CSS", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "jQuery", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Sass/SCSS", "level": "Intermédiaire", "years": "2+", "rating": 3}
        ]
    },
    "backend": {
        "title": "Développement Back-End",
        "description": "Frameworks et technologies serveur",
        "icon": "⚙️",
        "level": 88,
        "skills": [
            {"name": "Node.js", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Express.js", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Django", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "FastAPI", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Laravel", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "ASP.NET", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Flask", "level": "Avancé", "years": "2+", "rating": 4}
        ]
    },
    "datascience": {
        "title": "Data Science & IA",
        "description": "Outils et techniques d'analyse de données et d'intelligence artificielle",
        "icon": "📊",
        "level": 82,
        "skills": [
            {"name": "Pandas", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "NumPy", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "Scikit-learn", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "TensorFlow", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Keras", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "PyTorch", "level": "Débutant", "years": "1+", "rating": 2},
            {"name": "Matplotlib", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Seaborn", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Plotly", "level": "Avancé", "years": "2+", "rating": 4}
        ]
    },
    "databases": {
        "title": "Bases de Données",
        "description": "Systèmes de gestion de bases de données relationnelles et NoSQL",
        "icon": "🗄️",
        "level": 85,
        "skills": [
            {"name": "MySQL", "level": "Avancé", "years": "3+", "rating": 4},
            {"name": "PostgreSQL", "level": "Intermédiaire", "years": "2+", "rating": 3},
            {"name": "MongoDB", "level": "Intermédiaire", "years": "2+", "rating": 3},
            {"name": "Oracle DB", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "SQL Server", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Redis", "level": "Débutant", "years": "1+", "rating": 2}
        ]
    },
    "devops": {
        "title": "DevOps & Outils",
        "description": "Outils de développement, déploiement et collaboration",
        "icon": "🔧",
        "level": 75,
        "skills": [
            {"name": "Git", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "GitHub", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "Docker", "level": "Intermédiaire", "years": "1+", "rating": 3},
            {"name": "Linux", "level": "Avancé", "years": "2+", "rating": 4},
            {"name": "Windows", "level": "Expert", "years": "5+", "rating": 5},
            {"name": "VS Code", "level": "Expert", "years": "3+", "rating": 5},
            {"name": "Figma", "level": "Intermédiaire", "years": "2+", "rating": 3},
            {"name": "Adobe XD", "level": "Intermédiaire", "years": "1+", "rating": 3}
        ]
    }
}

# Données pour les graphiques
competences_niveaux = {
    'Catégorie': ['Langages', 'Frontend', 'Backend', 'Data Science', 'Databases', 'DevOps'],
    'Niveau': [90, 85, 88, 82, 85, 75]
}

tech_utilisation = {
    'Technologie': ['Python', 'JavaScript', 'React', 'Node.js', 'Java', 'Autres'],
    'Utilisation': [35, 25, 15, 12, 8, 5]
}

# Certifications et formations
certifications = [
    {
        "name": "Python for Data Science",
        "issuer": "IBM",
        "date": "2023",
        "status": "obtenu",
        "icon": "🐍"
    },
    {
        "name": "Machine Learning Specialization",
        "issuer": "Stanford/Coursera",
        "date": "2023",
        "status": "en_cours",
        "icon": "🤖"
    },
    {
        "name": "React Developer Certification",
        "issuer": "Meta",
        "date": "2023",
        "status": "obtenu",
        "icon": "⚛️"
    },
    {
        "name": "AWS Cloud Practitioner",
        "issuer": "Amazon",
        "date": "2024",
        "status": "planifie",
        "icon": "☁️"
    }
]

# Statistiques de compétences
skills_stats = {
    "total_langages": 11,
    "total_frameworks": 15,
    "total_databases": 6,
    "annees_experience": 3,
    "projets_realises": 25,
    "certifications_obtenues": 5
}

# Compétences par domaine d'application
domaines_application = {
    "web_development": {
        "title": "Développement Web",
        "technologies": ["React.js", "Node.js", "Express.js", "MongoDB", "JavaScript", "HTML5", "CSS3"],
        "projets": 8,
        "niveau": 90
    },
    "data_science": {
        "title": "Science des Données",
        "technologies": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Jupyter"],
        "projets": 6,
        "niveau": 85
    },
    "mobile_development": {
        "title": "Développement Mobile",
        "technologies": ["React Native", "Kotlin", "Java", "Firebase"],
        "projets": 3,
        "niveau": 70
    },
    "desktop_applications": {
        "title": "Applications Desktop",
        "technologies": ["Python", "Tkinter", "C#", "WPF", ".NET"],
        "projets": 4,
        "niveau": 75
    }
}

# Compétences organisées par niveau (version simple pour compatibilité)
competences = {
    "langages": [skill["name"] for skill in competences_categories["langages"]["skills"]],
    "frontend": [skill["name"] for skill in competences_categories["frontend"]["skills"]],
    "backend": [skill["name"] for skill in competences_categories["backend"]["skills"]],
    "datascience": [skill["name"] for skill in competences_categories["datascience"]["skills"]],
    "databases": [skill["name"] for skill in competences_categories["databases"]["skills"]],
    "outils": [skill["name"] for skill in competences_categories["devops"]["skills"]]
}