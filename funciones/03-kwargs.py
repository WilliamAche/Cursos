# Los kwargs (Keywords arguments) nos permiten empaquetar absolutamente todos los parámetros pero
# en solamente un parámetro.

# Para utilizarlo es necesario agregar adelante del parametro definido DOS astericos (**parametro).

def get_product(**datos):
    # Para acceder a uno de los datos es necesario colocar el nombre del parametro definido en la  
    # función (datos) en donde están empaquetados todos los demás parámetros, y al lado del
    # mismo se debe agregar corchetes [] y dentro de los corchetes el nombre del parametro 
    # que definimos al llamar la función
    print(datos["id"], datos["name"])


# Importante: Al utilizar los kwargs en la función, es necesario al momento de llamar la función
# definir el nombre de los parámetros junto al argumento. Ejemplo: nombreParametro="Argumento".
# Es muy parecido a los argumentos nombrados pero con la diferencia de que estos parametros no están
# definidos en la función, sino que se van definiendo al llamar la función, conforme sea el dato que
# necesitemos.
get_product(id="23",
            name="iPhone",
            desc="Esto es un iphone")

# El resultado que da una función en la que utilizamos kwargs es un objeto {'id': 'id'}
