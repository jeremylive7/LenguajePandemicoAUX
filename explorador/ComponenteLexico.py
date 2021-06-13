from explorador.CategoriaComponente import CategoriaComponente


# -----------------------------------  OBJETO COMPONENTES-LEXICOS  -----------------------------------
# aqui se almacenal los componentes lexicos, para luego ser llamados a impresion.
class ComponenteLexico:
    categoria_componente: CategoriaComponente  # Este categoria va a ser igual a la categoria que entra
    numero_linea: int                          # Este numero de linea va a ser igual a un int
    texto_componente: str                      # Este texto va a ser igual a un string
    atributo_componente: str                   # Este atributo va a ser igual a un string

    # Contructor de la clase.

    # GET
    # Es como se compone este objeto, conteniendo asi, una Categoria, un texto, un atributo.
    def __init__(self, pNumero_linea: int, nuevo_tipo: CategoriaComponente, nuevo_texto: str, pIndice: int,
                 nuevo_atributo: str):
        self.numero_linea = pNumero_linea
        self.categoria_componente = nuevo_tipo     # Construyo el Self categoria
        self.texto_componente = nuevo_texto        # Construyo el Self texto
        self.indice = pIndice                      # Construyo el Self indice
        self.atributo_componente = nuevo_atributo  # Construyo el Self atributo

    # SET
    # Valor de retorno,
    def __str__(self):
        # Saco los atributos del objeto.
        resultado = f'   {str(self.numero_linea):11}' \
                    f'{str(self.indice) :10} ' \
                    f'{str(self.categoria_componente)[20:]:24}' \
                    f'{self.texto_componente :20} ' \
                    f'{self.atributo_componente}'

        return resultado  # retorno el resultado
