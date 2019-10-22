# Funciones en arrays

import numpy as np
array = np.arange(5)

# Nos devuelve la raíz cuadrada de cada uno de los elementos
print(np.sqrt(array))

# Para crear arrays de forma aleatoria
array2 = np.random.rand(5)
print(array2)

lista = [5,6,7,8,9]
array3 = np.array(lista)
print(array)
print(array3)

suma = np.add(array, array3)
print(suma)

# máximo de los dos arrays
maximo = np.maximum(array,array3)
print(maximo)