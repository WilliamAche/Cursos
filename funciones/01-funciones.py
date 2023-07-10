"""
Los parámetros son las variables que están definidas dentro de los parentesis de la función y se
utilizan dentro de la misma función
"""


def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


# Cuando llamamos a una función y le pasamos un valor, le estamos pasando un argumento.
hola('Sarai', 'Gonzalez')
hola('Chanchito')

# Argumento nombrado:
# Se utilizan para indicar al parámetro de la función original un valor específico, que puede ir
# en orden o no, y en el caso de usarlos es obligatorio:
# 1) Utilizar los mismos nombres de los parámetros definidos.
# 2) Definir en todos los valores los "argumentos nombrados", es decir, no se puede utilizar en
# un solo argumento si hay más de uno (porque sino dará error).

hola(apellido="Schurmann", nombre="Nicolas")
