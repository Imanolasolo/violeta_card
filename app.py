import streamlit as st

from config.profile import PROFILE
from styles.main import load_styles

from components.language import render_language_selector
from components.hero import render_hero
from components.actions import render_actions
from components.sections import render_sections
from components.footer import render_footer


# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL DE STREAMLIT
# ---------------------------------------------------------

st.set_page_config(
    page_title=f"{PROFILE['name']} · {PROFILE['organization']}",
    page_icon="💙",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# CARGAMOS LOS ESTILOS
# ---------------------------------------------------------

load_styles()


# ---------------------------------------------------------
# SELECTOR DE IDIOMA
# ---------------------------------------------------------

language = render_language_selector()


# ---------------------------------------------------------
# CONTENEDOR PRINCIPAL DE LA TARJETA
# ---------------------------------------------------------

st.markdown('<div class="digital-card">', unsafe_allow_html=True)


# ---------------------------------------------------------
# COMPONENTES DE LA TARJETA
# ---------------------------------------------------------

render_hero(PROFILE, language)

render_actions(PROFILE, language)

render_sections(PROFILE, language)

render_footer(PROFILE, language)


# ---------------------------------------------------------
# CIERRE DE LA TARJETA
# ---------------------------------------------------------

st.markdown("</div>", unsafe_allow_html=True)