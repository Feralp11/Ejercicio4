*Importamos las librerias que vamos a utilizar*

import numpy as np
import time

*Generamos los numeros aleatorios que vamos a utilizar*

datos_aleatorios = np.random.normal(500,30,10000000)
print (datos_aleatorios)

"""Por medio de un ciclo for, realizamos la suma de numeros
que son menores a 500000"""

inicio = time.time()
datos_iniciales = []
for numeros in datos_aleatorios:
    if (numeros < 500000):
        datos_iniciales.append(numeros)
print ('La suma de los numeros es: ',sum(datos_iniciales))
print ('El tiempo de ejecucion fue: {}'.format(time.time() - inicio))