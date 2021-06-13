from utils.arbol.TipoNodo import TipoNodo


class VisitantePython:
    tabuladores = 0

    def visitar(self, nodo: TipoNodo):

        resultado = ''

        if nodo.tipo is TipoNodo.PROGRAMA:
            resultado = self.__visitar_programa(nodo)

        elif nodo.tipo is TipoNodo.ASIGNACION:
            resultado = self.__visitar_asignacion(nodo)

        elif nodo.tipo is TipoNodo.EXPRESION_MATEMATICA:
            resultado = self.__visitar_expresion_matematica(nodo)

        elif nodo.tipo is TipoNodo.EXPRESION:
            resultado = self.__visitar_expresion(nodo)

        elif nodo.tipo is TipoNodo.FUNCION:
            resultado = self.__visitar_funcion(nodo)

        elif nodo.tipo is TipoNodo.INVOCACION:
            resultado = self.__visitar_invocacion(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS_INVOCACION:
            resultado = self.__visitar_parametros_invocacion(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS_FUNCION:
            resultado = self.__visitar_parametros_funcion(nodo)

        elif nodo.tipo is TipoNodo.INSTRUCCION:
            resultado = self.__visitar_instruccion(nodo)

        elif nodo.tipo is TipoNodo.REPETIR_WHILE:
            resultado = self.__visitar_repeticion_while(nodo)
            print("------Prueba:\n" + resultado + "\n-----------------\n")

        elif nodo.tipo is TipoNodo.BIFURCACION:
            resultado = self.__visitar_bifurcacion(nodo)

        elif nodo.tipo is TipoNodo.SI_CONDICIONAL:
            resultado = self.__visitar_SI_CONDICIONAL(nodo)

        elif nodo.tipo is TipoNodo.SINO_CONDICIONAL:
            resultado = self.__visitar_SINO_CONDICIONAL(nodo)

        elif nodo.tipo is TipoNodo.NO_CONDICIONAL:
            resultado = self.__visitar_no_condicional(nodo)

        elif nodo.tipo is TipoNodo.OPERADOR_LOGICO:
            resultado = self.__visitar_operador_logico(nodo)

        elif nodo.tipo is TipoNodo.CONDICION:
            resultado = self.__visitar_condicion(nodo)

        elif nodo.tipo is TipoNodo.COMPARACION:
            resultado = self.__visitar_comparacion(nodo)

        elif nodo.tipo is TipoNodo.RETORNO:
            resultado = self.__visitar_retorno(nodo)

        elif nodo.tipo is TipoNodo.ERROR:
            resultado = self.__visitar_error(nodo)

        elif nodo.tipo is TipoNodo.PRINCIPAL:
            resultado = self.__visitar_principal(nodo)

        elif nodo.tipo is TipoNodo.BLOQUE_INSTRUCCIONES:
            resultado = self.__visitar_bloque_instrucciones(nodo)

        elif nodo.tipo is TipoNodo.OPERADOR:
            resultado = self.__visitar_operador(nodo)

        elif nodo.tipo is TipoNodo.MASCARILLA:
            resultado = self.__visitar_MASCARILLA(nodo)

        elif nodo.tipo is TipoNodo.COMPARADOR:
            resultado = self.__visitar_comparador(nodo)

        elif nodo.tipo is TipoNodo.RECETA:
            resultado = self.__visitar_RECETA(nodo)

        elif nodo.tipo is TipoNodo.MOLECULA:
            resultado = self.__visitar_MOLECULA(nodo)

        elif nodo.tipo is TipoNodo.MICROMOLECULA:
            resultado = self.__visitar_MICROMOLECULA(nodo)

        elif nodo.tipo is TipoNodo.IDENTIFICADOR:
            resultado = self.__visitar_identificador(nodo)

        elif nodo.tipo is TipoNodo.PALABRA_CLAVE:
            resultado = self.__visitar_palabra_clave(nodo)

        elif nodo.tipo is TipoNodo.LARGO:
            resultado = self.__visitar_largo(nodo)

        elif nodo.tipo is TipoNodo.INDICE:
            resultado = self.__visitar_indice(nodo)

        elif nodo.tipo is TipoNodo.CONCATENAR:
            resultado = self.__visitar_concatenar(nodo)

        else:
            raise Exception('Error: el tipo del nodo no fue encontrado :O')

        return resultado

    def __visitar_programa(self, nodo_actual):
        instrucciones = []
        # Se ignoran los comentarios

        for nodo in nodo_actual.nodos:
            instrucciones.append(nodo.visitar(self))

        return '\n'.join(instrucciones)

    def __visitar_asignacion(self, nodo_actual):
        """
        Asignación ::= Identificador metale (Identificador | Literal | ExpresiónMatemática | Invocación )
        """

        resultado = """{} = {}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones.append(nodo.visitar(self))

        return resultado.format(instrucciones[0], instrucciones[1])

    def __visitar_expresion_matematica(self, nodo_actual):
        """
        ExpresiónMatemática ::= (Expresión) | Número | Identificador

        Ojo esto soportaría un texto
        """

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return ' '.join(instrucciones)

    def __visitar_expresion(self, nodo_actual):
        """
        Expresión ::= ExpresiónMatemática Operador ExpresiónMatemática
        """

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return ' '.join(instrucciones)

    def __visitar_funcion(self, nodo_actual):
        """
        Función ::= (Comentario)? mae Identificador (ParámetrosFunción) BloqueInstrucciones
        """

        resultado = """\ndef {}({}):\n{}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return resultado.format(instrucciones[0], instrucciones[1], '\n'.join(instrucciones[2]))

    def __visitar_invocacion(self, nodo_actual):
        """
        Invocación ::= Identificador ( ParámetrosInvocación )
        """

        resultado = """{}({})"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return resultado.format(instrucciones[0], instrucciones[1])

    def __visitar_parametros_invocacion(self, nodo_actual):
        """
        ParámetrosInvocación ::= Valor (/ Valor)+
        """
        parameters = []

        for nodo in nodo_actual.nodos:
            parameters.append(nodo.visitar(self))

        if len(parameters) > 0:
            return ','.join(parameters)

        else:
            return ''

    def __visitar_parametros_funcion(self, nodo_actual):
        """
        ParámetrosFunción ::= Identificador (/ Identificador)+
        """

        parameters = []

        for nodo in nodo_actual.nodos:
            parameters.append(nodo.visitar(self))

        if len(parameters) > 0:
            return ' '.join(parameters)

        else:
            return ''

    def __visitar_instruccion(self, nodo_actual):
        """
        Instrucción ::= (Repetición | Bifurcación | (Asignación | Invocación) | Retorno | Error | Comentario )
        """

        valor = ""

        for nodo in nodo_actual.nodos:
            valor = nodo.visitar(self)

        return valor

    def __visitar_repeticion_while(self, nodo_actual):
        """
        Repetición ::= upee ( Condición ) BloqueInstrucciones
        """

        resultado = """while {}:\n{}"""

        instrucciones = []

        # Visita la condición
        for nodo in nodo_actual.nodos:
            instrucciones.append(nodo.visitar(self))

        return resultado.format(instrucciones[0], '\n'.join(instrucciones[1]))

    def __visitar_bifurcacion(self, nodo_actual):
        """
        Bifurcación ::= DiaySi (Sino)?
        """

        resultado = """{}{}"""

        instrucciones = []

        # Visita los dos nodos en el siguiente nivel si los hay
        for nodo in nodo_actual.nodos:
            instrucciones.append(nodo.visitar(self))

        return resultado.format(instrucciones[0], '')

    def __visitar_SI_CONDICIONAL(self, nodo_actual):
        """
        DiaySi ::= diay siii ( Condición ) BloqueInstrucciones
        """

        resultado = """if {}:\n{}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones.append(nodo.visitar(self))

        return resultado.format(instrucciones[0], '\n'.join(instrucciones[1]))

    def __visitar_SINO_CONDICIONAL(self, nodo_actual):
        """
        Sino ::= sino ni modo BloqueInstrucciones
        """

        resultado = """elif:\n  {}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return resultado.format('\n'.join(instrucciones[0]))

    def __visitar_no_condicional(self, nodo_actual):
        """
        Sino ::= sino ni modo BloqueInstrucciones
        """

        resultado = """else:\n  {}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return resultado.format('\n'.join(instrucciones[0]))

    def __visitar_condicion(self, nodo_actual):
        """
        Condición ::= Comparación ((divorcio|casorio) Comparación)?
        """

        resultado = """{} {} {}"""

        instrucciones = []

        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        if len(instrucciones) == 1:
            return resultado.format(instrucciones[0], '', '')
        else:
            return resultado.format(instrucciones[0], instrucciones[1], instrucciones[2])

    def __visitar_comparacion(self, nodo_actual):
        """
        Comparación ::= Valor Comparador Valor
        """

        resultado = '{} {} {}'

        elementos = []

        # Si los 'Valor' son identificadores se asegura que existan (IDENTIFICACIÓN)
        for nodo in nodo_actual.nodos:
            elementos.append(nodo.visitar(self))

        return resultado.format(elementos[0], elementos[1], elementos[2])

    def __visitar_valor(self, nodo_actual):
        """
        Valor ::= (Identificador | Literal)
        """
        # En realidad núnca se va a visitar por que lo saqué del árbol
        # duránte la etapa de análisiss

    def __visitar_retorno(self, nodo_actual):
        """
        Retorno :: sarpe (Valor)?
        """

        resultado = 'return {}'
        valor = ''

        for nodo in nodo_actual.nodos:
            valor = nodo.visitar(self)

        return resultado.format(valor)

    def __visitar_error(self, nodo_actual):
        """
        Error ::= safis Valor
        """
        resultado = 'print("\033[91m", {}, "\033[0m", file=sys.stderr)'
        valor = ''

        # Verifico si 'Valor' es un identificador que exista (IDENTIFICACIÓN)
        for nodo in nodo_actual.nodos:
            valor = nodo.visitar(self)

        return resultado.format(valor)

    def __visitar_principal(self, nodo_actual):
        """
        Principal ::= (Comentario)?  (jefe | jefa) mae BloqueInstrucciones
        """
        # Este mae solo va a tener un bloque de instrucciones que tengo que
        # ir a visitar

        resultado = """\ndef covid19():\n{}\n\nif __name__ == '__main__':\n\tprincipal()"""

        instrucciones = []

        # Lo pongo así por copy/paste... pero puede ser como el comentario
        # de más abajo.
        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        return resultado.format('\n'.join(instrucciones[0]))

    def __visitar_literal(self, nodo_actual):
        """
        Literal ::= (Número | Texto | ValorVerdad)
        """
        # En realidad núnca se va a visitar por que lo saqué del árbol
        # duránte la etapa de análisiss

    def __visitar_numero(self, nodo_actual):
        """
        Número ::= (Entero | Flotante)
        """
        # En realidad núnca se va a visitar por que lo saqué del árbol
        # duránte la etapa de análisiss

    def __visitar_bloque_instrucciones(self, nodo_actual):
        """
        BloqueInstrucciones ::= { Instrucción+ }
        """
        self.tabuladores += 2

        instrucciones = []

        # Visita todas las instrucciones que contiene
        for nodo in nodo_actual.nodos:
            instrucciones += [nodo.visitar(self)]

        instrucciones_tabuladas = []

        for instruccion in instrucciones:
            instrucciones_tabuladas += [self.__retornar_tabuladores() + instruccion]

        self.tabuladores -= 2

        return instrucciones_tabuladas

    def __visitar_operador(self, nodo_actual):
        """
        Operador ::= (echele | quitele | chuncherequee | desmadeje)
        """
        if nodo_actual.contenido == '#mas':
            return '+'

        elif nodo_actual.contenido == '#quitar':
            return '-'

        elif nodo_actual.contenido == '#por':
            return '*'

        elif nodo_actual.contenido == '#cortar':
            return '/'

        else:
            # Nunca llega aquí  
            return 'jijiji'

    def __visitar_MASCARILLA(self, nodo_actual):
        """
        ValorVerdad ::= (True | False)
        """
        return nodo_actual.contenido

    def __visitar_comparador(self, nodo_actual):
        if nodo_actual.contenido == '#mayorke':
            return '>'

        elif nodo_actual.contenido == '#menorke':
            return '<'

        elif nodo_actual.contenido == '#mismoke':
            return '=='

        elif nodo_actual.contenido == '#nadakever':
            return '!='

        else:
            # Nunca llega aquí  
            return 'jojojo'

    def __visitar_RECETA(self, nodo_actual):
        """
        Texto ::= ~/\w(\s\w)*)?~
        """
        return nodo_actual.contenido.replace('<', '"').replace('>', '"')

    def __visitar_MOLECULA(self, nodo_actual):
        """
        Entero ::= (-)?\d+
        """
        return nodo_actual.contenido

    def __visitar_MICROMOLECULA(self, nodo_actual):
        """
        Flotante ::= (-)?\d+.(-)?\d+
        """
        return nodo_actual.contenido

    def __visitar_identificador(self, nodo_actual):
        """
        Identificador ::= [a-z][a-zA-Z0-9]+
        """
        return nodo_actual.contenido

    def __retornar_tabuladores(self):
        return " " * self.tabuladores

    def __visitar_operador_logico(self, nodo_actual):  # TODO
        return 'aqui 1'

    def __visitar_palabra_clave(self, nodo_actual):  # TODO
        return 'aqui 2'

    def __visitar_largo(self, nodo_actual):  # DONE
        return 'aguja({})'.format(nodo_actual.nodos[0].contenido)

    def __visitar_indice(self, nodo_actual):  # TODO
        return 'aqui 3'

    def __visitar_concatenar(self, nodo_actual):  # TODO
        return 'aqui 4'
