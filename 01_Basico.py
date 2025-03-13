"""
Empezamos el curso, explicando lo más básico y fácil en Python. Para iniciar debemos saber que si queremos mostrar 
un mensaje por consola, con un simple "print("")" se puede lograr como en el primer ejemplo. Y otra cosa muy importante es 
que según Python no importa la especificación del dato (int, varchar, double, etc), tu puedes definir un dato con el valor 
que quieras y Python analizará el tipo de dato que ha escrito. En el segundo ejemplo se muestra como realizo 4 operaciones 
distintas con un dato int y otro float y muestro los mensajes por consola dando su resultado, para esto en código debes 
escribir print("tu_mensaje", tu_variable ,) aunque esto se puede hacer de distintas maneras esta es la más básica.
"""
#________________________________________________________________________
print("Hola mundo")

varchar = "Hola"

print(varchar, "Usuario")
#________________________________________________________________________
int = 20
float = 10.33

suma = int + float
resta = int - float
multi = int * float
div = int / float

print("\nLa suma de ", int, " + " , float, " es igual a: ", suma)
print("La resta de ", int, " - " , float, " es igual a: ", resta)
print("La multiplicacion de ", int, " x " , float, " es igual a: ", multi)
print("La division de ", int, " / " , float, " es igual a: ", div)

#Para poder preguntar datos se utiliza input de esta forma:
saludo = input("¿Como estas? ")
