"""
# input() Permite obtener datos del usuario de manera interactiva en la terminal
# IMPORTANTE: Los valores obtenidos del usuario estarán en formato string, estos se deben convertir
 a números si se quieren hacer operaciones matemáticas con ellos
"""
n1 = input("Ingresa primer numero") 
n2 = input("Ingresa segundo numero") 

# int() convierte un numero de formato string a un número real o de formato numérico
n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

"""
# IMPORTANTE: Para escribir variables dentro de un string se debe utilizar las {} y dentro de ellas
el nombre de la variable, y se debe agregar al principio de las comillas del string la letra f, para
que se puedan reconocer e interpretar las variables de manera correcta dentro del string
"""

mensajeDeResultado = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicacion es {multiplicacion},
el resultado de la division es {division},
"""

print(mensajeDeResultado)

