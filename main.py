class Person:
    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.__age = age
        self.__id = id

    def get_fn(self):
        return self.name + ' ' + self.surname

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise ValueError('Incorrect age! Type your real age.')

    def get_age(self):
        self.set_age(self.__age)
        return self.__age

        # if self.age not in range(1, 100):
        #     raise ValueError('Incorrect age! Type your real age.')
        # else:
        #     return self.age

    def get_id(self):
        return self.__id

    def __str__(self):
        return 'Fullname:'

class Director(Person):
    pass
class Teacher(Person):
    pass
class Student(Person):
    pass