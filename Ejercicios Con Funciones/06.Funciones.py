# Escribir una función que reciba una muestra de números en una lista 
# y devuelva su media.

# Definimos la lista
lista = [1,2,5,3,7,9,8,10]

# Definimos la funcion
def media(l):
    suma = 0
    for i in l:
        suma = i + suma
    total = suma / len(l)
    return total

# Imprimimos el resultado
print(f'La media de la lista {lista} es : {media(lista)}')