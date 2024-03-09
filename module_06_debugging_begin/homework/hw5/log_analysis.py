import json
from datetime import datetime

with open('logs_measure_me_level_info.json', 'r', encoding='utf-8') as log_file:
    start_time = []
    end_time = []
    for log in log_file.readlines():
        line = json.loads(log)
        if line['message'] == 'START':
            raw_time = datetime.strptime(line['time'], "%Y-%m-%d %H:%M:%S,%f")
            start_time.append(raw_time.timestamp())
        if line['message'] == 'END':
            raw_time = datetime.strptime(line['time'], "%Y-%m-%d %H:%M:%S,%f")
            end_time.append(raw_time.timestamp())


def result():
    log_range = len(start_time)
    avg_time = 0
    for index in range(log_range):
        avg_time += end_time[index] - start_time[index]

    return f'Среднее время выполнения функции {avg_time / log_range} sec'

