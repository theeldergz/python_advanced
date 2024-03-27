import logging


class FilterWithoutASCII(logging.Filter):
    def __int__(self):
        super().__init__()

    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        return msg.isascii()
