"""Condicionales: Son instrucciones importantes que le permiten al codigo como va actuar dependiendo
de la respuesta por el usuario y si se cumplen condiciones, estas se cumplen mediante la comparacion de datos.
"""

#IF, ELIF, ELSE...
num = int(input("Elige un numero entre el 1 y 3: "))  #Pide una respuesta al usuario
if num==1:   #Si el numero es 1, 2 o 3 se muestra un mensaje
    print("Perdiste :(")
elif num==2:
    print("¡Ganaste! :)")
elif num==3:
    print("Perdiste :(")
else:  #Si elijes un numero fuera del rango, te dara "ERROR"
    print("ERROR Solo se permiten numeros del 1 al 3")
    
"""
En estos casos utilize solo un operador pero tambien puedes hacer comparaciones de esta manera:
== igual
!= diferente
> mayor
< menor
>= mayor o igual
<= menor o igual

Todos estos operadores por lo general se manifiestan igual en cualquier lenguaje...
""" 
#\n sirve como para hacer un salto de linea
print("\n")

#Tambien puedes hacer condiciones dentro de condiciones como en este ejemplo muy basico:

saldo = 10000 

op = int(input("¿Que deseas realizar? \n1)Retirar dinero \n2)Depositar dinero \n3)Consultar saldo \n4)Salir \n- "))  #Menu de opciones elige un numero
if op==1:
    cant = int(input("Cantidad a retirar: ")) #Se analiza cuanto se retira y hace una serie de filtros para saber si la cantidad a retirar es valida
    saldo = saldo - cant
    if saldo<0:
        print("ERROR 'CANTIDAD MUY GRANDE'") #Si el saldo se queda en menos de 0 te mostrara error
    if cant<0:
        print("ERROR 'CANTIDAD INEXISTENTE'") #Si la cantidad es menor a 0 te mostrara error
    else:
        print(f"Tu saldo actual: {saldo}") #Al final si todo esta bien te muestra tu saldo
elif op==2:
    cant = int(input("Cantidad a depositar: ")) #Se analiza cuanto se depositara y hara una serie de filtros
    saldo = saldo + cant
    if cant<0:
        print("ERROR 'CANTIDAD INEXISTENTE'") #Si la cantidad a depositar es menor a cero
    else:
        print(f"Tu saldo actual: {saldo}") #Tu saldo actual
elif op==3:
    print(f"\nTu saldo actual: {saldo}")
elif op==4:
    print("Saliendo")
else:
    print("ERROR 'NUMERO INEXISTENTE'") #Si le diste un numero fuera de los rangos indicados (1-4) te mostrara este mensaje
    
#Este mismo ejercicio lo mejorare cuando veamos bucles