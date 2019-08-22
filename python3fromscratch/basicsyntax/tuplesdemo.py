""" Tuplas (Tuple)
Son como las listas pero inmutables """

myList = [1,2,3]
print(myList)

myTuple = (1,2,3)
print(myTuple)
# myTuple[0]=0  Esto da error:
print(myTuple[0])
print(myTuple[1:])
print(myTuple.index(2)) # Nos devuelve el íncide de la primera ocurrencia del objeto en la tupla, igual que con la lista

myTuple2 = (1,2,2,2,2,2,3)
print(myTuple2.count(2))
print(myTuple2.count(1))
print(myTuple2.count(11))

""" File "basicsyntax/tuplesdemo.py", line 9, in <module>
    myTuple[0]=0
TypeError: 'tuple' object does not support item assignment """