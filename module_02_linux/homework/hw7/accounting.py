"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):

    year: str = date[:4]
    month: str = date[4:6]
    day: str = date[6:]

    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year].setdefault('year_total', 0)
    storage[year][month].setdefault('month_total', 0)

    storage[year][month][day] += number
    month_total_sum = sum([value for key, value in storage[year][month].items() if key != 'month_total'])
    storage[year][month]['month_total'] = month_total_sum
    year_total_sum = sum([value['month_total'] for key, value in storage[year].items() if key != 'year_total'])
    storage[year]['year_total'] = year_total_sum

    return storage


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    year = str(year)
    return str(storage[year]['year_total'])


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    if month < 10:
        month = '0' + str(month)
    print(year, month)
    year = str(year)
    month = str(month)
    return str(storage[year][month]['month_total'])


if __name__ == "__main__":
    app.run(debug=True)
