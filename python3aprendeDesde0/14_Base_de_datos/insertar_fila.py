# SQLite3 - Insertar datos en nuestra tabla

import sqlite3

connection = sqlite3.connect("basededatos1.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Antonio Manuel','García','Fernández',35)")

connection.commit()
connection.close()