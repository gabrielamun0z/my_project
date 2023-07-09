#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- STRINGS / CADENAS DE TEXTO
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
var1="Hola mundo"
var2="Adiós mundo"
print(var1)
print(len(var1))
print(var1 + var2)

new_line_string="String \n con salto de línea" #salto de línea
print(new_line_string)

tab_string="\t String con tabulación" #tabulación
print(tab_string)

scape_string="\t String \n escapado" #tabulación + salto de línea (sin tabulación)
print(scape_string)

slap_string="Imprime una de las barras \\"
print(slap_string)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #2- FORMATEO DE STRINGS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
name, surname, age = "Gabriela", "Muñoz", 22 #string, string, entero

#-------------------------------------------------------------------------
#2.1- OLD STYLE
#-------------------------------------------------------------------------
#Concretamos el tipo de variable 
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))

#-------------------------------------------------------------------------
#2.2- NEW STYLE
#-------------------------------------------------------------------------
#No es necesario concretar el tipo de variable
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))

#-------------------------------------------------------------------------
#2.3- INFERENCIA/INTERPOLACIÓN DE DATOS (f-string)
#-------------------------------------------------------------------------
print(f"Mi nombre es {name} {surname} y tengo {age} años")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #3- DESEMPAQUETADO DE CARACTERES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
languaje = "Python"
a, b, c, d, e, f = languaje #número de variables por cada caracter del string
print(a)
print(b)
print(c, f)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #4- DIVISIÓN
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#Empezando por el principio de la cadena
languaje_slice=languaje[1:3]
print(languaje_slice)

languaje_slice=languaje[1:]
print(languaje_slice)

last_index=len(languaje) -1 #-1 porque empieza a contar en 0
languaje_slice=languaje[last_index]
print(languaje_slice)

#Empezando por el final de la cadena (índices negativos)
languaje_slice=languaje[-2]
print(languaje_slice)

#Tomar varios elementos
languaje_slice=languaje[0:6:2] #del elemento 0 al 6 dando saltos de dos en dos

#Revertir la cadena
reversed_languaje=languaje[:: -1]
print(reversed_languaje)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #5- FUNCIONES PARA STRING
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Al poner tras el nombre de la variable un punto, salen las operaciones que tenemos disponibles
print(languaje.capitalize()) #primera letra en mayúscula
print(languaje.upper()) #todas en mayúscula
print(languaje.upper().isupper()) #tranforma en mayúscula, comprueba si todas están en mayúscula
print(languaje.lower()) #todas minúsculas

print(languaje.count("t")) #número de veces que aparece un caracter
print(languaje.count("on")) #veces que aparece una cadena de texto, dentro de una cadena de texto
print(languaje.count("y", 2, 5)) #veces que aparece un caracter entre dos caracteres (posición)
print(languaje.endswith("on")) #si la cadena de texto termina con un/unos caracteres específicos
print(languaje.startswith("P")) #comprueba si la cadena empieza con un determinado caracter

print(languaje.find("h")) #última posición en que aparece un caracter 
print(languaje.find("ho")) #da la posición del comienzo de ese estracto de cadena
print(languaje.find("a")) #-1 (no aparece)
print(languaje.rfind("h")) #primera posición en que aparece un caracter

print(languaje.isnumeric()) #¿Es un número?
var="1"
print(type(var))
print(var.isnumeric()) #aunque esté definido como cadena de texto, reconoceque es un número

print(languaje.replace("Python", "Hola")) #reemplaza un/unos caracteres por otros
print(languaje.replace("P", "T"))

frase="Hola mundo"
print(frase.title()) #cada inicio de una nueva palabra en mayúscula