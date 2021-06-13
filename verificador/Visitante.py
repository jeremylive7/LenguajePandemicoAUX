from utils.arbol.TipoNodo import TipoNodo
from verificador.TablaSimbolos import TablaSimbolos
from utils.tipos import Tipos


class Visitante:
    tabla_simbolos: TablaSimbolos

    def __init__(self, tabla_simbolos):
        self.tabla_simbolos = tabla_simbolos

    def visitar(self, nodo: TipoNodo):
        if nodo.tipo is TipoNodo.PROGRAMA:
            self.__visitar_programa(nodo)

        elif nodo.tipo is TipoNodo.ASIGNACION:
            self.__visitar_asignación(nodo)

        elif nodo.tipo is TipoNodo.EXPRESION_MATEMATICA:
            self.__visitar_expresión_matemática(nodo)

        elif nodo.tipo is TipoNodo.EXPRESION:
            self.__visitar_expresión(nodo)

        elif nodo.tipo is TipoNodo.FUNCION:
            self.__visitar_función(nodo)

        elif nodo.tipo is TipoNodo.INVOCACION:
            self.__visitar_invocación(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS_INVOCACION:
            self.__visitar_parámetros_invocación(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS_FUNCION:
            self.__visitar_parámetros_función(nodo)

        elif nodo.tipo is TipoNodo.INSTRUCCION:
            self.__visitar_instrucción(nodo)

        elif nodo.tipo is TipoNodo.REPETIR_WHILE:
            self.__visitar_REPETIR_WHILE(nodo)

        elif nodo.tipo is TipoNodo.REPETIR_FOR:
            self.__visitar_REPETIR_WHILE(nodo)

        elif nodo.tipo is TipoNodo.BIFURCACION:
            self.__visitar_bifurcación(nodo)

        elif nodo.tipo is TipoNodo.SI_CONDICIONAL:
            self.__visitar_SI_CONDICIONAL(nodo)

        elif nodo.tipo is TipoNodo.SINO_CONDICIONAL:
            self.__visitar_SINO_CONDICIONAL(nodo)

        elif nodo.tipo is TipoNodo.NO_CONDICIONAL:  # nuevo
            self.__visitar_no_condicional(nodo)

        elif nodo.tipo is TipoNodo.OPERADOR_LOGICO:
            self.__visitar_operador_logico(nodo)

        elif nodo.tipo is TipoNodo.CONDICION:
            self.__visitar_condición(nodo)

        elif nodo.tipo is TipoNodo.COMPARACION:
            self.__visitar_comparación(nodo)

        elif nodo.tipo is TipoNodo.RETORNO:
            self.__visitar_retorno(nodo)

        elif nodo.tipo is TipoNodo.ERROR:
            self.__visitar_error(nodo)

        elif nodo.tipo is TipoNodo.PRINCIPAL:
            self.__visitar_principal(nodo)

        elif nodo.tipo is TipoNodo.BLOQUE_INSTRUCCIONES:
            self.__visitar_bloque_instrucciones(nodo)

        elif nodo.tipo is TipoNodo.OPERADOR:
            self.__visitar_operador(nodo)

        elif nodo.tipo is TipoNodo.MASCARILLA:
            self.__visitar_MASCARILLA(nodo)

        elif nodo.tipo is TipoNodo.COMPARADOR:
            self.__visitar_comparador(nodo)

        elif nodo.tipo is TipoNodo.RECETA:
            self.__visitar_RECETA(nodo)

        elif nodo.tipo is TipoNodo.MOLECULA:
            self.__visitar_entero(nodo)

        elif nodo.tipo is TipoNodo.MICROMOLECULA:
            self.__visitar_MICROMOLECULA(nodo)

        elif nodo.tipo is TipoNodo.IDENTIFICADOR:
            self.__visitar_identificador(nodo)

        elif nodo.tipo is TipoNodo.PALABRA_CLAVE:  # nuevo
            self.__visitar_palabra_clave(nodo)

        elif nodo.tipo is TipoNodo.LARGO:  # nuevo
            self.__visitar_largo(nodo)

        elif nodo.tipo is TipoNodo.INDICE:  # nuevo
            self.__visitar_indice(nodo)

        elif nodo.tipo is TipoNodo.CONCATENAR:  # nuevo
            self.__visitar_concatenar(nodo)

        else:
            raise Exception('Error')

    def __visitar_programa(self, nodo_actual):

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

    def __visitar_asignación(self, nodo_actual):
        self.tabla_simbolos.nuevo_registro(nodo_actual.nodos[0])

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = nodo_actual.nodos[1].atributos['tipo']
        nodo_actual.nodos[0].atributos['tipo'] = nodo_actual.nodos[1].atributos['tipo']

    def __visitar_expresión_matemática(self, nodo_actual):
        for nodo in nodo_actual.nodos:

            if nodo.tipo == TipoNodo.IDENTIFICADOR:
                registro = self.tabla_simbolos.verificar_existencia(nodo.contenido)

            nodo.visitar(self)
        nodo_actual.atributos['tipo'] = Tipos.MOLECULA

    def __visitar_expresión(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = Tipos.MOLECULA

    def __visitar_función(self, nodo_actual):
        self.tabla_simbolos.nuevo_registro(nodo_actual)

        self.tabla_simbolos.abrir_bloque()

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        self.tabla_simbolos.cerrar_bloque()
        nodo_actual.atributos['tipo'] = nodo_actual.nodos[2].atributos['tipo']

    def __visitar_invocación(self, nodo_actual):
        registro = self.tabla_simbolos.verificar_existencia(nodo_actual.nodos[0].contenido)
        if registro['referencia'].tipo != TipoNodo.FUNCIÓN:
            raise Exception('Esa vara es una variable...', registro)

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        nodo_actual.atributos['tipo'] = registro['referencia'].atributos['tipo']

    def __visitar_parámetros_invocación(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            if nodo.tipo == TipoNodo.IDENTIFICADOR:
                registro = self.tabla_simbolos.verificar_existencia(nodo.contenido)

            elif nodo.tipo == TipoNodo.FUNCIÓN:
                raise Exception('Esa vara es una función...', nodo.contenido)  # TODO: cambiar

            nodo.visitar(self)

    def __visitar_parámetros_función(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            self.tabla_simbolos.nuevo_registro(nodo)
            nodo.visitar(self)

    def __visitar_instrucción(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
            nodo_actual.atributos['tipo'] = nodo.atributos['tipo']

    def __visitar_REPETIR_WHILE(self, nodo_actual):
        self.tabla_simbolos.abrir_bloque()

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        self.tabla_simbolos.cerrar_bloque()
        nodo_actual.atributos['tipo'] = nodo_actual.nodos[1].atributos['tipo']

    def __visitar_bifurcación(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA

    def __visitar_SI_CONDICIONAL(self, nodo_actual):
        self.tabla_simbolos.abrir_bloque()

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        self.tabla_simbolos.cerrar_bloque()
        nodo_actual.atributos['tipo'] = nodo_actual.nodos[1].atributos['tipo']

    def __visitar_SINO_CONDICIONAL(self, nodo_actual):
        self.tabla_simbolos.abrir_bloque()

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        self.tabla_simbolos.cerrar_bloque()
        nodo_actual.atributos['tipo'] = nodo_actual.nodos[0].atributos['tipo']

    def __visitar_no_condicional(self, nodo_actual):
        self.tabla_simbolos.abrir_bloque()

        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        self.tabla_simbolos.cerrar_bloque()

        nodo_actual.atributos['tipo'] = nodo_actual.nodos[0].atributos['tipo']

    def __visitar_condición(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        nodo_actual.atributos['tipo'] = Tipos.MASCARILLA

    def __visitar_comparación(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            if nodo.tipo == TipoNodo.IDENTIFICADOR:
                registro = self.tabla_simbolos.verificar_existencia(nodo.contenido)

            nodo.visitar(self)

        valor_izq = nodo_actual.nodos[0]
        comparador = nodo_actual.nodos[1]
        valor_der = nodo_actual.nodos[2]

        if valor_izq.atributos['tipo'] == valor_der.atributos['tipo']:
            comparador.atributos['tipo'] = valor_izq.atributos['tipo']
            nodo_actual.atributos['tipo'] = Tipos.MASCARILLA

        elif valor_izq.atributos['tipo'] == Tipos.CUALQUIERA or \
                valor_der.atributos['tipo'] == Tipos.CUALQUIERA:

            comparador.atributos['tipo'] = Tipos.CUALQUIERA

            nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA

        else:
            raise Exception('Papo, algo tronó acá', str(nodo_actual))

    def __visitar_retorno(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        if nodo_actual.nodos == []:
            nodo_actual.atributos['tipo'] = Tipos.NINGUNO

        else:
            for nodo in nodo_actual.nodos:
                nodo.visitar(self)
                if nodo.tipo == TipoNodo.IDENTIFICADOR:
                    registro = self.tabla_simbolos.verificar_existencia(nodo.contenido)
                    nodo_actual.atributos['tipo'] = registro['referencia'].atributos['tipo']
                else:
                    nodo_actual.atributos['tipo'] = nodo.atributos['tipo']

    def __visitar_error(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            if nodo.tipo == TipoNodo.IDENTIFICADOR:
                self.tabla_simbolos.verificar_existencia(nodo.contenido)

        nodo_actual.atributos['tipo'] = Tipos.NINGUNO

    def __visitar_principal(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = nodo_actual.nodos[0].atributos['tipo']

    def __visitar_bloque_instrucciones(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)
        nodo_actual.atributos['tipo'] = Tipos.NINGUNO

        for nodo in nodo_actual.nodos:
            if nodo.atributos['tipo'] != Tipos.NINGUNO:
                nodo_actual.atributos['tipo'] = nodo.atributos['tipo']

    def __visitar_operador(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.MOLECULA

    def __visitar_MASCARILLA(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.MASCARILLA

    def __visitar_comparador(self, nodo_actual):
        if nodo_actual.contenido not in ['#mismoke', '#nadakever']:
            nodo_actual.atributos['tipo'] = Tipos.MOLECULA
        else:
            nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA

    def __visitar_RECETA(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.RECETA

    def __visitar_entero(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.MOLECULA

    def __visitar_MICROMOLECULA(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.MICROMOLECULA

    def __visitar_identificador(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA

    def __visitar_palabra_clave(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA  # TODO: verificar

    def __visitar_largo(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA  # TODO: verificar

    def __visitar_indice(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA  # TODO: verificar

    def __visitar_concatenar(self, nodo_actual):
        for nodo in nodo_actual.nodos:
            nodo.visitar(self)

        nodo_actual.atributos['tipo'] = Tipos.CUALQUIERA  # TODO: verificar

    def __visitar_operador_logico(self, nodo_actual):
        nodo_actual.atributos['tipo'] = Tipos.MASCARILLA  # TODO: verificar
