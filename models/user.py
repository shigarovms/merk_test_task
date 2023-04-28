import json


class User:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, salary: int, department: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.salary = salary
        self.department = department

    def __eq__(self, other):
        if isinstance(other, User):
            return self.first_name == other.first_name and \
                   self.last_name == other.last_name and \
                   self.age == other.age and \
                   self.email == other.email and \
                   self.salary == other.salary and \
                   self.department == other.department
        return False

    @staticmethod
    def new_user_from_json(json_path):
        with open(json_path) as f:
            data = json.load(f)
        return User(**data)

    @staticmethod
    def new_user_from_list_of_strings(list_of_strings):
        return User(list_of_strings[0],
                    list_of_strings[1],
                    int(list_of_strings[2]),
                    list_of_strings[3],
                    int(list_of_strings[4]),
                    list_of_strings[5])
