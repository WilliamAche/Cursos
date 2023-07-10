numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["chanchito", "feliz"]
palabrasFelices = ["chanchito", "feliz", "Felipe", "alumno"]
booleans = [True, False, True, True]
matriz = [[0, 1], [1, 0]]

# Se pueden multiplicar los elementos de una lista, para así no tener que estar escribiendo el mismo
# valor varias veces. Esto se puede utilizar con un valor [0] o más de uno [0, 1, 2 ...]. Ejemplo:
ceros = [0, 1] * 10
print(ceros)

# Se pueden también, juntar dos o más listas en una. Ejemplo:
alfanumerico = numeros + letras
print(alfanumerico)

# Se puede usar la funciones de python dentro de una lista, para esto se usará la función list(). 
# Está función necesita dentro de ella un valor que sea iterable, es decir una colección, range ó 
# strings, que también son iterables. 

# Dentro de la función list(), se puede colocar funciones o métodos de python, como elementos
# de la lista, como el méotodo de range() Ejemplo:
rango = list(range(1, 11))
print(rango)

# Para contar desde el número 1 con el método de range, se necesita hacerle unos ajustes, para ello
# agregaremos dentro del método de range, dos valores: 
# El del lado izquierdo es para indicar la posición donde iniciará (start). Por defecto es el 0
# El del lado derecho es para indicar la posición donde debe detenerse (stop). Está posición de stop 
# indica que no debe llegar hasta ese número, por eso no aparecé dentro del listado del range ese 
# valor; es decir, si la posición de stop es 11 en el range llegara a 10.

chars = list("Hola mundo")
print(chars)