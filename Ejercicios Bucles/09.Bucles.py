# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Declaramos variables

key = input('Introduce la contraseña: ')

#creamos una funcion:
def acceso(password):
    contrasenia = 'contraseña'
    while True:
        print('Contraseña Erronea, intentelo nuevamente')
        password = input('Introduce la contraseña: ')
        if password == contrasenia:
            print('Bienvenido!')
            break

# Imprimimos el resultado:
acceso(key) 