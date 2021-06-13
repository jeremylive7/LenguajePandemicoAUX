from utils.arbol.NodoArbol import NodoArbol


class ArbolAbstracto:
    raiz: NodoArbol

    def imprimir_preorden(self):
        """
        Función que llama a función auxiliar recursiva para imprimir arbol en preorden
        """
        self.__preorden(self.raiz)

    def __preorden(self, nodo):
        """
        Función auxiliar recursiva para imprimir arbol en preorden
        @param nodo: nodo actual
        """
        print(nodo)
        if nodo is not None:
            for nodo in nodo.nodos:
                self.__preorden(nodo)
