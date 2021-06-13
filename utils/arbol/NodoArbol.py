import copy

from utils.arbol import TipoNodo


class NodoArbol:
    tipo: TipoNodo
    nodos: list
    contenido: str
    atributos: dict

    def __init__(self, tipo, contenido=None, nodos=None, atributos=None):

        if atributos is None:
            atributos = {}
        if nodos is None:
            nodos = []

        self.tipo = tipo
        self.contenido = contenido
        self.nodos = nodos
        self.atributos = copy.deepcopy(atributos)

    def visitar(self, visitante):
        return visitante.visitar(self)

    def __str__(self):

        # Coloca la información del nodo
        resultado = '{:30}\t\t'.format(self.tipo)

        if self.contenido is not None:
            resultado += '{:30}\t'.format(self.contenido)
        else:
            resultado += '{:30}\t'.format('')

        if self.atributos != {}:
            resultado += '{:38}\t'.format(str(self.atributos))
        else:
            resultado += '{:38}\t'.format('')

        if self.nodos:
            resultado += '<'

            # Imprime los tipos de los nodos del nivel siguiente
            for nodo in self.nodos[:-1]:
                if nodo is not None:
                    resultado += '{},'.format(nodo.tipo)

            resultado += '{}'.format(self.nodos[-1].tipo)
            resultado += '>'

        return resultado
