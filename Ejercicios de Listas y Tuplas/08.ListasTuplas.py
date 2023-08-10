# Escribir un programa que pida al usuario una palabra y
# muestre por pantalla si es un palíndromo.

# solucion 1
palindromo = input('Introduce tu palindromo: ')
if palindromo == palindromo[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")

# solucion 2
palabra = input('introduce tu palindromo: ')
reversaPalabra = palabra
palabra = list(palabra)
reversaPalabra = list(reversaPalabra)
reversaPalabra.reverse()
if palabra == reversaPalabra:
    print('Es palindromo')
else:
    print('No Es palindromo')