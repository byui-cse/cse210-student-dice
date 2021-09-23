import random

# TODO: Define the Thrower class here.
class thrower:
  """A code template for a person who plays the game. The responsibility of 
    this class of objects is to keep track of the dice, throws, points, and if the game
    is continuable
    
    Attributes:
        dice_list (list): a list of five random numbers (1-6)
    """
  def __init__(self):
    """class constructor. delcares and initializes instance attributes.
    
    Args:
        Self (thrower): an instance of thrower/
    """
    self.dice = []
    self.num_throws = 0
   
  def can_throw(self):
      """Determines whether or not the Thrower can throw again according to 
        the rules. 
        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
      return (self.dice.count(5) > 0 or self.dice.count(1) >0
              or self. num_throws ==0)
    
    def get_points(self):
      """Calculates the total number of points for the current throw. Fives 
        are worth 50 points. Ones are worth 100 points. 
        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            number: The total points for the current throw.
        """
      return self.dice.count(5) * 50 + self.dice.count(1) * 100
    
    def throw_dice(self):
      """Throws the dice by randomly generating five new values. 
        Args: 
            self (Thrower): An instance of Thrower.
        """
      self.dice.clear()
      for i in range(5)
        result = random.randint(1, 6)
        self.dice.append(result)
      self.num_throws += 1
