# Vamos a añadir una línea a un fichero de texto ya existente
# a de at es de append
fichero = open("10_Ficheros_de_Texto/ficherotexto.txt","at")
cadena_para_incluir = "\nTercera línea del fichero"
fichero.write(cadena_para_incluir)