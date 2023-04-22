#Ejemplo de While

# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
    
# Loop Infinito, en estos casos es importante agregar una condicional para parar dicho loop.
# Ejemplo:

# while True:
#     comando = input("$ ")
#     print(comando)
#     if comando.lower() != "salir":
#         break