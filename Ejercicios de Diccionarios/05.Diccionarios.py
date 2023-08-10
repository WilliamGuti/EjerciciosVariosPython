# Escribir un programa que almacene el diccionario con los créditos de las 
# asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
# y después muestre por pantalla los créditos de cada asignatura en el
# formato <asignatura> tiene <créditos> créditos, donde <asignatura> 
# es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso.

# Definimos unas variables
total = 0

# Definir el diccionario:
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# bucle para imprimir cada una de las materias con su respectivos creditos
for key in asignaturas.keys():
    print('La asignatura:' ,key, "tiene =", asignaturas[key],'Creditos')

# Bucle para coger los valores de las keys y sumarlos
for i in asignaturas:
    creditos = asignaturas.get(i)
    total += creditos
print('los creditos totales son:' , total)