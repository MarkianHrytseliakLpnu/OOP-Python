from player import Player

class Substitute(Player):
    __is_substitute = True

    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)
        self.is_added = False

    def set_info(self, name, age, position, salary):
        super().set_info(name, age, position, salary)

    def add_to_club(self):
        print('Substitute added to club')
        self.is_added = True

    @staticmethod
    def print_info(name, age, position, salary):
        Player.print_info(name, age, position, salary)
        print('Is Substitute: Yes')
