import shlex
import subprocess
import sys


def process_count(username: str) -> int:
    # cmd = shlex.split(f'ps -u {username} | wc -l ')
    cmd = ['ps', '-u', username, '-o', 'pid']
    pid_list = subprocess.run(cmd, capture_output=True)
    result = len(pid_list.stdout.decode().splitlines()) - 1
    return result


def total_memory_usage(root_pid: int) -> float:
    cmd = ['ps', '--ppid', str(root_pid), '-o', '%mem']
    mem_list = subprocess.run(cmd, capture_output=True).stdout.decode().splitlines()
    result = sum(map(float, mem_list[1:]))
    return result


print(process_count('varjuhind'))
print(total_memory_usage(1))