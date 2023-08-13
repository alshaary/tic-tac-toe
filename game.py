import time 
from player import HumanPlayer , RandomComputerplayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3x3 board
        self.current_winner = None  # Keep track winner

    def printBoard(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row)+ ' |')

    @staticmethod
    def PrintBoardNums():
        # 0 | 1 | 2 etc (tells us what number correspounds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+ ' |')

    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ' ]
    #-------------------Another solution--------------------------------
    #    moves = []
    #   for (i, spot) in  enumerate(self,self.board):
    #       # ["X", "X", "O"] -> [(0, X), (1,X), (2,O)]
    #       if spot == ' ':
    #           moves.append
    #   return moves
    #----------------------------------------------------
    
    def emptySquares(self):
        return ' ' in self.board
    
    def NumEmptysquares(self):
        return self.board.count(' ')
    
    def makeMove(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return Ture. if invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check of these
        
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # check diagonals
        # but only if the square is an even number [0, 2, 4, 6, 8]
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all checks fail 
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winnner of the game!(the letter) or none for a tie
    if print_game:
        game.PrintBoardNums()
        
    letter = 'X' # Starting letter
    # Iterate while the game still has empty suares
    # We don't have to worry about winner because we'll just that
    # which breaks the loop
    # after we made our move, we need to alternate letters

    while game.emptySquares():
        # get the move from the apporopriate player
        if letter == 'O':
            square = o_player.getMove(game)
        else:
            square = x_player.getMove(game)

        if game.makeMove(square, letter):
            
            if print_game:
                print(letter + 'makes a move to square {}' .format(square))
                game.printBoard()
                print('') # just a line
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            
        letter = 'O' if letter == 'X' else 'X' # Switches Plyaer
        # if letter == 'X':
        #   letter = 'O'
        # else:
        #   letter ='X'

        # tiny break 
        time.sleep(0.8)
        
    if print_game:
        print('it\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerplayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)