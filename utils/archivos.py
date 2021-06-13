# Utilitarios para manejar archivos

def cargar_archivo(ruta_archivo):
    """
    Carga un archivo y lo retorna cómo un solo string pero línea por línea
    en caso de que el archivo 
    """
    # abre la ruta del archivo y le quita los saltos de linea del archivo.
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            yield linea.strip("\n") # le quito los saltos de linea.
