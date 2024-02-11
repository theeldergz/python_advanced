"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

import shlex, subprocess
import string
from typing import List
from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args: List[str] = request.args.getlist('arg')
    command_str = ''.join([shlex.quote(s) for s in args])
    command = f'ps {command_str}'
    # result = subprocess.run(command_str, capture_output=True)
    # output = result.stdout.decode(encoding='Windows-1251')

    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode()
    print(command_str, command, result, output)
    # return f'{output}'
    return string.Template(f'<pre>{output}</pre>').substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
