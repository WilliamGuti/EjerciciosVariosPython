# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
# una a una las letras de la palabra introducida empezando por la última.

letra = input('Introdue una palabra: ')

for i in range(len(letra)-1,-1,-1):
    print(letra[i])