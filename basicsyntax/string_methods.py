""" Ejemplos para ver métodos sobre strings disponibles en Python """

# Accediendo a caracteres en un string
cadena ="alc" 
first = cadena[0]
print(first)
cadena2 = "ESto es una Cadena LALALA"
print(cadena2)
print(cadena2.upper())
print(cadena2.lower())
print(len(cadena2))
print(cadena2 + str(51)) # str convierte un argumento a cadena

# replace
a = "123aaaabc34abc343abcdefghijkabc"
print(a)
print(a.replace('abc', 'ABC')) # el replace devuelve un string nuevo
print(a)

# Substring
# el índice inicial es inclusivo
# el índice final es exclusivo
substring = a[1:6]
print(substring)
step = a[1:6:1]
print(step)
step2 = a[1:6:2]
print(step2)