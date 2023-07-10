# Iterables: strings, range(), listados []. Para listarlas se necesita el for.
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

# Para obtener el indice de los listados se utiliza la función predeterminada de python: 
# enumerate(aqui la variable que contiene el listado)
# Esta función devuelve un tipo de dato que se conoce como tupla. Este tipo de dato es otro listado,
# el cual trae el indice y el valor del elemento del listado.
# for mascota in enumerate(mascotas):
#     print(mascota)
#     print(mascota[0]) # índice
#     print(mascota[1]) # valor del elemento
    
# Para obtener el indice sin entrar dentro de otro listado, usaremos el desempaquetado de la lección 
# anterior, y en el for definiremos el valor 1 (indice), el valor 2 (valor del elemento) del listado 
# que nos devuelve la función enumerate, para asi obtener dentro del for ambos valores, sin necesidad 
# de volver a iterarlos. Ejemplo:
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
    