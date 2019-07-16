""" Implement the function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value 
next to each other and preserving the original order of elements """
def unique_in_order(iterable):
    lista = []
    for i, ch in enumerate(iterable):
        if i == 0 or ch != iterable[i-1]:
            lista.append(ch)
    return lista
# lista = []
# if len(iterable) > 0: # Si tiene algo insertamos el primer caracter
#     lista.append(iterable[0])
# for itemP, item in zip(iterable, iterable[1:]):
#     # Comprobamos si el item no es el anterior
#     if itemP != item: # si el item cambia lo insertamos en la lista
#         lista.append(item)
# return lista


real = unique_in_order('AAAABBBCCDAABBB')

print(real)
print(['A', 'B', 'C', 'D', 'A', 'B'] == real)
