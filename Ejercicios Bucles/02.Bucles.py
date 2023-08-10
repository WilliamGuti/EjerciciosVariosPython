# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).

# Declarar la variable
edad = int(input('ingresa tu edad: '))

# Declarar la funcion:
def cumplidos(years):
    for i in range(years):    # declaramos un bucle
        print(f'ha cumplido: {i+1}')

# imprimimos el resultado:
cumplidos(edad)
