#!/usr/bin/env python
# coding: utf-8

# In[1]:


variable = "Hola mundo"


# In[2]:


variable


# In[3]:


variable = "adios"


# In[4]:


print(variable)


# # Números

# In[5]:


numero = 5


# In[6]:


numero


# In[7]:


numero


# In[8]:


decimal = 4.5


# In[9]:


type(decimal)


# In[10]:


type(numero)


# ## Operaciones

# In[11]:


numero2 = 2
suma = numero + numero2


# In[12]:


suma


# In[13]:


type(suma)


# In[14]:


suma = decimal + numero
print(suma)


# In[15]:


type(suma)


# ## Conversiones de tipos de datos

# In[16]:


numero = 3


# In[17]:


cadena = str(numero)


# In[18]:


cadena


# In[19]:


type (cadena)


# # Cadenas

# In[20]:


cadena = "Hola mundo"
cadena


# In[21]:


cadena[5]


# In[22]:


cadena[-1]


# In[23]:


cadena[2:6]


# Posición inicial hasta posición final menos uno, es decir, la última no está incluida.

# ## Funciones de las cadenas

# In[24]:


cadena = "Hola mundo"


# In[25]:


len(cadena)


# In[26]:


cadena.upper()


# In[27]:


cadena = cadena.upper()


# In[28]:


cadena


# In[29]:


cadena2 = "uva,pera,manzana,naranja"
cadena2.split()


# In[30]:


cadena2.split(",")


# ## Imprimir variables en una cadena

# In[31]:


nombre = "Antonio"
print("Buenos días "+nombre)


# In[32]:


# .format
nombre = "Antonio"
edad = 30
print("Buenos días {}, feliz {} cumpleaños".format(nombre,edad))


# In[33]:


resultado = 10 / 3
print("El resultado es {r}".format(r=resultado))


# In[34]:


# f-strings
nombre = "Antonio"
edad = 35
print(f"Buenos días {nombre}, feliz {edad} cumpleaños")


# # Entrada por teclado
# `input()`

# In[35]:


print("Introduce un nombre")
entrada = input()
print("Hola {}".format(entrada))


# # Operadores aritméticos (12)

# In[2]:


numero1 = 10
numero2 = 2
mult = numero1 * numero2
mult


# ## Operadores de asignación
# `(=, +=, -=, *=, /=, **=)`

# In[3]:


numero = 5


# In[4]:


print(numero)


# In[5]:


numero = numero + 4


# In[6]:


print(numero)


# In[7]:


numero = 5
numero


# In[8]:


numero += 4 # numero = numero + 4


# In[9]:


print(numero)


# In[10]:


numero -= 3 # numero = numero - 3
numero


# In[11]:


# exponente
numero = 2
numero = numero ** 3
numero


# In[12]:


numero = 2
numero **= 3 # numero = numero ** 3
numero


# In[13]:


# :)


# ## Operadores de comparación (14)

# Sirven para comparar valores (==, !=, &lt;, &gt;, &lt;=, &gt;=)

# In[1]:


cadena1 = "hola"
cadena2 = "hola"
cadena1 == cadena2


# In[3]:


cadena1 = "hola"
if cadena1 == 'hola':
    print("Dijo hola")


# In[4]:


# distinto de !=
numero1 = 3
numero2 = 5
numero1 != numero2


# In[5]:


numero1 = 3
numero2 = 5
numero1 > numero2


# ## Operadores lógicos (15)

# In[6]:


numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8


# In[7]:


numero1 > numero2


# In[8]:


numero3 < numero4


# In[9]:


(numero1 > numero2) and (numero3 < numero4)


# In[10]:


(numero1 > numero2) and (numero4 < numero3)


# In[11]:


# operador not
not(numero3 > numero4)


# ## Operadores de identidad (is, is not)

# In[14]:


frutas = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas


# In[15]:


frutas3 is frutas


# In[16]:


frutas3.append("naranja")


# In[17]:


frutas3 is frutas


# In[18]:


frutas


# In[19]:


# oh baia


# ## Operadores de pertenencia (in, not in)

# In[20]:


frutas1 = ["manzana", "pera","naranja"]
frutas2 = "pera"
frutas2 in frutas1


# In[21]:


frutas2 not in frutas1


# In[24]:


frutas3 = "melocoton"
frutas3 in frutas1


# In[25]:


frutas3 not in frutas1


# # Listas (18)

# In[26]:


colores = ["rojo", "amarillo", "verde"]


# In[27]:


colores


# In[28]:


colores[0]


# In[29]:


colores[1]


# In[30]:


colores[1] = "azul"


# In[31]:


colores[1]


# In[32]:


colores


# In[33]:


colores.remove("rojo")
colores


# In[34]:


for color in colores:
    print(color)


# In[35]:


colores.append("una patata se ha colao'")


# In[36]:


colores


# ## Tuplas
# Una tupla es una colecci'on de elementos ordenada que no se puede modificar, es inalterable

# In[37]:


# van entre paréntesis
tupla_colores = ("rojo","verde","amarillo")
for color in tupla_colores:
    print(color)

    


# In[39]:


tupla_colores[2]


# In[40]:


len(tupla_colores)


# ## Conjuntos

# In[41]:


