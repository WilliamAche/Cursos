# and, or, not 

# Nota: el operador lógico de "not" lo que hace es dar el valor contrario de un dato.
gas = False
encendido = True
edad = 18
    
if not gas and (encendido or edad > 17):
    print("Puedes avanzar 1")
   
   
# OPERADORES DE CORTO CIRCUITO 
"""
Al colocar operaciones en las condiciones de if en Python pueden dar como resultado las siguientes
acciones:

Si estamos usando "and" y en una de las operaciones da False ya no revisara las siguientes 
operaciones dentro del mismo if, solo basta con que una de False.

En el caso de "or" solo basta con que una de las operaciones de True, para no tener que revisar las
siguientes operaciones dentro del mismo if.

Esto hace las operaciones de Python de corto circuito.

En el caso de estar colocando las operaciones entre parentesis () la condicion entrara a cada una, 
revisando todo lo que hay adentro, así una de False (and) o de True (or).
"""
if not gas or encendido or edad > 17:
    print("Puedes avanzar 2")