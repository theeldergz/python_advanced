#!/usr/bin/python

"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys
import os


def get_mean_size(ls_output: list[str]) -> float:
    """
    Функция берет список строк с информацией о файлах из ls_output,
    и находит средний вес файла
    :param ls_output: список строк с информацией о файлах
    :return: mid_summ: средний вес файла
    """
    summ: float = 0
    mid_summ: float = 0
    for item in ls_output:
        summ += int(item.split()[4:5][0])
        mid_summ = summ / len(ls_output)
    return mid_summ


if __name__ == '__main__':
    data: list[str] = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(data)
    print(mean_size)
