# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

#declaramos variables
num1 = int(input('ingresa un numero: '))
num2 = int(input('ingresa un numero: '))
#definimos una funcion
def comprovacion(n1,n2):
    resultado = 0
    if n2 == 0:
        return "No se puede dividir entre cero"
    else:
        resultado = n1//n2
        return resultado
# imprimimos el resultado
print(comprovacion(num1,num2))