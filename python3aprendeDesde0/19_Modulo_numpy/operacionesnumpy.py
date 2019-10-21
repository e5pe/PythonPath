# Operaciones con arrays (+,-,*,/,**)
import numpy as np
array1 = np.array([1,2,3,4])

array2 = array1 + 4
print(array2) # Podemos realizar operaciones (aritméticas) con los items de un array

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)

print(array_doble)
print(array_doble.dtype)

print(array_doble + 6)
print(array_doble ** 2)