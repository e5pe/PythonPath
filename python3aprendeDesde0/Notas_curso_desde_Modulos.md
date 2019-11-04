# [Python 3. Curso completo de Python 3. Aprende desde cero](https://www.udemy.com/course/curso-python/)

> Nota: Antes de hacer nada ejecutar esto:

`source ../environments/test_env/bin/activate`

## Módulos

Un módulo es un fichero que contiene un conjunto de funciones que puedes incluir y usar en tu aplicación.

Se puede importar sólo una parte de un módulo (fichero) de la siguiente forma:

`from modulo1 import despedirse`

También se puede hacer lo siguiente:

`from modulo1 import despedirse as adios` Lo que va después del *as* es un alias

### Instalar un módulo nuevo: *pip*

*Pip* es un gestor de paquetes y módulos python.

Un **módulo** es una librería de código Python que puedes incluir en tu proyecto.

Si el módulo que queremos usar no está instalado nos dará un error como el siguiente:

```python
python pip2.py Traceback (most recent call last):
  File "pip2.py", line 5, in <module>
    import camelcase
ModuleNotFoundError: No module named 'camelcase'
```

Entonces debemos instalarlo desde la terminal así:

```bash
pip install camelcase
Collecting camelcase
  Downloading https://files.pythonhosted.org/packages/24/54/6bc20bf371c1c78193e2e4179097a7b779e56f420d0da41222a3b7d87890/camelcase-0.2.tar.gz
Building wheels for collected packages: camelcase
  Running setup.py bdist_wheel for camelcase ... done
  Stored in directory: /home/espe/.cache/pip/wheels/b1/fe/08/84d2143069bc44c20127c38cc1bf202332319b3da7315ca766
Successfully built camelcase
Installing collected packages: camelcase
Successfully installed camelcase-0.2
```

## Ficheros

Un *fichero* es una secuencia de bits que se almacena con un nombre en algún dispositivo físico.

## Expresiones regulares, JSON, fecha y hora

### Expresiones regulares

Hay que usar el módulo *re*.

`^` y la palabra va a buscar si hay alguna línea dentro de la cadena que empiece por esa palabra.
`.` para decir cualquier caracter y `*` para decir que puede aparecer 0 o más veces

El *findall* permite buscar todas las ocurrencias de un patrón en una cadena.
Ejemplo:

```python
texto = """
El coche de Luis es gris,
el coche de Antonio es rojo,
y el coche de María es rojo
"""

encontrados = re.findall("coche.*rojo",texto)
print(encontrados)
```

La salida:

```bash
['coche de Antonio es rojo', 'coche de María es rojo']
```

El *split* divide una cadena a partir de un patrón.
El `\s` va a dividir el texto en las palabras que lo forman poniéndole como patrón el espacio en blanco.

*sub* permite cambiar una palabra de una cadena por otra.
Ejemplo:

```python
texto = "La silla es blanca y vale 80"
resultado = re.sub("blanca","roja",texto)
print(resultado)
```

parámetros del método *sub*:

- el primero es la palabra que queremos cambiar
- el segundo es la palabra por la que queremos cambiar la anterior
- el último es el texto al que aplicar el método

### JSON

Es una forma de almacenar e intercambiar datos que están en formato texto. Es muy utilizado por las empresas para intercambiar datos entre ellas.

## Bases de datos

SQLite es un sistema de gestión de bases de datos relacionales.

### Tablas

Crear una tabla. Con el cursor de la base de datos, mediante el comando execute ejecuta la sentencia SQL:

```python
# SQLite3 - Crear una tabla en nuestra base de datos

import sqlite3

connection = sqlite3.connect("basededatos1.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

# con el cursor de la base de datos, mediante el comando execute ejecuta la sentencia SQL

connection.commit() # le dice a la base de datos que queremos mantener la sentencia para siempre

connection.close() # por último cerramos la conexión a la base de datos

```

## Módulo tkinter

> Sección 15

Sirve para crear interfaces gráficas, que son medios visuales que permiten a los usuarios interacturar con nuestro programa de forma gráfica.

### Componente raíz tk

Se crea de la siguiente forma:

