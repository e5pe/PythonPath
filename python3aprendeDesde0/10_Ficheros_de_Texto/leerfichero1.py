# Vamos a leer el fichero de texto 
# nombre del fichero, modo -> r de read y t de text
fichero = open("10_Ficheros_de_Texto/ficherotexto.txt","rt") # el método open devuelve un método al fichero
datos_fichero = fichero.read()
print(datos_fichero)

fichero.close()