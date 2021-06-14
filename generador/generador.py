# Implementa el veficador de ciruelas

from utils.arbol import ArbolAbstracto
from generador.visitadores import VisitantePython


class Generador:
    asa: ArbolAbstracto
    visitador: VisitantePython

    ambiente_estandar = """

def aguja(texto):
    return len(texto)

def pinchaso(sms, param):
    if param == "convertir":
        return 'list('+param+')'
    elif param == "imprimir"
        return '"".join('+param+')'
    return "error"

def antivirus(inicio, final):
    return random.randint(inicio, final);

def inyeccion(num1, num2):
    return num1 + num2

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
