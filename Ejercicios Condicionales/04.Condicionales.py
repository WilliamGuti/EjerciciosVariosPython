# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#declaramos las variables:
num1 = int(input('ingresa un numero: '))
#declaramos la funcion
def comprovar(n1):
    if n1 % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
#imprimimos el resultado 
print(comprovar(num1))