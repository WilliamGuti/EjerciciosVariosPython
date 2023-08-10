# Escribir un programa que pida al usuario una palabra y muestre por
# pantalla el número de veces que contiene cada vocal.

# Definimos las variables
contador = 0
letra = input('Introduce una palabra: ')
# Definimos las listas
vocales = ['a','e','i','o','u']
# Pasamos la variable a una Lista
letra = list(letra)
# creamos un bucle que vaya letra a letra en la lista
for i in letra:
    for j in vocales: # creamos un bucle anidado para que vaya letra a letra en la lista
        if i == j:
            contador = contador + 1

print(contador)