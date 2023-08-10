# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

#declaramos las variables
num = int(input('Introduce un numero entero superior a 2 y que no sea negativo: '))

#Declaramos una funcion:
def EsPrimo(number):
    for i in range(2, number):
        if number % i == 0:
            break
    if (i + 1) == number:
        print('Es primo')
    else:
        print('No es primo')
#imprimimos el resultado:
EsPrimo(num)