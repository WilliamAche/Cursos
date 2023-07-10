resultado = ""
op = ""
n2 = ""

texto_inicio = """Bienvenidos a la calculadora
Para salir escribre Salir
Las operaciones son suma, multi, div y resta"""
print(texto_inicio)

while True:
    if not resultado:
        resultado = input("Ingrese primer número: ")
        if resultado.lower() == "salir":
            break
        if resultado == "":
            continue # Salta al proximo bucle
        else:
            resultado = int(resultado)

    if not op:
        op = input("Ingrese una operación: ")
        if op.lower() == 'salir':
            break
        if op == "":
            continue # Salta al proximo bucle

    n2 = input("Ingrese segundo número: ")
    if n2.lower() == 'salir':
        break
    if n2 == "":
        continue # Salta al proximo bucle
    else:
        n2 = int(n2)
        
    if op.lower() == "suma" or op.lower() == "+":
        resultado += n2
    elif op.lower() == "resta" or op.lower() == "-":
        resultado -= n2
    elif op.lower() == "multi" or op.lower() =='*':
        resultado *= n2
    elif op.lower() == "div" or op.lower() =='/':
        resultado /= n2
    else:
        print("Operación no válida")
        break 
    
    print(f"El resultado es {resultado}")
    op = ""
    n2 = ""
    