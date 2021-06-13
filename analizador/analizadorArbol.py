from explorador.CategoriaComponente import CategoriaComponente as TipoComponente
from explorador.ComponenteLexico import ComponenteLexico as ComponenteLexico
from utils.arbol.ArbolAbstracto import ArbolAbstracto as ArbolSintaxisAbstracta
from utils.arbol.NodoArbol import NodoArbol as NodoArbol
from utils.arbol.TipoNodo import TipoNodo


class Analizador:
    componentes_lexicos: list
    cantidad_componentes: int
    posicion_componente_actual: int
    componente_actual: ComponenteLexico
    contador_encapsulacion = 0

    def __init__(self, lista_componentes):

        self.componentes_lexicos = lista_componentes
        self.cantidad_componentes = len(lista_componentes)

        self.posicion_componente_actual = 0
        self.componente_actual = lista_componentes[0]

        self.asa = ArbolSintaxisAbstracta()

    def analizar(self):
        """
        Método principal que inicia el análisis siguiendo el esquema de
        análisis por descenso recursivo
        """
        self.asa.raiz = self.__analizar_programa()

    def imprimir_asa(self):
        """
        Imprime el árbol de sintáxis abstracta
        """

        if self.asa.raiz is None:
            print([])
        else:
            self.asa.imprimir_preorden()

    def __analizar_programa(self):
        """
        Programa ::= (Comentario | Asignación | Función)* Principal
        """

        nodos_nuevos = []

        while (True):
            if self.componente_actual.categoria_componente == TipoComponente.IDENTIFICADOR:

                nodos_nuevos = [self.__analizar_asignación()]

            # Si es función
            elif self.componente_actual.texto_componente == 'virus':
                nodos_nuevos += [self.__analizar_función()]
                
                #if self.posicion_componente_actual == self.cantidad_componentes and self.contador_encapsulacion != 0:
                #    print("ERROR INESPERADO!:     Te hacen falta }empalido")
                #elif self.contador_encapsulacion == 0 and self.posicion_componente_actual  != self.cantidad_componentes:
                #    print("ERROR INESPERADO!:     Tienes Exceso de }empalido")
                #print("~~~~ Fin del analisis de pandemico. ~~~~~")
                
                #return NodoArbol(TipoNodo.PROGRAMA, nodos=nodos_nuevos)
            else:
                break

        # De fijo al final una función principal
        if self.componente_actual.texto_componente in ['covid19']:
            nodos_nuevos += [self.__analizar_principal()]
        else:
            raise SyntaxError(str(self.componente_actual))
            # print("Error1: ", str(self.componente_actual))
            # self.componente_actual.texto_componente == '}empalido' and
            #if self.contador_encapsulacion == 0 and self.posicion_componente_actual + 1 != self.cantidad_componentes:
            #    print("ERROR INESPERADO!:     Tienes Exceso de }empalido")
            #print("~~~~ Fin del analisis de pandemico.... ~~~~~")

        return NodoArbol(TipoNodo.PROGRAMA, nodos=nodos_nuevos)

    def __analizar_asignación(self):
        """
        Asignación ::= Identificador metale ( Literal | ExpresiónMatemática | (Invocación | Identificador) )

        Acá también cambié la gramática
        """

        nodos_nuevos = []
        # El identificador en esta posición es obligatorio
        nodos_nuevos += [self.__verificar_identificador()]
        self.__verificar(':=')
        # Igual el métale
        if self.componente_actual.texto_componente == '@inyeccion':
            nodos_nuevos += [self.__analizar_concatenar()]

        elif self.componente_actual.texto_componente == '@pinchaso':
            nodos_nuevos += [self.__analizar_indice()]

        elif self.componente_actual.texto_componente == '@aguja':
            nodos_nuevos += [self.__analizar_largo()]

        elif self.componente_actual.texto_componente == '@antivirus':
            nodos_nuevos += [self.__analizar_solicitar()]

        elif self.componente_actual.texto_componente == '@curado':
            nodos_nuevos += [self.__analizar_convertir()]


        # El siguiente bloque es de opcionales
        elif self.componente_actual.categoria_componente in [TipoComponente.MOLECULA,
                                                             TipoComponente.MICROMOLECULA,
                                                             TipoComponente.MASCARILLA, TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_literal()]

        # los paréntesis obligatorios (es un poco feo)
        elif self.componente_actual.texto_componente == '(':
            nodos_nuevos += [self.__analizar_expresión_matemática()]

        # Acá tengo que decidir si es Invocación o solo un identificador
        elif self.componente_actual.categoria_componente == TipoComponente.IDENTIFICADOR:

            if self.__componente_venidero().texto_componente == '(':
                nodos_nuevos += [self.__analizar_invocación()]
            else:
                nodos_nuevos += [self.__verificar_identificador()]

        else:
            # raise SyntaxError('Viejo... acá algo reventó', self.componente_actual)
            self.__pasar_siguiente_componente()

        return NodoArbol(TipoNodo.ASIGNACION, nodos=nodos_nuevos)

    def __analizar_expresión_matemática(self):
        """
        ExpresiónMatemática ::= (Expresión) | Número | Identificador
        """

        nodos_nuevos = []

        # Primera opción
        if self.componente_actual.texto_componente == '(':

            # Los verificar no se incluyen por que son para forzar cierta
            # forma de escribir... pero no aportan nada a la semántica
            self.__verificar('(')

            nodos_nuevos += [self.__analizar_expresión()]

            self.__verificar(')')

        # Acá yo se que estan bien formados por que eso lo hizo el
        # explorador... es nada más revisar las posiciones.
        elif self.componente_actual.categoria_componente == TipoComponente.MASCARILLA:
            nodos_nuevos += [self.__verificar_valor_verdad()]

        elif self.componente_actual.categoria_componente == TipoComponente.MOLECULA:
            nodos_nuevos += [self.__verificar_entero()]

        elif self.componente_actual.categoria_componente == TipoComponente.MICROMOLECULA:
            nodos_nuevos += [self.__verificar_flotante()]

        elif self.componente_actual.categoria_componente == TipoComponente.RECETA:
            nodos_nuevos += [self.__verificar_texto()]

        else:
            nodos_nuevos += [self.__verificar_identificador()]

        return NodoArbol(TipoNodo.EXPRESION_MATEMATICA, nodos=nodos_nuevos, contenido="expresion matematica")

    def __analizar_expresión(self):
        """
        Expresión ::= ExpresiónMatemática Operador ExpresiónMatemática
        """

        nodos_nuevos = []

        nodos_nuevos += [self.__analizar_expresión_matemática()]
        '''Si encuentra un error en los operadores, lo indica y se lo brinca.'''
        if self.__analizar_error() == False:
            nodos_nuevos += [self.__verificar_operador()]
        else:
            self.__pasar_siguiente_componente()
        nodos_nuevos += [self.__analizar_expresión_matemática()]

        return NodoArbol(TipoNodo.EXPRESION, nodos=nodos_nuevos, contenido="expresion matematica")

    def __analizar_función(self):
        """
        Función ::= virus Identificador Parametros? :{ Instrucciones }empalido
        """
        nodos_nuevos = []
        # Comentario con doble check azul dela muerte... (ignorado)

        # Esta sección es obligatoria en este orden
        self.__verificar('virus')
        nodos_nuevos += [self.__verificar_identificador()]
        if self.componente_actual.texto_componente != ':{':
            nodos_nuevos += [self.__analizar_parámetros_función()]
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]
        # La función lleva el nombre del identificador
        return NodoArbol(TipoNodo.FUNCION, contenido="virus", nodos=nodos_nuevos)

    def __analizar_invocación(self):
        """
        Invocación ::= Identificador ( ParámetrosInvocación )
        """
        nodos_nuevos = []

        # todos son obligatorios en ese orden
        nodos_nuevos += [self.__verificar_identificador()]
        self.__verificar('(')
        nodos_nuevos += [self.__analizar_parámetros_invocación()]
        self.__verificar(')')

        return NodoArbol(TipoNodo.INVOCACION, nodos=nodos_nuevos, contenido="LlamadaFuncion")

    def __analizar_parámetros_función(self):
        """
        ParametrosFunción ::= Identificador (/ Identificador)+
        """
        nodos_nuevos = []

        # Fijo un valor tiene que haber
        if (self.__analizar_error() == False):
            nodos_nuevos += [self.__verificar_identificador()]
        else:
            self.__pasar_siguiente_componente()
        while self.componente_actual.texto_componente == ',':
            self.__verificar(',')
            if self.__analizar_error() == False:
                nodos_nuevos += [self.__verificar_identificador()]
            else:
                self.__pasar_siguiente_componente()

        return NodoArbol(TipoNodo.PARAMETROS_FUNCION, nodos=nodos_nuevos, contenido="parametrosContenidos")

    def __analizar_parámetros_invocación(self):
        """
        ParametrosInvocación ::= Valor (/ Valor)+
        """
        nodos_nuevos = []

        nodos_nuevos += [self.__analizar_valor()]

        while self.componente_actual.texto_componente == ',':
            self.__verificar(',')
            nodos_nuevos += [self.__analizar_valor()]

        return NodoArbol(TipoNodo.PARAMETROS_INVOCACION, nodos=nodos_nuevos, contenido="parametrosInvolucrados")

    def __analizar_instrucción(self):
        """
        Syntaxis Lenguaje Pandemico.
                Instrucciones ::= (Asignación | LlamadaFuncion ) | Identificador | RepetirWhile | RepetirFor |
                SiCondicional | Comentario | Retorno
        """
        nodos_nuevos = []
        if self.componente_actual.categoria_componente == TipoComponente.PALABRA_CLAVE:
            nodos_nuevos += [self.__verificar_palabra_clave()]
        # Acá todo con if por que son opcionales
        if self.componente_actual.texto_componente == 'cuarentena':
            nodos_nuevos += [self.__analizar_repetición()]

        if self.componente_actual.texto_componente == 'aislamiento':
            nodos_nuevos += [self.__analizar_repetición_FOR()]

        elif self.componente_actual.texto_componente == 'estornudo_acapela':
            nodos_nuevos += [self.__analizar_bifurcación()]

        elif self.componente_actual.categoria_componente == TipoComponente.IDENTIFICADOR:
            if self.__componente_venidero().texto_componente == ':=':
                nodos_nuevos += [self.__analizar_asignación()]
                return NodoArbol(TipoNodo.INSTRUCCION, nodos=nodos_nuevos, contenido='')
                #self.__analizar_instrucción()
            else:
                nodos_nuevos += [self.__analizar_invocación()]
        elif self.componente_actual.texto_componente == '@vacuna':
            nodos_nuevos += [self.__analizar_impresion()]

        elif self.componente_actual.texto_componente == '@vomito':
            nodos_nuevos += [self.__analizar_retorno()]


        else:  # Muy apropiado el chiste de ir a revisar si tiene error al último.
            nodos_nuevos += [self.__analizar_error()]
            self.__pasar_siguiente_componente()
            #### IMPORTANTE NO QUITAR.
            if self.componente_actual.categoria_componente == TipoComponente.ENCAPSULACION:
                return NodoArbol(TipoNodo.INSTRUCCION, nodos=nodos_nuevos)
            else:
                return self.__analizar_instrucción()

        return NodoArbol(TipoNodo.INSTRUCCION, nodos=nodos_nuevos)

    def __analizar_impresion(self):
        """
            Impresión ::= @ vacuna Identificador | Literal
        """
        nodos_nuevos = []
        self.__verificar('@vacuna')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,
                                                           TipoComponente.MOLECULA,
                                                           TipoComponente.MICROMOLECULA,
                                                           TipoComponente.MASCARILLA, TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]

        return NodoArbol(TipoNodo.IMPRESION, nodos=nodos_nuevos, contenido='@vacuna')

    def __analizar_indice(self):
        """
            Funcion preprogramada
        """
        nodos_nuevos = []
        self.__verificar('@pinchaso')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,
                                                           TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]
        self.__verificar(',')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,TipoComponente.MOLECULA]:
            nodos_nuevos += [self.__analizar_valor()]
        return NodoArbol(TipoNodo.INDICE, nodos=nodos_nuevos,contenido='@pinchaso')

    def __analizar_solicitar(self):
        """
            Funcion preprogramada
        """
        nodos_nuevos = []
        self.__verificar('@antivirus')
        return NodoArbol(TipoNodo.SOLICITAR, nodos=nodos_nuevos,contenido='@antivirus')

    def __analizar_largo(self):
        """
            Funcion preprogramada
        """
        nodos_nuevos = []
        self.__verificar('@aguja')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,
                                                           TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]
        return NodoArbol(TipoNodo.LARGO, nodos=nodos_nuevos,contenido='@aguja')

    def __analizar_convertir(self):
        """
            Funcion preprogramada
        """
        nodos_nuevos = []
        self.__verificar('@curado')
        if self.componente_actual.categoria_componente in [TipoComponente.MOLECULA,
                                                           TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]
        self.__verificar(',')
        if self.componente_actual.categoria_componente in [TipoComponente.MOLECULA,
                                                           TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]
        return NodoArbol(TipoNodo.CONVERTIR, nodos=nodos_nuevos,contenido='@curado')

    def __analizar_concatenar(self):
        """
            Funcion preprogramada
        """
        nodos_nuevos = []
        self.__verificar('@inyeccion')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]
        self.__verificar(',')
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,
                                                           TipoComponente.MOLECULA,
                                                           TipoComponente.MICROMOLECULA,
                                                           TipoComponente.MASCARILLA, TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]

        return NodoArbol(TipoNodo.CONCATENAR, nodos=nodos_nuevos, contenido='@inyeccion')

    def __analizar_repetición(self):
        """
        RepetirWhile ::= cuarentena ExpCondicional :{ Instrucciones+ }empalido
        """
        nodos_nuevos = []

        # Todos presentes en ese orden... sin opciones
        self.__verificar('cuarentena')
        nodos_nuevos += [self.__analizar_condición()]
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]
        return NodoArbol(TipoNodo.REPETIR_WHILE, nodos=nodos_nuevos, contenido='cuarentena')

    def __analizar_repetición_FOR(self):
        """
         RepetirFor ::= aislamiento Identificador Molécula, Molécula :{ Instrucciones+ }empalido
        """
        nodos_nuevos = []

        # Todos presentes en ese orden... sin opciones
        self.__verificar('aislamiento')
        nodos_nuevos += [self.__verificar_identificador()]
        nodos_nuevos += [self.__analizar_condición()]

        # Yo acá tengo dos elecciones... creo otro nivel con Bloque de
        # instrucciones o pongo directamente las instrucciones en este
        # nivel... yo voy con la primera por facilidad... pero eso hace más
        # grande el árbol
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]

        return NodoArbol(TipoNodo.REPETIR_FOR, nodos=nodos_nuevos, contenido='aislamiento')

    def __analizar_bifurcación(self):
        """
        Bifurcación ::= SiCondicional (Sino)?
        """
        nodos_nuevos = []

        # el sino es opcional
        nodos_nuevos += [self.__analizar_si()]

        if self.componente_actual.texto_componente == 'estornudo_tapado':
            nodos_nuevos += [self.__analizar_sino()]

        if self.componente_actual.texto_componente == 'me_capeo':
            nodos_nuevos += [self.__analizar_no()]
        # y sino era solo el 'diay siii'
        return NodoArbol(TipoNodo.BIFURCACION, nodos=nodos_nuevos)

    def __analizar_si(self):
        """
        SiCondicional ::= estornudo_acapela ExpCondicional :{ Instrucciones+ }empalido
        """
        nodos_nuevos = []

        # Todos presentes en ese orden... sin opciones
        self.__verificar('estornudo_acapela')
        nodos_nuevos += [self.__analizar_condición()]
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]

        return NodoArbol(TipoNodo.SI_CONDICIONAL, nodos=nodos_nuevos, contenido='estornudo_acapela')

    def __analizar_sino(self):
        """
        SinoCondicional ::= estornudo_tapado ExpCondicional :{ Instrucciones+ }empalido
        """

        nodos_nuevos = []

        # Todos presentes en ese orden... sin opciones
        self.__verificar('estornudo_tapado')
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]

        return NodoArbol(TipoNodo.SINO_CONDICIONAL, nodos=nodos_nuevos, contenido='estornudo_tapado')

    def __analizar_no(self):
        """
        NoCondicional ::= me_capeo :{ Instrucciones+ }empalido
        """
        nodos_nuevos = []
        self.__verificar('me_capeo')
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]
        return NodoArbol(TipoNodo.NO_CONDICIONAL, nodos=nodos_nuevos, contenido='me_capeo')

    def __analizar_condición(self):
        """
        ExpCondicional ::= Comparación ( (#yke | #oke ) Comparación)?
        """
        nodos_nuevos = []

        nodos_nuevos += [self.__analizar_comparación()]

        if self.componente_actual.categoria_componente == TipoComponente.PALABRA_CLAVE:

            if self.componente_actual.texto_componente == '#yke':
                nodo = NodoArbol(TipoNodo.OPERADOR_LOGICO, contenido='#yke')
                nodos_nuevos += [nodo]
                self.__verificar('#yke')

            else:  # Aquí hay potencial horrible para fallo
                nodo = NodoArbol(TipoNodo.OPERADOR_LOGICO, contenido='#oke')
                nodos_nuevos += [nodo]

                self.__verificar('#oke')

            # Un poco tieso, pero funcional
            nodos_nuevos += [self.__analizar_comparación()]

        # Si no ha reventado vamos bien
        return NodoArbol(TipoNodo.CONDICION, nodos=nodos_nuevos)

    def __analizar_comparación(self):
        """
         Comparación ::= (Identificador | Literal) Comparador (Identificador | Literal)
        """
        nodos_nuevos = []

        # Sin opciones, todo se analiza
        nodos_nuevos += [self.__analizar_valor()]
        nodos_nuevos += [self.__verificar_comparador()]
        nodos_nuevos += [self.__analizar_valor()]

        return NodoArbol(TipoNodo.COMPARACION, nodos=nodos_nuevos)

    def __analizar_valor(self):
        """
        Valor ::= (Identificador | Literal)
        """
        # Acá voy a cambiar el esquema de trabajo y voy a elminar algunos
        # niveles del árbol

        # El uno o el otro
        if self.componente_actual.categoria_componente is TipoComponente.IDENTIFICADOR:
            nodo = self.__verificar_identificador()
        else:
            nodo = self.__analizar_literal()

        return nodo

    def __analizar_retorno(self):
        """
        Retorno ::= @ vomito Identificador | Literal | LlamadaFunción
        """
        nodos_nuevos = []

        self.__verificar('@vomito')

        # Este hay que validarlo para evitar el error en caso de que no
        # aparezca
        if self.componente_actual.categoria_componente in [TipoComponente.IDENTIFICADOR,
                                                           TipoComponente.MOLECULA,
                                                           TipoComponente.MICROMOLECULA,
                                                           TipoComponente.MASCARILLA, TipoComponente.RECETA]:
            nodos_nuevos += [self.__analizar_valor()]

        return NodoArbol(TipoNodo.RETORNO, nodos=nodos_nuevos, contenido='@vomito')

    def __analizar_error(self):
        """
        4 tipos de errores 
        """
        nodos_nuevos = []

        # Sin opciones

        if self.componente_actual.categoria_componente in [TipoComponente.ERRORENCAPSULACION,
                                                           TipoComponente.ERRORPARAMETRO,
                                                           TipoComponente.ERRORFLOTANTE,
                                                           TipoComponente.ERRORVARIABLE]:
            print("ERROR INESPERADO!: ", self.componente_actual)
            return NodoArbol(TipoNodo.ERROR, nodos=nodos_nuevos, contenido='ERROR')
        # nodos_nuevos += [self.__analizar_valor()]

        return False

    def __analizar_principal(self):
        """
            Inicio ::= covid19 :{ Instrucciones+ }empalido
        """
        nodos_nuevos = []

        if self.componente_actual.texto_componente == 'covid19':
            self.__verificar('covid19')
            
        nodos_nuevos += [self.__analizar_bloque_instrucciones()]

        return NodoArbol(TipoNodo.PRINCIPAL, nodos=nodos_nuevos)

    def __analizar_literal(self):
        """
        Literal ::= Receta | Mascarilla
        evaluo, si es texto, booleano,
        """

        # Acá le voy a dar vuelta por que me da pereza tanta validación
        if self.componente_actual.categoria_componente is TipoComponente.RECETA:
            nodo = self.__verificar_texto()

        elif self.componente_actual.categoria_componente is TipoComponente.MASCARILLA:
            nodo = self.__verificar_valor_verdad()

        else:
            nodo = self.__analizar_número()

        return nodo

    def __analizar_número(self):
        """
        Número ::= (Entero | Flotante)
        """
        if self.componente_actual.categoria_componente == TipoComponente.MOLECULA:
            nodo = self.__verificar_entero()
        else:
            nodo = self.__verificar_flotante()
        return nodo

    def __analizar_bloque_instrucciones(self):
        """
        Este es nuevo y me lo inventé para simplicicar un poco el código...
        correspondería actualizar la gramática.

        BloqueInstrucciones ::= { Instrucción+ }
        """
        nodos_nuevos = []

        # Obligatorio]
        self.contador_encapsulacion += 1
        self.__verificar(':{')

        # mínimo una
        nodos_nuevos += [self.__analizar_instrucción()]
        self.__analizar_error()
        # Acá todo puede venir uno o más

        while self.componente_actual.texto_componente != '}empalido':
            nodos_nuevos += [self.__analizar_instrucción()]
        # Obligatorioself.__verificar('}empalido')
        if self.posicion_componente_actual <= self.cantidad_componentes:
            self.__verificar('}empalido')
            self.contador_encapsulacion -= 1

        return NodoArbol(TipoNodo.BLOQUE_INSTRUCCIONES, nodos=nodos_nuevos)

    # Todos estos verificar se pueden unificar =*=
    def __verificar_operador(self):
        """
        Operador ::= #mas | #quitar | #por | #cortar
        """
        self.__verificar_tipo_componente(TipoComponente.OPERADOR)

        nodo = NodoArbol(TipoNodo.OPERADOR, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()

        return nodo

    def __verificar_valor_verdad(self):
        """
        Mascarilla ::= #positivo | #negativo
        """
        self.__verificar_tipo_componente(TipoComponente.MASCARILLA)

        nodo = NodoArbol(TipoNodo.MASCARILLA, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_palabra_clave(self):
        """
        Palabra clave
        """
        self.__verificar_tipo_componente(TipoComponente.PALABRA_CLAVE)
        nodo = NodoArbol(TipoNodo.PALABRA_CLAVE, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_comparador(self):
        """
        ExpCondicional ::= Comparación ( (#yke | #oke ) Comparación)?
        """
        self.__verificar_tipo_componente(TipoComponente.COMPARADOR)
        nodo = NodoArbol(TipoNodo.COMPARADOR, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_texto(self):
        """
        Receta ::= <[a-z A-Z _ 0-9]+>
        """
        self.__verificar_tipo_componente(TipoComponente.RECETA)

        nodo = NodoArbol(TipoNodo.RECETA, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_entero(self):
        """
        Molécula ::= -?[0-9]+
        """
        self.__verificar_tipo_componente(TipoComponente.MOLECULA)

        nodo = NodoArbol(TipoNodo.MOLECULA, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_flotante(self):
        """
        Micromolécula ::= -?[0-9]+.[0-9]+
        """
        self.__verificar_tipo_componente(TipoComponente.MICROMOLECULA)

        nodo = NodoArbol(TipoNodo.MICROMOLECULA, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()
        return nodo

    def __verificar_identificador(self):
        """
        Verifica si el tipo del componente léxico actuales de tipo
        IDENTIFICADOR

        Identificador ::= [a-z][a-zA-Z0-9]+
        """


        self.__verificar_tipo_componente(TipoComponente.IDENTIFICADOR)

        nodo = NodoArbol(TipoNodo.IDENTIFICADOR, contenido=self.componente_actual.texto_componente)
        self.__pasar_siguiente_componente()

        return nodo

    def __verificar(self, texto_esperado):

        """
        Syntaxis Lenguaje Pandemico.
        Verifica veracicamente si lo que esta actualmente leyendo sea efectivamente
            lo pasado por parametro.
        Da error si no es el caso.
        """
        if texto_esperado == '}empalido' and self.posicion_componente_actual <= self.cantidad_componentes:
            pass

        elif self.componente_actual.texto_componente != texto_esperado:
            print()
            raise SyntaxError ((texto_esperado, str(self.componente_actual)))

        self.__pasar_siguiente_componente()

    def __verificar_tipo_componente(self, tipo_esperado):
        """
        Verifica un componente por tipo... no hace mucho pero es para
        centralizar el manejo de errores
        """

        if self.componente_actual.categoria_componente is not tipo_esperado:
            print()
            print("RECIBI: ", self.componente_actual.categoria_componente, "    ESPERABA: ", tipo_esperado)
            # raise SyntaxError((tipo_esperado, str(self.componente_actual)))
            print("Error3: ", str(self.componente_actual))
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
