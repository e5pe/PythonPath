# SQLite3 - Consultar datos que cumplan una determinada condición

import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS where edad > 18")
personas = cursor.fetchall()

for p in personas: 
    print(p)

conexion.close()