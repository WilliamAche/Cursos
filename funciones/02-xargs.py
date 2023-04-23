# Hay una instrucción que nos permitira agregar todos los argumentos que queramos en el llamado de
# una función, sin necesidad de estar colocándolos como parámetros.

# Se mostrara un ejemplo para el caso de necesitar está instrucción y así facilitar dicha función:
# Al llamar una función que se le tenga que pasar como argumentos números, para poder ir sumandolo,
# que pueda tener más argumentos o menos, y que se tenga que definir parametros por cada uno de
# los argumentos agregados. Ejemplo:

# def suma(a, b, c):
#     print(a + b + c)

# suma(2, 5, 7)
# suma(2, 5)
# suma(2, 5, 3, 4) # Aqui hay un argumento más, habría que definirlo en la función como otro
# parametro (d).

# Para poder facilitar está función utilizaremos la instrucción xargs (x arguments), en la cual
# definiremos en la función un parametro en plural (para que indique que es más de un elemento),
# y colocaremos el signo de * adelante del parametro para así indicarle que es un iterable
# (el cual puede recorrerse con un ciclo for). Es decir, el *nombreParametroEnPlural convierte los
# parámetros en iterables.


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero

    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 3, 12)
