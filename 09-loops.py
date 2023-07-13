#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- LOOPS / BUCLES
                        #while loop
                        #for loop
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Sirve para iterar, pasar por el mismo código varias veces
#-------------------------------------------------------------------------
#1.1- WHILE LOOP
        #while condition:
                #código
#-------------------------------------------------------------------------
#Se ejecuta el bloque mientras que una condición sea VERDADERA. Si la condición es FALSA
#paran ejecutándose las siguientes lineas del código
my_condition = 0

while my_condition<10:
    print(my_condition)
    my_condition+=2 
print(my_condition) #10 (queda almacenada con el último valor que tomó)
                    #al valor 8 (<10) le suma 2, y como 10 (=8+2) no es <10, no vuelve a hacer el bucle y por eso no lo imprime
#Si queremos ejecutar un código cuando deje de cumplirse el while
my_condition=0
while my_condition<10:
    my_condition+=2 
    print(my_condition) 
else:                   #opcional 
    print("Mayor o igual que 10")

#-------------------------------------------------------------------------
#1.2- BREAK AND CONTINUE (1)
#-------------------------------------------------------------------------
#BREAK: cuando queremos salir o parar el loop
        #while condition:
                #código
                #if condition2:
                    #break
my_condition=0
while my_condition<10:
    print(my_condition)
    my_condition+=2
    if my_condition==3: #no para porque nunca toma el valor 3
        break

my_condition=0
while my_condition<10:
    print(my_condition)
    my_condition+=2
    if my_condition==4: #para en el 2 (primero imprime 2, luego +2 =4 y luego comprueba el if)
        break

#CONTINUE: podemos saltar la iteración y continuar con la siguiente (si esa condición no se cumple)
my_condition=0
while my_condition<20:
    print(my_condition)
    my_condition+= 2
    if my_condition == 8:
        print("Mi condicion es 8")
        continue
#-------------------------------------------------------------------------
#1.3- FOR LOOP
        #for iterator in lista/tupla/diccionario/set/string
                #código
#-------------------------------------------------------------------------
#Iterar en una secuancia que es: lista, tupla, diccionario, set o string (cualquier estructura que tenga la capacidad de almacenar elementos)
#Un "for" se repite tantas veces como elementos tenga la secuencia

#Lista 
lista=[0, 1, 2, 3, 4, 5]
for element in lista: #element = nombre temporal para refrirnos a los elementos de la lista
    print(element) #elementos de la lista

#Set
set={"Gabriela", "Muñoz", 22}
for element in set:
    print(element) #elementos del set

#Tupla
tupla=("Gabriela", "Muñoz", 22, 1.55)
for element in tupla:
    print(element) #elementos de la tupla

#Diccionario
dict={"Nombre":"Gabriela", "Apellido":"Muñoz", "Edad":22, "País":"España"}

#a) 
for element in dict:
    print(element) #clases 


for element in dict:
    print(element)
    if element == "Edad":  #en cada iteración comprueba si element == "Edad", cuando ocurre eso, para el bucle
        break


#b)
for element in list(dict.values()):
    print(element) #valores

#String
languaje = "Python"
for element in languaje:
    print (element) #cada uno de los caracteres

for i in range(len(languaje)): #igual
    print(languaje[i])

print(range(len(languaje))) #range(0, 6) : numeros del 0 al 5 (6-1)

#-------------------------------------------------------------------------
#1.4- FUNCIÓN RANGE
        #range(start, end, step)
#-------------------------------------------------------------------------
#La función "range" necesita por lo menos un parámetro: end
#Por defecto empieza en 0 y el step vale 1
#Crea una LISTA de números

#Lista
lista=list(range(11))
print(lista)

#Set
st=set(range(0, 11, 2))
print(st)
#-------------------------------------------------------------------------
#1.5- NESTED PARA LOOP
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#1.6- FOR ELSE
#-------------------------------------------------------------------------
