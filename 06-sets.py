#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- SETS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Set: colección de elementos, sin ordenar y sin índices y no modificable (aunque si permite añadir nuevos elementos)
st = set() #forma 1
st1 = {} #forma 2

print(type(st1)) #Inicialemnte dice que es un diccionario
st1 = {22, "Gabriela", "Muñoz"}
print(type(st1)) #Ahora adopata la clase de set

#print(st1[1]) #ERROR
#Un set no es una estructura ordenada (su forma de guardar elementos es desordenada)

#Cambiar de set a lista
lista1 = list(st1)
print(type(lista1))

#-------------------------------------------------------------------------
#1.1- OPERACIONES CON ELEMENTOS
#-------------------------------------------------------------------------
st = {"1item", "2item", "3item"}

#Añadir elementos
#a) Añadir elementos de uno en uno
st.add("4item") 
print(st) #lo añade al inicio del set

#b) Añadir varios elementos a la vez
st.update(["5item", "6item"])

#Cada vez que ejecutamos el programa, almacena los elementos que añadimos en un lugar del set,
#ese lugar es aleatorio

st.add("4item") #No añade elementos repetidos
print(st)

#Búsqueda de un elemento en el set
print("1item" in st)

#Eliminar elementos de un set
#a) Función "remove"
st.remove("6item")
print(st)
#Problema: si el elemento no está en el set, da error
#st.remove("8item") #KeyError: '8item'

#b) Función "discard"
st.discard("5item")
print(st)
#Si el elemento no está en el set, NO da error

#Eliminar la lista entera
#a) Limpiar / Vaciar (pero el set sigue creado)
st1.clear()

#b) Elimiar (el set deja de estar definido)
del st1



#-------------------------------------------------------------------------
#1.2- OPERACIONES CON SETS
#-------------------------------------------------------------------------
#Número de elementos totales
print(len(st))

#Juntar sets / Unión
st2= {"other_item"}
#a) Creando un nuevo set
st3 = st.union(st2)
print(st3)

#b) Añaiendo elementos a un set ya creado
st.update(st2)
print(st.update(st2))

#Intersección de sets
st4={"H", "J", "K"}
st5={"K", "L"}
st6={"K"}
print(st4.intersection(st5))

#Contenido
#a) Contenido en...
print(st6.issubset(st4)) #True (st6 contenido en st4)
print(st5.issubset(st4)) #False7

#b) Contiene a...
print(st4.issuperset(st6)) #True 
