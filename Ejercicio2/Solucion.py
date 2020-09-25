"""Importamos las librerias que vamis a utilizar"""

import time
import pandas as pd 
import numpy as np

"""Consultamos nuestras dos fuentes de datos, las cuales estan alojadas en archivo txt"""

with open ('libros_24_meses.txt') as libros_vendidos:
    periodo24_ventas_libros = libros_vendidos.read().split('\n')

with open ('catalogo_libros.txt') as libros_vendidos:
    catalogo_libros = libros_vendidos.read().split('\n')

"""Usamos un arreglo de numpy que nos permite crear un arreglo entre los dos campos que buscamos comparar
por ultimo, imprimos el tiempo de duracion y nuestro resultado"""

inicio = time.time()
libros_vendidos = np.array(periodo24_ventas_libros, catalogo_libros)
print(len(libros_vendidos))
print('Duracion:{} segundos' .format(time.time() - inicio))