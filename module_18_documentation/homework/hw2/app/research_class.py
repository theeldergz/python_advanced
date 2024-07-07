from routes_spec_aside_code import app
from clients import BookClient
from werkzeug.serving import WSGIRequestHandler
from datetime import datetime
from models import init_db
import requests
import json

URL = 'http://127.0.0.1:5000/api/books'
client = BookClient()


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now() - start
        print(f'Время работы функции заняло {end}')
        return res

    return wrapper


class Research:
    @staticmethod
    @timer
    def without_session(count):
        for _ in range(count):
            data = requests.post(URL,
                                 data=json.dumps({'title': '123', 'author': 'name'}),
                                 headers={'content-type': 'application/json'})
            print(data.status_code)

    @staticmethod
    @timer
    def with_session(self, count):
        for _ in range(count):
            client.session.post(
                client.URL,
                data=json.dumps({'title': '123', 'author': 'name'}),
                headers={'content-type': 'application/json'}
            )


if __name__ == "__main__":
    init_db(initial_records=DATA)
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run('127.0.0.1', debug=True)
    Research.with_session(count=10)
