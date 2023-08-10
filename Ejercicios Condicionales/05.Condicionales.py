# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
# iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su 
# edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# Declaramos las variables
edad = int(input('Ingresa tu edad: '))
ingresos = float(input('Ingresa tus ingresos: '))

# Declaramos las funciones
def impuestos(age,entry):
    result = ''
    if age >= 16 and entry >= 1000:
        result = 'tiene que tributar'
        return result
    else:
        result = 'NO tiene que tributar'
        return result

# Imprimimos el resultado
print(impuestos(edad,ingresos))
