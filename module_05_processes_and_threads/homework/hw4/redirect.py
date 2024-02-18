"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

import sys
import traceback
from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.new_stdout = stdout
        self.new_stderr = stderr

    def __enter__(self):
        if self.new_stdout:
            sys.stdout = self.new_stdout
        if self.new_stderr:
            sys.stderr = self.new_stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if self.new_stdout:
            self.new_stdout.close()
            sys.stdout = self.old_stdout
        if self.new_stderr:
            sys.stderr.write(traceback.format_exc())
            self.new_stderr.close()
            sys.stderr = self.old_stderr
        return True
