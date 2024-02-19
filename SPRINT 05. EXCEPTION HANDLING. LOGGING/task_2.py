import logging
import math

logger = logging.getLogger()


logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='app.log', mode="w")
c_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)

c_handler.setLevel(logging.DEBUG)

my_string_form = "%(levelname)s:%(name)s:%(message)s"

file_formatter = logging.Formatter(my_string_form)
c_formatter = logging.Formatter(my_string_form)

file_handler.setFormatter(file_formatter)
c_handler.setFormatter(c_formatter)

logger.addHandler(file_handler)
# logger.addHandler(c_handler)


# logger.debug("A debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.critical("critical message")




def findingTangent(sin_alpha, cos_alpha):
    logger.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logger.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    try:
        tan_alpha = sin_alpha / cos_alpha

    except ZeroDivisionError:
        logger.warning(f"The cosine of the angle alpha = {cos_alpha}. The tangent is not defined.")

    except TypeError:
        logger.critical(f"The tangent of the angle alpha is not defined.")

    else:
        logger.debug(f"The value of the tangent of the angle alpha is found = {tan_alpha}")

findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)
