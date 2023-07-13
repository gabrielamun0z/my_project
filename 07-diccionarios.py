#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
                #1- DICCIONARIOS
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Diccionario: colección de elementos sin ordenar y modificable.

dict=dict() #forma 1
dict={} #forma 2 (el interior el lo que le diferencia del set)

dict={
    "Nombre": "Gabriela", 
    "Apellido":"Muñoz", 
    "Edad" : 22, 
    "Ciudad": ["León", "Santiago"],
    1: 1.57,
    "Dirección":{
        "Calle" : "Tal",
        "Código postal": "00032", #POR QUÉ NO ME DEJA PONERLO SIN "" Y EN 1 SI ?
    }
    } 
        #Relación: clave - valor
        #Estructura que nos sirve para relacionar datos
        #La clave y el valor puede ser cualquier tipo de data type (+ diccionario dentro de diccionario)
print(dict)

#Cambiar de diccionacio a lista de tuplas
print(dict.items())
print(type(dict.items()))

#-------------------------------------------------------------------------
#1.1- OPERACIONES CON ELEMENTOS
#-------------------------------------------------------------------------
#Número de claves
print(len(dict)) 

#Acceso a los valores de la clave
print(dict["Nombre"])
print(dict["Dirección"]["Calle"]) #Diccionario dentro de diccionario

#Modificar valores
dict["Nombre"]="Pedro"
print(dict) 
print(dict["Nombre"]) 

#Añadir una clave
dict["Nueva clave"]="new item"
print(dict)

#Eliminar una clave
del dict["Ciudad"]
print(dict)

#Eliminar un valor
dict.pop("Edad")
print(dict) #Aunque no apareza, la clave sigue creada
dict["Edad"] = 22 #y puedo añadir elementos a ella sin necesidad de volver a crearla
print(dict)

#Eliminar el último valor
dict.popitem()
print(type(dict.popitem)) #<class 'builtin_function_or_method'>

#Buscar un elememto 
print("Nombre" in dict) #True (solo comprueba la clave)
print("Gabriela" in dict) #False (no los valores)

#-------------------------------------------------------------------------
#1.2- OPERACIONES CON DICCIONARIOS
#-------------------------------------------------------------------------
#Eliminar el diccionario
#a) Eliminar
#del dict

#b)Limpiar / Vaciar
#dict.clear()

#Copia
dict_copy = dict.copy

#Tomar las claves del diccionario
claves = dict.keys()
print(claves)
print(type(claves)) #<class 'dict_keys'>

#Tomar los valores 
valores=dict.values()
print(valores)
print(type(valores)) #<class 'dict_values'>

#Creación de un diccionario nuevo sin valores
new_dict=print(dict.fromkeys(("new key1", "new_key2"))) #dict palabra reservada (no hace ref al diccionario que estábamos usando)
print(new_dict)                                         #podemos hacerlo a partir de un diccionario que ya existe, pero el resultado será igual

