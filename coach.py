class Coach:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.is_hired = False

    def set_info(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def hire_to_club(self):
        print('Coach hired to club')
        self.is_hired = True

    @staticmethod
    def print_info(name, age, salary):
        print(f'Name: {name}\nAge: {age}\nSalary: {salary}')
