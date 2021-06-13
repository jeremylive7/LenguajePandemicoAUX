from enum import Enum, auto


class TipoNodo(Enum):
    """
    Describe el tipo de nodo según la gramática deffinida, se adjunta la gramática para tener una mejor guía.
    """
    PROGRAMA = auto()  # Programa ::= (Comentario | Asignación | Función)* Inicio
    ASIGNACION = auto()  # Asignación ::= (mascarilla | molecula | micro_molecula | receta) Identificador := (Identificador | LlamadaFunción | Expresión)
    FUNCION = auto()  # Función ::= virus Identificador Parametros? :{ Instrucciones }empalido
    IDENTIFICADOR = auto()  # Identificador ::= [a-z][a-z A-Z 0-9]+
    LLAMADA_FUNCION = auto()  # LlamadaFunción ::= @ Identificador (Parametros | Literal | LlamadaFunción)*
    PARAMETROS_FUNCION = auto()  # Parámetros ::= Identificador (, Identificador)*
    PARAMETROS_INVOCACION = auto()
    SI_CONDICIONAL = auto()  # SiCondicional ::= estornudo_acapela ExpCondicional: {Instrucciones +} empalido
    SINO_CONDICIONAL = auto  # SinoCondicional ::= estornudo_tapado ExpCondicional: {Instrucciones +} empalido
    NO_CONDICIONAL = auto()  # NoCondicional ::= me_capeo: {Instrucciones +} empalido
    INSTRUCCION = auto()  # Instrucciones ::= Asignación | Identificador |  RepetirWhile | RepetirFor | SiCondicional | Comentario | Retorno
    REPETIR_WHILE = auto()  # RepetirWhile ::= cuarentena ExpCondicional: {Instrucciones +}empalido
    REPETIR_FOR = auto()  # RepetirFor ::= aislamiento Identificador Molécula, Molécula: {Instrucciones +} empalido
    OPERADOR_LOGICO = auto()
    EXPRESION_MATEMATICA = auto()
    INVOCACION = auto()
    BIFURCACION = auto()
    EXPRESION = auto()  # Expresión ::= (MiniExpreción) | Literal | Identificador | LlamadaFunción
    CONDICION = auto()
    COMPARACION = auto()  # Comparación ::= (Identificador | Literal) Comparador(Identificador | Literal)
    RETORNO = auto()  # Retorno ::= @vomito Identificador | Literal | LlamadaFunción
    ERROR = auto()
    PRINCIPAL = auto()
    BLOQUE_INSTRUCCIONES = auto()
    OPERADOR = auto()  # Operador ::=  # mas | #quitar | #por | #cortar
    MASCARILLA = auto()
    COMPARADOR = auto()
    RECETA = auto()
    MOLECULA = auto()  # int
    MICROMOLECULA = auto()  # float
    PALABRA_CLAVE = auto()
    IMPRESION = auto()
    CONCATENAR = auto()
    INDICE = auto()
    LARGO = auto()
    SOLICITAR = auto()
    CONVERTIR = auto()
