# Indexación con arrays

import numpy as np
array = np.arange(0,11)
print(array)
print(array[0:3])
print(array[2:5])

array_copia = array.copy()
print(array_copia)
array_copia[0:3] = 20
print(array_copia)
print(array)

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2[1])