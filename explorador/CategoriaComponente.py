from enum import Enum, auto


# -----------------------------------  TODOS LOS TIPOS QUE MANEJA NUESTRO LENGUAJE  -----------------------------------
# este apartado contiene las categorias a la que pueden ser asignadas los tokes del lenguaje,
# tales como palabras claves y las distintas categorias de los componentes lexicos.
class CategoriaComponente(Enum):
    COMENTARIO = auto()
    PALABRA_CLAVE = auto()
    ERRORENCAPSULACION = auto()
    ENCAPSULACION = auto()
    CONDICIONAL = auto()
    REPETICION = auto()
    ASIGNACION = auto()
    FUNCION = auto()
    EXPCONDICIONAL = auto()
    OPERADOR = auto()
    COMPARADOR = auto()
    IDENTIFICADOR = auto()
    NOMBREFUNCION = auto()
    ERRORPARAMETRO = auto()
    ERRORVARIABLE = auto()
    LLAMADAFUNCION = auto()
    ERRORFLOTANTE = auto()
    MASCARILLA = auto()
    RECETA = auto()
    MICROMOLECULA = auto()
    MOLECULA = auto()
    PUNTUACION = auto()
    ESPACIO = auto()
    NINGUNO = auto()
