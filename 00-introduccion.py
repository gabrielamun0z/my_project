#comentario

"""
Esto es un comentario en varias líneas, 
sin necesidad de poner # en cada línea
"""
'''
Esto tambien en un comentario en varias líneas, 
sin necesidad de poner # en cada línea
'''

print("Hola mundo")
print('Hola mundo')
#las cadenas de texto las podemos poner con comilla doble (") o simple (')
print(3)

#"print" puede llevar varios argumentos separados por comas
print(3, "Hola mundo", "Adiós")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                    #1- DATA TYPES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Consultar el tipo de datos (para que lo muestre por pantalla añadimos print)
print(type(3)) 
print(type("3")) #al ponerlo entre comillas lo lee como una lista

#-------------------------------------------------------------------------
#1.1- NÚMEROS
    #Integer
    #Float
    #Complejo
#-------------------------------------------------------------------------
print(type(5))
print(type(4.76))
print(type(1+3j))

#-------------------------------------------------------------------------
#1.2- STRING / CADENAS DE TEXTO
#-------------------------------------------------------------------------
#Cualquier cosa entr comillas " " la va a identificar como una  cadena de texto
print(type("Hola mundo"))
print(type("1.5"))

#-------------------------------------------------------------------------
#1.3- BULEANOS (true / false)
#-------------------------------------------------------------------------
print(type(True))

#-------------------------------------------------------------------------
#1.4- LISTA
#-------------------------------------------------------------------------
#Listas: colección ordenada y modificable, que permite elementos duplicados
#Cualquier cosa entre corchetes [] la identifica como lista
#los elementos de una lista son cualquiera de los anteriores
print(type([1, 2, 3]))
print(type(["hola", 2, 4.5]))

#-------------------------------------------------------------------------
#1.5 - DICCIONARIOS
#-------------------------------------------------------------------------
#Diccionario: colección no ordenada, modificable y con índices, que no permite elementos duplicados.
print(type({'name' : 'Hola'}))

#-------------------------------------------------------------------------
#1.6- SET
#-------------------------------------------------------------------------
#Set: colección no ordenada, no modificable y sin índices, que no permite elementos duplicados.
#Aunque sea no modificable, permite añadir nuevos elementos.
print(type({2, 4.4, 1}))

#-------------------------------------------------------------------------
#1.7- TUPLA
#-------------------------------------------------------------------------
#Tupla: colección ordenada, no modificable, que permite elementos duplicados.
print(type((2, 4.4, 1)))












