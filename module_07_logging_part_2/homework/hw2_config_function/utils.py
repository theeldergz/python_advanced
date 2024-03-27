import logging
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
custom_handler = logging.StreamHandler()
custom_handler.setLevel('DEBUG')
formatter = logging.Formatter(fmt='%(name)s || %(levelname)s || %(message)s')
custom_handler.setFormatter(formatter)


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        utils_logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        utils_logger.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]

