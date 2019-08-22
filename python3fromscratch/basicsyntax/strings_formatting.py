""" Ejemplos para enseñar cómo funciona el formateo de strings en Python """

city = "Valencia"
event = "el concierto"

print("Bienvenido a " + city + " y disfruta "+event)  # poop
print("Bienvenido a %s y disfruta %s" %(city, event))  # cool