conjunto_colores = {"rojo","verde", "azul"}


# In[42]:


conjunto_colores


# In[43]:


for color in conjunto_colores:
    print(color)


# In[44]:


conjunto_colores[0]


# In[45]:


len(conjunto_colores)


# In[46]:


conjunto_colores.add("negro")


# In[47]:


conjunto_colores


# In[48]:


# mete el negro por en medio porque es un conjunto DESORDENADO


# ## Diccionarios (21)

# Un diccionario es una colección de elementos que están indexados, no están ordenados y se pueden modificar.
# Son escritos entre llaves y están formados por pares de elmentos, clave valor.

# In[1]:


diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo"}
diccionario_colores


# In[2]:


diccionario_colores["red"]


# In[3]:


valor = diccionario_colores["yellow"]


# In[4]:


valor


# In[6]:


# podemos añadir elementos a un diccionario
diccionario_colores["black"] = "negro"


# In[7]:


diccionario_colores


# In[8]:


# podemos borrar colores
diccionario_colores.pop("yellow")


# In[9]:


# nos devuelve el valor que ha quitado
diccionario_colores


# In[10]:


# también se puede hacer con del y pasandole la clave del elemento a borrar
del(diccionario_colores["black"])


# In[11]:


diccionario_colores


# In[12]:


print(diccionario_colores)


# In[13]:


for color in diccionario_colores:
    print(color)


# In[14]:


# si queremos mostrar o visualizar ambas cosas: la clave y el valor
for clave, valor in diccionario_colores.items():
    print(clave, valor)


# # Bucles y condiciones
# ## Condiciones if... else

# In[15]:


a = 8
b = 4
a > b


# In[16]:


a < b # da False


# In[17]:


if a > b:
    print("a es mayor que b")
elif a < b:
    print("b es mayor que a")
else:
    print("a y b son iguales")


# In[18]:


a = 8
b = 4
c = 2
d = 6
if (a > c) and (b < d):
    print("La primera expresión es correcta")


# In[19]:


if (a > c) and (b > d):
    print("La primera expresión es correcta")
else:
    print("La primera expresión no es correcta")


# In[20]:


a = 8
b = 4
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")


# In[21]:


a = 8
b = 8
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")


# In[22]:


a = 5
b = 8
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")


# ## Bucle for (23)
# Bucle for es utilizado para iterar sobre una secuencia de elementos, como una lista, un diccionario, etc

# In[23]:


colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)


# In[24]:


# también podemos iterar sobre una cadena
cadena = "Hola mundo"
for c in cadena:
    print(c)


# In[25]:


range(8) # el último no está incluido


# In[26]:


for numero in range(8): # si no ponemos nada el primero es 0
    print(numero)


# In[27]:


for numero in range(3,8):
    print(numero)


# In[28]:


for numero in range(3,12,2): # el último número indica el step o el paso
    print(numero)


# In[29]:


# break - para parar el bucle
for numero in range(10):
    if numero == 5:
        break
    print(numero)


# In[30]:


# continue - para parar sólo la iteración actual
for numero in range(10):
    if numero == 5:
        continue
    print(numero)


# In[31]:


# for doble
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1,numero2)


# ## Bucle while (24)
# Podemos ejecutar un conjunto de acciones mientras sea cierta la condición

# In[32]:


valor = 1
fin = 10
while valor < fin:
    print(valor)
    valor +=1


# In[33]:


valor = 1
fin = 10
while valor < fin:
    print(valor)
    valor +=1
    if valor == 5:
        break


# # Clases y objetos (25)

# In[1]:


# Programación orientada a objetos. POO
class ClaseSilla:
    color = "blanco"
    precio = 100


# In[2]:


silla1 = ClaseSilla()


# In[3]:


silla1


# In[5]:


silla1.color


# In[6]:


silla1.precio


# In[7]:


silla2 = ClaseSilla()
silla2.color = "verde"
silla2.precio = 120


# In[8]:


silla2.precio


# In[9]:


silla2.color


# In[19]:


# Clase persona
class Persona:
    # método init para cada persona. Un constructor con parámetros.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Este método muestra por pantalla un saludo
    def saludar(self):
        print("Hola, me llamo {} y tengo {} años".format(self.nombre,self.edad))       


# In[20]:


persona1 = Persona("Juan",64)


# In[21]:


persona1.edad


# ## Funciones (26)

# In[22]:


def saludar():
    print("Buenos días")


# In[23]:


saludar()


# In[24]:


def saludar(nombre):
    print("Buenos días "+nombre)


# In[25]:


nombre = "Antonio"
saludar(nombre)


# In[26]:


def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma


# In[27]:


sumar(6,8)


# In[31]:


# paso de valores por referencia
colores = ["rojo","verde","azul"]

def incluir_color(colores,color): # al pasarla por referencia puede modificar la lista
    colores.append(color)


# In[32]:


color = "negro"
incluir_color(colores,color)


# In[33]:


colores


# ### Funciones lambda
# Función pequeña y anónima.

# In[34]:


resultado = lambda numero : numero + 30


# In[35]:


resultado(10)


# In[36]:


resultado2 = lambda numero1, numero2 : numero1 + numero2


# In[37]:


resultado2(13, 20)


# # Módulos (28)

# In[ ]:




