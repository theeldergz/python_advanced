"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


@app.errorhandler(404)
def page_not_found(error):
    original = getattr(error, 'original_exception', None)
    available_url_endpoints = []
    response_string_template = 'Данная страница не найдена! Попробуйте перейти по ссылкам ниже:<br>'
    base_url = 'http://127.0.0.1:5000'
    if isinstance(original, TypeError):
        pass

    with app.app_context():
        for rule in app.url_map.iter_rules():
            print(rule)
            second_url = base_url + str(rule)
            response_string_template += f'<br><a href="{second_url}">{second_url}</a>'
            available_url_endpoints.append(second_url)

    return f'{response_string_template}', 500


if __name__ == '__main__':
    app.run(debug=True)
    app.config['WTF_CSRF_ENABLED'] = False
