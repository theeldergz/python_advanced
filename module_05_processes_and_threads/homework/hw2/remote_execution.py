"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField()
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    command = f'prlimit --nproc=1:1 python -c "{code}"'
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    try:
        outs, errs = proc.communicate(timeout=timeout)
    except TimeoutError:
        proc.kill()
        outs, errs = proc.communicate()
    # output = proc.stdout.read().decode('utf-8')

    return outs


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        data = run_python_code_in_subproccess(code, timeout)
        return data, 200
    else:
        return f'Error: {form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
