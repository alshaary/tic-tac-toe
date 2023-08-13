import math
import random

class Player:
    def __init__(self, letter):
        # Letter is etheir x or o
        self.letter = letter
    
    # We want to move the players to get their next move given a game
    def getMove(self, game):
        pass

class RandomComputerplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # We're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we sat its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                valid_square = True # If these are seccessful, then fine.
            except ValueError:
                print("Invalid suare. try again")
        return val