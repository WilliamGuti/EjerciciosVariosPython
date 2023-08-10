# Escribir un programa que pregunte el nombre el un producto,
# su precio y un número de unidades y muestre por pantalla una 
# cadena con el nombre del producto seguido de su precio unitario 
# con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos
# y el coste total con 8 dígitos enteros y 2 decimales.

producto = input("Introduce un producto: ")
precio = float(input("Ingresa el precio: "))
unidades = int(input("Ingresa la cantidad de unidades: "))
total = unidades * precio
print(producto , ":" , unidades , "Unidades X " , round(precio,2) , "€ =" , round(total,2))