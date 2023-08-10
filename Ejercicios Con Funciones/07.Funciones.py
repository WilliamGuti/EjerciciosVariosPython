# Escribir una función que reciba una muestra de números en una lista 
# y devuelva otra lista con sus cuadrados.

# Definimos la muestra
muestra = [1,3,5,7,8,9,44,20,665,12,20,33]

# Definimos la funcion
def cuadrados(sample):
    square = 0
    # Definimos una muestra vacia
    resultado = []
    # realizamos la operacion
    for i in sample:
        square = i ** 2
        resultado.append(square)
    return resultado

# Imprimir los resultados
print(f'Los cuadrados de la muestra {muestra} son {cuadrados(muestra)}')
