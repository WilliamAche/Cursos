mascotas = ["Pelusa", "Wolfgang", "Felipe", "Wolfgang", "Chanchito Feliz"]

# Métodos para buscar elementos dentro de un listado

# Método index():
# Devolvera el índice (posición) del elemento buscado
# En caso de no conseguir el valor, dara error. Por esto es necesario crear una condición para
# revisar si el elemento se encuentra dentro del listado.add()

if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))
    
# Para contar cuentas veces existe algo dentro de un arreglo, utilizaremos el método count()

print(mascotas.count("Wolfgang"))