l1 = [1,2,3]
l2 = [6,7,8,20,30,40]

""" zip creará un par de elementos pasandole n listas, como vemos en este ejemplo """

for a,b in zip(l1,l2):
    # en este caso sólo iterará como la lista más corta, en este caso l1
    """ print(a)
    print(b) """
    if(a > b):
        print(a)
    else:
        print(b)
