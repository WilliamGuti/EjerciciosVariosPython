# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# definir las variables:
num = int(input('Ingresa un numero entero positivo: '))

# Definir una funcion:
def cuentaAtras(n):
    for i in range(n , -1 , -1): # declaracion de bucle
        print(i, end=' , ')

# impresion de resutados:
cuentaAtras(num)