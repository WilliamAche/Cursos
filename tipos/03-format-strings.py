nombre = "Erika"
apellido = "Gonzalez"

"""Concatenar Variables"""
nombre_completo = nombre + " " + apellido

""" 
con el formateo (f) en python se puede concatenar dentro de un string variables y hacer 
operaciones dentro de las mismas {}. La f se coloca al lado izquierdo de la comilla inicial,
en donde empieza el string
"""
nombre_completo2 = f"{nombre} {apellido}"
nombre_completo3 = f"{nombre[0]} {2 + 5}"

print(nombre_completo)
print(nombre_completo2)
print(nombre_completo3)

