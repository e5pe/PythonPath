x = 10
""" Colección de piezas de información """
cars = ["bmw","honda","audi"]
emptyList = []
print (cars)
print (emptyList)

x = "cadena" # colection of characters
print(cars[0])

num_list = [1,2,3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

cars[1] = "seat"

print(cars)

""" built-in methods to help manipulating a list - 4_2"""
print("**************************\nbuilt-in methods to help manipulating a list:\n")
cars2 = ["bmw","honda","audi"]

length = len(cars2)
print(length)

cars2.append("Benz")

cars2.insert(1,"Jeep")
print(cars2)

x = cars2.index("honda")
print(x)

y = cars2.pop() # quita el último ítem de la lista
print(y) # Nos devuelve el valor que acabamos de sacar de la lista
print(cars2)

cars2.remove("Jeep") # no nos da el ítme eliminado
print(cars2)

slicing = cars2[0:2]
print(slicing)

otroSlice = cars2[1:]
print(otroSlice)
cars2.sort() # ordena los ítems de la lista
print(cars2)