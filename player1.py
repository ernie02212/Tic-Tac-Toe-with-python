import socket
import gameboard
def player2_Info():
    
    """Ask for the host name and IP address of player 2"""
    
    player2IP = str(input("Enter the IP address of player 2:"))
    portNum = int(input("Enter the port number:"))
    return player2IP, portNum
"""
Using that information they will attempt to connect to player 2
Upon successful connection they will send player 2 the their user name 
If the connection cannot be made then the user will be asked if they want to try again:
If the user enters 'y' then you will request the host information from the user again
If the user enters 'n' then you will end the program

"""

if __name__ == "__main__":
    p1UserName = input("Enter player username:")
    p1Board = gameboard.BoardClass(p1UserName)
    p2ServerAddress, p2ServerPort = player2_Info()
    p1ConnectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        p1ConnectionSocket.connect((p2ServerAddress, p2ServerPort))
        p1UserNameData = bytes(str(p1UserName),"ascii")
        p1ConnectionSocket.send(p1UserNameData)
        
        p2UserNameData = p1ConnectionSocket.recv(1024)
        p2UserName = p2UserNameData.decode("ascii")
        while True:
            print("Player 1's turn")
            p1Position = input("Enter two number(with comma) from 1 to 3(Example:1,2) to determine location of the board or press q/Q to quit:")
            if p1Position == "q":
                exit()
            if p1Board.updateGameBoard(p1Position,"player1") == False:
                continue
            else:
                p1PositionData = bytes(str(p1Position), "ascii")
                p1ConnectionSocket.send(p1PositionData)
                p1Board.getBoard()
                p1Board.lastTurn = p1UserName
                # every false + 1
                if (p1Board.isWinner() == "x"):
                    p1Board.numWin += 1
                    p1Board.updateGamesPlayed()
                    # end of game
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                        continue
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()
                if (p1Board.isWinner() == "o"):
                    p1Board.numLoss += 1
                    p1Board.updateGamesPlayed()
                    # end of game
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                        continue
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()
                if (p1Board.isWinner() == "f" and p1Board.boardIsFull() == True):
                    p1Board.numTie += 1
                    p1Board.updateGamesPlayed()
                    # end of game
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                        continue
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()

                print("Player 2's turn")
                p2PositionData = p1ConnectionSocket.recv(1024)
                p2Position = p2PositionData.decode('ascii')
                p1Board.updateGameBoard(p2Position,"player2")
                p1Board.getBoard()
  
                p1Board.lastTurn = p2UserName
                if (p1Board.isWinner() == "x"):
                    p1Board.numWin += 1
                    # end of game
                    p1Board.updateGamesPlayed()
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                        continue
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()
                if (p1Board.isWinner() == "o"):
                    p1Board.numLoss += 1
                    # end of game
                    p1Board.updateGamesPlayed()
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                        continue
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()
                if (p1Board.isWinner() == "f" and p1Board.boardIsFull() == True):
                    self.numTie += 1
                    # end of game
                    p1Board.updateGamesPlayed()
                    playAgain = input("Enter y/Y for rematch or n/N to not.")
                    if playAgain == "y" or playAgain == "Y":
                        p1ConnectionSocket.send(b'Play Again')
                        p1Board.resetGameBoard()
                    elif playAgain == "n" or playAgain == "N":
                        p1ConnectionSocket.send(b'Fun Times')
                        p1Board.printStats()
                        exit()
                           
    except Exception:
        reconnectDecision = input("Try reconnecting to player 2 again?(y/n)\n")
        if reconnectDecision == "n" or reconnectDecision == "N":
            print("Thank you for playing!")
            exit()
        elif reconnectDecision == "y" or reconnectDecision == "Y":
            break
        continue

        
        


    
