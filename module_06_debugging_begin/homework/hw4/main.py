"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
import pprint
from itertools import groupby
from typing import Dict

with open('skillbox_json_messages.log', 'r', encoding='utf-8') as log_file:
    DATA = []
    for line in log_file.readlines():
        DATA.append(json.loads(line))


def time_to_sec(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total = hours * 3600 + minutes * 60 + seconds
    return total


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    output = {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0
    }

    for log in DATA:
        if log['level'] == 'DEBUG':
            output['DEBUG'] += 1
        elif log['level'] == 'INFO':
            output['INFO'] += 1
        elif log['level'] == 'WARNING':
            output['WARNING'] += 1
        elif log['level'] == 'ERROR':
            output['ERROR'] += 1
        elif log['level'] == 'CRITICAL':
            output['CRITICAL'] += 1

    return output


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    one_hour_in_sec = 3600
    end_time = 0
    log_counter = 0
    count_list = []
    while end_time < 86400:
        start_time = end_time
        end_time = start_time + one_hour_in_sec
        for log in DATA:
            log_time = time_to_sec(log['time'])
            if start_time <= log_time <= end_time:
                log_counter += 1
        count_list.append(log_counter)
        log_counter = 0
    hour = count_list.index(max(count_list))
    return hour


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    time_start = time_to_sec('05:00:00')
    time_stop = time_to_sec('05:20:00')
    count = 0
    for log in DATA:
        log_time = time_to_sec(log['time'])
        if time_start < log_time <= time_stop and 'CRITICAL' in log['level']:
            count += 1

    return count


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    count = 0
    for log in DATA:
        if 'dog' in log['message']:
            count += 1

    return count


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    count_words = {}
    words_list = []
    for log in DATA:
        if log['level'] == 'WARNING':
            words_list.extend(log['message'].lower().split())

    for word in words_list:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words.setdefault(word, 1)

    keys = list(count_words.keys())
    values = list(count_words.values())
    index_max_elem = values.index(max(values))
    req_word = keys[index_max_elem]

    return req_word


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
