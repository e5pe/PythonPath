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
