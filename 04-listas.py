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

lista = [35, 24, 62, 52, 30, 30, 15]
print(type(lista))
print("Edades: ", lista)

#-------------------------------------------------------------------------
#1.1- ACCESO A ELEMENTOS  
#-------------------------------------------------------------------------
#Empezando por el principio de la lista
#0, 1, 2, 3, ...
print(lista[1])
print(lista[2:4]) #del elemento 2 al 3 (4-1)
print(lista[1:4:2]) #del elemento 1 al 4 saltando de dos en dos
print(lista[::2]) #todas la lista saltando de dos en dos

#Empezando por el final de la lista
#...-3, -2, -1
print(lista[-1]) #último elemento

#Desempaquetar elementos de una lista
lista1=["1item", "2item", "3item", "4item", "5item", "6item"]

first_item, second_item, third_item, *rest = lista1
print(first_item)  
print(second_item)   
print(third_item)     
print(rest) 

first_item, second_item, *rest, sixth_item = lista1
print(first_item)  
print(second_item)   
print(rest) 
print(sixth_item)     

#-------------------------------------------------------------------------
#1.2- OPERACIOES CON ELEMENTOS 
#-------------------------------------------------------------------------
#Número de veces que aparece un elemento 
print(lista.count(30))

#Modificar elementos de la lista
lista[1]=18 #cambio el elemento en la posición 1 por el número 18

#Comprobar elementos de la lista
does_exist =30 in lista
print(does_exist)

print(24 in lista)

#Añadir elementos AL FINAL de una lista
lista1.append("new_item")
print(lista1)

#Añadir elementos EN UN DETERMINADO ÍNDICE a una lista
lista1.insert(0, "0item") #(índice, "elemento")
print(lista1)

#Eliminar elementos de una lista USANDO EL NOMBRE DEL ELEMENTO
lista1.remove("2item") #.remove("elemento")
print(lista1)

#Eliminar elementos de una lista USANDO EL ÍNDICE DEL ELEMENTO
#a) Eliminando un único elemento (pop)
lista1.pop(2) #.pop(índice)
print(lista1)

#b) Seleccionando varios elementos
del lista1[1:3] 
print(lista1)

#del lista1 #Elimina la lista entera (dando error)
#print(lista1) #NameError: name 'lista1' is not defined.

#Eliminar la lista entera (no da error)
lista1.clear()
print(lista1) #[]

#Índice de un elemento
print(lista.index(18))


#-------------------------------------------------------------------------
#1.2- OPERACIONES CON LISTAS
#-------------------------------------------------------------------------
pos=[1, 2, 3, 4, 5]
neg=[-5, -4, -3, -2, -1]
zero=[0]
#Copiar una lista 
lista=lista.copy

#Juntar listas
#a) Creando una nueva lista
enteros = pos + zero + neg
print(enteros)

#b) Modificando una de las listas
pos.extend(zero)
print(pos)

#Revertir
pos.reverse()
print(pos)

#Ordenar elementos 
#a) Cambiando la lista original
pos.sort() #ascendente
print(pos)

pos.sort(reverse=True) #descendente
print(pos)

#b) Sin cambiar la lista original
print(sorted(enteros)) #ascendente
print(sorted(enteros, reverse=True))