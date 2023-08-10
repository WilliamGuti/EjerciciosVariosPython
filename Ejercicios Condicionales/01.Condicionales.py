# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# declarar variables
edad = int(input('ingresa tu edad: '))
#declarar una funcion
def edades(age):
    resultado = ''
    if age >= 18:
        resultado = "Es mayor de edad"
        return resultado 
    else:
        resultado = "No es mayor de edad"
        return resultado
print(edades(edad)) 