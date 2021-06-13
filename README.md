# Compiladores e interpretes ITCR Prof. Aurelio

## EXPLORACION (Scanning):
Esta primera etapa de análisis tiene como objetivo leer una entrada y devolver una secuencia de componentes léxicos (Tokens)
presentes en un archivo de texto y validar si estos son validos para el lenguaje y en caso de ser necesario retornar errores.

### Contenido
#### Carpetas:
- explorador
- utils
- docs

#### Archivos:
- pandemico.py

#### Archivos en carpetas:

- Carpeta explorador:
    - AtributoComponente.py
    - CategoriaComponente.py
    - ComponenteLexico.py
    - DescriptoresComponentes.py
    - ExploradorDeComponentes.py_

- Carpeta docs:  
    - ebnf: ebnf.txt 
    - ejemplos: calcularimpuesto.covid, eliminarcaracter.covid, factorial.covid, factorialerror.covid, holamundo.covid, sumatoria.covid
    - enunciado: Proyecto2_Explorador.pdf

- Carpeta utils:
    - archivo.py

### Para pruebas:
Ingresar el nombre del archivo que se desea probar en el archivo `pandemico.py` y posteriormente ejecutar `python3 pandemico.py` en la terminal.
