"""
Hero / perfil principal de Violeta.
"""

import base64
from io import BytesIO
from pathlib import Path
from mimetypes import guess_type

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


def _image_data_uri(image_path):
    mime_type, _ = guess_type(image_path.as_posix())
    if not mime_type:
        mime_type = "image/png"

    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


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

    photo_html = (
        f'<img class="hero-photo" src="{_image_data_uri(photo_path)}" alt="{name}">'
        if photo_path.exists()
        else '<div class="profile-photo-placeholder">VM</div>'
    )

    logo_html = (
        f'<img class="hero-logo" src="{_image_data_uri(logo_path)}" alt="{organization}">'
        if logo_path.exists()
        else ""
    )

    st.markdown(
        f"""
        <div class="hero-media-row">
            {photo_html}
            {logo_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.title(name)
    st.markdown(f"**{role}**")
    st.caption(organization)
    st.write(f"“{quote}”")