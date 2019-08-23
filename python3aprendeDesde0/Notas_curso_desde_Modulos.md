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
