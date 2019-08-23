# Vamos a grabar un fichero de texto 
# nombre del fichero, modo -> w de write y t de text
fichero = open("10_Ficheros_de_Texto/ficherotextoNuevo.txt","wt") # el método open devuelve un método al fichero
texto_fichero = "Esta es la línea que vamos a grabar en el fichero"
datos_fichero = fichero.write(texto_fichero)

fichero.close()