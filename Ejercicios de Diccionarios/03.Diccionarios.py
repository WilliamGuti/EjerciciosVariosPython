# Escribir un programa que guarde en un diccionario los precios de las frutas
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre
# por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Declarar los diccionarios:
dicFrutas = {'Platano','Manzana','Pera','Naranja'}
dicFrutas2 = {}
# Ingresamos los valores a las llaves
for i in dicFrutas:
    precios = float(input('Ingresa el precio de: '+ str(i) + ' ')) 
    dicFrutas2.update({i : precios})
print(dicFrutas2)
# Declaramos las variables
total = 0
fruta = input('Ingresa tu fruta: ')
fruta = fruta.title()
kilos = float(input('ingresa el numero de kilos: '))
# condicionamos  para obtener el valor a pagar
if fruta.title() in dicFrutas2 :
    precio = dicFrutas2.get(fruta.title())
    total = precio * kilos
    print('El precio por los kilos a llevar es de:', total) 
else:
    print("esta fruta no esta disponible")
