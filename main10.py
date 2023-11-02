# object oriented programming

class Employee:
    __name = None
    __id = 0
    __salary = 0  # double underscore here means variable is private

    def __init_(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


priya = Employee()
print(priya.get_id())
