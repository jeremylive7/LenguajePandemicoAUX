# ESTA ES LA ETAPA DE EXPLORACION
# Desde este archivo se importa los demas archivos que componen la carpeta del explorador.
# Ademas es en este archivo donde ocurre el proceso de analisis, el resto de clases
# son auxiliares.

# -----------------------------------  IMPORTS LAS CLASES  -----------------------------------
from explorador.CategoriaComponente import CategoriaComponente
from explorador.ComponenteLexico import ComponenteLexico
from explorador.DescriptoresComponentes import DescriptoresComponentes
from explorador.AtributoComponente import AtributoComponente
import re

class ExploradorDeComponentes:
    ''' constructor
    La linea de texto.
    Aqui almacenare el resultado.
    '''
    def __init__(self, contenido_archivo):
        self.linea_de_texto = contenido_archivo  
        self.lista_de_tokens = []  

    ''' Esta funcion se encarga de trocear el texto en lineas procesables.
    conteo de linea, para manejo de errores
    cojo el texto y le saco todas las lineas
    tengo la linea, pues la proceso.
    agrego la linea procesada a la lista de tokens(resultado).
    '''
    def explorar(self):
        print('\n')
        contador = 1  
        for linea in self.linea_de_texto:  
            resultado = self.procesar_linea(linea, contador)  
            self.lista_de_tokens = self.lista_de_tokens + resultado  
            contador += 1


    ''' Funcion para imprimir los componentes o resultado o lista de tokens.
    recorro la lista
    imprimo :)
    '''
    def imprimir_componentes(self):
        titulos = f'\n#Linea{"":5}{"#Indice":14}{"Categoría":24}{"Componente":21}{"Descripcion"}\n'
        print(titulos)
        for resultado_explorador in self.lista_de_tokens:  
            print(resultado_explorador)  


    ''' ---------------- PROCESAMIENTO DE DATOS ----------------
    # Esta funcion procesa la linea de texto,
    # Agarro los token y los comparo en mis Descriptores de compoentes
    # Recibo el resultado del match entre token y lista
    # Si existe dentro del los descriptores de componentes
    # el error es referente a un parametro.
    '''
    def procesar_linea(self, fragmento_linea, contador):
        componentes = []
        cont = 0
        linea_completa = fragmento_linea

        while fragmento_linea != "": 
            for mi_componente, Token in DescriptoresComponentes.descriptores_componentes:  

                respuesta = re.match(Token, fragmento_linea)  
                fragmento = fragmento_linea.split()

                if respuesta is not None:
                    if mi_componente is CategoriaComponente.ERRORPARAMETRO:
                        print("ERROR al procesar linea #" + str(contador) + ":   ", linea_completa +
                              " >>> Un parametro esta contaminada con otros elementos en >>> ", fragmento[0])
                        nuevo_componente = ComponenteLexico(contador,
                                                            mi_componente,
                                                            fragmento[0],
                                                            cont + 1,
                                                            "Un parametro esta contaminada con otros elementos")

                        componentes.append(nuevo_componente)

                    ''' Error flotante'''
                    if mi_componente is CategoriaComponente.ERRORFLOTANTE:
                        print("ERROR al procesar linea #" + str(contador) + "   ", linea_completa +
                              " >>> Su flotante tiene varicela en >>> ", fragmento[0])

                        nuevo_componente = ComponenteLexico(contador,
                                                            mi_componente,
                                                            fragmento[0],
                                                            cont + 1,
                                                            "Su flotante tiene varicela")
                        '''Modifique aqui.'''
                        diferencia = len(componentes[-1].texto_componente) - len(nuevo_componente.texto_componente)
                        componentes[-1].texto_componente = componentes[-1].texto_componente[:diferencia]
                        componentes.append(nuevo_componente)
                        fragmento_linea = fragmento_linea[diferencia+1:]

                    ''' Error variable '''
                    if mi_componente is CategoriaComponente.ERRORVARIABLE:
                        print("ERROR al procesar linea #" + str(contador) + ":   ", linea_completa +
                              " >>> Una variable esta contaminada con otros elementos en >>> ", fragmento[0])
                        nuevo_componente = ComponenteLexico(contador,
                                                            mi_componente,
                                                            fragmento[0],
                                                            cont + 1,
                                                            "Una variable esta contaminada con otros elementos")

                        componentes.append(nuevo_componente)
                        diferencia = len(componentes[-1].texto_componente)
                        fragmento_linea = fragmento_linea[diferencia:]

                    ''' Error encapsulacion '''
                    if mi_componente is CategoriaComponente.ERRORENCAPSULACION:
                        print("ERROR al procesar linea #" + str(contador) + ":   ", linea_completa +
                              " >>> El encapsulamiento esta enfermo en >>> ", fragmento[0])
                        nuevo_componente = ComponenteLexico(contador,
                                                            mi_componente,
                                                            fragmento[0],
                                                            cont + 1,
                                                            "El encapsulamiento esta enfermo")

                        componentes.append(nuevo_componente)

                    ''' -- Ok! parece q no hay error asi que tiro pa abajo. --
                    # me deshago de los comentarios y espacios.
                    # corto la linea.
                    '''
                    if mi_componente is not CategoriaComponente.ESPACIO \
                            and mi_componente is not CategoriaComponente.COMENTARIO and mi_componente not in [CategoriaComponente.ERRORENCAPSULACION,
                                                           CategoriaComponente.ERRORPARAMETRO,
                                                           CategoriaComponente.ERRORFLOTANTE,
                                                           CategoriaComponente.ERRORVARIABLE]:

                        nuevo_componente = ComponenteLexico(contador,
                                                            mi_componente,
                                                            fragmento[0],
                                                            cont + 1,
                                                            AtributoComponente.evaluar_token(respuesta.group(),
                                                                                             mi_componente))
                        componentes.append(nuevo_componente)
                    fragmento_linea = fragmento_linea[respuesta.end():]
                    break

            cont += 1
        return componentes
