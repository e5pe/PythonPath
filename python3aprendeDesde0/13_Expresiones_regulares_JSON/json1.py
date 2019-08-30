# Convertir datos de un diccionario en Python a una estructura JSON
# utilizamos una librería que se llama JSON 
import json
producto1 = {"nombre": "silla", "color": "blanco", "precio": 80}


producto1json = json.dumps(producto1) # nos devuelve una estructura JSON
print(producto1json)

print(producto1["nombre"])
# print(producto1json["nombre"]) # esto peta porque ya no es un diccionario
print(producto1json[0])

# Ahora vamos a convertir una estructura en un diccionario en python
producto1convertido = json.loads(producto1json)
print(producto1convertido) # imprime un diccionario por pantalla