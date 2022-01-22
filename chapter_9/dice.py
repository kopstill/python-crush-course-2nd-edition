from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice = Dice(6)
dice.roll_die()
dice.roll_die()
dice.roll_die()

print('**********')

dice = Dice(20)
dice.roll_die()
dice.roll_die()
dice.roll_die()
