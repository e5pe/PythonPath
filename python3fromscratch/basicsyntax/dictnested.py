""" Nested Dictionary:
d = {"k1": {'nestk1':'nestvalue1', 'nestk2':'nestvalue2'}} 
d["k1"]["nestk1"] # Nos dará nestvalue1 """

cars = {
    "bmw": {"model": "550i", "year": 2016},
    "benz": {"model": "E350", "year": 2015}
}

print(cars)

print(cars["bmw"]["year"])