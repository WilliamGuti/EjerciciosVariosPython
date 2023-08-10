# Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!.

# Definimos una variable
nombre = input('Introduce un nombre: ')
# Definimos la funcion
def saludo(name):
    print('¡hola',name ,'!')
# Llamamos la funcion
saludo(nombre)