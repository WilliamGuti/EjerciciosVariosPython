# Escribir un programa que pregunte al usuario su nombre, edad, dirección 
# y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
# el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
# teléfono es <teléfono>.

# declaramos las variables
nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))
direccion = input('Ingresa tu direccion: ')
telefono = int(input('Ingresa tu numero de telefono: '))
# Declaramos un diccionario vacio:
datos = {}
# Ingresamos los valores al diccionario
datos.update({"nombre" : nombre})
datos.update({"edad" : edad})
datos.update({"direccion" : direccion})
datos.update({"telefono" : telefono})
#imprimimos los resultados
print(datos)
print(datos['nombre'], 'tiene', datos['edad'], 'años, vive en', datos['direccion'], 'y su número de teléfono es', datos['telefono'])
