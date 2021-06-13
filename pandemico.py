# Archivo principal para el compilador pandemico

# -----------------------------------  IMPORTS  -----------------------------------
from utils import archivos  # carga los archivos de prueba y los corta.
from explorador.ExploradorDeComponentes import ExploradorDeComponentes  # Explorador
from analizador.analizadorArbol import Analizador
from explorador.CategoriaComponente import CategoriaComponente as TipoComponente
from generador.generador import Generador

# Para pruebas
from verificador.verificador import Verificador

if __name__ == '__main__':
    texto = archivos.cargar_archivo("./docs/ejemplos/holamundo.covid")
    exp = ExploradorDeComponentes(texto)
    print("------------------------ EXPLORADOR --------------------------------")
    exp.explorar()
    exp.imprimir_componentes()

    print("------------------------ ANALIZADOR --------------------------------")
    # analizador = Analizador(exp.lista_de_tokens, TipoComponente)
    analizador = Analizador(exp.lista_de_tokens)
    analizador.analizar()
    analizador.imprimir_asa()

    print("\n\n------------------------ VERIFICADOR --------------------------------")
    verificador = Verificador(analizador.asa)
    verificador.verificar()
    verificador.imprimir_asa()

    print("\n\n------------------------ Generador --------------------------------")

    generador = Generador(verificador.asa)
    generador.generar()
