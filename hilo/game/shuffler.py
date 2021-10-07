"""Shuffler Class"""
import random as r

class Shuffler:
    """Attributes:"""
    def __init__(self):
        
        self.card = []

    def canPlay(self, points):
        if(points <= 0):
            return False
        else:
            return True

    def getScore(self):
        """Args:
        self: an instance of shuffler"""
        #True if the users card is greater than the shufflers
        #False if its less than the shufflers
        if self.card[0] > self.card[1]:
            return True
        if self.card[1] >= self.card[0]:
            return False
        

    def getCard(self):
        self.card = []
        self.card.append(r.randint(1,13))
        self.card.append(r.randint(1,13))
