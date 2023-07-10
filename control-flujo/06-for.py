"""
range(n): Es una función iterable incluida dentro de python, la 'n' hace mención a cualquier número 
entero. Y lo que hace es traer un listado de números que empieza en 0 y que límita el listado al 
valor de 'n' 

Ejemplo: range(5) = 0,1,2,3,4
"""
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado ', buscar)
        break #esta instruccion permite detener la ejecución del for, apenas encuentre el número indicado

else: # Este es un 'for else', hace exactamente los mismo que el else del if
    print("no encontre el número buscado :c")
    
"""
Hay muchos iterables dentro de python como por ejemplo: las listas, las tuplas, los strings, etc
"""
    
for char in "Ultimate python":
    print(char)
    
