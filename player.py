class Player:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def set_info(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def add_to_club(self):
        print('Player added to club')

    @staticmethod
    def print_info(name, age, position, salary):
        # Використовуємо правильне форматування
        print(f'Name: {name}\nAge: {age}\nPosition: {position}\nSalary: {salary}')