# Dataframes

import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
# webbrowser.open(website)

# De la página vamos a ver los campeones
dataframe_nba = pd.read_clipboard()
# Pondrá los datos que pandas ha leído del clipboard
print(dataframe_nba)
print(dataframe_nba.columns)
print(dataframe_nba['Campeón del Oeste '])
print(dataframe_nba.loc[5])

print(dataframe_nba.head())
# nos muestra las 5 primeras filas del dataframe
print(dataframe_nba.tail())
# Con el número nos muestra el número de elementos que queramos
print(dataframe_nba.head(2))


lista_asignaturas = ['matematicas', 'historia', 'fisica']
lista_notas = [8, 7, 9]
diccionario = {'Asignaturas': lista_asignaturas, 'Notas': lista_notas}
print(diccionario)
dataframe_notas = pd.DataFrame(diccionario)

print(dataframe_notas)
print(dataframe_notas.head(2))