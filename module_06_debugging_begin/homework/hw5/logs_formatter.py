import json
import logging


class JsFormatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        log_record = {
            'time': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage()
        }
        return json.dumps(log_record)

