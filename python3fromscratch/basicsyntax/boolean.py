""" Ejemplos para enseñar cómo funcionan los boleanos en Python """
a = True
b = False

print(a,b)

# Anything not empty or not none is True
print(bool(0))

c = ""
print('Cadena vacía es',bool(c))
c = "Cadena"
print(c,"es", bool(c))