# SQLite3 - Consultar datos de nuestra tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall() # con este método recogemos todas las filas y columnas

for p in personas:
    print(p)

conexion.close()
