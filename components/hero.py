"""
Hero / perfil principal de Violeta.
"""

from pathlib import Path

import streamlit as st

from utils.i18n import t


def render_hero(profile, language):

    # -----------------------------------------------------
    # FOTOGRAFÍA
    # -----------------------------------------------------

    photo_path = Path("assets") / profile["photo_file"]
    logo_path = Path("assets") / profile["logo_file"]

    # -----------------------------------------------------
    # INFORMACIÓN
    # -----------------------------------------------------

    name = profile["name"]
    role = t(profile["role"], language)
    organization = profile["organization"]
    quote = t(profile["quote"], language)

    # -----------------------------------------------------
    # RENDER
    # -----------------------------------------------------

    photo_col, logo_col = st.columns(2)

    with photo_col:
        if photo_path.exists():
            st.image(photo_path.as_posix(), width=140)
        else:
            st.markdown(
                """
                <div class="profile-photo-placeholder">
                    VM
                </div>
                """,
                unsafe_allow_html=True,
            )

    with logo_col:
        if logo_path.exists():
            st.image(logo_path.as_posix(), width=140)

    st.title(name)
    st.markdown(f"**{role}**")
    st.caption(organization)
    st.write(f"“{quote}”")