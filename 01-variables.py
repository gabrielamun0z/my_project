#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                    # 1- VARIABLES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
var1=3 #variable integer
print(var1)

var2="Hola mundo" #variable string
print(var2)

var3=False #variable buleana
print(var3)

print(var1, var2, var3) 

#Crear variables en una sola linea
nombre, apellido, edad = "Gabri", "Muñoz", 22 #puedo mezclar tipos de datos (string, string, integer)
print(nombre)
print(nombre ,apellido)
print("Me llamo", nombre, apellido, "y tengo: ", edad, "años.")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #2- OPERACIONES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#2.1- TRANSFORMAR EL TIPO DE DATO
#-------------------------------------------------------------------------
#Obviamente el tipo de dato tiene que ser coherente a lo que lo queremos tranformar
var4=str(var1) #tranformar en string
var5="10" #variable string 
var6= int(var5) #transformar en integer
print(type(var5))
print(type(var6))
var7="True" #variable string
var8=bool(var7) #tranformar a buleano
print(type(var7))
print(type(var8))
#var9=int(var7) #error
#print(type(var9))

#-------------------------------------------------------------------------
#2.2- LEN
#-------------------------------------------------------------------------
#La función "len" solo es válida para cadenas de texto
print(len(var2)) #cuenta los espacios
#print(len(var1)) #error
print(len(var4)) #tranformada en caracter
#print(len(var3)) #error

#-------------------------------------------------------------------------
#2.3- INPUT
#-------------------------------------------------------------------------
#Escribir sobre la consola y almacenar esa variable
ciudad=input("¿Dónde vives?")
print(ciudad)


