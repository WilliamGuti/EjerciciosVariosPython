# Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas = float(input("Ingrese el numero de horas trabajadas: "))
costePorHora = float(input("Ingresa el coste por hora: "))
totalPagar = horasTrabajadas * costePorHora
print("Tu paga es: " , totalPagar)