# Índices

import pandas as pd
lista_valores = [1,2,3]
lista_indices = ['a','b','c']

serie = pd.Series(lista_valores, lista_indices)

print(serie)
print(serie.index)
print(serie.index[0])
# serie.index[0] = 3 # Los nombres de los indices no se pueden cambiar.

# Recuperar los indices de un dataframe

lista_valores = [[6,7,8],[4,7,9],[5,8,7]]
lista_indices = ['matematicas','historia','fisica']

lista_nombres = ['Antonio','Maria','Pedro']

dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_nombres)
print(dataframe)