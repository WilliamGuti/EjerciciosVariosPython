# Escribir una función que reciba un número entero positivo y devuelva su factorial.
# definimos la variable
num = int(input('Introduce un numero entero positivo: '))
# definimos la funcion
def factorial(number):
    if number < 0: 
        print("Factorial de un numero entero no existe")

    elif number == 0: 
        return 1
        
    else: 
        fact = 1
        while(number > 1): 
            fact *= number 
            number -= 1
        return fact 
# llamamos la funcion
print(factorial(num))