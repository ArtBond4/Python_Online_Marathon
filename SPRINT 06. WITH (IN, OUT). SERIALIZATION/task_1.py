import json

def find(file, key):
    out_list = []
    with open(file) as f:
        my_dict = json.load(f)

    if type(my_dict) is list:  # FIRST CHOICE IF JSON IS LIST
        for first_loop in my_dict:
            if type(first_loop) is dict:
                if key in first_loop.keys():
                    out_list.append(first_loop[key])
                for second_loop in first_loop:
                    if type(first_loop[second_loop]) is dict:
                        if key in first_loop[second_loop].keys():
                            out_list.append(first_loop[second_loop][key])

    elif type(my_dict) is dict:  # SECOND CHOICE IF JSON IS DICT
        for first_loop in my_dict:
            if key == first_loop:
                out_list.append(my_dict[key])
            elif type(my_dict[first_loop]) is list:  # FIRST CHOICE IF JSON IS LIST
                for second_loop in my_dict[first_loop]:
                    if type(second_loop) is dict:
                        for third_loop in second_loop:
                            if key == third_loop:
                                out_list.append(second_loop[key])
                            elif type(second_loop[third_loop]) is list:
                                for fourth_loop in second_loop[third_loop]:
                                    if type(fourth_loop) is dict:
                                        for fifth_loop in fourth_loop:
                                            if key == fifth_loop:
                                                out_list.append(fourth_loop[key])

    if len(out_list) > 0:
        out_two = []
        for value in out_list:
            if type(value) == list:
                for second_value in value:
                    if second_value not in out_two:
                        out_two.append(second_value)
            else:
                if value not in out_two:
                    out_two.append(value)
        return out_two
    return out_list
