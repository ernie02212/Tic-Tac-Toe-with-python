class BoardClass:
    """ A class that store and handle information about player1 and player2.

    Attributes:
        playerName(str): Players user name
        lastPlayer(str): User name of the last player to have a turn
        numWin(int): Number of wins
        numTie(int): Number of ties
        numLoss(int): Number of losses
    """
    def __init__(self, playerName: str = "", lastTurn : str = "", numWin: int = 0, numTie:int = 0, numLoss:int = 0,gamesPlayed:int = 0)-> None:
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.playerName = playerName
        self.lastTurn = lastTurn
        self.numWin= numWin
        self.numTie = numTie
        self.numLoss = numLoss
        self.gamesPlayed = gamesPlayed

    def updateGamesPlayed(self):
        """Keeps track of how many games have started."""
        self.gamesPlayed = self.gamesPlayed + 1
        return self.gamesPlayed   

    def resetGameBoard(self):
        """Clear all the move from game board."""
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        return self.board 

    def updateGameBoard(self, position, player = ""):
        """Updates the game board with the player's move."""
        if player == "player2":
            mark = "o"
        else:
            mark = "x"
        coord = position.split(",")
        r = ["x","o"]
        x = int(coord[0])-1
        y = int(coord[1])-1
        if x not in range(0,3) or y not in range(0,3):
            print("Coordinate out of range")
            return False
        
        if self.board[x][y] in r:
            print("Coordinate taken!")
            return False
        else:
            self.board[x][y] = mark
        return self.board     
    
    def isWinner(self):
        # determines true or false
        """Checks if the latest move resulted in a win.

        Updates the wins and losses count.
        """
        """
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 'x' or   # rows
            numWin += 1
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'x':
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'x':
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'x':  # columns
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'x':
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'x':
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'x':  # diagonals
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'x':
            return True
        else:
            return False
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 'o':  # rows
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'o':
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'o':
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'o':  # columns
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'o':
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'o':
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'o':  # diagonals
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'o':
            return True
        else:
            return False
        """

            
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] == 'x'
            or self.board[1][0] == self.board[1][1] == self.board[1][2] == 'x'
            or self.board[2][0] == self.board[2][1] == self.board[2][2] == 'x'
            or self.board[0][0] == self.board[1][0] == self.board[2][0] == 'x'  # columns
            or self.board[0][1] == self.board[1][1] == self.board[2][1] == 'x'
            or self.board[0][2] == self.board[1][2] == self.board[2][2] == 'x'
            or self.board[0][0] == self.board[1][1] == self.board[2][2] == 'x'  # diagonals
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'x'):
            winnerMark="x"
            return winnerMark
  
        elif(self.board[0][0] == self.board[0][1] == self.board[0][2] == 'o'
            or self.board[1][0] == self.board[1][1] == self.board[1][2] == 'o'
            or self.board[2][0] == self.board[2][1] == self.board[2][2] == 'o'
            or self.board[0][0] == self.board[1][0] == self.board[2][0] == 'o'  # columns
            or self.board[0][1] == self.board[1][1] == self.board[2][1] == 'o'
            or self.board[0][2] == self.board[1][2] == self.board[2][2] == 'o'
            or self.board[0][0] == self.board[1][1] == self.board[2][2] == 'o'  # diagonals
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'o'):
            winnerMark = "o"
            return winnerMark
        else:
            winnerMark = "f"
            return winnerMark
        """    
        if winnerMark = "x" or winnermark = "o": 
            self.numwin += 1
        if loserMark = "o" or losermark = "x":
            self.numLoss += 1
        """

    def boardIsFull(self)-> bool:
        """Check if the board is full(I.e. no more moves to make - tie).

        Updates the ties count.
        """
        boardfull = True
        for row in self.board:
            for element in row:
                if element == "":
                    boardfull = False
        if boardfull:
            self.numTie += 1
        return boardfull
    
    def printStats(self):
        """
        Prints the players user name
        Prints the user name of the last person to make a move
        prints the number of games
        Prints the number of wins
        Prints the number of losses
        Prints the number of ties
        """
        return print("Players user name:{}\n"\
               "User name of last person to make a move:{}\n"\
               "Number of games:{}\n"\
               "Number of wins :{}\n"\
               "Number of losses:{}\n"\
               "Number of ties:{}\n".format(self.playerName, self.lastTurn,
                self.gamesPlayed, self.numWin, self.numLoss, self.numTie))
    def getBoard(self):
        return(print(f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}\n{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}\n{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}'))
                    

