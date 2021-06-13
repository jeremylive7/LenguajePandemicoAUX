# -----------------------------------  Imports -----------------------------------
from explorador.ComponenteLexico import CategoriaComponente


# -----------------------------------  LISTA DE LOS COMPONENTES LEXICOS -----------------------------------
# aqui vamos a reconocer a que categoria pertenece cada compenente lexico del lenguaje
# diviendolos asi por su respectivo tipo para ser categorizados.
class DescriptoresComponentes:
    # contiene una lista de tuplas de CATEGORIA - Regex.
    descriptores_componentes = [
        (CategoriaComponente.ESPACIO, r'^(\s)+'),
        (CategoriaComponente.COMENTARIO, r'^xxx[a-z A-Z -_ / ]+'),
        (CategoriaComponente.PALABRA_CLAVE, r'^(covid19|virus|mascarilla|receta|micro_molecula|molecula)'),
        (CategoriaComponente.ERRORENCAPSULACION, r'^(}empalido[a-z A-Z -_ / ])'),
        (CategoriaComponente.ENCAPSULACION, r'^(:{|}empalido)'),
        (CategoriaComponente.CONDICIONAL, r'^(estornudo_acapela|estornudo_tapado|me_capeo)'),
        (CategoriaComponente.REPETICION, r'^(cuarentena|aislamiento)'),
        (CategoriaComponente.ASIGNACION, r'^(:=)'),
        (CategoriaComponente.FUNCION, r'^(@vacuna|@inyeccion|@pinchaso|@penicilina|@aguja|@antibiotico|@antivirus|@curado|@vomito|@covid19)'),
        (CategoriaComponente.EXPCONDICIONAL, r'^(#yke|#oke)'),
        (CategoriaComponente.OPERADOR, r'^(#mas|#quitar|#por|#cortar)'),
        (CategoriaComponente.COMPARADOR, r'^(#mayorke|#menorke|#mismoke|#nadakever)'),
        (CategoriaComponente.IDENTIFICADOR, r'^([a-z]([a-zA-z0-9])*)'),
        (CategoriaComponente.LLAMADAFUNCION, r'^(@[a-z]([a-zA-z0-9])*)'),
        (CategoriaComponente.ERRORPARAMETRO, r'^([0-9]+[a-z]([a-zA-z0-9])*)'),
        (CategoriaComponente.ERRORFLOTANTE, r'^(\.[0-9])'),
        (CategoriaComponente.MASCARILLA, r'^(#positivo|#negativo)'),
        (CategoriaComponente.RECETA, r'^(<[a-z A-Z _ 0-9]*>)'),
        (CategoriaComponente.MICROMOLECULA, r'^(-?[0-9]+\.[0-9]+)'),
        (CategoriaComponente.MOLECULA, r'^(-?[0-9]+)'),
        (CategoriaComponente.PUNTUACION, r'^([(),])'),
        (CategoriaComponente.ERRORVARIABLE, r'^([:{}~!@$%#&*-+\|;?/"]+)'),
    ]


