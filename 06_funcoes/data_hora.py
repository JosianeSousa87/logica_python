import datetime
import calendar

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"
]

semana = [
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sabado",
    "domingo"
]

#21/12/2024
data = datetime.date(2024, 12, 21)
print(data)

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month -1]} de {hoje.year}")

print(f"2024 é Bissexto: {calendar.isleap(2024)}")

print(f"É o último dia do mês? {calendar.monthrange(2026, 10)[1]}")