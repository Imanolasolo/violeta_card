"""
Utilidades mínimas de internacionalización para la tarjeta.
"""


def t(value, language="es"):
    """
    Devuelve el texto traducido según el idioma solicitado.

    Si `value` no es un diccionario, se devuelve tal cual.
    Si falta la traducción solicitada, se prioriza español y luego inglés.
    """

    if not isinstance(value, dict):
        return value

    if language in value:
        return value[language]

    if "es" in value:
        return value["es"]

    if "en" in value:
        return value["en"]

    return next(iter(value.values()), "")