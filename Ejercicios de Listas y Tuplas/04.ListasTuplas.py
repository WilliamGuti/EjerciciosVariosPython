# Escribir un programa que pregunte al usuario los números ganadores
# de la lotería primitiva, los almacene en una lista y los muestre por
# pantalla ordenados de menor a mayor.

# creamos una lista vacia
loteria = [] 

# definir las variables
cantidad = int(input('Ingresa cuantos numeros son los ganadores de la loteria: '))

#entramos a un bucle para introducir elementos a la lista vacia
for i in range(cantidad):
    numeros = float(input('Ingresa los numeros ganadores de la loteria: '))
    loteria.append(numeros)

# funcion para ordenar la lista
def organizado(lotery):
    ordenado = True
    while ordenado:
        ordenado = False
        for i in range(len(lotery) - 1):
            if lotery[i] > lotery[i + 1]:
                ordenado = True
                lotery[i], lotery[i + 1] = lotery[i + 1], lotery[i]
    print(lotery)
    
# loteria.sort() # esta funcion permite ordenar los numeros
#imprimimos los resultados:
organizado(loteria)

