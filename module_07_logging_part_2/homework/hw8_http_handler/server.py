import json
from logging import config
from flask import Flask, request


app = Flask(__name__)


messages = []


@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, статус код успешной работы

    """
    form = request.form
    print(f"{form['levelname']} | {form['name']} | {form['msg']} | {form['asctime']}")
    messages.append(f"{form['levelname']} | {form['name']} | {form['msg']} | {form['asctime']}")
    return 'OK', 200


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    output = '\n'.join(messages)
    return f'<pre>{output}</pre>'


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
