mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
#Seleccionar elemento
print(mascotas[0])

#Cambiar elemento del listado
mascotas[0] = "Bicho"
print(mascotas)

#Devolver una cantidad de elementos, el elemento de la izquierda es el índice del arreglo por el cual
# queremos comenzar a recortar este arreglo (por defecto toma el 0) y el elemento de la derecha 
# es para indicar hasta donde va a llegar el arreglo (por defecto toma el último elemento).
print(mascotas[:3])
print(mascotas[2:])
print(mascotas[0:2])

# Al colocar números negativos lo que hará es buscar de derecha a izquierda, ya que la posición
# 0 es el primer elemento, como no hay elementos antes, busca en los últimos.

# Si coloco -1 lo que hara es buscar el último elemento de la lista. 
print(mascotas[-1])

# Hay una manera de saltar los elementos de un listado con la siguiente forma:
# print(mascotas[1:2:2]) 
# El primer parámetro indica donde empezara.
# El segundo parámetro indica el ínidice limitante hasta donde puede llegar, es decir menos o igual a 
# ese límite.
# El tercer parámetro indica la cantidad de elementos que pasara para seguir seleccionando componentes 
# del listado.

numeros = list(range(21))
print(numeros[::2]) #Números pares
print(numeros[1::2]) #Números impares

# Otra manera de mostrar elementos impare:
# Esto se puede hacer cambiando el número inicial en la función range():
# range(1, 21) Al hacer esto cambiara la estructura de la lista empezando desde 1.
# El primer parámetro indica el número donde va a empezar. Por defecto toma el 0.
# El segundo parámetro indica el número limitante.
# Ejemplo:

numerosImpares = list(range(1, 21))
# Con esto ya no traera los pares sino los impares, debido al cambio en el listado con el range, ya 
# que se cambio la posición inicial del listado, pasando de ser 0 a 1.
print(numerosImpares[::2]) 



# Acceder a los elementos pares del listado
print(mascotas[::2])

