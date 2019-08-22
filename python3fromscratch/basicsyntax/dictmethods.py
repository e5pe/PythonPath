car = {"make": 'bmw', "model": "550i", "year": 2016}
cars = {
    "bmw": {"model": "550i", "year": 2016},
    "benz": {"model": "E350", "year": 2015}
}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())

print("----------------------------------------------\n")

print(car.items())
carCopy = car.copy()
print(carCopy)

print(car.pop("model"))
print(car)
car.clear() # vacía el diccionario
print(car)

