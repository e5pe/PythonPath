# Python

**pip** es un gestor de paquetes de software que están escritos en _Python_ ([Pyhton Package Index](https://pypi.python.org/pypi).
)
> *pip3* para usar el "pip" de python3

- Cómo instalar un paquete

```bash
pip3 install wheel
```

- Para ver los paquetes instalados:

```bash
pip3 list
```

- Para que nos muestre toda la información sobre un paquete:

```bash
pip show wheel
```

Ejemplo de respuesta:

```bash
    Name: wheel
    Version: 0.33.4
    Summary: A built-package format for Python.
    Home-page: https://github.com/pypa/wheel
    Author: Daniel Holth
    Author-email: dholth@fastmail.fm
    License: MIT
    Location: /home/espe/Proyectos/environments/test_env/lib/python3.6/site-packages
    Requires:
```

- Para desinstalar un paquete:

```bash
pip uninstall wheel
```

- Para buscar un paquete:

```bash
pip search wheel
```

----------
### Codificación

Para indicar la codificación tenemos que hacerlo como un comentario:

```python3
# -*- coding: utf-8 -*-
```

----------

## IDEs

Personalmente usaré **Visual Studio Code**, ya que es menos IDE y me resulta más cómodo.

### [Anaconda python](https://www.anaconda.com/distribution/)

> The open-source Anaconda Distribution is the easiest way to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X. With over 11 million users worldwide, it is the industry standard for developing, testing, and training on a single machine, enabling individual data scientists to:

- Quickly download 1,500+ Python/R data science packages
- Manage libraries, dependencies, and environments with Conda
- Develop and train machine learning and deep learning models with scikit-learn, TensorFlow, and Theano
- Analyze data with scalability and performance with Dask, NumPy, pandas, and Numba
- Visualize results with Matplotlib, Bokeh, Datashader, and Holoviews

### PyCharm

----------

## Lenguaje

**print** nos permite indicarle el separador, entonces imprimir un array de objetos e indicarle el separador es muy fácil y sencillo.

```python3
print('Casa','perro','gato', sep=', ')
```

Output:

`Casa, perro, gato`

*Ayuda de la consola:*

```bash
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

### Variables (3_1, 3_2)

No puede empezar por número.

----------

Nota:
> En casi cada sesión del curso el chico crea un archivo nuevo, por eso hay tantos.

#### Boolean

Anything not empty or not none is True.

#### String

- A string is a sequence of characters.
- Contains a-z, 0-9, @...
- In double or sigle quotes ("", '').

##### Métodos

- str convierte un argumento a cadena
- lower y upper cambian el case de la cadena
- len nos devuelve la longitud de la cadena, la cual tiene que ser pasada como argumento a la función
- replace: para reemplazar ciertos caracteres de una cadena por otros. Devuelve un string nuevo, no cambia la cadena sobre la que se realiza el replace

##### Substrings (3_10) 

- el índice inicial es inclusivo
- el índice final es exclusivo

Trabajando con índices y strings (**3_11**):

```python
>>> a = "This is a string"
>>> a
'This is a string'
>>> a[:]
'This is a string'
>>> a[1:]
'his is a string'
>>> a[0:]
'This is a string'
>>> a[:6]
'This i'
>>> a[:-1]
'This is a strin'
>>> a[:-5]
'This is a s'
>>> a[:len(a)-5]
'This is a s'
```

`::` es para indicar el espacio

Ejemplos:

```python
>>> a[::]
'This is a string'
>>> a[::1]
'This is a string'
>>> a[::2]
'Ti sasrn'
>>> a[::3]
'Tss rg'
>>> a[::-1]
'gnirts a si sihT'
>>> a[::-2]
'git  ish'
```

Si el paso es negativo nos devuelve la cadena a la inversa.

### Listas (4_1)

> Son muy similares a las de JavaScript.

### Diccionarios (4_3)

Dictionary items are in brackets {} (llaves) in key:value pairs, separated with ",": 
`{'k1':'v1','k2':'v2'}`
Como un hashmap en Java, por ejemplo.
Es mejor, porque puedes mezclar tipos de valores, como se puede ver abajo.
No tiene un orden particular.

### Booleans

El orden es NAO:

1. not
2. and
3. or

*Indentation* is **REALLY IMPORTANT**

## Lógica condicional

No hay paréntesis en los if y hay que poner `:` al final.

```python
value = 'verde'

if value == 'verde':
    print("Es verde")
elif value == 'rojo':
    print("Es rojo")
```

## Loops (o bucles)

```python
""" Loops
Items iterables son Strings, Listas, Tuplas y Diccionarios
"""
x = 1
while x <= 10:
    print("Value of x is "+str(x))
    x = x + 1

l = []
y = 0
while y < 10:
    l.append(y)
    y = y + 1

print(l)
```

### Break y Continue en bucles

```Python
""" 
break: Para salir del bucle?
continua: Para empezar la siguiente iteración del bucle
"""
x = 0
while x < 10:
    print("Value of x is "+str(x))
    x = x + 1

    if x == 8:
        break
    print("¡Este ejemplo es genial!")
    print("*"*20)
else: # Si está en un else y hay break entonces lo del else no se ejecuta
    print("Se salió del bucle")
# x = 0
# while x < 10:
#     print("Value of x is "+str(x))
#     x = x + 1

#     if x == 8:
#         continue # Continúa
#     print("¡Este ejemplo es genial!")
#     print("*"*20)
```
