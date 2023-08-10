# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

# *
# **
# ***
# ****
# *****

# Declaracion de las variables:
numero = int(input("Introduce un numero para tu rectangulo: "))

# Declaramos una funcion
def triangulo(num):
    for i in range(num):
        for j in range(i+1):
            print('*' , end='')
        print('')
# Imprimimos los resultados:
triangulo(numero)