```python
# tkinter - Componente raíz (tk)

import tkinter

raiz = tkinter.Tk() # devuelve el elemento raíz
raiz.title("Mi programa")

raiz.mainloop() # Para que esté todo el rato ejecutandose
```

### Frame

El componente frame nos permite crear otros componentes dentro de él.

### Label

Componente label o etiqueta, en español.
Con el config le indicamos el color, el color de fondo y la fuente:

```python
etiqueta.config(fg="green", bg="lightgrey",font=("Cortana",30))
```

### Entry

Campo de texto corto para la entrada de datos por teclado

### Text

Campo de texto largo, de varias líneas, para introducir texto por teclado.

### Button

Un botón.
Al crearlo lee pasamos la raiz, el texto que mostrará el botón y por último el comando que tiene que ejecutar, en nuestro caso será una función llamada accion.
Como se puede ver a continuación:

```python
def accion():
    print("Hola mundo")

# Creamos nuestro componente Button

boton = tkinter.Button(raiz, text="Ejecutar",command=accion) 
```

## Documentación automática

### pydoc

Sirve para generar documentación desde la terminal.
Ponemos:

```bash
pydoc <ruta fichero/nombre del fichero>
```

Ejemplo:

`pydoc len` nos devuelve lo siguiente:

```python
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
(END)
```

Ejemplo de una clase que hemos creado:

`pydoc3.6 /home/espe/Proyectos/CursosPython/python3aprendeDesde0/16_Documentacion_auto/saludos.py` nos devuelve:

```python
Help on module saludos:

NAME
    saludos - # pydoc - Generar documentación automática desde la consola o Terminal de comandos

CLASSES
    builtins.object
        Saludos
    
    class Saludos(builtins.object)
     |  Esta clase tendrá dos funciones
     |  Ambas funciones recibirán como parámetro un nombre
     |  
     |  Methods defined here:
     |  
     |  adios(self, nombre)
     |      Esta función sirve para decir adiós
     |  
     |  buenosdias(self, nombre)
     |      Esta función sirve para decir buenos días
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    saludo = <saludos.Saludos object>

FILE
    /home/espe/Proyectos/CursosPython/python3aprendeDesde0/16_Documentacion_auto/saludos.py
```

También podemos hacer que genere un fichero html con la documentación generada. Como a continuación:

`pydoc3.6 -w /home/espe/Proyectos/CursosPython/python3aprendeDesde0/16_Documentacion_auto/saludos.py`. Simplemente tenemos que poner pydoc **-w**

## Pruebas automáticas

### Doctest

Dentro de las comillas dobles ponemos nuestras pruebas.
Por ejemplo:

```python
    """
    >>> sumar(4,3)
    7
    """
```

Y al final del documento ponemos lo siguiente:

```python
import doctest
doctest.testmod()
```

En el caso de nuestro documento para pasar los tests de doctest tenemos que poner **-v** al final:

`python python3aprendeDesde0/17_Pruebas_automaticas/sumar.py -v`

output:

```bash
6
Trying:
    sumar(4,3)
Expecting:
    7
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.sumar
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

### Unittest

Sirve para crear pruebas dentrod el propio código.
Se parece un poco a las clases de test de java con junit:

```python
# Unittest - Sirve para crear pruebas dentrod el propio código
def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)

import unittest
class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(4,2), 8)

if __name__ == "__main__":
    unittest.main()
```

Resultado de la ejecución:

```bash
8
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Funciones avanzadas

### Funciones generadoras

Un ejemplo sería **range**. Ejemplo:

`range(0,11)`

Genera números del 0 al 10, el último no está incluido.
Un ejemplo de función generadora:

```python
def pares(maximo):
    for numero in range(0,maximo)
        if numero % 2 == 0:
            yield numero
```

Como es una función generadora ponemos *yield* al final en vez de return.

### Filter

Filter = Función para filtrar resultados según la condición.

```python
def positivo(numero):
    if numero > 0:
        return True
    else:
        return False
```

Con una función condicional, por ejemplo *positivo* podemos usar filter.

### Map

Map sive para aplicar una función a cada uno de los elementos de una lista.

Distintos ejemplos:

