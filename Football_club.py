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


class Coach:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def set_info(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def hire_to_club(self):
        print('Coach hired to club')

    @staticmethod
    def print_info(name, age, salary):
        print(f'Name: {name}\nAge: {age}\nSalary: {salary}')


class Substitute(Player):
    __is_substitute = True

    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)

    def set_info(self, name, age, position, salary):
        super().set_info(name, age, position, salary)

    def add_to_club(self):
        print('Substitute added to club')

    @staticmethod
    def print_info(name, age, position, salary):
        Player.print_info(name, age, position, salary)
        print('Is Substitute: Yes')


class PlayingCoach(Player, Coach):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)

    def set_info(self, name, age, position, salary):
        super().set_info(name, age, position, salary)

    def hire_to_club(self):
        print('Playing Coach hired to club')

    @staticmethod
    def print_info(name, age, position, salary):
        Player.print_info(name, age, position, salary)


# Створення об'єктів і виклик методів
coach1 = Coach('Andrew Lando', 50, 10000)
coach2 = PlayingCoach('John Conrad', 30, 'GK', 15000)

# Порівняння зарплат і вибір тренера
if coach1.salary < coach2.salary:
    coach1.print_info(coach1.name, coach1.age, coach1.salary)
    coach1.hire_to_club()
    print()
else:
    coach2.print_info(coach2.name, coach2.age, coach2.position, coach2.salary)
    coach2.hire_to_club()
    print()

player1 = Player('Rick French', 18, 'ST', 20000)
player2 = Player('Stan Cook', 29, 'CM', 25000)
sub1 = Substitute('Jack Tingly', 36, 'CB', 12000)
sub2 = Substitute('Max Freeman', 23, 'LW', 12000)

player2.set_info('Stan Cook', 29, 'CM', 22000)
sub1.set_info('Jack Tingly', 36, 'CB', 11500)

# Додавання гравців у клуб
Player.print_info(player1.name, player1.age, player1.position, player1.salary)
player1.add_to_club()
print()

Player.print_info(player2.name, player2.age, player2.position, player2.salary)
player2.add_to_club()
print()

Substitute.print_info(sub1.name, sub1.age, sub1.position, sub1.salary)
sub1.add_to_club()
print()

Substitute.print_info(sub2.name, sub2.age, sub2.position, sub2.salary)
sub2.add_to_club()
print()




