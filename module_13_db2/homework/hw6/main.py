import sqlite3
from datetime import datetime
from datetime import timedelta


def generate_employee_dict(cursor: sqlite3.Cursor) -> dict:
    """
    Создаем словарь с ключами в виде дней недели, и значениями в виде списка
    сотрудников которые НЕ МОГУТ работать в этот день.
    """
    hobby_list = ('футбол', 'хоккей', 'шахматы', 'SUP сёрфинг', 'бокс', 'Dota2', 'шах-бокс')
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    working_days_info = {}
    sql_get_employee_info = """SELECT id, name FROM table_friendship_employees WHERE preferable_sport = ?"""

    for index, hobby in enumerate(hobby_list):
        weekday = days[index]
        cursor.execute(sql_get_employee_info, (hobby,))
        employees = cursor.fetchall()
        working_days_info.setdefault(weekday)
        working_days_info[weekday] = [employee[0] for employee in employees]

    return working_days_info


def _gen_weekday_schedule(cursor: sqlite3.Cursor, data: dict, sql_request) -> None:
    spent_workers = set()
    #создаем множество сотрудников которые уже отработали
    employees_id = set([i for i in range(1, 367)])
    # создаем множество с id всех сотрудников
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')

    for _ in range(52):
        # в году около 52 недель, соответственно и цикл с таким же кол-вом итераций
        for weekday in data:
            # цикл по 7 дням недели
            start_date += timedelta(days=1)
            # добавляем один день к начальной дате 
            not_ready_workers = set(data[weekday])
            # сотрудники которые не могут выйти на смену т.к. у них тренировка
            ready_workers = employees_id.difference(not_ready_workers).difference(spent_workers)
            # сотрудники которые готовы к работе в этот день цикла
            ready_workers = list(ready_workers)
            # преобразовываем множество в список, для более удобного взаимодействия 

            if len(spent_workers) >= 350:
                spent_workers.clear()
            # по сути костыль, если кол-во рабочих которые УЖЕ отработали приближается
            # к 350 (максимальное значение при котором не возникает ошибок итерации),
            # то очищаем список этих рабочих, чтобы они вновь могли выйти на смену

            for i in range(10):
                worker = ready_workers[i]
                cursor.execute(sql_request, (worker, start_date))
                spent_workers.add(worker)
            # добавляем в таблицу 10 сотрудников (в день)


def update_work_schedule(cursor: sqlite3.Cursor, data: dict) -> None:
    sql_insert_table_friendship_schedule = """INSERT INTO table_friendship_schedule (employee_id, date) VALUES (?, ?)"""
    _gen_weekday_schedule(cursor, data, sql_insert_table_friendship_schedule)


if __name__ == '__main__':
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        data = generate_employee_dict(cursor)
        update_work_schedule(cursor, data)
        conn.commit()
