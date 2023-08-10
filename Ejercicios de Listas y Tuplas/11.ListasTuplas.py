# Escribir un programa que almacene los vectores (1,2,3) 
# y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

vec1 = (1,2,3)
vec2 = (-1,0,2)
total = 0
for i in range(len(vec1)):
    total = total + vec1[i]*vec2[i]
        
print(total)