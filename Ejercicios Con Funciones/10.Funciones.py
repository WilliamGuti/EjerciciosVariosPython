# Escribir una función que convierta un número decimal en binario y 
# otra que convierta un número binario en decimal.

# Definimos los numeros, tambien se puede hacer que se ingresen por consola
decimal = 13
binario = 1101

# Definimos las funciones
def decBin(num):
    resultado = []
    while num > 0: 
        cociente = num // 2
        residuo = num % 2
        resultado.append(residuo)
        num = cociente
    
    return resultado[-1::-1]

def binDec(num):
    representacionDecimal = 0
    num = list(str(num))
    num.reverse()
    for i in range(len(num)):
        if num[i] == '1':
            representacionDecimal = representacionDecimal + 2 ** i
    return representacionDecimal

# Imprimimos los resultados
print(f'El resultado de {decimal} a binario es: {decBin(decimal)}')
print(f'El resultado de {binario} a decimal es: {binDec(binario)}')