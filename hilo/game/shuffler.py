"""Shuffler Class"""
import random as r

class Shuffler:
    """
    Contains functions vital to play in the director class such as checking 
    if player can play, getting score, and getting cards
    Attributes: 
        card (array): List of two cards to compare
    """
    def __init__(self):
        """ Constructor
        
        Args: 
            self : an instance of shuffler
        """
        
        self.card = []

    def canPlay(self, points):
        """Returns a bool value if player can or cannot continue playing

        Args:
            self : an instance of shuffler
            points (number): number of points for given game
        """
        if(points <= 0):
            return False
        else:
            return True

    def getScore(self):
        """Returns a bool value if card is higher or lower than previous card
        
        Args:
            self : an instance of shuffler
        """
        #True if the users card is greater than the shufflers
        #False if its less than the shufflers
        if self.card[0] > self.card[1]:
            return True
        if self.card[1] >= self.card[0]:
            return False
        

    def getCard(self):
        """Generates cards to append self.card
        
        Args:
            self : an instance of shuffler
        """
        if len(self.card) > 0:
            cardTemp = self.card[1]
        else:
            cardTemp = r.randint(1,13)
        self.card = []
        self.card.append(cardTemp)
        self.card.append(r.randint(1,13))
