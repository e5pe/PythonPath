# SQLite3 - Crear una tabla en nuestra base de datos

import sqlite3

connection = sqlite3.connect("basededatos1.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

# con el cursor de la base de datos, mediante el comando execute ejecuta la sentencia SQL

connection.commit() # le dice a la base de datos que queremos mantener la sentencia para siempre

connection.close() # por último cerramos la conexión a la base de datos

