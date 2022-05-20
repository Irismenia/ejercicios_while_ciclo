"""Ejercicio 1:
Calcular la suma de los N primeros números naturales"""

suma = 0
x = 1
N=int(input("Por favor deme el valor de N: "))

while (x <= N):
    suma = suma + x
    x = x + 1
print("La suma es:" , suma)
