# Expresiones regulares (search, findall, split, sub)
texto = "Hola, mi nombre es Antonio"
import re
match = re.search("nombre", texto) # Si lo encuentra devuelve un objeto de tipo Match
print(match)
match2 = re.search("Hola", texto)
print(match2)

if(match):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")

texto = """
El coche de Luis es gris,
el coche de Antonio es rojo,
y el coche de María es rojo
"""

encontrados = re.findall("coche.*rojo",texto)
print(encontrados)

# El split divide una cadena a partir de un patrón
texto = "La silla es blanca y vale 80"
salida = re.split("\s",texto)
print(salida)

texto = "La silla es blanca y vale 80"
resultado = re.sub("blanca","roja",texto)
print(resultado)