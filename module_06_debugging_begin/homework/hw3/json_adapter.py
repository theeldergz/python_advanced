"""
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать. 
Сконфигурируйте логгер так, чтобы он писал логи в файл skillbox_json_messages.log в следующем формате:

{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}

Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:

{"time": "21:54:15", "level": "INFO", "message": "“"}

Чтобы этого избежать, потребуется LoggerAdapter. Это класс из модуля logging,
который позволяет модифицировать логи перед тем, как они выводятся.
У него есть единственный метод — process, который изменяет сообщение или именованные аргументы, переданные на вход.

class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs

Использовать можно так:

logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')

Вам нужно дописать метод process так, чтобы в логах была всегда JSON-валидная строка.
"""
import json
import logging
import re
from logging import config


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        pattern = r'\w+|[ ]'
        new_message = ''.join(re.findall(pattern, msg))
        return new_message, kwargs


if __name__ == '__main__':
    logging.basicConfig(filename='skillbox_json_messages.json',
                        format="time: %(asctime)s, level: %(levelname)s, message: %(message)s",
                        encoding='utf-8',
                        )
    logger = JsonAdapter(logging.getLogger(__name__))
    logger.setLevel(logging.DEBUG)
    logger.info('Сообщение\n')
    logger.error('Кавычка)"')
    logger.debug("Еще одно сообщение")
