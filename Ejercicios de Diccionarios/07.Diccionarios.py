# Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar.
# Después se debe mostrar por pantalla la lista de la compra y el coste total,
# con el siguiente formato

# ARTICULO1 = PRECIO
# ARTICULO2 = PRECIO
# TOTAL = PRECIO

# creamos un diccionario vacio el cual llenaremos mas adelante
disCesta = {}
# creamos variables
continuar = True
costo = 0
total = 0
# creamos un bucle para preguntar sobre los articulos y sus precios
while continuar:
    articulo = input('ingresa el nombre del articulo: ')
    articulo.title()
    precio = int(input('Ingresa el precio del articulo: '))
    disCesta.update({articulo:precio})
    continuar = input('¿Quieres añadir más información (s/n)? ') == "s"
# creamos un bucle para operar los valores e imprimir los valores del diccionario
for key in disCesta.keys():
    print(key, "->", disCesta[key])
    costo = disCesta.get(key)
    total = total + costo
print('El total a pagar es de:' , total)

