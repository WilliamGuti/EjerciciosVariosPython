# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos 
# puntos, y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla 
# palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# crear un diccionario vacio 
diccionario = {}
# variables
continuar = True
continuar2 = True
#crear un bucle para ingresarle dato al diccionario
while continuar:
    español = input('ingresa la palabra en español: ')
    español.title()
    ingles = input('Ingresa la palabra en ingles: ')
    diccionario.update({español:ingles})
    continuar = input('¿Quieres añadir más información (s/n)? ') == "s"
# crear otro bucle para hacer las traducciones
while continuar2:
    palabra = input('Que palabra quieres traducir? ')
    palabra.title()
    if palabra in diccionario:
        print(palabra , "en su traduccion es: " , diccionario.get(palabra))    
    else:
        print('Esta palabra no esta dentro del diccionario')   
    continuar2 = input('¿Quieres continuar? (s/n)? ') == "s"
print('Adios / Bye')

