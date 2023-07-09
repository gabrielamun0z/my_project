#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                    #1- OPERADORES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#1.1 - OPERADORES DE ASIGNACIÓN
#-------------------------------------------------------------------------
#Asignar valores a variables 
x=5
x+=3 #x=x+3
x/=2 #x=x/2

#-------------------------------------------------------------------------
#1.2- OPERADORES ARITMÉTICOS
#-------------------------------------------------------------------------
#1.2.1- Operadores aritméticos con números
print(3 + 4) #sumar
print(3 * 4) #producto
print(4 / 2) #división
print(4 % 2) #módulo (resto de la división)
print(10 / 3)
print(10 // 3) #división floor (resultado un entero)
print(2 ** 3) #exponente
print(2 - 5 **6 // 8) #combinación de operadores

#1.2.2- Operadores aritméticos con cadenas de texto
print("Hola" + "mundo") #concatenación de strings
#Con cadenas de texto no todos los operadores son válidos (-, *,  **...)

#1.3.3- Operadores artiméticos con cadenas de texto y números
#print("Hola" + 5) #error
print("Hola" + str(5)) #debemos transformar int en str
print("Hola" * 5) #solo válido para enteros
#No todos los operadores son válidos

"""
print("Hola" * (2.5 * 2)) #error (aún teniendo que 2.5 * 2 = 5)
Esto ocurre porque en realidad toma 2.5 * 2.0 = 5.0 FLOAT
print(2.5*2)
print(type(2.5 *2))
"""

#-------------------------------------------------------------------------
#1.3- OPERARDORES DE COMPARACIÓN 
#-------------------------------------------------------------------------
#El resultado es  TRUE / FALSE
#1.3.1- Operadores de comparación entre números 
print(3 < 4)
print(3 <= 4)
print(3 > 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)
print(4 > 3 > 2) #comparación usando varios operadores 

#1.3.2- Operadores de comparación entre cadenas de  texto
print("aaaa" < "aaab") #ordenación alfabética por ASCII 
print("AAAA" == "aaaa") #tiene en cuenta las mayúsculas
print(len("aaa") < len("aaaaa")) #comparación de los caracteres

#-------------------------------------------------------------------------
#1.4- OPERADORES LÓGICOS
#-------------------------------------------------------------------------
#and / or / not
#Utiliza la lógica buleana
print(3 > 4 and "aaaa" > "aaab") #False and False = False
print(3 > 4 or "aaaa" > "aaab") #False o False = False
print(not 3 > 4 ) #not False = True