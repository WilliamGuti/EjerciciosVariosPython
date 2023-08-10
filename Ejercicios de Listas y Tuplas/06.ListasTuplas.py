# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
# de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el 
# usuario tiene que repetir.

# Declaramos las listas
asignaturas = ['Matematicas','Fisica','Química', 'Historia', 'Lengua']
notas = []

# creamos un bucle para asignar la nota a una lista nueva
for i in asignaturas:
    nota = float(input('Ingresa la nota de: '+ i + ' '))
    if nota > 3:
        notas.append(i)
# eliminamos la lista que se crea apartir de las notas
for j in notas:
    asignaturas.remove(j)
#imprimimos los resultados
print('Tienes que repetir las siguientes asignaturas: ' , asignaturas)
