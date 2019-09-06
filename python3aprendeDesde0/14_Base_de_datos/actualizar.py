# SQLite3 - Actualizar datos de nuestra tabla PERSONAS

import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS set nombre = 'Homer', edad = 45 where nombre = 'Bart'")

conexion.commit()
conexion.close()