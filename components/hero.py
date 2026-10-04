"""
Hero / perfil principal de Violeta.
"""

from io import BytesIO
from pathlib import Path

from PIL import Image, ImageChops
import streamlit as st

from utils.i18n import t


def _trim_image_whitespace(image_path):
    image = Image.open(image_path).convert("RGBA")
    background = Image.new("RGBA", image.size, (255, 255, 255, 0))
    difference = ImageChops.difference(image, background)
    bounding_box = difference.getbbox()

    if bounding_box:
        image = image.crop(bounding_box)

    return image


def _load_logo_image(image_path):
    image = _trim_image_whitespace(image_path)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


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

    photo_col, logo_col = st.columns([1.05, 0.75], gap="small")

    with photo_col:
        if photo_path.exists():
            st.image(photo_path.as_posix(), width=124)
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
            st.image(_load_logo_image(logo_path), width=120)

    st.title(name)
    st.markdown(f"**{role}**")
    st.caption(organization)
    st.write(f"“{quote}”")