from custom_handler import CustomHttpHandler
base_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple"
        },
        "http_handler": {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "host": "127.0.0.1:5000",
            "url": "/log",
            "method": "POST"
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console_handler", "http_handler"]
    }
}
