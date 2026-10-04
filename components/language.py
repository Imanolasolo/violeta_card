"""
Selector de idioma de la tarjeta.
"""

import streamlit as st


def render_language_selector():
    """
    Renderiza el selector ES / EN.

    Guarda el idioma seleccionado en session_state para
    mantenerlo mientras el usuario navega/interactúa.
    """

    # -----------------------------------------------------
    # IDIOMA INICIAL
    # -----------------------------------------------------

    if "language" not in st.session_state:
        st.session_state.language = "es"

    # -----------------------------------------------------
    # SELECTOR
    # -----------------------------------------------------

    col1, col2, col3 = st.columns([1, 0.8, 1])

    with col2:

        selected = st.radio(
            "language",
            options=["es", "en"],
            format_func=lambda x: "ES" if x == "es" else "EN",
            horizontal=True,
            label_visibility="collapsed",
        )

        st.session_state.language = selected

    return st.session_state.language