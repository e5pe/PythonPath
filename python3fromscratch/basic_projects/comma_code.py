spam = ['apples', 'bananas', 'tofu', 'cats']

""" Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it. """


def separateList(lista):
    # Devuelve un string con todos los items separados por comas
    dev = ''
    for index in range(len(lista)):
        if index == len(lista) - 1:
            # si es el último añadimos un and
            dev += 'and ' + lista[index]
        else:
            dev += lista[index]+', '
    return dev


listaNueva = separateList(spam)
print(listaNueva)
