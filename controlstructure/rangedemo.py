""" 
6_6
Built-in function
Crea una secuencia de números pero no los guarda en memoria
Muy útil para generar números 
El párametro final no se incluye en la "lista" que genera
"""

print(list(range(1,30)))

a = range(12,40,2)
print(list(a))

# lista = [1,2,3]
# for num in lista:
#     print(num)
for num in range(1,4): # Sirve para iterar x veces, por ejemplo.
    print(num)

