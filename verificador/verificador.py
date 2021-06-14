from utils.arbol import ArbolAbstracto, NodoArbol
from utils.arbol.TipoNodo import TipoNodo
from verificador.Visitante import Visitante
from verificador.TablaSimbolos import TablaSimbolos


class Verificador:
    asa: ArbolAbstracto
    visitador: Visitante
    tabla_simbolos: TablaSimbolos

    def __init__(self, nuevo_asa: ArbolAbstracto):

        self.asa = nuevo_asa

        self.tabla_simbolos = TablaSimbolos()

        self.__cargar_ambiente_estándar()

        self.visitador = Visitante(self.tabla_simbolos)

    def __cargar_ambiente_estándar(self):
        # funciones de decoracion del arbol
        funciones_estandar = [
            ('los pigmentos son parecidos', TipoNodo.ASIGNACION),
            ('La estructura viral', TipoNodo.FUNCION),
            ('Aca esta la letra de doctor', TipoNodo.IDENTIFICADOR),
            ('Se le necesita en urgencias ', TipoNodo.LLAMADA_FUNCION),
            ('Una tableta de', TipoNodo.PARAMETROS_FUNCION),
            ('Llamada urgente para', TipoNodo.PARAMETROS_INVOCACION),
            ('Tapece la boca', TipoNodo.SI_CONDICIONAL),
            ('Lavese las manos despues de esto', TipoNodo.SINO_CONDICIONAL),
            ('a 2 metros de distancia para evitar contagio', TipoNodo.NO_CONDICIONAL),
            ('El doctor recomienda', TipoNodo.INSTRUCCION),
            ('El gobierno mantiene restricciones', TipoNodo.REPETIR_WHILE),
            ('El gobierno tiene restriccion de placas', TipoNodo.REPETIR_FOR),
            ('Se solicita al Doctor Logica a operaciones', TipoNodo.OPERADOR_LOGICO),
            ('Formula de la medicina', TipoNodo.EXPRESION_MATEMATICA),
            ('Llamada de emergencia', TipoNodo.INVOCACION),
            ('Corte de paciente de grado', TipoNodo.BIFURCACION),
            ('Mensaje urgente para', TipoNodo.EXPRESION),
            ('El libro de medicina dice', TipoNodo.CONDICION),
            ('Son los mismos padecimientos que', TipoNodo.COMPARACION),
            ('Regurgitar', TipoNodo.RETORNO),
            ('Se complico el paciente', TipoNodo.ERROR),
            ('Dr Medico Cirujano', TipoNodo.PRINCIPAL),
            ('Los documentos del paciente son', TipoNodo.BLOQUE_INSTRUCCIONES),
            ('Necesitamos Operar de imnediato', TipoNodo.OPERADOR),
            ('N95', TipoNodo.MASCARILLA),
            ('Esta formula es igual que', TipoNodo.COMPARADOR),
            ('tome cada 2 dias un poco de', TipoNodo.RECETA),
            ('SARS-COV-2', TipoNodo.MOLECULA),
            ('COV-2', TipoNodo.MICROMOLECULA),
            ('', TipoNodo.PALABRA_CLAVE),
            ('Dictamen medico', TipoNodo.IMPRESION),
            ('tomese tambien un poco de', TipoNodo.CONCATENAR),
            ('Cantidad de pastillas', TipoNodo.INDICE),
            ('mililitros', TipoNodo.LARGO),
            ('Consultar', TipoNodo.SOLICITAR),
            ('En lugar de tomar esto puede tomar de', TipoNodo.CONVERTIR)
        ]

        for nombre, tipo in funciones_estandar:
            nodo = NodoArbol(TipoNodo.FUNCION, contenido=nombre, atributos={'tipo': tipo})
            self.tabla_simbolos.nuevo_registro(nodo)

    def verificar(self):
        self.visitador.visitar(self.asa.raiz)

    def imprimir_asa(self):
        if self.asa.raiz is None:
            print([])
        else:
            self.asa.imprimir_preorden()
