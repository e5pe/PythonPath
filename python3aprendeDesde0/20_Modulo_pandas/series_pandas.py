# Series

import pandas as pd

serie1 = pd.Series([3,5,7])
print(serie1)
print(serie1[1])

asignaturas = ['matematicas','historia','fisica','literatura']
notas = [8,6,9,7]

serie_notas_daniel = pd.Series(notas, index=asignaturas)
print(serie_notas_daniel)

print(serie_notas_daniel[serie_notas_daniel >= 8])

serie_notas_daniel.name = "Notas de Daniel"
serie_notas_daniel.index.name = "Asignaturas de Daniel"

print(serie_notas_daniel)

diccionario = serie_notas_daniel.to_dict()
print(diccionario)
serie_back = pd.Series(diccionario)