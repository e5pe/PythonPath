# Seleccionar datos en las series
import pandas as pd
import numpy as np

lista_valores = np.arange(3)
print(lista_valores)

indices = ['i1','i2','i3']
serie = pd.Series(lista_valores,index = indices)
print(serie)
serie = serie * 2
print(serie)

print(serie['i2'])
print(serie[1]) # Es lo mismo que lo anterior
print(serie[2])

print(serie['i1':'i2'])
print(serie[serie > 3]) # Nos devuelve sólo los que cumplen la condición

serie[serie > 3] = 6
print(serie)