### CLASES ###
'''
DEFINICION

una clase es una plantilla para la creación de objetos. 
Los objetos son instancias de clases y representan entidades del mundo real. 
Las clases proporcionan una forma de encapsular datos y funciones que operan en esos datos en un solo conjunto lógico. 
Utilizando programación orientada a objetos (OOP, por sus siglas en inglés), puedes modelar y organizar tu código de manera más efectiva.

'''
# definimos una clase
class Persona:
	pass # el pass es esencial para q una clase funcione sino esta sale error

print("hola")


# una clasae con __init__
class Person:
	def __init__(self, nombre, apellido): # el __init__ se define el constructor, self es algo obligatorio, si nosotros queremos crear una clase q tenga un constructor el self es obligatorio, se refiere "a el mismo"
		pass
my_person = Person("hector", "kirl")
print(my_person)
	

# una clasae con self
class Person:
	def __init__(self, nombre, apellido): 
		self.nombre= nombre 
		self.apellido= apellido # si nostros estamos adrento de la clase persona, se refiere a la instancia de persona 
my_person = Person("hector", "kirl")
print(my_person.name)
print(my_person) # da hector

# ejemplo de una clase q tiene funciones
class Person:
	def __init__(self, name, apellido):
		self.full_name = f"{name}{apellido}"

	def walk(self):
		print(f"{self.full_name} esta camiando ")

my_person= Person("kaka","ruiz")
print(my_person.full_name)
my_person.walk()


