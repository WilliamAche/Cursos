nombre_curso = "Ultimate Python"
nombre_test = """Salto
Linea"""
descripcion_curso = """
Ultimate Python, este curso contempla todos los detalles
que necesitas aprender para
un trabajo como programador.
"""
"""
La funcion:
len() cuenta los caracteres de un texto
print() es para imprimir
"""

print(nombre_curso, descripcion_curso)
print(len(nombre_test))

"""Se puede obtener el valor de un caracter usando los [] al lado de la variable 
y dentro de ellos un numero que indica el valor del caracter, es como un array y los elementos del mismo
son los caracteres. Los cuales empiezan en 0

El [:] sirve para extraer partes de un string. Para utilizarlo se debe especificar 
el numero del caracter desde donde empieza y termina. Del lado izquiero de los : se coloca el numero 
del caractar donde empieza y del lado derecho el numero del caracter donde termina.
"""

print(nombre_curso[0])
print(nombre_curso[0:8])
print(nombre_curso[9:])
print(nombre_curso[:8])
print(nombre_curso[:])

