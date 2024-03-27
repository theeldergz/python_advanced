import logging
import sys
from utils import string_to_operator
from logger_helper import get_logger

app_logger = get_logger('app_logger')


def calc(args):
    app_logger.info(f'Arguments func {calc.__name__}: {args}')

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
    # calc(sys.argv[1:])
    calc('2+3')
