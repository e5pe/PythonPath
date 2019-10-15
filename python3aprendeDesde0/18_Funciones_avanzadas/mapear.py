# Map - Sive para aplicar una función a cada uno de los elementos de una lista

def multiplicardos(numero):
    return numero * 2

numeros = [3,5,6,8]

mapeo = map(multiplicardos, numeros)
for i in mapeo:
    print(i)

print("\nEn la misma línea:")
lista_resultado = list(map(multiplicardos, numeros))
print(lista_resultado)

# con función lambda
print("\nCon función lambda:")
lista_resultado = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado)