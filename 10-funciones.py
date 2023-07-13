#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- FUNCIONES
                        #def function_name():
                                #código
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Código REUTILIZABLE que ejecuta una tarea determinada

#def function_name():
                    #código


##-------------------------------------------------------------------------
#1.1- FUNCIÓN SIN PARÁMETROS
#-------------------------------------------------------------------------
def funcion():
    print("Esto es una función")
funcion() #llamada a la función

#Return 
def sum_two_values():
    valor1=2
    valor2=5
    total=valor1 + valor2
    return total
print(sum_two_values()) #7
#La función "return" necesita un print porque el valor está almacenado en una variable
#Análogamente:
my_result = sum_two_values()
print(my_result)


#-------------------------------------------------------------------------
#1.2- FUNCIÓN CON PARÁMETROS
#-------------------------------------------------------------------------
def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def generate_full_name(name, surname):
    space = " "
    full_name=name + space + surname
    return full_name
print(generate_full_name("Gabriela", "Muñoz"))
print(generate_full_name(surname="Muñoz", name="Gabriela")) #el orden no importa


#En cuanto llega el return, deja de ejecutar
def is_even(num):
    if num %2==0:
        print("Par")
        return True
    return False
is_even(2) #Par
print(is_even(2)) #Par / True

#-------------------------------------------------------------------------
#1.3- PARÁMETROS POR DEFECTO (default)
#-------------------------------------------------------------------------
#Dentro de los parámetros de entrada, le indico cuál es por defecto
def generate_full_name_with_default(name, surname, alias = "Sin alias"):
    full_name_default= name + " " + surname + " " + alias
    return full_name_default
print(generate_full_name_with_default("Gabriela", "Muñoz"))
print(generate_full_name_with_default("Gabriela", "Muñoz,", "Gabri"))


