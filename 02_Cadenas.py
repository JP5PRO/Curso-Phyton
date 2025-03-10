"""
CADENAS/TEXTO
Las cadenas de caracteres (texto) las podemos convertir, buscar o arrojar 
resultados segun todos los comandos a continuacion mostrados:
'"Recordemos que las cadenas son VARCHAR"'
"""

texto = "Hola usuario"  #Una variable llamada texto que almacena una cadena
print("__________________________________________")

print(texto) #Muestra la cadena
print(texto.lower()) #Para mostrar la cadena en Minusculas
print(texto.upper()) #Para mostrar la cadena en Mayusculas
print(texto.title()) #Para mostrar la cadena en Forma titulo
print("__________________________________________")

print(texto.find("Hola")) #Pocision donde se encuentra la cadena a buscar
print(texto.count("o")) #Numero de veces en la que se encuentra nuestra busqueda la cadena
print(texto.count("3"))
print("__________________________________________")

textofinal = texto.replace("o", "0")
print(textofinal) #Remplazar una cadena .replace("dato, remplazo")

valor = texto.isnumeric() #Arroja un resultado dependiendo si es numerico no
print(valor)

cadenasep = texto.split(" ")
print(cadenasep) #Te separa la cadena como tupla
