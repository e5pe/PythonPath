# Entrada y salida con arrays

import numpy as np

array1 = np.arange(6)
print(array1)

np.save('array1s', array1)
array2 = np.load('array1s.npy')
print(array2)
array2 = np.arange(8)
print(array2)

# Salvar dos arrays a la vez
np.savez('arrays',x=array1,y=array2)

# Para recuperarlos
array_recuperado = np.load('arrays.npz')
array1_recuperado = array_recuperado['x']
array2_recuperado = array_recuperado['y']
print(array_recuperado)
print(array1_recuperado)
print(array2_recuperado)

# También se pueden salvar en un fichero de texto
np.savetxt('mificheroarray.txt',array2,delimiter=',') # delimiter indicia por qué están separados los números