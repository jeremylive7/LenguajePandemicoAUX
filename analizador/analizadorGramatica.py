class Analizador:
    posicion_componente_actual = 0
    componente_actual = ""
    TipoComponente = []
    contador_encapsulacion = 0

    def __init__(self, lista_componentes, pTiposComponente):

        self.componentes_lexicos = lista_componentes
        self.cantidad_componentes = len(lista_componentes)
        self.posicion_componente_actual = 0
        self.componente_actual = lista_componentes[0]
        self.TipoComponente = pTiposComponente

    def analizar(self):
        """
        Método principal que inicia el análisis siguiendo el esquema de
        análisis por descenso recursivo
        """
        self.__analizar_programa()

    def __analizar_programa(self):
        """
        Programa ::= (Comentario | Asignación | Función)* Principal
        """
        while True:
            if self.componente_actual.categoria_componente in [self.TipoComponente.ERRORENCAPSULACION,
                                                               self.TipoComponente.ERRORPARAMETRO,
                                                               self.TipoComponente.ERRORFLOTANTE,
                                                               self.TipoComponente.ERRORVARIABLE]:
                print("Error: ", self.componente_actual)
                self.__pasar_siguiente_componente()
            elif self.componente_actual.categoria_componente == self.TipoComponente.IDENTIFICADOR:
                self.__analizar_asignacion()

            elif self.componente_actual.texto_componente == 'virus':
                self.__analizar_funcion()
            else:
                break

        # Inicio ::= covid19 :{ Instrucciones+ }empalido
        if self.componente_actual.texto_componente in ['covid19']:
            self.__analizar_principal()

        elif self.componente_actual.texto_componente == "}empalido":
            if self.posicion_componente_actual >= self.cantidad_componentes:
                if self.contador_encapsulacion != 0:
                    print('Error: Faltan mas empalidos en tu codigo')
            else:
                print('Error: Exceso de empalidos')
            # self.contador_encapsulacion
            print("Se termino de analizar el codigo del lenguaje Pandemiaaaa")

        else:
            raise SyntaxError(str(self.componente_actual))

    def __analizar_asignacion(self):
        """
        Asignación ::= Identificador := (Identificador | LlamadaFunción)
        """

        '''Identifico si el tipo es un identificador.'''
        self.__verificar_identificador()

        '''Voy bien.. ya encontre un identificador 
        entonces el siguientes es un igual? '''
        self.__verificar(':=')

        if self.componente_actual.categoria_componente in [self.TipoComponente.MOLECULA,
                                                           self.TipoComponente.MICROMOLECULA,
                                                           self.TipoComponente.MASCARILLA, self.TipoComponente.RECETA]:
            self.__analizar_literal()

        elif self.componente_actual.texto_componente == '(':
            self.__analizar_expresion_matematica()
        else:
            self.__analizar_invocacion()

    def __analizar_expresion_matematica(self):
        """
        ExpresiónMatemática ::= (Expresión) | Literal | Identificador
        """
        # NO se aumenta el contador de indice
        # Primera opción
        if self.componente_actual.texto_componente == '(':
            self.__verificar('(')
            self.__analizar_expresion()
            self.__verificar(')')

        # Acá yo se que estan bien formados por que eso lo hizo el
        # explorador... es nada más revisar las posiciones.
        elif self.componente_actual.categoria_componente in [self.TipoComponente.MOLECULA,
                                                             self.TipoComponente.MICROMOLECULA,
                                                             self.TipoComponente.MASCARILLA,
                                                             self.TipoComponente.RECETA]:
            self.__analizar_literal()
        # Lllamada funcion...falta

        # Este código se simplifica si invierto la opción anterior y esta
        else:
            self.__verificar_identificador()

    def __analizar_expresion(self):
        """
        Expresión ::= ExpresiónMatemática Operador ExpresiónMatemática
        """

        # Acá no hay nada que hacer todas son obligatorias en esas
        # posiciones
        self.__analizar_expresion_matematica()
        self.__verificar_operador()
        self.__analizar_expresion_matematica()

    def __analizar_funcion(self):
        """
        Función ::= virus Identificador Parametros? :{ Instrucciones }empalido
        """
        self.__verificar('virus')
        self.__verificar_identificador()
        self.__analizar_parametros()
        self.__analizar_bloque_instrucciones()

    def __analizar_invocacion(self):
        """
        IDENTIFICADOR = [a-z]([a-zA-z0-9])*
        """
        self.__verificar_identificador()
        self.__analizar_parametros()

    def __analizar_parametros(self):
        """
        Parametros ::= Valor (, Valor)+
        """
        self.__analizar_valor()

        # Funciona con los parametros que sea, solo que no valida cuantos deben pasar.
        while self.componente_actual.texto_componente == ',':
            self.__verificar(',')
            self.__analizar_valor()

    def __analizar_instruccion(self):
        """
        Syntaxis Lenguaje Pandemico.
            Instrucciones ::= (Asignación | LlamadaFuncion ) | Identificador | RepetirWhile | RepetirFor |
             SiCondicional | Comentario | Retorno
        """
        if self.componente_actual.texto_componente == 'cuarentena':
            self.__analizar_repeticion()

        elif self.componente_actual.texto_componente == 'aislamiento':
            self.__analizar_repeticionFor()

        elif self.componente_actual.texto_componente == 'estornudo_acapela':
            self.__analizar_bifurcacion()

        elif self.componente_actual.categoria_componente == self.TipoComponente.IDENTIFICADOR:
            if self.__componente_venidero().texto_componente == ':=':
                self.__analizar_asignacion()
            else:
                self.__analizar_invocacion()

        elif self.componente_actual.texto_componente == '@vomito':
            self.__analizar_retorno()

        else:
            self.__analizar_error()

    def __analizar_repeticion(self):
        """
        RepetirWhile ::= cuarentena ExpCondicional :{ Instrucciones+ }empalido
        """
        self.__verificar('cuarentena')
        self.__analizar_condicion()
        self.__analizar_bloque_instrucciones()

    def __analizar_repeticionFor(self):
        """
        RepetirFor ::= aislamiento Identificador Molécula, Molécula :{ Instrucciones+ }empalido
        """

        self.__verificar('aislamiento')
        self.__verificar_identificador()
        self.__analizar_parametros()
        self.__analizar_bloque_instrucciones()

    def __analizar_bifurcacion(self):
        """
        Bifurcación ::= SiCondicional (Sino)?
        """
        self.__analizar_si()

        if self.componente_actual.texto_componente == 'estornudo_tapado':
            self.__analizar_sino()

        self.__analizar_no()

    def __analizar_si(self):
        """
        SiCondicional ::= estornudo_acapela ExpCondicional :{ Instrucciones+ }empalido
        """
        self.__verificar('estornudo_acapela')
        self.__analizar_condicion()
        self.__analizar_bloque_instrucciones()

    def __analizar_sino(self):
        """
        SinoCondicional ::= estornudo_tapado ExpCondicional :{ Instrucciones+ }empalido
        """
        self.__verificar('estornudo_tapado')
        self.__analizar_condicion()
        self.__analizar_bloque_instrucciones()

    def __analizar_no(self):
        """
        NoCondicional ::= me_capeo :{ Instrucciones+ }empalido
        """
        self.__verificar('me_capeo')
        self.__analizar_condicion()
        self.__analizar_bloque_instrucciones()

    def __analizar_condicion(self):
        """
        Condición ::= Comparación ((divorcio|casorio) Comparación)?
        ExpCondicional ::= Comparación ( (#yke | #oke ) Comparación)?
        """
        self.__analizar_comparacion()

        if self.componente_actual.categoria_componente == self.TipoComponente.PALABRA_CLAVE:

            if self.componente_actual.texto_componente == '#yke':  # and
                self.__verificar('#yke')
            else:
                self.__verificar('#oke')  # or

            self.__analizar_comparacion()  # comparador

    def __analizar_comparacion(self):
        """
        Comparación ::= (Identificador | Literal) Comparador (Identificador | Literal)
        """
        self.__analizar_valor()
        self.__verificar_comparador()
        self.__analizar_valor()

    def __analizar_valor(self):
        """
        Valor ::= (Identificador | Literal)
        """
        # El uno o el otro
        if self.componente_actual.categoria_componente is self.TipoComponente.IDENTIFICADOR:
            self.__verificar_identificador()
        else:
            self.__analizar_literal()

    def __analizar_retorno(self):
        """
        Retorno ::= @ vomito Identificador | Literal | LlamadaFunción
        """
        self.__verificar('@vomito')

        # Este hay que validarlo para evitar el error en caso de que no
        # aparezca
        if self.componente_actual.categoria_componente in [self.TipoComponente.IDENTIFICADOR,
                                                           self.TipoComponente.MOLECULA,
                                                           self.TipoComponente.MICROMOLECULA,
                                                           self.TipoComponente.MASCARILLA, self.TipoComponente.RECETA]:
            self.__analizar_valor()
        elif self.componente_actual.categoria_componente == self.TipoComponente.FUNCION:
            self.__analizar_invocacion()

    def __analizar_error(self):
        """
        Cuatro errores.
        """
        if self.componente_actual.categoria_componente in [self.TipoComponente.ERRORENCAPSULACION,
                                                           self.TipoComponente.ERRORPARAMETRO,
                                                           self.TipoComponente.ERRORFLOTANTE,
                                                           self.TipoComponente.ERRORVARIABLE]:
            print("Error: ", self.componente_actual)
            self.__pasar_siguiente_componente()

    def __analizar_principal(self):
        """
        Inicio ::= covid19 :{ Instrucciones+ }empalido
        """
        if self.componente_actual == 'covid19':
            self.__verificar('covid19')

        self.__analizar_bloque_instrucciones()

    def __analizar_literal(self):
        """
        Literal ::= Receta | Molécula | Micro_Molécula | Mascarilla
        evaluo, si es texto, booleano, entero o fotante.
        """
        if self.componente_actual.categoria_componente is self.TipoComponente.RECETA:
            self.__verificar_texto()

        elif self.componente_actual.categoria_componente is self.TipoComponente.MASCARILLA:
            self.__verificar_valor_verdad()

        elif self.componente_actual.categoria_componente == self.TipoComponente.MOLECULA:
            self.__verificar_entero()

        elif self.componente_actual.categoria_componente == self.TipoComponente.MICROMOLECULA:
            self.__verificar_flotante()

    def __analizar_bloque_instrucciones(self):
        """
        BloqueInstrucciones ::= { Instrucción+ }
        """
        self.__verificar(':{')
        self.contador_encapsulacion += 1
        self.__analizar_instruccion()

        while self.componente_actual.texto_componente in ['cuarentena', 'aislamiento' 'estornudo_acapela',
                                                          'estornudo_tapado', 'me_capeo', '@vomito'] \
                or self.componente_actual.categoria_componente == self.TipoComponente.IDENTIFICADOR:
            self.__analizar_instruccion()

        # agregue esto.
        if self.posicion_componente_actual >= self.cantidad_componentes:
            return
        else:
            self.__verificar('}empalido')
            self.contador_encapsulacion -= 1

    def __verificar_operador(self):
        """
        Operador ::= #mas | #quitar | #por | #cortar
        """
        self.__verificar_tipo_componente(self.TipoComponente.OPERADOR)

    def __verificar_comparador(self):
        """
        ExpCondicional ::= Comparación ( (#yke | #oke ) Comparación)?
        """
        self.__verificar_tipo_componente(self.TipoComponente.COMPARADOR)

    def __verificar_identificador(self):
        """
        Identificador ::= [a-z][a-z A-Z 0-9]+
        """
        self.__verificar_tipo_componente(self.TipoComponente.IDENTIFICADOR)

    def __verificar_valor_verdad(self):
        """
        Mascarilla ::= #positivo | #negativo
        """
        self.__verificar_tipo_componente(self.TipoComponente.MASCARILLA)

    def __verificar_texto(self):
        """
        Receta ::= <[a-z A-Z _ 0-9]+>
        """
        self.__verificar_tipo_componente(self.TipoComponente.RECETA)

    def __verificar_entero(self):
        """
        Molécula ::= -?[0-9]+
        """
        self.__verificar_tipo_componente(self.TipoComponente.MOLECULA)

    def __verificar_flotante(self):
        """
        Micromolécula ::= -?[0-9]+.[0-9]+
        """
        self.__verificar_tipo_componente(self.TipoComponente.MICROMOLECULA)

    def __verificar(self, texto_esperado):
        """
        Syntaxis Lenguaje Pandemico.
        Verifica veracicamente si lo que esta actualmente leyendo sea efectivamente
            lo pasado por parametro.
        Da error si no es el caso.
        """
        if self.componente_actual.texto_componente != texto_esperado:
            print("Error: ", str(self.componente_actual))
            # raise SyntaxError (str(self.componente_actual))

        self.__pasar_siguiente_componente()

    def __verificar_tipo_componente(self, tipo_esperado):
        if self.componente_actual.categoria_componente is not tipo_esperado:
            print("Error: ", str(self.componente_actual))
            # raise SyntaxError (str(self.componente_actual))

        self.__pasar_siguiente_componente()

    def __pasar_siguiente_componente(self):
        """
        Pasa al siguiente componente léxico
        Esto revienta por ahora
        """
        self.posicion_componente_actual += 1
        if self.posicion_componente_actual >= self.cantidad_componentes:
            return
        self.componente_actual = \
            self.componentes_lexicos[self.posicion_componente_actual]

    def __componente_venidero(self, avance=1):
        """
        Retorna el componente léxico que está 'avance' posiciones más
        adelante... por default el siguiente. Esto sin adelantar el
        contador del componente actual.
        """
        return self.componentes_lexicos[self.posicion_componente_actual + avance]
