# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.


# declaracion de variables
cantidad = float(input('Cuanto quiere invertir: '))
interes = float(input('Cual es el interes anual: '))
agnios = int(input('Ingrese el numero de años: '))

# declaracion de las funciones
def ganancias(amount,interest,years):
    
    for i in range(years):
        amount = (amount * interest / 100) + amount
        print('El interes tras', i+1 , 'años' , str(round(amount,2)))

#imprimimos los resultados:
ganancias(cantidad,interes,agnios)