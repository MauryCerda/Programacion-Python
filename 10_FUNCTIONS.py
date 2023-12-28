### FUNCIONES ###

'''
DEFINICION

Una función es un bloque de código reutilizable que realiza una tarea específica. 
Las funciones permiten organizar el código en fragmentos más pequeños y modulares, 
lo que facilita la lectura, el mantenimiento y la reutilización del código. 
Una función puede recibir datos como entrada (llamados argumentos o parámetros), realizar alguna operación y devolver un resultado.

'''
#Definimos una funcion
def mi_funcion():
	print("esto es una funcion")

# llamamos a la funcion, la podemos llamar cuantas veces queramos en el codigo 
mi_funcion()

# ejemplo de suma de dos valores enteros
def suma_dos_valores(numero1, numero2):
	print(numero1 + numero2)

suma_dos_valores(7,7)

# ejemplo de suma de dos valores tipo string
def suma_dos_valores(numero1, numero2):
	print(numero1 + numero2) # da 77

suma_dos_valores("7","7")

# ejemplo de suma de dos valores enteros si o si
def suma_dos_valores(numero1: int, numero2: int):
	print(numero1 + numero2)

suma_dos_valores(7,7)

# ejemplo de suma de dos valores decimales
def suma_dos_valores(numero1, numero2):
	print(numero1 + numero2) # da 14.4

suma_dos_valores(7.2, 7.2)

# definimos una funcion y q esta retorna algo(retorna o devuelve el resultado)
def suma_dos_valores_con_return(numero1, numero2):
	return numero1 + numero2

mi_resultado = suma_dos_valores_con_return(5,5)
print(mi_resultado) # la funcion retorna la suma q es 10

# ejemplo de una funcion con parametro cadena de texto y que la funcion lo concatene
def print_nombre (nombre, apellido):
	print(f"{nombre} {apellido}")

print_nombre("Juan","luich")

# ejemplo mas pero esta vez si la pers no pasa un alias ya la funcion lo tiene por defecto
def print_nombre (nombre, apellido, alias="sin alias"):
	print(f"{nombre} {apellido}")

print_nombre("Juan","luich") # sale Juan luich sin alias

#hacer una funcion q reiba parametros y lo tranforma a texto
def print_texto(*text):
	print(text) # da ('hola','che','españa')

print_texto("hola", "che","españa")

