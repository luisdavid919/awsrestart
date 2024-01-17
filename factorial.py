#Escribe un programa que solicite al usuario un número entero no negativo y calcule su factorial. 
#El factorial de un número entero positivo 'n' se define como el producto de todos los enteros desde 1 hasta 'n'.
#Utiliza un bucle para realizar el cálculo y muestra el resultado. 
#Si el usuario ingresa un número negativo, muestra un mensaje de error y pide un número válido.
from math import factorial

print("Factorial de un número")
numero = int(input("Ingresa el numero para determinar su factorial: "))
print("Factorial is", factorial(numero))