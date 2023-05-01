def no_espace(texto):
    nuevo_texto = ''
    for char in texto:
        if char != ' ':
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = texto.lower()
    texto = no_espace(texto)
    texto_al_reves = reverse(texto)

    # texto_reverse = texto[::-1] # Asi coloque la palabra al reves, bucando en internet
    return texto == texto_al_reves


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no somos", es_palindromo("Somos o no somos"))
