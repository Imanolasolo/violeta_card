"""
Generador de archivo vCard.

No necesita base de datos ni servicios externos.
"""


def escape_vcard(value):
    """
    Escapa caracteres especiales utilizados por vCard.
    """

    if not value:
        return ""

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def create_vcard(profile):
    """
    Genera una vCard 3.0 a partir del perfil.
    """

    name = escape_vcard(profile["name"])
    organization = escape_vcard(profile["organization"])
    phone = escape_vcard(profile["phone"])
    email = escape_vcard(profile["email"])
    linkedin = escape_vcard(profile["linkedin"])

    # -----------------------------------------------------
    # CONTENIDO VCARD
    # -----------------------------------------------------

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
ORG:{organization}
TITLE:Gerente General
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=WORK:{email}
URL:{linkedin}
END:VCARD
"""

    return vcard