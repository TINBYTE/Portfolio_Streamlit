import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_competences_chart(data):
    """Création du graphique des compétences"""
    df = pd.DataFrame(data)
    fig = px.bar(
        df, 
        x='Niveau', 
        y='Catégorie',
        orientation='h',
        title="Niveau de Compétences par Catégorie",
        color='Niveau',
        color_continuous_scale='viridis'
    )
    fig.update_layout(height=400)
    return fig

def create_tech_pie_chart(data):
    """Création du graphique en secteurs des technologies"""
    df = pd.DataFrame(data)
    fig = px.pie(
        df,
        values='Utilisation',
        names='Technologie',
        title="Répartition d'utilisation des technologies"
    )
    fig.update_layout(height=400)
    return fig

def create_langues_chart(data):
    """Création du graphique des langues"""
    df = pd.DataFrame(data)
    fig = px.bar(
        df,
        x='Langue',
        y='Niveau',
        color='Type',
        title="Niveau de maîtrise des langues (%)",
        text='Niveau'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=500)
    return fig