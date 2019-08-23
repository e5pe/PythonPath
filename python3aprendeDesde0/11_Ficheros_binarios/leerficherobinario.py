import pickle

fichero = open("11_Ficheros_binarios/ficherobinariocolores.pckl", "rb")
datos_fichero = pickle.load(fichero)
print(datos_fichero)
