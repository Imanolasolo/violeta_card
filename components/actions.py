"""
Acciones principales de contacto.
"""

import streamlit as st
from urllib.parse import quote

from utils.i18n import t


def render_actions(profile, language):

    # -----------------------------------------------------
    # DATOS
    # -----------------------------------------------------

    phone = profile["phone"]
    email = profile["email"]
    linkedin = profile["linkedin"]

    # WhatsApp necesita únicamente números.
    whatsapp_number = (
        phone
        .replace("+", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
    )

    whatsapp_message = quote(
        (
            f"Hola Violeta, vi tu tarjeta digital de "
            f"{profile['organization']}."
        )
    )

    whatsapp_url = (
        f"https://wa.me/{whatsapp_number}"
        f"?text={whatsapp_message}"
    )

    # -----------------------------------------------------
    # BOTONES
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button(
            t({"es": "WhatsApp", "en": "WhatsApp"}, language),
            whatsapp_url,
            type="primary",
            use_container_width=True,
        )

    with col2:
        st.link_button(
            t({"es": "Email", "en": "Email"}, language),
            f"mailto:{email}",
            use_container_width=True,
        )

    with col3:
        st.link_button(
            t({"es": "LinkedIn", "en": "LinkedIn"}, language),
            linkedin,
            use_container_width=True,
        )