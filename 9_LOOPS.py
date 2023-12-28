### LOOPS ###
'''
DEFINICION

Los bucles, también conocidos como "loops" en inglés, son estructuras de control de flujo que permiten 
ejecutar un bloque de código repetidamente mientras se cumpla una condición específica. 
En Python, hay dos tipos principales de bucles: for y while.

'''

#WHILE
#  El bucle while se ejecuta mientras una condición sea verdadera.

mi_condicion = 0

while mi_condicion <10:
	print(mi_condicion)
	mi_condicion +=2
else: # es opcional  ( es el unico que deja poner el elif no da salta error)
	print("Mi condicion es mayor o igual que 10")
print("El codigo continua") # hacemos esto para saber que el programa salio del bucle while


#########################
# Otro ejemplo

while mi_condicion < 20:
	mi_condicion +=2 # ++ no sirve aca hacer eso lo correcto es +=2 0 -=3
	if mi_condicion ==15:
		print("Mi condicion es 15")
	# break # Sirve para cortar la ejecucion en este lugar del codigo
	print("Mi condicion es menor q 20")
print("Termino el bucle pa")


# FOR
# El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena de caracteres, etc.) o cualquier objeto iterable.
# en el FOR tampoco deja usar el el elif da error

mi_lista = [34,23,234,2,24,5,444,98]
for elemento in mi_lista: 
	print(elemento)

################
# ejemplo para un set
mi_set = {"brian", "brisa", "boludo"}
for elemento in mi_set:
	print(elemento)

################
# ejemplo para un diccionario

mi_dic = {"Nombre":"Mauri", "Apellido":"Cerda", "Edad":23}
for elemento in mi_dic: # tener en cuenta q aca solo va a mostrar las claves
	print(elemento)

for elemento in mi_dic.values(): # tener en cuenta q aca solo va a mostrar los valores
	print(elemento)

############

for elemento in mi_dic:
	print(elemento)
	if elemento == "Edad":
		break
else:
	print("El bucle for para cadiccionario ha finalizado")

###########
for elemento in mi_dic:
	print(elemento)
	if elemento == "Edad":
		continue # es como decirle al codigo ok sigue para adelante, se usa a veces como un condicional
else:
	print("El bucle for para cadiccionario ha finalizado")


################
# ejemplo para una tupla

mi_tuple = (23,4,"anto", "gio")
for elemento in mi_tuple:
	print(elemento)