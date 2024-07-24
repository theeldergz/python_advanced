import json
import time
from multiprocessing import cpu_count

import requests
from multiprocessing.pool import ThreadPool
import logging


# logging.basicConfig(level=logging.DEBUG)


class BookClient:
    URL: str = 'http://127.0.0.1:5000/api/books'
    TIMEOUT: int = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_books(self) -> dict:
        response = self.session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_book(self, data: dict):
        response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def get_book_url(self, book_id):
        new_url = f'{self.URL}/{book_id}'
        return new_url



class Research:
    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time() - start
            print(f'Время работы функции {func.__name__} заняло {end:.5f} секунд')
            return res

        return wrapper

    @staticmethod
    @timer
    def without_session(count):
        for _ in range(count):
            new_url = client.get_book_url(count)
            requests.get(new_url)

    @staticmethod
    @timer
    def with_session(count):
        for _ in range(count):
            new_url = client.get_book_url(count)
            client.session.get(new_url)

    @staticmethod
    @timer
    def with_threading_without_session(count):
        pool = ThreadPool(processes=cpu_count())
        pool.map(requests.get, (f'{client.URL}/{book_id}' for book_id in range(count)))
        pool.close()
        pool.join()

    @staticmethod
    @timer
    def with_threading_with_session(count):
        pool = ThreadPool(processes=cpu_count())
        pool.map(client.session.get, (f'{client.URL}/{book_id}' for book_id in range(count)))
        pool.close()
        pool.join()


if __name__ == '__main__':
    client = BookClient()

    Research.without_session(10)
    Research.with_threading_without_session(10)
    Research.with_session(10)
    Research.with_threading_with_session(10)

    print()
    print('-' * 100)
    print()

    Research.without_session(100)
    Research.with_threading_without_session(100)
    Research.with_session(100)
    Research.with_threading_with_session(100)

    print()
    print('-' * 100)
    print()

    Research.without_session(1000)
    Research.with_threading_without_session(1000)
    Research.with_session(1000)
    Research.with_threading_with_session(1000)
