"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime

WEEKDAYS_NAMES = (
    "Понедельник(а)",
    "Вторник(а)",
    "Среды",
    "Пятницы",
    "Субботы",
    "Воскресенья",
)

app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username):
    weekday = datetime.today().weekday()
    return f"Привет, {username}. Хорошей {WEEKDAYS_NAMES[weekday]}!"


if __name__ == "__main__":
    app.run(debug=True)
