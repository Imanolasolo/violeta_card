"""
Componente de marca.

Muestra el logo de Fundación Corazones Liberados
en la parte superior de la tarjeta.
"""

from pathlib import Path
import streamlit as st


def render_brand(profile, language):

    # -----------------------------------------------------
    # LOCALIZACIÓN DEL LOGO
    # -----------------------------------------------------

    logo_path = Path("assets") / profile["logo_file"]

    # -----------------------------------------------------
    # RENDER
    # -----------------------------------------------------

    if logo_path.exists():
        st.image(logo_path.as_posix(), width=180)