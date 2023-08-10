# Escribir un programa que cree un diccionario vacío y lo vaya 
# llenado con información sobre una persona (por ejemplo nombre, edad,
# sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# creamos los diccionarios
dicInformacion = {}

# creamos variables con un bucle
while True:   
    x = input('Que informacion quieres ingresa? ')
    x = x.upper()
    y = input('Ingresa el dato: ')
    y = y.title()
    dicInformacion.update({x:y})
    print(dicInformacion)
    x = input('Deseas continuar? S/N ')
    x = x.upper()
    if x == 'N':
        break
# imprimimos los resultados
print(dicInformacion)







