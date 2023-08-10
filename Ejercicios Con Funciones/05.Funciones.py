# Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.

#importamos una libreria, pero este paso solo es opcional
import math

# Escribimos la funcion
def areaCirculo(ratio):
    areaCircular = math.pi * (ratio) ** 2
    return round(areaCircular , 2)

def volumenCilindro(height):
    areaCilindrica = areaCirculo(radio) * height
    return round (areaCilindrica,2)

radio = float(input("Ingrese el radio del circulo: ")) 
altura = float(input("Ingrese la altura del cilindro: "))

print(f'El área del circulo es: {areaCirculo(radio)}')
print(f'El volumen del cilindro es: {volumenCilindro(altura)}')
