# En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden
# ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

# Declaracion de variable
score = float(input('Ingresa tu puntuacion: '))

# Declaracion de funciones:
def calificacion(score):
    rendimiento = ''
    resultado = 0
    if score == 0.0:
        rendimiento = 'Inaceptable'
        resultado = score * 2.400
        print("Su resultado ha sido:",rendimiento,'con un total a pagar en bonificacion de:',resultado)
        return
    elif score == 0.4:
        rendimiento = 'Aceptable'
        resultado = score * 2.400
        print("Su resultado ha sido:",rendimiento,'con un total a pagar en bonificacion de:',resultado)
        return
    elif score == 0.6:
        rendimiento = 'Aceptable'
        resultado = score * 2.400
        print("Su resultado ha sido:",rendimiento,'con un total a pagar en bonificacion de:',resultado) 
        return
    else:
        print("Ingresa un valor correcto!")  
        return
# Impresion de resultados
calificacion(score)