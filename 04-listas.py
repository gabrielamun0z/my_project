#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- LISTAS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Listas: colección ordenada y modificable, que permite elementos duplicados.
#Los elementos de una lista son cualesquiera (strings o números)

#Defino la variable como lista 
lista = list() #forma 1
lista = [] #forma 2

lista = [35, 24, 62, 52, 30, 30, 17]
print(type(lista))
print("Edades: ", lista)

#-------------------------------------------------------------------------
#1.1- DIVISIÓN 
#-------------------------------------------------------------------------
#Empezando por el principio de la lista
print(lista[1])
print(lista[2:4]) #del elemento 2 al 3 (4-1)
print(lista[1:4:2]) #del elemento 1 al 4 saltando de dos en dos
                