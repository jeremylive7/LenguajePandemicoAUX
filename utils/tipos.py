from enum import Enum, auto


class Tipos(Enum):
    RECETA = auto()  # STRING
    MOLECULA = auto()  # INT
    MICROMOLECULA = auto()  # FLOAT
    MASCARILLA = auto()  # BOOL
    CUALQUIERA = auto()
    NINGUNO = auto()
