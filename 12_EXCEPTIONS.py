### EXCEPCIONES ###
'''
DEFINICION
las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de ejecución. 
Cuando ocurre una excepción, se crea un objeto de excepción que contiene información sobre el error, como el tipo de excepción, 
el mensaje de error y la ubicación en el código donde ocurrió la excepción.

try = Tenemos un codigo y metemos try, Vamos a correr un codigo (si queremos controlar errorer)
except = si este codigo presenta un error en la ejecucion, se va por un bloque q se llama except
else = sino se produce un error se va por el bloque else 
finally =  pase lo pase, ya sea except o else se va por el bloque de finally 
'''
numero1 = 5

numero2= 1
numero2= "1"

print(numero1 + numero2) # da erro ya que python no suma enteros con cadena de texto

# UNA FORMA DE CORREGIR EL ERRO DE FORMA A "MANO", NO ES LO RECOEMDABLE, ADEMAS SABEMOS CUAL ES EL ERROR Y QUEREMOS CONTROLARLA
if type(numero2) == int:
	print(numero1 + numero2)
else:
	print("No se cumplio condicion")

# ACA YA LE METEMOS UN TRY Y EMPEZAMOS A USAR LAS EXCEPCIONES
#try except 
try:
	print(numero1 + numero2)
	print("No se ha producido un error")
except:
	print("se ha producido un error")

#try except else
try:
	print(numero1 + numero2)
	print("No se ha producido un error")
except: # se ejecuta si no se produce un try
	print("se ha producido un error")
else: # se ejecuta si no se produce un except
	print("la ejecucion continua correctamente") # no aparece ya que se ha producido un error y el progrma queda en la line de codigo de except

finally: # se ejecuta siempre, pase lo pase
	print("la ejecucion continua")

#excepciones por tipo, va a salir el mensaje dependiendo del error lo demas errores no lo va a mostrar
try:
	print(numero1 + numero2)
	print("No se ha producido un error")
except TypeError: 
	print("se ha producido un error TypeError")
except ValueError: 
	print("se ha producido un error ValueError")


#Captura de la informacion de la excepcion
try:
	print(numero1 + numero2)
	print("No se ha producido un error")
except ValueError as error: 
	print(error)
except Exception as exception:  # esto se usa cuando no se sabe el tipo de error q es y que el codigo muesrtre el error ( en exception o error puede ir cualquier nombre)
	print(exception)

