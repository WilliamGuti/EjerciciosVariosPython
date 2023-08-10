# Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.

# Definimos los numeros, tambien se puede hacer que se ingresen por consola
num1 = 36
num2 = 24

# Definimos la función del máximo común divisor
def minDiv(n1 , n2):
    # primero definimos cual es el numero mas grande
    mayor = 0
    menor = 0
    mcd = 0
    
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1
    
    # Procedemos a operar   
    resultado = mayor // menor
    residuo = mayor % menor
    
    if mayor == menor:
        mcd = mayor
    
    elif resultado == 0:
        mcd = menor
        
    else:
        mcd = menor % residuo
        if mcd == 0:
            mcd = residuo

    return mcd

# Definimimos la función del mínimo común múltiplo
def minMul(n1 , n2):
    mcm = 0 
    
    # Procedemos a operar
    mcm = (n1 * n2) // minDiv(n1, n2)
    
    return mcm

# Imprimimos los resultado
print(f'El máximo común divisor de {num1} y {num2} es: {minDiv(num1 , num2)}')
print(f'El mínimo común múltiplo de {num1} y {num2} es: {minMul(num1 , num2)}')