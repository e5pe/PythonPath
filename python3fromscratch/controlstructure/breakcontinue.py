""" 
break: Para salir del bucle?
continua: Para empezar la siguiente iteración del bucle
"""
x = 0
while x < 10:
    print("Value of x is "+str(x))
    x = x + 1

    if x == 8:
        break
    print("¡Este ejemplo es genial!")
    print("*"*20)
else: # Si está en un else y hay break entonces lo del else no se ejecuta
    print("Se salió del bucle")
# x = 0
# while x < 10:
#     print("Value of x is "+str(x))
#     x = x + 1

#     if x == 8:
#         continue
#     print("¡Este ejemplo es genial!")
#     print("*"*20)