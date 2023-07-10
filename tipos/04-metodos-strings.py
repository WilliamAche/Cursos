animal = "  chanCHito feliz  "

"""
Método upper() coloca en Mayusculas todo el string
"""
print(animal.upper())

"""
Método lower() coloca en minusculas todo el string
"""
print(animal.lower())

"""
Método capitalize() coloca en Mayuscula la primera letra de SOLO la primera palabra del string
"""
print(animal.strip().capitalize())

"""
Método title() coloca en Mayuscula la primera letra del cada palabra del string
"""
print(animal.title())

"""
Método strip() elimina los espacios adicionales del inicio y final de todo el string
"""
print(animal.strip())

"""
Método strip() elimina los espacios adicionales del lado izquiero del string
"""
print(animal.lstrip())

"""
Método strip() elimina los espacios adicionales del lado derecho del string
"""
print(animal.rstrip())

"""
Método find() busca un string, y nos devuelve el índice de la primera
letra obtenida. Sino lo consigue da -1
"""
print(animal.find("CH"))

"""
Método replace() busca un string y lo reemplaza 
"""
print(animal.replace("nCH", "j"))

"""
Con este método podemos confirmar si un string existe y nos devolvera un booleano, en caso de 
ser verdadero y consigue el string dará True, en caso de no conseguirlo dara False
"""
print("nCH" in animal)

"""
Con este método podemos confirmar si no existe un string y nos devolvera un booleano
"""
print("nCH" not in animal)
