# Escribir un programa que pregunte una fecha en formato 
# dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# creamos un diccionario con los meses del año
dicMeses = {
    1 : 'Enero', 
    2 : 'Febrero', 
    3 : 'Marzo', 
    4 : "Abril",
    5 : 'Mayo',
    6 : 'Junio',
    7 : 'Julio',
    8 : 'Agosto',
    9 : 'Septiembre',
    10 : 'octubre',
    11 : 'Noviembre',
    12 : 'Diciembre'
}
# Creamos las variables
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
# imprimimos los resultados
print(fecha[0], 'de', dicMeses[int(fecha[1])], 'de', fecha[2])


