# Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Introduce un correo electronico: ")
correo1 = ''
dominio = "@"
for letra in correo:
    if letra == dominio:
        correo1 = correo1 + '@ceu.es'
        break
    else:
        correo1 = correo1 + letra
print("El correo es" , correo1)

# otra solucion
# email = input("Introduce tu correo electrónico: ")
# print(email[:email.find('@')] + '@ceu.es')