"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""
import psutil
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    sys_uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    return f'Current uptime is {sys_uptime}'


if __name__ == '__main__':
    app.run(debug=True)
