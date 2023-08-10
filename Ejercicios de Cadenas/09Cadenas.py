# Escribir un programa que pregunte al usuario la fecha de su nacimiento 
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día 
# o el mes se introduzcan con un solo carácter.
fecha = input("introduce la fecha con este formato: dd/mm/aaaa ")
print("El dia",fecha[:2],"El mes",fecha[3:5],"y año",fecha[6:])
