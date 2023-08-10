# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo 
# impositivo que le corresponde.

# declaracion de variables
renta = int(input('ingresa su renta anual: '))

# declaracion de funcion
def pagare(rent):
    if rent <= 10000:
        impositivo = 0.05 
        resultado = rent * impositivo
        return resultado
    elif rent > 10000 and rent <= 20000:
        impositivo = 0.15 
        resultado = rent * impositivo
        return resultado
    elif rent > 20000 and rent <= 35000:
        impositivo = 0.20
        resultado = rent * impositivo
        return resultado
    elif rent > 35000 and rent <= 60000:
        impositivo = 0.30 
        resultado = rent * impositivo
        return resultado
    elif rent > 60000:
        impositivo = 0.45 
        resultado = rent * impositivo
        return resultado
    else:
        return None

# impresion del resultado

print("El total a pagar de impositivo sobre el valor de:",renta,"es",pagare(renta))