# Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por
# una divisa y muestre su símbolo o un mensaje de aviso si la divisa 
# no está en el diccionario.

# Ingresamos el Diccionario principal
divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# Ingresamos la variable
pregunta = input('Que divisa necesitas? ')

# ponemos un condicional a evaluar
if pregunta.title() in divisa:
    print(divisa.get(pregunta.title()))
else:
    print('Tu moneda no esta disponible')

