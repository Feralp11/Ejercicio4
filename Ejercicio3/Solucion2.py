"""Importamos las librerias que vamos a utilizar"""

import time
import pandas as pd
import numpy as np

"""Mandamos a llamar nuestra fuente de datos e imprimimos los datos"""

datos = np.genfromtxt('costos.txt', delimiter= ',')
print(datos)

"""Verificamos que los datos sean menores o iguales a 25, para que puedan sumarse"""

tiempo = time.time()
lista_deseos = datos[datos <= 25]

"""Definimos el objeto sumar, con el fin de obtener el gasto total que la empresa tendra, si el valor cumple con la condicion inicial
este ira sumado en el contador"
"""

def sumar(lista_deseos):
    suma = 0
    for i in lista_deseos:
        suma = np.sum(lista_deseos)
    return suma

"""Imprimimmos los resultados de la operacion"""
    
print ('Duracion: {} segundos'.format(time.time() - tiempo))
print(sumar(lista_deseos))