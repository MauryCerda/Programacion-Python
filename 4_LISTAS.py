### LISTA ###

## Son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos. ##

# 2 forma de Crear una lista 
my_list = list() # 1 forma de crear una lista
my_otra_lista = [] # 2 forma de crear una lista 

# ver la longuitud que tiene una lista
print (len(my_list)) # Da cero por que no tiene elementos o datos.

# Colocamos datos a la lista, en este caso del mismo tipo 
my_list = [35, 7, 56, 5, 77, 7, 232, 67,] 
print(my_list)
print (len(my_list)) # nos da que hay 7 datos o elementos 

# Colocamos datos a la lista, en este caso de diferentes tipos
my_otra_lista =[34, 1.77, "Mauri", "Cerda"]


#Conocer el tipo de la lista
print(type(my_otra_lista)) #Sale en pantalla list lo cual es correcto
print(type(my_list)) #Sale en pantalla list lo cual es correcto

# Un array no es lo mismo que una lista, la lista nos proporciona operaciones propias de racista, como ordenaciones, riverse, inyeccion de elementos insertada en un indice concreto.
# Un array en cambio es una estructura mucho mas inamovible. 

# Acceder a un elemento especifico de uan lista, a traves del indice
print(my_otra_lista[0]) # Da como resultado 34 
print(my_otra_lista[1]) # Da como resultado 1.77 
print(my_otra_lista[3]) # Da como resultado Mauri
print(my_otra_lista[4]) # Da como resultado Cerda
print(my_otra_lista[-1]) # Da como resultado Cerda 
print(my_otra_lista[-2]) # Da como resultado Mauri
print(my_otra_lista[-3]) # Da como resultado 1.77
print(my_otra_lista[-4]) # Da como resultado 34 


# Imprimir en pantalla las cantidad que se repite un elemento en la lista
print(my_otra_lista.count(7)) # Nos da como resultado 2, ya que se repite dos veces el siete en la lista.


age, altura, nombre, apellido = my_otra_lista  # podemos poner cualquier nombre a la variable q no jode, pero si la 1 variable va con el 1 elemento y asi sucesivamente
print(altura) # da como resultado 1.77 

print(my_list + my_otra_lista) # este si se puede realiazar 
print (my_list * my_otra_lista) # da error ya q no es posible hacerlo asi
print (my_list - my_otra_lista) # da error ya q no es posible hacerlo asi

# convertir una lista a string
my_list = " hola que tal ya no soy una lista sino un string"
print(type(my_list)) # string


## OPERCIONES EN UNA LISTA ##

# Insertar un elemento al final de la lista
my_otra_lista.append("MaoreDev")
print(my_otra_lista)

# Insertar un dato en un elemento especifico de la lista
my_otra_lista.insert(1, "azul")
print(my_otra_lista)

#Eliminar un valor o elemento de la lista
my_otra_lista.remove("azul")
print(my_otra_lista)

#Sacar el ultima elemento de una lista
my_otra_lista.pop()
print(my_otra_lista)

#Sacar el elemento de una lista con el pop a traves del indice del elemento
my_otra_lista.pop(2)
print(my_otra_lista)

# Eliminar un elemento de una forma eficiente de una lista 
# recomendado
del my_list[2]
print(my_list)

# eliminar una lista
my_list.clear()
print(my_list)

# copiar los elementos de una lista a una nueva lista
my_new_list = my_list.copy()
print(my_new_list)

# Mostrar los elementos desde el final hacia el principio 
my_new_list.reverse()
print(my_new_list)

# Mostrar los elementos de una lista de  menor a mayor
my_new_list.sort()
print(my_new_list)

#Mostrar solo un parametro de elementos de uan lista

print(my_new_list[1:3]) # mostrara solo los elementos del 1 hasta el 3 y no el resto


