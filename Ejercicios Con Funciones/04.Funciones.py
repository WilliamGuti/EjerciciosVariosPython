# Escribir una función que calcule el total de una factura tras 
# aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

# Definimos la función
def totalFactura(cantidad, iva = 21 ):
    total = 0
    total = cantidad + ((cantidad  * iva) / 100)
    return total

#imprimimos el resultado
print(totalFactura(1000, 10))
print(totalFactura(1000))