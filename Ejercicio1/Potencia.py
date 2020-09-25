"""Este programa permite obtener la potencia de un numero, se ha creado un objeto llamado potencia, el cual recibe
los parametros de base y exponente de un numero"""

def potencia (base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
print(potencia(3,3))

