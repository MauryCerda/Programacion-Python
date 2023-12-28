### TUPLAS ### 

'''
Una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. 
Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas.

'''

# DEFINIMOS UNA TUPLA
my_tuple= tuple()
my_otra_tuple = ()

# colocamos datos a la tupla
my_tuple = (35, 1.77, "mauri", "cerda", "mauri")
print(my_tuple)
print(type(my_tuple))

#Accedemor a cierto elemento de la tupla
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[4]) # da  error por q ese indice no existe en la tupla
print(my_tuple[-6]) # da error por supera el indice de la tupla, no existe

#Contar cuanta veces un elemento se repite
print(my_tuple.count("mauri")) # dos veces se repite

#conocer el indice de un elemento de la tupla
print(my_tuple.index("mauri"))

# Vemos q una tupla es inmutable es decir q no deja modificar los valores de los elementos
my_tuple[1]= 1.80 # si queremos modificar la altura saltaria error 
print(my_tuple) # en una lista si deja modificar en una tupla no

# OPERADORES CON TUPLAS #
print(my_tuple + my_otra_tuple)
mi_suma = my_tuple + my_otra_tuple # otr aforma mas larga 
print(mi_suma)

# Mostrar un rango de valores de los elementos de una tupla
print(my_tuple[2:3])

# comvertir una tupla a lista
my_tuple = list(my_tuple)
my_tuple(type(my_tuple)) # da q es una lista

# modificar un valor de una tupla de forma formazada
my_tuple1 = list(my_tuple)
my_tuple1.insert(1, 2.33)
my_tuple = tuple(my_tuple1)
print(my_tuple)
print(type(my_tuple))

# eliminar la tupla
del my_tuple

# Tampoco se puede eliminar un determinado elemento d euna tupla
del my_tuple[2] # da error