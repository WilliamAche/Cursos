numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# bonito!

# Los nombres estan en la posición correspondiente de cada elemento dentro del array
# IMPORTANTE: En este ejemplo se nombran todos los elementos, no se pueden obtener uno solo o dos,
# sino todos lo elementos.

# numeros = [1, 2, 3]
# primero, segundo, tercero = numeros

# print(primero)
# print(primero, segundo, tercero)

# Si quisieramos obtener solo uno o dos (varios menos todos los elementos), se haría de la siguiente
# manera:

# Se debe colocar un *para indicar el resto de elementos iterables
primero, segundo, *otros, penu, ultimo = numeros 

# Para obtener los úlltimos elementos, se deben denominar de ultimo, es decir, luego de la palabra con 
# la que definimos el iterable con *, en este caso "*otros" sería el iterable, luego de él, se deben 
# denominar los últimos elementos y así podremos desempaquetarlos de nuestro listado.
print(primero, segundo, penu, ultimo, otros)
