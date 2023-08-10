# Escribir un programa que almacene en una lista los números
# del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# Definimos lista vacia:
listaVacia = []
# Entramos a un bucle para insertarle numeros del 1 al 10 ordenados
for i in range(10):
    i = i + 1
    listaVacia.append(i)
# definimos una funcion para ordenar los numeros de adelante hacia atras
def reversa(numeros):
    back = True
    while back:
        back = False
        for i in range(len(numeros)-1):
            if numeros[i] < numeros[i+1]:
                back = True
                numeros[i] , numeros [i+1] = numeros [i+1] , numeros[i]
    print(numeros)
#listaVacia.reverse() # esta funcion permite revertir la lista
# llamamos la funcion para mostrar los resultados
reversa(listaVacia)