dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '%(name)s || %(levelname)s || %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'base'
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'S',
            'interval': '10',
            'backupCount': 5,
            'level': 'DEBUG',
            'formatter': 'base',
            'filename': 'test_logfile.log',
            'mode': 'a'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['file', 'console']
        }
    }
}