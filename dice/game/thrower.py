import random

class Thrower:
    """This class is responsible for manipulating the actions of the dice
    and tallying the points received based on the dice roll.

    Attributes:
        dice (list of numbers): A list of randomly generated number ranging from 1-6.
        num_throws (number): The number of throws that have been made.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of Thrower.
        """
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        """Determines whether or not the Thrower can throw again.
        It returns a boolean value that is true if the dice have
        at least a five, or a one, or the num_throws is zero.
        Otherwise, it returns false.
        
        Args:
            self (Thrower): an instance of Thrower
        """
        if self.dice.count(5) > 0 or self.dice.count(1) > 0 or self.num_throws == 0:
            return True
        else:
            return False

    def get_points(self):
        """Calculates and returns the total points for the current dice.
        Ones are worth 100 points. Fives are worth 50 points.

        Args:
            self (Thrower): an instance of Thrower
        """
        total = 0

        for i in range(5):
            if self.dice[i-1] == 1:
                total += 100
            elif self.dice[i-1] == 5:
                total += 50
        
        return total

    def throw_dice(self):
        """Randomly generates five new dice values and adds them to the dice list.
        It also increments the num_throws attribute by one.

        Args:
            self (Thrower): an instance of Thrower
        """
        self.dice.clear()

        for _ in range(5):
            roll = random.randint(1,6)
            self.dice.append(roll)
        self.num_throws += 1