from datetime import datetime, timedelta
import os
import random
import re
from flask import Flask


app = Flask(__name__)

CAT_LIST = [
    'корниш-рекс', 'русская голубая',
    'шотландская вислоухая', 'мейн-кун', 'манчкин'
]
CAR_LIST = ['Chevrolet', 'Renault', 'Ford', 'Lada']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def word_return():
    text_path = os.path.join(BASE_DIR, 'war_and_peace.txt')
    with open('war_and_peace.txt', 'r', encoding='utf-8') as raw_text:
        text = raw_text.read()
        word_list = re.findall(r'\b(\w+)\b', text)
        return random.choice(word_list)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return ' '.join(CAR_LIST)


@app.route('/cats')
def cats():
    return random.choice(CAT_LIST)


@app.route('/get_time/now')
def get_time_now():
    return '«Точное время: {current_time}»'.format(current_time=datetime.now())


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}»'


@app.route('/get_random_word')
def get_random_word():
    return word_return()


@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)
counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)
