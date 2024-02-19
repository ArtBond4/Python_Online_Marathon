class ToSmallNumberGroupError(Exception):
    def __str__(self):
        return f"We obtain error:Number of your group can't be less than 10"


# enter your code
def check_number_group(number):
    try:
        if int(number) > 10:
            return f"Number of your group {number} is valid"

        elif int(number) <= 10:
            raise ToSmallNumberGroupError
        #

    except ToSmallNumberGroupError as e:
        return e

    except ValueError:
        return f"You entered incorrect data. Please try again."
