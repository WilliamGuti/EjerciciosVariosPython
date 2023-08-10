# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto.\
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
# grupo que le corresponde.

# Declaracion de variables
nombre = input('ingresa tu nombre: ')
genero = input('Ingresa tu genero (M , F): ')


# definimos una funcion
def seleccion(name, gender):
    if gender.lower() == 'f': 
        if name.lower() <= 'm':
            resultado = 'eres del grupo A'
            return resultado
        else:
            resultado = 'eres del grupo B'
            return resultado
    else:
        if name.lower() >= 'n':
            resultado = "eres del grupo A"
            return resultado
        else:
            resultado = 'eres del grupo B'
            return resultado

# imprimimos el resultado
print(seleccion(nombre,genero))