"""Director Class"""
from game.shuffler import Shuffler

class Director:
    """
    Code that directs the game. Keeps track of score and controls sequence of play.

    Attributes:
        shuffler (Shuffler): An instance of the Shuffler Class
        keep_playing (bool): Whether the player chooses to continue or loses the game
        points (number): Total points earned
    """

    def __init__(self):
        """Constructor
        
        Args:
            self : an instance of Director
        """
        self.shuffler = Shuffler()
        self.keep_playing = True
        self.points = 300
        

    
    def startGame(self):
        """Makes a loop to make sure that the game keeps playing as long as there are 
            enough points and the player still wants to play
        
        Args:
            self : an instance of Director
            """
        while self.keep_playing:
            self.doOutputs()


    def getInputs(self):
        """Gets inputs during play and runs doUpdate function
        
        Args:
            Args:
            self : an instance of Director
        """
        choice = "q"
        while choice.lower() not in ["h","l"]:
            choice = input("Higher or Lower? [h/l] ")
        self.doUpdates(choice)
        pass

    def doUpdates(self, choice):
        """Updates Score 
        
        Args:
            self : an instance of Director
            choice (char): the user input for higher or lower
        """
        if ((not self.shuffler.getScore() and choice == "h") or (self.shuffler.getScore() and choice == "l")) and not (self.shuffler.card[0] == self.shuffler.card[1]):
            self.points = 100 + self.points
            
        else:
            self.points = self.points - 75
            
        pass

    def doOutputs(self):
        """Outputs game information for each round. Calls input function. Displays cards and score. (¬‿ ¬)
        
        Args:
            self : an instance of Director
        """
        self.shuffler.getCard()
        print(f"The card is: {self.shuffler.card[0]}")
        self.getInputs()
        print(f"The next card is: {self.shuffler.card[1]}")
        print(f"Your score is: {self.points}")
        if (self.shuffler.canPlay(self.points)):
            choice = "q"
            while choice.lower() not in ["y","n"]:
                choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
            if choice != "n":
                print()
        else:
            self.keep_playing = False
        
        pass
