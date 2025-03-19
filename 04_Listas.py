'''
Listas: Son estructuras de datos que nos permiten almacenar distintos valores
son de esta forma equivalentes a los arrays en otros lenguajes como Java
Son estructuras dinamicas, pueden Mutar(editar).
'''
lista = ["Usuario", 30, 75.2, True]  #Crea lista con un dato String, con un dato Int, un dato Float y un dato Boolean
print(lista) 
print(lista[:]) #
print(lista[2]) #Te muestra el 2do valor 0=usuario, 1=30, 2=75.2
print(lista[-1]) #Te muestra el ultimo valor

print(lista[1:3]) #Muestra la lista desde dos puntos_asignados
print(lista[:2]) #Muestra la lista hasta el valor_asignado
print(lista[3:]) #Muestra la lista desde el valor_asignado

lista.append("You Tube") #Agrega valores a la lista
print(lista)

lista.insert(5, "Mexico") #Tambien agrega valores a la lista pero indicando la pocision
print(lista)

lista.extend(["Ags", "Aguascalientes", 7624, True]) #De igual forma agrega valores pero mediante otra lista (se extiende)
print(lista)

print(lista.index("Ags")) #Busca un valor en la lista y te devuelve la pocision en la que se ubica
lista.remove(7624) #Elimina valores en una lista dando el valor indicado
print(lista)

lista.pop(7) #Elimina valores en una lista dando la pocision indicada
print(lista)
print(lista * 4) #Puedes imprimir la lista muchas veces (en este caso 4)

print("User" in lista) #Otra forma de buscar valores pero te devuelve un resultado booleano (True / False)

""" /Ejemplo\ """
listaUsers = []
nombre = input("¿Cual es tu nombre? ")
listaUsers.append(nombre)

edad = int(input("¿Cual es tu edad? "))
listaUsers.append(edad)

correo = input("¿Cual es tu correo? ")
listaUsers.append(correo)


guardar = int(input("¿Deseas guardar? 1)True o 2)False: "))

if guardar == 1:
    print(f"Tus datos guardados: {listaUsers}")
    
    op = int(input("¿Que deceas hacer? 1)Buscar_Datos o 2)Salir \n-"))
    if op == 1:
        dato = input("Dato a buscar: ")
        busqueda_ = (dato in listaUsers)
        if busqueda_ == True:
            print("¡Dato encontrado con exito!")
        else:
            print("Dato no encontrado")
            
    elif op == 2:
        print("Gracias por usar el servicio") 
           
elif guardar == 2:
    listaUsers.remove(nombre)
    listaUsers.remove(edad)
    listaUsers.remove(correo)
    print("Lista borrada, saliendo...")

else:
    print("ERROR 'NO EXISTE TU VALOR'")
    
"""Por el momento el ejemplo es muy simple nada utiliable pero mientras avancemos en el curso este ejemplo y el anterior 
del 03_condicionales los estare intentando mejorar...
"""