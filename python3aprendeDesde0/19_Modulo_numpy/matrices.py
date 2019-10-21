# Arrays o matrices traspuestas (c
import numpy as np

array = np.arange(0,15).reshape(3,5)
# la forma que le vamos a dar va a ser 3 filas y 5 columnas
print(array)
print(array[1][1])

array_tras = array.T
print(array_tras)