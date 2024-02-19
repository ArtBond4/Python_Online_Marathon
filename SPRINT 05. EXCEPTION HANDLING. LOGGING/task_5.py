import logging


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='app.log', mode="w")
c_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)
c_handler.setLevel(logging.DEBUG)

my_string_form = "%(name)s - %(levelname)s - %(message)s"

file_formatter = logging.Formatter(my_string_form)
c_formatter = logging.Formatter(my_string_form)

file_handler.setFormatter(file_formatter)
c_handler.setFormatter(c_formatter)

logger.addHandler(file_handler)
# logger.addHandler(c_handler)


def average(numbers):
    try:
        answer = sum(numbers) / len(numbers)
        logger.info(answer)


    except ZeroDivisionError:
        logger.debug("The list is empty")
        logger.warning("Division by zero")

    except TypeError:
        logger.critical("Incorrect data entered")
        
        
average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])
