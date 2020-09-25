"""Importamos la libreria math, la cual nos permite realizar operaciones matematicas en python"""

import math

"""X es igual valor del cual encontraremos el factorial, para este caso sera el numero 10"""

x = 10

"""Se utiliza la funcion math.factorial, la cual permite imprimir el factorial de un numero"""

print (math.factorial(x))

"""Definimos el objeto factorial_numero, el cual recibira los parametros mateticos para poder llevar a cabo 
la operacion matematica de nuestro ejercicio"""

def factorial_numero(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print (factorial_numero(x))    