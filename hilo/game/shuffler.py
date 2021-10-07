"""Shuffler Class"""
import random as r

class Shuffler:
    def __init__(self):

        self.points = 300
        self.card = []

    def canPlay(self):
        
        if(self.points <= 0):
            return False
        else:
            return True

    def getScore(self):
        """args:"""

    def getCard(self):

        self.card = []
        self.card.append(r.randint(1,13))
        self.card.append(r.randint(1,13))