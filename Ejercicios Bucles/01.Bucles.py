# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# Declaracion de variables
palabra = input('ingresa una palabra: ')

#declaracio de funcion
def conteo(word):
    for i in range(10): # declaramos un bucle for
        print(word)
# se imprime el resultado
conteo(palabra)