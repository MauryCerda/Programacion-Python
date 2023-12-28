### SETS ####

'''

DEFINICION
Un sets  es una colección de elementos únicos y no ordenados.
Esto significa que no puede haber elementos duplicados en un conjunto, y 
los elementos no se almacenan en un orden específico, como en una lista o una tupla.

'''
my_set = set() # La creacion de un set
print(type(my_set)) # set lo que significa es un tipo de dato

my_otro_set = {}
print(type(my_otro_set)) # no sale q el tipo es diccionario, pero no ser. por que?

my_otro_set = {"matias", "lendro", 23 }
print(type(my_otro_set)) # nos muestra q el tipo ahora es un set. por q si ante era un diccionario

''' La repuesta es que viene ya por si definido en el lenjuague de python, ya python los tipos son dinamicos
esto significa q si yo primero defino set despu lo puedo definir como diccionario y desp pasar a string y no hay problema, esto es
por que no es u tipiado fuerte. Pero en el momento que le ponemos datos a los {...} ya python sabe q es un set, por q la froma es que 
introducimos dato en la variable {} si es una forma correcta. '''

# saber la cantidad de elemento que tiene un set
print(len(my_otro_set)) # nos da 3 

# para acceder a un elemento especifico 
print(my_otro_set[0]) # nos da error, lo que no da a entender q no es lo mismo que una lista o tupla para acceder

# para agregar un elemento a un set 
my_otro_set.add("cabildo")
print(my_otro_set) # nos da cabildo, matias, lendro, 23 POR QUE si debria ser matias, lendro, 23, cabildo. Esto nos da la pauta q no es un lista ya q la lista era ordenado

## UN SET NO ES UNA ESTRUCTURA ORDENADA ## es por eso q al acceder a un elemento nos da error por q no es ordando indici 0,1,2,3..etc. Se desordena porq es a nivel de deficion q lo hace asi.



# agregamos un elemento mas pero repetido
my_otro_set.add("cabildo")
print(my_otro_set) # nos da cabildo, matias, lendro, 23. Esto es por que no permite o admite repetidos un set. UNA LISTA Y TUPLA SI ADMITEN REPETIDOS


# Comprobar si un elemento existe o no en un set
print("mauri" in my_otro_set) # nos da falso ya q no existe
print("matias" in my_otro_set) # nos da verdadero ya q si existe

#Eliminar un elemento de un set
my_otro_set.remove("matias")
print(my_otro_set) # lendro, 23 sale como resultado

# Borrar todos los elementos de un set
my_otro_set.clear()
print(my_otro_set) # set() nos da como repuesta
print(len(my_otro_set)) # 0  quiere decir q no hay elementos

# Eliminar un set
del my_otro_set
print(my_otro_set) #salta error ya que no existe el tipo set. no confundir con clear no es lo mismo ya q el clear elimina todos los  elemento

# convertir un set a lita 
my_set = {"chicago", "florida", "boston"}
my_list = list(my_set) # ESTE NO SUELE SER LO MEJOR YA QUE UN TIPO DE EJECUCION EL SET DA UN ORDEN Y AL SIGUIENTE EJECUCION OTRO ORDEN
print(my_list) # nos da ['chicago', 'florida', 'boston']
print(my_list[0]) # nos da chicago pero OJO en este tipo de ejecucion y volvemos a ejecutar de nuevo el codigo dara otro orden por el SET


# UNIR dos set
# creamos un set diferente para el ejemplo
my_other_set = {"kaka", "messi", "cr7"}
my_new_set = my_list.union(my_other_set)
print(my_new_set) # nos da (chicago, messi, florida, cr7, boston, kaka), ver q el set lo ordena de forma aletoria no ordenada

#Volvemos a unir pero esta vez con una de la lista repetida
my_new_set = my_list.union(my_other_set)
print(my_new_set.union(my_new_set)) # nos da los mismo (chicago, messi, florida, cr7, boston, kaka) ya que no permite repetirlo o duplicarlo
print(my_new_set.union(my_new_set).union({"java", "c++"})) # nos da (chicago, messi, java, florida, cr7, boston, kaka, c++) ESTO SI ESTA PERMITIDO HACERLO YA Q ESTAMOS INGRESANDO UN SET DIFERENTE (ES DECIR CON ELEMENTOS DIFERENTES)

# sacar los elementos de un set en la union de dos set o x cantidad de ser (unidos)
print(my_new_set.difference(my_set))
'''
vemos que my_new_set tiene los siguiente elementos:chicago, messi, florida, cr7, boston, kaka
despues vemos que my_list tiene los siguientes elementos: chicago, florida, boston

Al realiazar el difference nos da chicago, messi, florida, cr7, boston, kaka. Esto quiere decir que los elementos de my_set lo saca 

'''
'''
CUANDO UTILIZAR UNA LISTA, TUPLA O SET

* si queremos que sea inmutable, lo ideal es usar una TUPLA. (PODEMOS ACCEDER PERO NO MODIFICAR, LOS ELEMENTOS SON ORDENADOS)
* si queres modificar los elementos, nos sirve una LISTA. (PODEMOS ACCEDER Y MODIFICAR, LOS ELEMENTOS SON ORDENADOS Y REPETIDOS )
* si nos da igual el orden, pero no queremos que hallan elemenentos repetidos, nos sirve un SER (PODEMOS ACCEDER PERO NO MODIFICAR, LOS ELEMENTOS NO SON ORDENADOS NI REPETIDOS)

'''

