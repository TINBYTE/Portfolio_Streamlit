# ===== FICHIER : components/footer.py =====
import streamlit as st

def render_footer():
    """Rendu du footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
        <p><strong>💼 Abdelfattah BOUHLALI</strong> - Software Engineer & Junior Data Scientist</p>
        <p>🚀 Transformant les défis complexes en solutions innovantes | 📧 bouhlali2407@gmail.com</p>
        <p><em>Créé avec ❤️ en utilisant Streamlit</em></p>
    </div>
    """, unsafe_allow_html=True)