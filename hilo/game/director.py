"""Director Class"""
from game.shuffler import Shuffler

class Director:
    """Attributes:"""

    def __init__(self):
        """Args:"""
        self.shuffler = Shuffler()
        self.keep_playing = True
        self.score_points = True
        self.points = 300
        

    
    def startGame(self):
        """Makes a loop to make sure that the game keeps playing as long as there are 
            enough points and the player still wants to play
            Args: self """
        while self.keep_playing:
            self.doOutputs()


    def getInputs(self):
        """Args:"""
        choice = input("Higher or Lower? [h/l] ")
        self.score_points = self.doUpdates(choice)
        pass

    def doUpdates(self, choice):
        """Args:"""
        if (not self.shuffler.getScore() and choice == "h") or (self.shuffler.getScore() and choice == "l") and not (self.Shuffler.card[0] != self.shuffler.card[1]):
            self.points = 100 + self.points
            return True
        else:
            self.points = self.points - 75
            return False
        pass

    def doOutputs(self):
        """Args:"""
        print(f"The card is: {self.shuffler.card[0]}")
        self.getInputs()
        print(f"The next card is: {self.shuffler.card[1]}")
        print(f"Your score is: {self.points}")
        choice = input("Keep playing? [y/n] ")
        self.keep_playing = (choice == "y")
        pass
