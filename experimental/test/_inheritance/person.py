class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid

    def get_sid(self):
        return self.sid

    def set_sid(self, sid):
        self.side = sid

class Employee(Person):
    def __init__(self, name, age, company=None):
        super().__init__(name, age)
        self.company = None

    def is_unemployed(self):
        return self.company is None

    def get_best_job(self):
        self.set_job('Google')

    def get_job(self):
        return self.company

    def set_job(self, company):
        self.company = company

