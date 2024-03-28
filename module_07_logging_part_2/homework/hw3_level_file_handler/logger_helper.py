import logging
import sys


class LevelFileHandler(logging.Handler):
    def __init__(self, filename: str, mode: str = 'a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        if record.levelname == 'DEBUG':
            sub_filename = self.filename + '_debug'
            with open(file=sub_filename, mode=self.mode, encoding='utf-8') as log_file:
                log_file.write(message + '\n')
        if record.levelname == 'INFO':
            sub_filename = self.filename + '_info'
            with open(file=sub_filename, mode=self.mode, encoding='utf-8') as log_file:
                log_file.write(message + '\n')
        if record.levelname == 'WARNING':
            sub_filename = self.filename + '_warning'
            with open(file=sub_filename, mode=self.mode, encoding='utf-8') as log_file:
                log_file.write(message + '\n')
        if record.levelname == 'ERROR':
            sub_filename = self.filename + '_error'
            with open(file=sub_filename, mode=self.mode, encoding='utf-8') as log_file:
                log_file.write(message + '\n')
        if record.levelname == 'CRITICAL':
            sub_filename = self.filename + '_critical'
            with open(file=sub_filename, mode=self.mode, encoding='utf-8') as log_file:
                log_file.write(message + '\n')


def get_logger(name):
    app_logger = logging.getLogger(f'{name}')
    custom_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt='%(name)s || %(levelname)s || %(message)s')
    custom_handler.setFormatter(formatter)
    app_logger.addHandler(custom_handler)
    app_logger.setLevel('DEBUG')
    custom_handler = LevelFileHandler('test_log', 'a')
    app_logger.addHandler(custom_handler)
    custom_handler.setFormatter(formatter)
    return app_logger
