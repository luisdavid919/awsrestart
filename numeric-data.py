print("Python tiene 3 tipos de datos numericos: int, float y complex")
#esto es un comentario de una linea y será ignorado
"""
este es un comentario multilinea
No puede comenzar con un número.
No puede contener espacios en blanco.
No puede contener caracteres especiales, excepto el guión bajo (_).
No puede ser una palabra reservada.
Sensible a mayúsculas y minúsculas.
No debe utilizar caracteres acentuados ni espacios.
No debe comenzar con guión doble (__).
Evitar usar nombres que sobrescriban funciones integradas.
No debe ser demasiado largo o confuso.
"""

miVariable = 10

print(miVariable,type(miVariable))

miVariable = 5.7

print(miVariable, type(miVariable))

miVariable = 6j

print(miVariable, type(miVariable)) 

numero = 5

numero_convertido = float(numero)

print (numero_convertido)

# Conversiones 
"""
int()
float()
complex()
"""
miVariable = 2 + 6j

print(miVariable, type(miVariable))

numero = 5

numero_convertido = float(numero)

print(numero_convertido)

# Conversiones

"""
int()
float()
complex()
"""

variable = "5"

variable_convertida = int(variable)

print(variable_convertida)

#str

variable = 56

variable_convertida = str(variable)
print(variable_convertida,type(variable_convertida))

# imprimir concatenando cualquier tipo de variable
# separado por coma

print(variable,variable_convertida, miVariable)

#imprimir concatenando strings
#concatenar es una operacion de strings
nombre = "Juan"
apellido = "Perez"

print(nombre + " " + apellido)
print(nombre,apellido)

print("Hola mi nombre es "+ nombre + " " + apellido)
# sinónimo
print(f"Hola mi nombre es {nombre} {apellido}")

#bool = booleano (verdadero, falso)

llover = True

nublado = False

print(llover,nublado,type(llover))

##validaciones entre booleanos
#or
#and
#not
print("Operacion booleanos:")
print (llover or nublado)
print(llover and nublado)
print(not llover)












