import random


class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 1
        self.size = 30

    def roll_dice(self):
        self.value = random.randint(1, 6)

    def read_dice(self):
        return self.value

    def print_dice(self):
        print('주사위의 값: ', self.value)


dice = Dice(100, 100)
dice.roll_dice()
dice.print_dice()
