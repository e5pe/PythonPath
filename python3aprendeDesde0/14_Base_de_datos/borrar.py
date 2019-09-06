# SQLite3 - Borrar datos de nuestra tabla PERSONAS

import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS where nombre = 'Pablo'")

conexion.commit()
conexion.close()