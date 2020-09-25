"""Importamos las librerias para llevar a cabo el ejercicio"""

import time
import pandas as pd
import numpy as np

"""Leemos nuestra fuente de datos e imprimimos los datos"""

datos = np.genfromtxt('costos.txt', delimiter= ',')
print(datos)

"""Creamos un arreglo de numpy con los datos de nuestra fuente de datos, usan np.array"""
"""Validamos que si los datos son menores a 25, deben sumarse"""

tiempo = time.time()
lista_deseos = np.array(datos)
total_normal = lista_deseos[lista_deseos < 25]
total_normal = np.sum(total_normal)

"""Aplicamos el iva a nuestro resultado multiplicando por 1.13, para obtener el resultado esperado y
encontramos la diferencia entre ambos resultados"""

total_iva = 1.13 * total_normal
diferencia_totales = total_iva - total_normal

"""Imprimimos los resultados esperados"""

print ('Costo sin iva es: $' ,total_normal)
print ('Costo con iva es: $' ,total_iva)
print ('La diferencia de costos es: $' ,diferencia_totales)
print ('Duracion: {} segundos'.format(time.time() - tiempo))