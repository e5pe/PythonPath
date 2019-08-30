# fecha y hora
from datetime import datetime

ahora = datetime.now() # devuelve la fecha y hora actuales
print(ahora)
year = ahora.year
month = ahora.month
day = ahora.day

print("El año es {}, el mes es {} y el día de hoy es {}".format(year,month,day))

hora = ahora.hour
minutos = ahora.minute
segundos = ahora.second
microsegundos = ahora.microsecond

print("Son las {}:{}:{}".format(hora,minutos,segundos))