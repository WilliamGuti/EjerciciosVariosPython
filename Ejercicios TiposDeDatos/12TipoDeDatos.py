# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es del día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas 
# que no son del día. Después el programa debe mostrar el precio habitual 
# de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barra = int(input("\nIngresa la cantidad de panes que no son del dia: "))
precio = 3.49
descuento = 0.6
print("\nEl precio de un pan del dia tiene un costo de 3.49€\n")
total = round(barra * (precio - (precio * descuento)),2)
print("El coste de una barra fresca es ", precio ,"€")
print("El descuento sobre una barra no fresca es " , (descuento * 100) , "%")
print("El coste final a pagar es: " , total, "€")