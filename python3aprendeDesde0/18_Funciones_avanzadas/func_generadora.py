# un ejemplo sería range
for n in range(0,11):
    print(n)

def pares(maximo):
    for numero in range(0,maximo):
        if numero % 2 == 0:
            yield numero


for numero in pares(13):
    print(numero)