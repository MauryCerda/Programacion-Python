### MODULOS ###
'''
DEFINICION 

un módulo es un archivo que contiene código Python. Este código puede incluir funciones, clases y variables, 
y su propósito es organizar y reutilizar el código de manera efectiva. 
Los módulos permiten dividir un programa grande en partes más pequeñas y manejables.


'''
# HAY Q TENER EN CUENTA LA NOMENCLATURA DE LOS MODULOS
import module
module.suma(7,8)

# un ejemplo de como acceder a una funcion especifica de un modulo o fichero 
from functions import suma
functions.suma(7,8) # esto da error porque ya estamos importando esa funcion especifica
suma(7,8) # si importamos la funcion especifica, basta con poner el nombre de la funcion y pasar los parametros

# modulos ya integrados a la hora de instalar python
import math  # estos son modulos q ya viene instalado a la hora de instalar pyhton
