#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
              #1- TUPLAS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Tupla: colección de data types ordeandos y no modificable.
#Por lo tanto, la mayoría de las operaciones de elementos que había en listas, ahora no podemos usarlas
tupla = tuple() #forma 1
tupla = ()  #forma 2

tupla = (22, 1.57, "Gabriela", "Muñoz")

#-------------------------------------------------------------------------
#1.1- ACCESO A ELEMENTOS
#-------------------------------------------------------------------------
#Funciona análogo a las listas
#Empezando por el principio de la lista
print(tupla[0]) #elemento en esa posición
print(tupla[0:2]) #del elemento 0 al 1 (2-1)
print(tupla[0:]) #todos los elementos (del 0 al final)
print(tupla[1:3]) 
print(tupla[::2])

#Empezando por el final de la lista
print(tupla[-2])

#Desempaquetar elementos
first_item, *rest = tupla
print(first_item)

#Cambiar de tupla a lista
tupla1=("1item", "2item", "3item")
print(type(tupla1))
lista1 = list(tupla1)
print(type(lista1))
print(type(tupla1)) #lo que definimos como tupla sigue siéndolo
print(tupla1) #()
print(lista1) #[]

#-------------------------------------------------------------------------
#1.2- OPERACIONES CON ELEMENTOS
#-------------------------------------------------------------------------
#Número de veces que aaparece un elemento
print(tupla.count("Gabriela"))

#Comprobar elementos de la tupla
print("Gabriela" in tupla)

#Eliminar una tupla entera 
del tupla
#print(tupla) #NameError: name 'tupla1' is not defined.

#-------------------------------------------------------------------------
#1.3- OPERACIONES CON TUPLAS
#-------------------------------------------------------------------------
#Número de elementos
print(len(tupla1))

#Juntar tuplas 
tupla2 = ("4item", "5item")
tupla3= tupla1 + tupla2
#para tuplas no existe la función de modificar una de ellas

