from explorador.CategoriaComponente import CategoriaComponente


# -----------------------------------  ATRIBUTOS DE LOS COMPONENTES  -----------------------------------
# este apartado contiene los atributos de cada token
# (una pequeña descripcion de lo que hace, o como se usa).

class AtributoComponente:
    def evaluar_token(mitoken, mi_componente):
        AtributosComponente = {
            'cuarentena': 'equivalente a While',
            'aislamiento': 'equivalente a For',
            'estornudo_acapela': 'Si condicional',
            'estornudo_tapado': 'Sino condicional',
            'me_capeo': 'No condicional',
            '#yke': 'equivalente a and',
            '#oke': 'equivalente a or',
            '#positivo': 'equivalente a True',
            '#negativo': 'equivalente a False',
            '#mas': 'Operador logico de suma + ',
            '#quitar': 'Operador logico de resta - ',
            '#por': 'Operador logico de multiplicacion * ',
            '#cortar': 'Operador logico de division / ',
            '#mayorke': 'Su nombre lo dice todo xd',
            '#menorke': 'Su nombre lo dice todo xd',
            '#mismoke': 'Igual comparativo ',
            '#nadakever': 'Diferente comparativo',
            '@vacuna': 'imprime cualquier variable o texto ',
            '@inyeccion': 'Este te concatena 2 textos',
            '@pinchaso': 'Te saco el caracter de tu texto',
            '@penicilina': 'Te saco un elemento de tu lista',
            '@aguja': 'Este te muestra el largo de tu texto E: Texto S: Entero',
            '@antibiotico': 'Este te muestra el largo de tu lista  E: Lista S: Entero',
            '@antivirus': 'Recibe valores tipo imput, Dame la cura pa!',
            '@curado': 'Te paso tu texto a entero o viceversa, q dices?',
            '@vomito': 'Retorno todo, hasta el desayuno si queres',
            'covid19': 'Inicio de funcion.',
            '}empalido': 'inicio con :{ y termino con }empalido',
            ':=': 'equivalente a = ',
            'virus': 'con este inicias una Funcion',
            ':{': 'inicio con :{ y termino con }empalido',
        }
        # revisa que el token exista en la lista, en caso de ser variables o identificadores
        # retorna el mismo mensaje.
        if mitoken not in AtributosComponente:
            if mi_componente is CategoriaComponente.NOMBREFUNCION:
                return 'Esto es un nombre de una funcion'
            if mi_componente is CategoriaComponente.PUNTUACION:
                return 'Esto es un signo de puntuacion'
            if mi_componente is CategoriaComponente.MOLECULA:
                return 'Esto es un numero entero'
            if mi_componente is CategoriaComponente.MASCARILLA:
                return 'Esto es un booleano'
            if mi_componente is CategoriaComponente.MICROMOLECULA:
                return 'Esto es un flotante'
            if mi_componente is CategoriaComponente.RECETA:
                return 'Esto es un texto'
            return 'Identificadores o variables'
        # si el token si existe, busco y traigo el atributo.
        else:
            return AtributosComponente.get(mitoken)
