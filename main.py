from player import Player
from coach import Coach
from substitute import Substitute
from playing_coach import PlayingCoach

coach1 = Coach('Andrew Lando', 50, 10000)
coach2 = PlayingCoach('John Conrad', 30, 'GK', 15000)


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
