"""
Secciones informativas de la tarjeta.
"""

import streamlit as st

from utils.i18n import t


def render_sections(profile, language):

    # -----------------------------------------------------
    # SOBRE MÍ
    # -----------------------------------------------------

    bio_title = t(
        {
            "es": "Sobre mí",
            "en": "About me",
        },
        language,
    )

    bio = t(profile["bio"], language)

    st.subheader(bio_title)
    st.write(bio)

    # -----------------------------------------------------
    # MISIÓN
    # -----------------------------------------------------

    mission_title = t(
        {
            "es": "Nuestra misión",
            "en": "Our mission",
        },
        language,
    )

    mission = t(profile["mission"], language)

    st.subheader(mission_title)
    st.write(mission)