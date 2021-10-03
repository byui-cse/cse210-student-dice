import random

class Thrower(object):

    def __init__(self):
        self.dice = []
        self.points = 0

    def throw_dice(self):
        self.dice.clear()
        for die in range(5):
            self.dice.append(random.randint(1,6))

    def get_points(self):
        self.points = sum([100 if die == 1 else 0 for die in self.dice]) + sum([50 if die == 5 else 0 for die in self.dice])
        return self.points
    
    def can_throw(self):
        return any((die == 1 or die == 5) for die in self.dice)

