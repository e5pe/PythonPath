# Eliminar elementos en series y dataframes
import pandas as pd
import numpy as np

np.arange(3)
serie = pd.Series(np.arange(4), index = ['a','b','c','d'])

serie.drop('c') # nos elimina el elemento cuyo indice es c

lista_valores = np.arange(9).reshape(3,3)
print(lista_valores)

lista_indices = ['a','b','c']
lista_columnas = ['columna1','columna2','columna3']
dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns=lista_columnas)
print(dataframe)
print(dataframe.drop('b'))
print(dataframe.drop('columna2',axis=1))
print(dataframe)
# Le tenemos que pasar el eje en el que considera que está las columnas

# para guardar los datos tendríamos que hacerlo así:
print("Parte 2:")
print(dataframe)
dataframe = dataframe.drop('b')
print(dataframe)
dataframe = dataframe.drop('columna2',axis=1)
print(dataframe)