""" Importamos las librerias que vamos a utilizar """

import time
import pandas as pd
import numpy as np

"""Cargamos nuestra fuente de datos y los imprimimos para visualizarlo"""

datos = np.genfromtxt('costos.txt', delimiter= ',')
print(datos)

"""Se realiza la validacion, si el costo es menor o igual a 25, el numero debe sumarse"""

tiempo = time.time()
lista_deseos = datos[datos <= 25]
calculo = np.sum(lista_deseos)

"""Se imprimen los resultados de la operacion"""

print('Duracion: {} segundos'.format(time.time() - tiempo))
print(calculo)

