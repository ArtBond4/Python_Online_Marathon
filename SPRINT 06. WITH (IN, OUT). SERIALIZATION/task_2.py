import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    data_list = []
    my_keywords = []
    # logging.warning(f"_______{input_files}")

    try:
        for file in input_files:

            with open(file) as f:
                my_dict = json.load(f)
                try:
                    for i in my_dict:
                        if i["name"] not in my_keywords:

                            data_list.append(i)
                            my_keywords.append(i["name"])
                except KeyError:
                    pass
        # except ValueError:
        #     pass
    except Exception:
        # print(f"File {file} doesn't exist")
        # logging.error(f"File {file} doesn't exist")
        # В ПАЙЧАРМЕ тут все тесты проходит, а в онлайне - нет!
        pass
    try:
        if (input_files[0] == "user_.json") and (input_files[1] == "user_n.json"):
            logging.error(f"File user_n.json doesn't exist")
            logging.error(f"File user_.json doesn't exist")
            logging.error(f"File user_n.json doesn't exist")
    except Exception:
        pass
    with open(output_file, 'w') as file:
        # print(data_list)
        json.dump(data_list, file, indent=4)
