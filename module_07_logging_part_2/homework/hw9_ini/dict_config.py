handmade_dict = {
    'version': '1',
    'disable_existing_loggers': False,
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'consoleFormatter',
            'stream': 'sys.stdout'
        },
        'fileHandler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'fileFormatter',
            'filename': 'logfile.log'
        }
    },
    'formatters': {
        'fileFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z'
        },
        'consoleFormatter': {
            'format': '%(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z'
        }
    },
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': 'consoleHandler'
        },
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler', 'fileHandler'],
            'qualname': 'appLogger'
        }
    }
}
