from player import Player
from coach import Coach

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
