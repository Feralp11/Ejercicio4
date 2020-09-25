"""Declaramos los dos valores que el programa recibira, para poder operarlos en la calculadora,
el usuario digitara la operacion que desee realizar y el sistema validara dicha operacion"""

numero_uno = float(input("Digite el primer numero"))        
numero_dos = float(input("Digite el segundo numero"))
operacion = input("Digite la operacion que desea realizar").upper()

"""Aca se realiza la validacion de la operacion que el usuario desea llevar a cabo, 
y se imprimira el resultado de dichas operaciones"""

if operacion =='S':                                                                                                                                             
    suma = numero_uno+numero_dos
    print(f"\nLa suma es: {suma}")
elif operacion =='R':
    resta = numero_uno-numero_dos
    print(f"\nLa resta es: {resta}")
elif operacion =='M':
    multiplicacion = numero_uno*numero_dos
    print(f"\nLa multiplicacion es: {multiplicacion:.2f}")
elif operacion =='D':
    division = numero_uno/numero_dos
    print(f"\nLa division es: {division:.2f}")
else:
    print("\nSe equivoco de operacion")