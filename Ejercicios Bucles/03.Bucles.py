# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# Declarar la variable:
numeroEntero = int(input('Escriba un numero entero: '))

# Declarar una funcion:
def impares(num):
    for i in range(num):
        if i % 2 != 0: # declaracion de bucle
            print(i , end=',')

# Imprimimos los resultados:
impares(numeroEntero)