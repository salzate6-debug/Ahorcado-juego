import random

PALABRAS = [
    "PYTHON",
    "PROGRAMACION",
    "AHORCADO",
    "DESARROLLO",
    "REPOSITORIO",
    "GITHUB",
    "ALGORITMO"
]

def obtener_palabra():
    """Selecciona y retorna una palabra aleatoria en mayúsculas."""
    return random.choice(PALABRAS)