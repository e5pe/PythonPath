# Filter = Función para filtrar resultados según la condición
def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

# Con una función condicional, por ejemplo positivo podemos usar filter

numeros = [2,-5,6,-7,5,-6,8,9,-5,-3]

# Queremos obtener una lista de los valores positivos => Usamos un filtro

filtro = filter(positivo, numeros)
resultado = list(filtro)
print(resultado)