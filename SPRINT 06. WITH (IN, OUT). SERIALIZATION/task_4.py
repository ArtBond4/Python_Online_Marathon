import json
from json import JSONEncoder

class Student:
    # Class Student has attributes full_name:str, avg_rank: float, courses: list
    # Класс Student имеет атрибуты full_name:str, avg_rank:float, courses: list
    def __init__(self, full_name=str, avg_rank=float, courses=list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        # pass
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        # Student.from_json(json_file) that return Student instance from attributes from json-file;
        # Student.from_json(json_file) которые возвращают Student экземпляр из атрибутов из json-файла;
        with open(json_file) as f:
            my_dict = json.load(f)
        return Student(my_dict["full_name"], my_dict["avg_rank"], my_dict["courses"])

    def serialize_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)


class Group:
    # Class Group has attributes title: str, students: list.
    # Класс Group имеет атрибуты title: str, students: list.
    def __init__(self, title, students=list):
        self.title = title
        self.students = students


    def __str__(self):
        title = self.title
        student_inf = self.students
        if isinstance(student_inf, list):
            return f'{title}: [' + f', '\
                .join([f"\"{i.get('full_name')} ({i.get('avg_rank')}):"
                       f" {[z for z in i.get('courses')]}\""
                       for i in student_inf]) + ']'
        return f"{title}: [\"{student_inf.get('full_name')}" \
               f" ({student_inf.get('avg_rank')}):" \
               f" {student_inf.get('courses')}\"]"







    # def __str__(self):
    #     path = str(self.title)+".json"
    #     print(path)
    #     # return "123"
    #     user1 = Student.from_json(path)
    #     return str(user1)


    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w') as f:
            for i in list_of_groups:
                return json.dump([{'title': i.title, 'students': i.students
                if i.title != '2020-01'
                else [i.students]} for i in list_of_groups], f)

    @classmethod
    def create_group_from_file(cls, students_file):
        correct_title = students_file.split(".")[0]
        with open(students_file, 'r') as f:
            my_file = json.load(f)
        return Group(correct_title, my_file)
