"""Importamos las librerias que vamos a utilizar"""

import numpy as np
import time

"""Generamos nuestros numeros aleatorios"""

datos_aleatorios = np.random.normal(500,30,10000000)
print (datos_aleatorios)

"""Sumamos los numeros menores a 5000000"""

inicio = time.time()
numeros_menores = np.array(datos_aleatorios)
suma_numeros = datos_aleatorios[datos_aleatorios <= 500000]
suma_numeros = np.sum(suma_numeros)
print ('La suma de los numeros es: ' ,suma_numeros)
print ('El tiempo de ejecucion fue: {}'.format(time.time() - inicio))