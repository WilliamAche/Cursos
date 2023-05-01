saludo = "Hola Global"


def saludar():
    # El método "global" nos ayuda a poder utilizar una variable de alcance global, es decir que este
    # afuera de la función en un alcance inicial o superior por encima de las demás, como por ejemplo
    # la variable saludo, tienen el mismo nombre tanto global como en la funcion y para poder usarla
    # de modo global, es decir dar entender que es la variable de afuera de la función y no la interna
    # (local) dentro de la función, se necesita escribir primero el método: global y luego el nombre
    # de la variable a la que queremos utilizar dentro de la función de manera global.
    # Luego de esto podremos usar la variables dentro de dicha función en otra línea de comando.

    # IMPORTANTE: Luego de instanciar de manera global dicha variable, no se puede crear otra variable
    # con el mismo nombre de manera local dentro de la función, ya que no serviría, debido a que
    # esa variable ya se definió como global y se tomará solo como global, cambiando ducho valor de
    # esa variable en todo el alcance dado, es decir en todo el código.
    
    # RECOMENDACIÓN: Es mejor no utilizar variables globales, sino mejor instancias locales dentro 
    # de las funciones, ya que estás son una mala práctica y pueden generar errores a futuro debido 
    # a su uso en la sintaxis o resultado de valores.
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
print(saludo)
