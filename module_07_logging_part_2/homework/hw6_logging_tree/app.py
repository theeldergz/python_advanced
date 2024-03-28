import logging
import logging.config
import sys
import time
from logging_tree import printout
from utils import string_to_operator, utils_logger
from logger_config import base_config

logging.config.dictConfig(base_config)
app_logger = logging.getLogger('app_logger')

with open('logging_tree2.txt', mode='w+', encoding='utf-8') as file:
    sys.stdout = file
    sys.stderr = file
    printout()


def calc(args):
    app_logger.debug(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        app_logger.warning("Error while converting number 1")
        app_logger.warning(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        app_logger.warning("Error while converting number 1")
        app_logger.warning(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    app_logger.info(f"Result: {result}")
    app_logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    for _ in range(300):
        time.sleep(1)
        calc('2+3')
        try:
            calc('2 + y')
        except Exception as exc:
            pass

    print(app_logger.parent)
    print(app_logger)
    print(utils_logger)
