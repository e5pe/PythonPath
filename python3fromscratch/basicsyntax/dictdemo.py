""" Dictionary items are in brackets {} (llaves) in key:value pairs, separated with "," {'k1':'v1','k2':'v2'} 
Como un hashmap en Java, por ejemplo.
Es mejor, porque puedes mezclar tipos de valores, como se puede ver abajo.
No tiene un orden particular
"""

car = {"make": 'bmw', "model": "550i", "year": 2016}
print(car)
print(car['model'])

d = {}
d["one"] = 1
print(d)
d["two"] = 2
print(d)

suma = d['two'] + 8
print(suma)

d["two"] = d['two'] + 8
print(d)