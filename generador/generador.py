# Implementa el veficador de ciruelas

from utils.arbol import ArbolAbstracto
from generador.visitadores import VisitantePython


class Generador:
    asa: ArbolAbstracto
    visitador: VisitantePython

    ambiente_estandar = """import sys

def aguja(texto):
    return len(texto)

##################################### cambiar por funciones nuestras
def hacer_menjunje(texto1, texto2):
    return texto1 + texto2

def viene_bolita(texto, indice):
    return texto[indice]

def trome(texto):
    return len(texto)

def sueltele(texto):
    print(texto)

def echandi_jiménez():
    return input()
########################################################################## 
"""

    def __init__(self, nuevo_asa: ArbolAbstracto):

        self.asa = nuevo_asa
        self.visitador = VisitantePython()

    def imprimir_asa(self):
        """
        Imprime el árbol de sintáxis abstracta
        """

        if self.asa.raiz is None:
            print([])
        else:
            self.asa.imprimir_preorden()

    def generar(self):
        resultado = self.visitador.visitar(self.asa.raiz)
        print(self.ambiente_estandar)
        print(resultado)
