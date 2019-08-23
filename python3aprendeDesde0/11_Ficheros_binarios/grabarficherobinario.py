import pickle
# Pickle (módulo para grabar ficheros binarios)

lista_colores = ["verde","rojo","amarillo"]
fichero = open("11_Ficheros_binarios/ficherobinariocolores.pckl","wb") # la b es de binario
pickle.dump(lista_colores, fichero)
fichero.close()
