def largo(texto):
    resultado = 0
    # Al subrayarse una palabra en python, puede indicar que esa variable no se está utilizando,
    # en el caso de un for en el que no se utilice dicha variable definida en el mismo for, se
    # puede evitar ese subrayado si se utiliza el "_", suplantando _ por la variable como se
    # muestra en dicho ejemplo:
    for _ in texto:
        resultado += 1
    return resultado

print("chanchito")
l = largo("Hola Mundo")
print(l)

# Para depurar nuestro código python necesitamos crear primero un archivo launch.json, Vsc nos lo 
# crea de manera mas sencilla, para ello debemos ir a 'Run and Debug' que está en el menú lateral de 
# Vsc (sidebar), automáticamente al darle click nos indicará si tenemos dicho archivo o no, en caso
# de no tenerlo colocara un texto tipo enlace de color azul el cual indica que creara dicho archivo,
# al darle click abrirá un select en donde te pedira que indiques la configuración a la que se 
# destinara dicho archivo, en el caso de python se utilizara el de "Python file", al seleccionarlo
# se creara de manera automática el archivo launch.json.

# El archivo se creara dentro de una carpeta en la raíz del proyecto que tiene por nombre: .vscode
# Ya con esto se puede utilizar el depurador de Vsc, en el mismo lugar de 'Run and Debug', el cual 
# tiene un boton de play para correr el depurador.

 # IMPORTANTE: Es necesario al ejecutar el depurador, indicar un punto donde el depurador se va a 
 # detener, y así pueda mostrar resultados claros, y no nada. Para colocar ese punto de paro,
 # conocido como breakpoint, del lado izquierdo de los números que indican que línea de código estamos
 # usando, del editor de código, al mover el mouse allí, se veran unos puntos rojos, y al darle click 
 # a uno de esos puntos de una línea de código, habremos indicado en nuestra aplicación cual será 
 # nuestro punto de paro o breakpoint.
 
 # Otro dato importante, luego de que el depurador tenga su punto de paro o breakpoint, al ejecutarse, 
 # mostrará  del lado izquierdo del Run and Debug, las variables y funciones utilizadas, entre otras 
 # cosas, y aparecerá del lado derecho del archivo en el que estamos, una seria de operaciones,
 # con las cuales podremos ir dando pasos hacia adelante o hacia atrás a partir de nuestro punto 
 # breakpoint.
 