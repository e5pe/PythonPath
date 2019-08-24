# try... except... else... finally
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except Exception as e:
    print("Ha habido un error")
# para controlar el error usaremos el bloque try

try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except Exception as e:
    print("Ha habido un error")

print("Ejemplo con else:")
try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except Exception as e:
    print("Ha habido un error")
else:
    print("La divisón funcionó correctamente")
finally:
    print("Esta prueba del try se ha acabado")