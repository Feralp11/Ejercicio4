"""Importamos la libreria math, para poder llevar a cabo operaciones matematicas"""

import math

"""Valor al que sacaremos su raiz cuadrada, se ha identificado con una x"""

x = 100

"""Se ocupa la funcion math.sqrt, la cual nos permite obtener la raiz cuadrada de un numero"""

print(math.sqrt(x))

"""Definimos el objeto raiz cuadrada, en el cual se hara el calculo de la raiz cuadrada en forma de objeto"""

def raiz_cuadrada(n):   
    x = 0
    while x * x <= n:

        x += 0.001
    return x
print (raiz_cuadrada(x))    