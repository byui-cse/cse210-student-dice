from random import randrange
#  function: method
#data, variable: attribute
# TODO: Define the Thrower class here.

class Thrower:

    """ A code template for a person who throw the dices"""
    
    def __init__(self):
        

        self.dice = []
        self.num_throws = 0

    def can_throw(self):

        """Determines if the player can throw again"""

        return (self.dice.count(5) > 0 or self.dice.count(1) > 0 or self.num_throws == 0)

    def get_points(self):

        """Calculate the points, 1 = 100 and 5 = 50"""
        
        self.point = 0

        for i in self.dice:

            if i == 1:
                i = 100
            elif i == 5:
                i = 50
            else:
                i = 0
            
            self.point += i
        
        return self.point

    def throw_dice(self):
        """Generate random five numbers from 1 to 6 and added to the list self.dices"""

        self.dice.clear()
        self.dice = [randrange(1, 7) for i in range(5)]
        self.num_throws +=1