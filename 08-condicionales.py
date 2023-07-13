#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- CONDICIONALES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#1.1- IF CONDITION
        #if condition:
                #esta parte se ejecuta para condiciones verdaderas
#-------------------------------------------------------------------------
#Comprobar si una condición es VERDADERA y ejecutar el bloque entero
#EJ: condición verdadera
my_condition = True #buleano
if my_condition:
        print("Se ejecuta la condición del if")

print("La ejecución contniúa")

#EJ: condición falsa
my_condition2 = False
if my_condition2: #no se ejecuta (solo lo hace cuando es True)
        print("No se ejecuta la condición del if")

print("La ejecución continúa")

#-------------------------------------------------------------------------
#1.2- IF ELSE
        #if condition:
                #esta parte se ejecuta para condiciones verdaderas
        #else:
                #esta parte se ejecuta para condiciones falsas
#-------------------------------------------------------------------------
#Si la condición es VERDADERA ejecuta el bloque "if", en caso contrario ejecita el bloque "else"
my_condition = 5*2
if my_condition2 > 10:
        print("Es mayor que 10")
else:
        print("Es menor o igual que 10")

#EJ: Varias condiciones (operadores lógicos)
if my_condition >10 and my_condition<20:
        print("Es mayor que 10 y menor que 20")
else:
        print("Es menor o igual que 10 o mayor o igual que 20")


#-------------------------------------------------------------------------
#1.3- IF ELIF ELSE
        #if condition1 :
                #esta parte se ejecuta si condiciton1 es verdadera
        #elif condition2:
                #esta parte se ejecuta si condition2 es verdadera
        #...

        #else:
                #si ninguna de las condiciones de arriba se cumple
#-------------------------------------------------------------------------
#Para comprobar si cumple varias condiciones a la vez
if my_condition > 10:
        print("Es mayor que 10")
elif my_condition == 10:
        print("Es igual a 10")
else:
        print("Es menor que 10")

#-------------------------------------------------------------------------
#1.4 SHORT HAND
        #código if condition else código
#-------------------------------------------------------------------------
#Cuando solo tenemos una condición que ejecutar (una para if y otra para else), podemos escribirlo todo en una línea
print("Es mayor que 10") if my_condition > 10 else print("Es menor o igual que 10")

#-------------------------------------------------------------------------
#1.5- NESTED CONDITIONS
        #if condition:
                #se ejecuta si condition es verdadera
                #if condition2:
                        #se ejecuta si condition2 es verdadera
#-------------------------------------------------------------------------
#If dentro de un if
if my_condition > 10:
        if my_condition % 2 == 0:
                print("Mayor que 10 y par")
        else:
                print("Mayor que 10 e impar")
elif my_condition ==0:
        print("Igual a 0")
else:
        if my_condition %2 ==0:
                print("Menor que 10 y par")
        else:
                print("Menor que 10 e impar")

#-------------------------------------------------------------------------
#1.6- IF CONDITION AND LOGICAL OPERATOR
        #if condition1 and condition2:
                #se ejecuta si ambas son verdaderas
#-------------------------------------------------------------------------
if my_condition >10 and my_condition<20:
        print("Es mayor que 10 y menor que 20")
else:
        print("Es menor o igual que 10 o mayor o igual que 20")

#-------------------------------------------------------------------------
#1.7- IF AND OR LOGICAL OPERATOR
        #if condition1 or condition2:
                #se ejecuta si al menos una de ellas es verdadera
#-------------------------------------------------------------------------
user = "Gabriela"
access_level=3
if user=="admin" or access_level>=4:
        print("Acceso permitido")
else:
        print("Acceso denegado")

