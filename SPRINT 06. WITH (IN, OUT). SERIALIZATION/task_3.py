import json
import jsonschema
from jsonschema import validate
import csv

# type your code heree
class DepartmentName(Exception):
    pass


class InvalidInstanceError(Exception):
    pass


def user_with_department(csv_file, user_json, department_json):
    def write_in_csv(str_in, mode):
        with open(csv_file, mode, newline="") as f:
            writer = csv.writer(f)
            writer.writerow(str_in)

    write_in_csv(["name", "department"], "w")

    # CONVERT DATA TO DICT
    with open(user_json) as f:
        user_json_to_dict = json.load(f)
    with open(department_json) as f:
        department_json_to_dict = json.load(f)


    # CHECK DEP_ID IN USERS
    for i in user_json_to_dict:
        if not "department_id" in i:
            raise InvalidInstanceError("Error in user schema")

    # CHECK DEP_ID IN DEP
    for i in department_json_to_dict:
        if not "id" in i:
            raise InvalidInstanceError("Error in department schema")

    # CREATE ID DEPARTMENT LIST
    id_department_list = [i["id"] for i in department_json_to_dict]


    # MAGIC
    for i in user_json_to_dict:
        if i["department_id"] in id_department_list:
            corrected_id_dep = "Dep " + str(i["department_id"])
            write_in_csv([i["name"], corrected_id_dep], "a")
        else:
            raise DepartmentName(f"Department with id {i['department_id']} doesn't exists")
