""" Variable scope 
(Alcance de la Variable) """

a = 10
def test_method(a): 
    print("El valor de la variable local a es: "+str(a))
    a = 2
    print("Nuevo valor de a es: "+str(a))

print("Valor de a es: "+str(a))
test_method(a) # ¿Se pasan por copia?