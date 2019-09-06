# SQLite3 - Consultar datos y ordenarlos por alguna columna

import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS order by edad")
personas = cursor.fetchall()

for p in personas: 
    print(p)

conexion.close()