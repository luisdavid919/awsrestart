print ("Conteo hasta 10")

#utilizando el range (rango)
inicio = 0
final = 10
#range (incio, valor_final-1)
for x in range(inicio, final + 1):
    print(x)
    
print("\nRange con un argumento")
#range(final) con aumentos de 1 y da por hecho que inicia en 0
for x in range(final+1):
    print(x)
    
print("\nRange con tres argumentos")
#range(inicio, final, intervalo)
salto = 2
for x in range(inicio, final + 1, salto):
    print(x)
    








