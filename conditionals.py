userReply = input ("Necesitas que te entreguemos un paquete? (si o no)")

if userReply == "si":
    #esto se ejecuta si el if se cumple
    print("Podemos ayudarte a entregar tu paquete")
else: 
    print("Gracias. vuelve pronto")
    exit()

userReply = input("Quisiera comprar estampas, una caja o una copia? (estampas, caja, copia)")

if userReply == "estampas":
    print("Tenemos diferentes estampas para ti")
elif userReply == "caja":
    print("Tenemos diferentes tamaños de cajas")
elif userReply == "copia":
    copies = input("Cuantas copias quiere sacar?")
    print(f"Aqui hay {copies} copias")
else:
    print("Opción no válida")
    
    
    
    