#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- CLASES
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Creamos clases para crear objetos (todo lo que esté dentro de una cierta clase tiene que responder a una cierta lógica)
#Todo elemento en un programa de Python es un objeto de una clase
#-------------------------------------------------------------------------
#1.1- DEFINICIÓN
#-------------------------------------------------------------------------
#Crear una clase
class Person: 
    pass #evitar error
print(Person)  #<class '__main__.Person'>
print(Person()) #se ponene los paréntesis cuando necesite algo para poder ejecutarse

#Crear un objeto
p = Person()
print(p) #<__main__.Person object at 0x00000291F906E410>

#-------------------------------------------------------------------------
#1.2- CONSTRUCTOR DE CLASE (__init__(self, ...))
#-------------------------------------------------------------------------
class Person:
    def __init__(self, name, surname): #lugar donde podemos establecer ciertos valores asociados a "persona" 
        pass                           #SELF es necesario

#Creación de propiedades dentro de la clase
class Person:
    def __init__(self, name, surname):
        self.name = name            #propiedad 1     
        self.surname = surname      #propiedad 2
my_person=Person(name="Gabriela", surname="Muñoz")

#Acceso a los valores
print(my_person) #no hace nada
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")
print(my_person.name, my_person.surname)


class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self): #función dentro de la clase
        print(f"{self.full_name} está caminando")
my_person= Person("Gabriela", "Muñoz")
print(my_person.full_name)
my_person.walk()

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #2- OBJETOS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------