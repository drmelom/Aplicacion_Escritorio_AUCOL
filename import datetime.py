import datetime

year = 2023
month = 3

# creamos un objeto datetime para el primer día del mes
start_date = datetime.date(year, month, 1)

# calculamos el número total de días en el mes
num_days = (datetime.date(year, month + 1, 1) - start_date).days

# inicializamos el contador de días
count = 0

# iteramos por cada día del mes
for i in range(num_days):
    # creamos un objeto datetime para el día actual
    date = start_date + datetime.timedelta(days=i)
    # si el día es martes, jueves o sábado, aumentamos el contador
    if date.weekday() in [1, 3, 5]:
        count += 1

print(count) # muestra el resultado