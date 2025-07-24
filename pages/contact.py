# ===== CORRECTION : pages/contact.py =====
import streamlit as st
from data.personal_data import personal_info, reseaux_sociaux

def render():
    """Page contact"""
    st.markdown('<div class="section-header"><h2>📞 Informations de Contact</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="contact-info">
            <h3>📧 Contact Direct</h3>
            <p><strong>Email :</strong> {personal_info['email']}</p>
            <p><strong>Téléphone :</strong> {personal_info['telephone']}</p>
            <p><strong>Localisation :</strong> {personal_info['ville']}</p>
            <p><strong>Âge :</strong> {personal_info['age']}</p>
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
        st.markdown("### 🌐 Réseaux Sociaux")
        st.write(f"🔗 [LinkedIn]({reseaux_sociaux['linkedin']})")
        st.write(f"📺 [YouTube]({reseaux_sociaux['youtube']})")
        st.write(f"📝 [Blog Medium]({reseaux_sociaux['website']})")
        st.write("💻 [GitHub BYDEVMAR](https://github.com/BYDEVMAR)")
        st.write("💻 [GitHub TINBYTE](https://github.com/TINBYTE)")
        
        # Carte de disponibilité
        st.markdown("### 📅 Disponibilité")
        disponibilite = st.select_slider(
            "Actuellement disponible pour :",
            options=["Projets freelance", "Stages", "CDI", "Missions courtes", "Collaborations"],
            value="CDI"
        )
        st.info(f"Je suis actuellement ouvert aux opportunités de : **{disponibilite}**")
