# SQLite3 - Insertar varios registros a la vez en nuestra tabla

import sqlite3

connection = sqlite3.connect("basededatos1.db")

cursor = connection.cursor()

lista_personas = [('Pedro','García', 'Rodriguez',40),
                    ('Lisa','Simpson', 'Tal',10),
                    ('Bart','Simpson', 'Tal',10),
                    ('Andrea','Rastoll', 'Perez',20),
                    ('Pablo','García', 'Perez',22)]

# la sentencia se ejecuta tantas veces como elementos haya en la lista personas
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

connection.commit()
connection.close()