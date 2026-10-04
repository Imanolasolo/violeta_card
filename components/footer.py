"""
Footer de la tarjeta.
"""

import streamlit as st

from utils.i18n import t


def render_footer(profile, language):

    location = t(profile["location"], language)

    st.caption(f"📍 {location}")
    st.markdown(
        f"[Instagram]({profile['instagram']}) · [Facebook]({profile['facebook']})"
    )
    st.caption(profile["organization"])
    