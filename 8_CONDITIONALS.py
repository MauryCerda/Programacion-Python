### CONDICIONAL ###
'''
DEFINICION

Los condicionales son estructuras de control de flujo que permiten ejecutar cierto bloque de código 
si se cumple una condición específica. Los condicionales más comunes en Python son if, else, y elif (abreviatura de "else if").

'''

# CONDICIONAL IF

my_condicion = True
if my_condicion: # if my_condicion: es lo mismo que poner if my_condicion == True:
	print ("Se ejecuta la condicion del if ") # se va aejecutar siempre y cuando que my_condicion sea vervadero
print("La ejecucion continua")# se ejecuta cuando la condicion sea falso ademas esta afuera de lo que es la condicion IF	


my_condicion = 5 * 2
if my_condicion == 10: # if my_condicion: es lo mismo que poner if my_condicion == 5 * 2:
	print ("Se ejecuta la condicion del if ") # se va aejecutar siempre y cuando que my_condicion sea vervadero
print("La ejecucion continua")# se ejecuta cuando la condicion sea falso ademas esta afuera de lo que es la condicion IF

my_condicion > 10
if my_condicion > 10: 
	print ("la condicion es mayor q 10, se ejecuta ") 
else
	print("La condicion es menor o igual que 10")



my_condicion > 14
if my_condicion > 10 and my_condicion <20
	print (" es mayor q 10 y menos q 20 ") 
else
	print("Es menor o igual que 10 0 mayor o igual que 20")
print("la ejecucion continua") # este esta afuera de lo que es la condicion IF


my_condicion > 1
if my_condicion > 10 and my_condicion <20
	print (" es mayor q 10 y menos q 20 ") 
elif my_condicion == 1:
	print(" es igual a 1 ")
else
	print("Es menor o igual que 10 0 mayor o igual que 20")

print("la ejecucion continua") # este esta afuera de lo que es la condicion IF


# tiene jerarquia de ejecucion primero evalua el IF despues el elif y despues el else (por defecto)

my_string = ""

if not my_string:
	print("Mi cadena de texto es vacia")

if  my_string ==  "	Mi cadena de texo"
	print("Estas cadenas de texto coinciden")

