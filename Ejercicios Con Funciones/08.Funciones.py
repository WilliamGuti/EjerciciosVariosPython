# Escribir una función que reciba una muestra de números en una lista 
# y devuelva un diccionario con su media, varianza y desviación típica.


# Definimos la muestra
muestra = [1,2,3,4,5,6,7,8,9]

# Definimos la funcion
def recibirMuestra(sample):
    resultado = {}
    
    # Operacion para la media
    suma = 0
    for i in sample:
        suma = i + suma
    media = suma / len(sample)
    
    # Operación para la Varianza
    divisor = 0
    for j in sample:
        divisor = ((j - media) ** 2) + divisor
    varianza = divisor / len(sample)
    
    # Operacion para la Desviación Típica
    # podriamos importar la libreria de math pero en este caso lo haremos a la vieja escuela
    desviacion = 0
    desviacion = varianza ** 0.5
    
    resultado.update({'Media: ': media})
    resultado.update({'Varianza: ': varianza})
    resultado.update({'Desviación Típica: ': desviacion})
    
    return resultado

#imprimimos los resultados
print(f'Resultado {recibirMuestra(muestra)}')
