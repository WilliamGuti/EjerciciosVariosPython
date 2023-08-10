# Escribir un programa que muestre el eco de todo lo que el usuario 
# introduzca hasta que el usuario escriba “salir” que terminará.

# Declaramos el bucle infinito
while True:
    frase = input("introduce algo: ")
    frase = frase.lower()
    if frase == "salir":
        print('Haz salido!')
        break
    print(frase)