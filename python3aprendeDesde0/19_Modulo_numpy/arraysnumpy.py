import numpy as np

print(np.zeros(4))

print(np.ones(5))
print(np.arange(5)) # Tiene 5 elementos del 0 al 4

print(np.arange(2,20,3)) # Inicio, fin y el step

lista1 = [1,2,3,4]
array1 = np.array(lista1) # Nos permite convertir una lista en un array
print(array1)
print(lista1)

# Lista doble
lista1 = [2,3,4,5]
lista2 = [5,6,7,8]

lista_doble = (lista1,lista2)
print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble) # ¿Igual se refiere a matrices?