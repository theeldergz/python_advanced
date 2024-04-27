import sqlite3
import threading
import requests
import time


def create_table():
    conn = sqlite3.connect('hw_11_db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS
                      person_info (id integer primary key autoincrement,
                      name text not null, age integer not null, gender integer not null)""")

    conn.commit()
    conn.close()


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'\tВремя работы функции {func.__name__} составило', round(end - start, 3), 'секунд')
        return result

    return wrapper


def del_table():
    conn = sqlite3.connect('hw_11_db')
    cursor = conn.cursor()
    cursor.execute(f"delete from person_info")
    conn.commit()


def write_to_db(data):
    conn = sqlite3.connect('hw_11_db')
    cursor = conn.cursor()
    cursor.execute(f"insert into person_info (name, age, gender) values ('{data[0]}', '{data[1]}', '{data[2]}')")
    conn.commit()


def get_data(person_id):
    response = requests.get(f'https://swapi.py4e.com/api/people/{person_id}')
    name = response.json().get('name')
    age = response.json().get('birth_year')
    gender = response.json().get('gender')

    info = (name, age, gender)
    write_to_db(info)


@timer
def no_threading():
    for i in range(1, 21):
        get_data(i)


@timer
def with_threading():
    threads = []

    for i in range(1, 21):
        thread = threading.Thread(target=get_data, args=(i,))

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def main():
    create_table()
    del_table()
    print('Без потоков:')
    no_threading()
    del_table()
    print('С потоками:')
    with_threading()


if __name__ == '__main__':
    main()
