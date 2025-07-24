# PORTFOLIO INTERACTIF - Abdelfattah BOUHLALI

## 📋 Description
Application Streamlit interactive présentant le CV d'Abdelfattah BOUHLALI, Software Engineer et Junior Data Scientist.

## 🏗️ Structure du projet
```
cv_streamlit/
├── main.py                 # Fichier principal
├── requirements.txt        # Dépendances
├── README.md              # Documentation
├── config/
│   └── page_config.py     # Configuration de la page
├── styles/
│   └── css_styles.py      # Styles CSS personnalisés
├── data/
│   ├── personal_data.py   # Données personnelles
│   ├── experiences_data.py # Données des expériences
│   ├── formations_data.py  # Données de formation
│   ├── projets_data.py    # Données des projets
│   ├── competences_data.py # Données des compétences
│   └── langues_data.py    # Données des langues
├── components/
│   ├── header.py          # Composant header
│   ├── sidebar.py         # Composant sidebar
│   └── footer.py          # Composant footer
├── pages/
│   ├── __init__.py        # Init du module pages
│   ├── accueil.py         # Page d'accueil
│   ├── profil.py          # Page profil
│   ├── experiences.py     # Page expériences
│   ├── formation.py       # Page formation
│   ├── projets.py         # Page projets
│   ├── competences.py     # Page compétences
│   ├── langues.py         # Page langues
│   └── contact.py         # Page contact
└── utils/
    └── charts.py          # Utilitaires pour les graphiques
```

##  Installation et lancement

### 1. Cloner le projet
```bash
git clone [url-du-repo]
cd cv_streamlit
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer l'application
```bash
streamlit run main.py
```

##  Fonctionnalités

### 📱 Navigation
- Interface avec sidebar intuitive
- Navigation par sections
- Métriques rapides

### 🎨 Design
- CSS personnalisé avec gradients
- Cartes colorées par section
- Badges pour les compétences
- Design responsive

### 📊 Visualisations
- Graphiques de compétences interactifs
- Répartition des technologies
- Niveaux de langues
- Charts Plotly

### 🗂️ Sections
1. **Accueil** - Profil et réseaux sociaux
2. **Profil** - Informations détaillées
3. **Expériences** - Parcours professionnel
4. **Formation** - Éducation et certifications
5. **Projets** - Portfolio de réalisations
6. **Compétences** - Technologies maîtrisées
7. **Langues** - Compétences linguistiques
8. **Contact** - Informations de contact

## 🛠️ Technologies utilisées
- **Streamlit** - Framework web
- **Plotly** - Visualisations interactives
- **Pandas** - Manipulation de données
- **HTML/CSS** - Styling personnalisé

## 👨‍💻 Développeur
**Abdelfattah BOUHLALI**
- Email: bouhlali2407@gmail.com
- LinkedIn: [bouhlaliabdelfattah](https://www.linkedin.com/in/bouhlaliabdelfattah/)
- GitHub: [@BYDEVMAR](https://github.com/BYDEVMAR)

## 📝 Licence
Ce projet est à des fins de démonstration du CV d'Abdelfattah BOUHLALI.

---

## 🔧 Personnalisation

### Modifier les données
Pour personnaliser le CV, modifiez les fichiers dans le dossier `data/`:
- `personal_data.py` - Informations personnelles
- `experiences_data.py` - Expériences professionnelles
- `formations_data.py` - Formation et certifications
- `projets_data.py` - Projets réalisés
- `competences_data.py` - Compétences techniques
- `langues_data.py` - Compétences linguistiques

### Modifier les styles
Les styles CSS se trouvent dans `styles/css_styles.py`

### Ajouter de nouvelles pages
1. Créer un nouveau fichier dans `pages/`
2. Définir une fonction `render()`
3. Ajouter la page au mapping dans `main.py`

## 🐛 Résolution de problèmes

### Erreur d'import
Assurez-vous que tous les dossiers contiennent un fichier `__init__.py`

### Graphiques non affichés
Vérifiez que Plotly est correctement installé:
```bash
pip install plotly --upgrade
```

### Styles CSS non appliqués
Vérifiez que `unsafe_allow_html=True` est présent dans les appels `st.markdown()`