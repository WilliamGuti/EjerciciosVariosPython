# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Ingrese una cantidad a invertir: "))
interesAnual = float(input("Ingrese el interes anual: "))
agnios = int(input("ingresa el numero de años: "))
capital = round(inversion * (interesAnual/100 + 1)** agnios , 2)
print("Su inversion fue de:",inversion,"con un interes de:",interesAnual,"a",agnios,"años, donde su capital obtenido fue: ",capital )