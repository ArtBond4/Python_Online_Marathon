class MyExceptions(Exception):
    pass

def sum_slice_array(my_list, a, b):
    try:
        if a < 1 or b < 1:
            raise MyExceptions
        elif a > b:
            a, b = b, a
            slice_array = my_list[a : b ]
            return f"{float(sum(slice_array))}"

        elif a == b:
            slice_array = my_list[a - 1: b]
            return f"{float(sum(slice_array))*2}"

        slice_array = my_list[a - 1: b]
        return f"{float(sum(slice_array))}"

    except TypeError:
        raise MyExceptions
