"""Director Class"""
from game.shuffler import Shuffler

class Director:
    """Attributes:"""

    def __init__(self):
        """Args:"""
        self.keep_playing = True
        self.score_points = True

    
    def startGame(self):
        """Makes a loop to make sure that the game keeps playing as long as there are 
            enough points and the player still wants to play
            Args: self """
        while self.keep_playing:
            self.getInputs()
            self.doUpdates()
            self.doOutputs()


    def getInputs(self):
        """Args:"""
        pass

    def doUpdates(self):
        """Args:"""
        pass

    def doOutputs(self):
        """Args:"""
        pass
