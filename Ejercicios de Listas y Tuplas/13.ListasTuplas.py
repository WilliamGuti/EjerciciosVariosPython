# Escribir un programa que pregunte por una muestra de números, 
# separados por comas, los guarde en una lista y muestre por pantalla
# su media y desviación típica.
muestras = []
suma = 0
media = 0
desviacion = 0
desviacion1= 0
cantidad = int(input('Introduce la cantidad de muestras: '))
for i in range(cantidad):
    muestra = int(input('introduce la muetras: '))
    muestras.append(i+1)
for i in muestras:
    suma = suma + i
    desviacion1 = desviacion1 + i**2
media = suma / cantidad
desviacion = (desviacion1/cantidad-media**2)**(1/2)

print('La lista tiene: ' , muestras)
print('la suma de los elementos de la lista es: ' ,suma)
print('La media es: ', media)
print('La desviacion es: ' , desviacion)