import logging, logging.config, logging.handlers
from typing import Union, Callable
from operator import sub, mul, truediv, add

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]

utils_logger = logging.getLogger('utils_logger')


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    utils_logger.debug('test debug')
    utils_logger.info('test info')
    utils_logger.warning('test warning')
    utils_logger.error('test error')
    utils_logger.critical('test ctitical')

    if not isinstance(value, str):
        utils_logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        utils_logger.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
