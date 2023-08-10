# Escribir un programa que permita gestionar la base de datos de clientes
# de una empresa. Los clientes se guardarán en un diccionario en el que la
# clave de cada cliente será su NIF, y el valor será otro diccionario con los
# datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
# (4) Listar todos los clientes, (5) Listar clientes preferentes, 
# (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:

# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo
# a la base de datos.
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3. Preguntar por el NIF del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6. Terminar el programa.

# creamos un diccionario donde vamos a ingresar los datos de los clientes
baseDeDatos = {}
# creamos una variable
opcion = ''
# entramos a un bucle para ingresar las opciones 
while opcion != '6':
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        baseInterna = {'nombre':nombre,'nif': nif, 'direccion':direccion,'telefono':telefono,'email':email,'vip':vip=='s'}
        baseDeDatos[nif] = baseInterna
    if opcion == '2':
        nif = input('Cual es el NIF del cliente? ')
        if nif in baseDeDatos:
            del baseDeDatos[nif]
        else:
            print('Este NIF no existe en nuestra base de datos' , nif)
    if opcion == '3':
        nif = input('Cual es el NIF del cliente? ')
        if nif in baseDeDatos:
            print('NIF:', nif)
            for clave, valor in baseDeDatos.items():
                print(clave ,':', valor)
            else:
                print('Este NIF no existe en nuestra base de datos' , nif)
    if opcion == '4':
        print('Lista de Clientes: ')
        for clave, valor in baseDeDatos.items():
            print(clave ,',',valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in baseDeDatos.items():
            if valor['vip']:
                print(clave, valor['nombre'])
print(baseDeDatos)
    
            

