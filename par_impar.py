print("Par e Impar")

numero = int(input("Ingresa un numero entero positivo: "))
par = 0
impar = 0

while numero <=1:
    for numero in range (numero,0):
        if numero % 2 == 0:
            par=+1
        elif numero %2 !=0:
            impar=+1
    numero=-numero
print("El valor de los números pares es: ", par)
print("El valor de los números pares es: ", impar)

