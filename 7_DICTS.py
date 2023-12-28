#### DICCIONARIO ####

'''
DEFINICION 

Un diccionario es una estructura de datos que permite almacenar pares clave-valor. 
Cada elemento en un diccionario tiene una clave única que se utiliza para acceder al valor asociado. 
Los diccionarios en Python son muy flexibles y pueden contener valores de cualquier tipo, incluyendo otros diccionarios.

Puedes pensar en un diccionario como una especie de lista, pero en lugar de acceder a los elementos por su posición (como en una lista), 
accedes a los elementos por su clave. Los diccionarios son objetos mutables, 
lo que significa que puedes agregar, modificar o eliminar elementos después de que el diccionario ha sido creado.

'''

# FROMA DE DEFINIR UN DICCIONARIO
my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # TIPO DICCCIONARIO
print(type(my_other_dict)) # TIPO DICCCIONARIO

# ACCEDEMOS A UN VALOR DEUN DICCIONARIO
print(my_dict["Nombre"]) # Sale: mauri

# METEMOS DATOS AL DICCIONARIO (forma simple)
my_other_dict = {"Nombre": "Mauri", "Apellido": "Cerda","Edad":"23", 1:"Java"}

# METEMOS DATOS AL DICCIONARIO (forma mas complicada)
my_dict = {
	"Nombre": "Mauri", 
	"Apellido": "Cerda",
	"Edad":"23", 
	1:"España",
	"lenguaje":{"java","pythpn","node"},
	2:1.54
}

print(my_dict) # sale : "Nombre": "Mauri", "Apellido": "Cerda","Edad":"23", 1:"España","lenguaje":{"java","pythpn","node"}, 2:1.54
print(my_other_dict) # sale: "Nombre": "Mauri", "Apellido": "Cerda","Edad":"23", 1:"Java"

# MODIFICAMOS UN VALOR A UNA CLAVE DEL DICCIONARIO
print(my_dict["Nombre"])="Pedro"
print(my_dict["Nombre"]) # sale : pedro

#SABER LA LONGUITUD DE UN DICCIONARIO
print(len(my_other_dict)) # son 4 ya q toma la clave y valor como un elemento


# BUSCAR UNA CLAVE EN UN DICCIONARIO
print(my_dict["1"]) # esto da error ya que la clave no es string  sino entero
print(my_dict[1]) # esta seria la forma correcta , lo q da como resultado: 1.54

# AGREGAMOS UNA NUVA CLAVE Y NUEVO VALOR A UN DICCIONARIO 
print(my_dict["Calle"]) = "SanLorenzo"
print(my_dict) # sale : "Nombre": "Mauri", "Apellido": "Cerda","Edad":"23", 1:"España","lenguaje":{"java","pythpn","node"}, 2:1.54, "Calle":"SanLorenzo"


# OPERACIONES EN DICCIONARIO 
# ELIMINAR UNA CLAVE CON SU VALOR DE UN DICICONARIO
del my_dict["Calle"]
print(my_dict) # "Nombre": "Mauri", "Apellido": "Cerda","Edad":"23", 1:"España","lenguaje":{"java","pythpn","node"}, 2:1.54

#ELIMINAR UNA DICCIONARIO ENTERO CON TODOS SUS CLAVE Y VALORES
del my_dict

# BUSCAR SI EXISTE O SI ESTA ALGO EN EL DICCIONARIO 
print("Cerda" in my_dict) # esto da errro ya que no busca en el diccionario por el valor sino por la clave. A TNER EN CUENTA
print("Apellido" in my_dict) # Sale True ya que es una clave y si busca por clave 

#MOSTRAR UN LISTADO CON CADA UNO DE LOS ITEMS
print(my_dict.items())

#MOSTRAR EN FORMA DE LISTA SOLAMENTE LAS CLAVES
print(my_dict.keys())

#MOSTRAR EN FORMA DE LISTA LOS VALORES DE UN DICICONARIO
print(my_dict.values())

#CREAR UN DICCIONARIO NUEVO PERO SIN VALORES
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso")) # Aca ponemos las claves en la que queremos que no tengan un valor, en este caso es Nombre y 1
print(my_new_dict) #{'Nombre': None, 1:None, 'Piso': None}

#CONVERTIR UN DICCIONARIO A LISTA
print(list(my_new_dict))

# CONVERTIR UN DICCIONARIO A TUPLA
print(tuple(my_new_dict))

# CONVERTIR UN DICCIONARIO A SET
print(set(my_new_dict))




