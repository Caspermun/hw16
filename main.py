class Person:
    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id

    def get_fn(self):
        return self.name + ' ' + self.surname
    def get_age(self):
        if self.age < 1 or self.age > 100:
            raise ValueError('Incorrect age! Type your real age.')
        else:
            return self.age
    def get_id(self):
        return self.id

    def __str__(self):
        return 'Fullname:'

class Director(Person):
    pass
class Teacher(Person):
    pass
class Student(Person):
    pass