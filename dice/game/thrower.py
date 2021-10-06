import random

class thrower:
    def __init__(self):
        dice = 5
        num_throws = 0
    
    def can_throw(self):
        if dice == 5 or dice == 1 or num_throws == 0:
            play = True
            return play
        else: 
            play = False
            return play

    def get_points(self):
        if dice == 1:
            points = points + 100
        elif dice == 5:
            points = points + 50

    def throw_dice(self):
        dice = []