```python
# Map - Sive para aplicar una función a cada uno de los elementos de una lista

def multiplicardos(numero):
    return numero * 2

numeros = [3,5,6,8]

mapeo = map(multiplicardos, numeros)
for i in mapeo:
    print(i)

print("\nEn la misma línea:")
lista_resultado = list(map(multiplicardos, numeros))
print(lista_resultado)

# con función lambda
print("\nCon función lambda:")
lista_resultado = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado)
```

## Módulo *numpy*
Debemos importar el módulo para utilizarlo:

`import numpy as np`

El as sirve para crear un alias.

### Creando arrays

```python
print(np.zeros(4))

print(np.ones(5))
print(np.arange(5)) # Tiene 5 elementos del 0 al 4

print(np.arange(2,20,3)) # Inicio, fin y el step

lista1 = [1,2,3,4]
array1 = np.array(lista1) # Nos permite convertir una lista en un array
```

#### Operaciones

**Podemos** realizar operaciones (aritméticas) con los items de un array

```python
array2 = array1 + 4
print(array2)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)

print(array_doble + 6)
print(array_doble ** 2)
```

#### Indexación

```python
array = np.arange(0,11)
print(array)
print(array[0:3])
print(array[2:5])

array_copia = array.copy()
print(array_copia)
array_copia[0:3] = 20
print(array_copia)
print(array)

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2[1])
```

### Matrices traspuestas

Cambiar ordenadamente las filas por las columnas)

`array = np.arange(0,15).reshape(3,5)`
Con *reshape* indicamos la forma que le vamos a dar, que va a ser 3 filas y 5 columnas.

`array_tras = array.T`
Así conseguimos la matriz traspuesta a otra.

### Entrada y salida con arrays

Guardar un array:

`np.save('array1s', array1)`

Cargar un array:

`array2 = np.load('array1s.npy')`

Salvar dos arrays a la vez se hace de la siguiente forma:

`np.savez('arrays',x=array1,y=array2)`

Y para recuperarlo:

`array_recuperado = np.load('arrays.npz')`

```python
array_recuperado = np.load('arrays.npz')
array1_recuperado = array_recuperado['x']
array2_recuperado = array_recuperado['y']
print(array_recuperado)
print(array1_recuperado)
print(array2_recuperado)
```

También se pueden salvar en un fichero de texto con:

`np.savetxt('mificheroarray.txt',array2,delimiter=',')`

*delimiter* indicia por qué están separados los números.

### Funciones con arrays

**Raiz cuadrada**:

`np.sqrt(array)`

Para crear arrays de forma aleatoria:

`array2 = np.random.rand(5)`

Otros ejemplos:

`suma = np.add(array, array3)`

Máximo de los dos arrays:

`maximo = np.maximum(array,array3)`

## Módulo pandas

### Series

Una serie es parecido a un array de numpy pero es una lista de valores indexada.
Ejemplo output:

```bash
Asignaturas de Daniel
matematicas    8
historia       6
fisica         9
literatura     7
Name: Notas de Daniel, dtype: int64
```

Se les puede poner nombre y al index también:

```python
asignaturas = ['matematicas','historia','fisica','literatura']
notas = [8,6,9,7]

serie_notas_daniel = pd.Series(notas, index=asignaturas)
print(serie_notas_daniel)

print(serie_notas_daniel[serie_notas_daniel >= 8])

serie_notas_daniel.name = "Notas de Daniel"
serie_notas_daniel.index.name = "Asignaturas de Daniel"

print(serie_notas_daniel)
```

Se pueden convertir a muchas cosas, como por ejemplo a un diccionario:
`diccionario = serie_notas_daniel.to_dict()`

### DataFrames

Tenemos varias funciones al usar dataframes, como *head* o *tail*. Un ejemplo:

```python
import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
# webbrowser.open(website)

# De la página vamos a ver los campeones
dataframe_nba = pd.read_clipboard()
# Pondrá los datos que pandas ha leído del clipboard
# Así que antes de ejecutar el código debemos copiar la tabla
print(dataframe_nba)
print(dataframe_nba.columns)
print(dataframe_nba['Campeón del Oeste '])
print(dataframe_nba.loc[5])

print(dataframe_nba.head())
# nos muestra las 5 primeras filas del dataframe
print(dataframe_nba.tail())
# Con el número nos muestra el número de elementos que queramos
print(dataframe_nba.head(2))
```