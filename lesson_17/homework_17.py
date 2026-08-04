import functools
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def log_arguments_and_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Call %s with args=%s kwargs=%s", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        logger.info("%s returned %r", func.__name__, result)
        return result

    return wrapper


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            logger.error("%s failed: %s", func.__name__, error)
            return None

        if hasattr(result, "__iter__") and hasattr(result, "__next__"):
            return _handle_generator_exceptions(result, func.__name__)

        return result

    return wrapper


def _handle_generator_exceptions(generator, func_name):
    try:
        yield from generator
    except Exception as error:
        logger.error("%s failed: %s", func_name, error)


@handle_exceptions
def even_numbers_generator(limit):
    if limit < 0:
        raise ValueError("Limit must be greater than or equal to 0")

    for number in range(0, limit + 1, 2):
        yield number


@handle_exceptions
def fibonacci_generator(limit):
    if limit < 0:
        raise ValueError("Limit must be greater than or equal to 0")

    first, second = 0, 1
    while first <= limit:
        yield first
        first, second = second, first + second


class ReverseListIterator:
    def __init__(self, items):
        self.items = items
        self.index = len(items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.items[self.index]


class EvenNumbersIterator:
    def __init__(self, limit):
        if limit < 0:
            raise ValueError("Limit must be greater than or equal to 0")

        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        number = self.current
        self.current += 2
        return number


@log_arguments_and_result
def get_reversed_list(items):
    return list(ReverseListIterator(items))


@log_arguments_and_result
def get_even_numbers_from_iterator(limit):
    return list(EvenNumbersIterator(limit))


if __name__ == "__main__":
    print("Even generator:", list(even_numbers_generator(10)))
    print("Fibonacci generator:", list(fibonacci_generator(50)))
    print("Reverse iterator:", get_reversed_list([1, 2, 3, 4, 5]))
    print("Even iterator:", get_even_numbers_from_iterator(10))

    list(even_numbers_generator(-1))
