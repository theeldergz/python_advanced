"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
import os
import shlex
import signal
import subprocess
import time
from typing import List

from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    command_str = 'lsof -i :{}'.format(port)
    command = shlex.split(command_str)
    pids_out = subprocess.run(command, capture_output=True)
    pids_by_lines = pids_out.stdout.decode('utf-8').splitlines()
    print(pids_by_lines)
    for line in pids_by_lines[1:]:
        # Выражением ниже, достаем значение pid из строки и сразу преобразуем его в int
        pid = int(line.split()[1])
        pids.append(pid)

    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    for pid in pids:
        os.kill(pid, signal.SIGINT)


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    # timeout
    time.sleep(0.1)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
