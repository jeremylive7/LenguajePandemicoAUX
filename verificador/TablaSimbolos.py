class TablaSimbolos:
    """
    Esta es la tabla donde se va a almacenar la informacion para decorar el  arbol de sintaxis
    La estructura de símbolos esta basada en una lista de diccionarios
    """
    simbolos: list = []
    profundidad: int = 0

    def abrir_bloque(self):
        self.profundidad += 1

    def cerrar_bloque(self):
        for registro in self.simbolos:
            if registro['profundidad'] == self.profundidad:
                self.simbolos.remove(registro)

        self.profundidad -= 1

    def nuevo_registro(self, nodo, nombre_registro=''):
        diccionario = {}

        diccionario['nombre'] = nodo.contenido
        diccionario['profundidad'] = self.profundidad
        diccionario['referencia'] = nodo

        self.simbolos.append(diccionario)

    def verificar_existencia(self, nombre):
        for registro in self.simbolos:

            if registro['nombre'] == nombre and registro['profundidad'] <= self.profundidad:
                return registro

        raise Exception('Esa vara no existe', nombre)

    def __str__(self):

        resultado = 'TABLA DE SÍMBOLOS\n\n'
        resultado += 'Profundidad: ' + str(self.profundidad) + '\n\n'
        for registro in self.simbolos:
            resultado += str(registro) + '\n'

        return resultado
