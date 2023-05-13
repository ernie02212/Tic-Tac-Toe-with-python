import socket
import gameboard

def player2_Info():
    
    """Ask for the host name and IP address of player 2"""
    player2IP = str(input("Enter the Host name/IP address of player 2:"))
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
    #Create a socket object on the server
    p2ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p2Name = input("Enter player username:") 
    p2Host, p2Port = player2_Info()
    #Bind host with port number
    p2ServerSocket.bind((p2Host, p2Port))
    p2ServerSocket.listen(1)

    p1ClientSocket, p1ClientAddress = p2ServerSocket.accept()
    #Get the username of player 1
    #Decode username of player 1
    p1ClientData = p1ClientSocket.recv(1024)
    p1Name = p1ClientData.decode()

    #Encode username of player 2
    #Send
    p1ClientSocket.send(b"player2")

    p2Board = gameboard.BoardClass(p2Name)
    while True:
        print("Player 1's turn")
        p1PositionData = p1ClientSocket.recv(1024)
        p1Position = p1PositionData.decode()
        p2Board.updateGameBoard(p1Position, "player1")
        p2Board.getBoard()
        p2Board.lastTurn = p1Name
        if(p2Board.isWinner() == "o"): 
            p2Board.numWin += 1
            p2Board.updateGamesPlayed()
            p1DecisionData = p1ClientSocket.recv(1024)
            p1Decision = p1DecisionData.decode("ascii")
            if p1Decision == "Play Again":
                p2Board.resetGameBoard()
                continue
            elif p1Decision == "Fun Times":
                p2Board.printStats()
                exit()
        if(p2Board.isWinner() == "x"): 
            p2Board.numLoss += 1
            p2Board.updateGamesPlayed()
            p1DecisionData = p1ClientSocket.recv(1024)
            p1Decision = p1DecisionData.decode("ascii")
            if p1Decision == "Play Again":
                p2Board.resetGameBoard()
                continue
            elif p1Decision == "Fun Times":
                p2Board.printStats()
                exit()
        if(p2Board.isWinner() == "f" and p2Board.boardIsFull() == True): 
            p2Board.numTie += 1
            p2Board.updateGamesPlayed()
            p1DecisionData = p1ClientSocket.recv(1024)
            p1Decision = p1DecisionData.decode("ascii")
            if p1Decision == "Play Again":
                p2Board.resetGameBoard()
                continue
            elif p1Decision == "Fun Times":
                p2Board.printStats()
                exit()
        

        while True:
            print("Player 2's turn")
            p2Position = input("Enter two number(with comma) from 1 to 3(Example:1,2) to determine location of the board or press q/Q to quit:")
            if p2Position == "q":
                exit()
            if p2Board.updateGameBoard(p2Position,"player2") == False:
                continue
            else:
                p2PositionData = bytes(str(p2Position),"ascii")
                p1ClientSocket.send(p2PositionData)
                p2Board.getBoard()
                p2Board.lastTurn = p1Name
                if(p2Board.isWinner() == "o"): 
                    p2Board.numWin += 1
                    p2Board.updateGamesPlayed()
                    p1DecisionData = p1ClientSocket.recv(1024)
                    p1Decision = p1DecisionData.decode("ascii")
                    if p1Decision == "Play Again":
                        p2Board.resetGameBoard()
                        continue
                    elif p1Decision == "Fun Times":
                        p2Board.printStats()
                        exit()
                if(p2Board.isWinner() == "x"): 
                    p2Board.numLoss += 1
                    p2Board.updateGamesPlayed()
                    p1DecisionData = p1ClientSocket.recv(1024)
                    p1Decision = p1DecisionData.decode("ascii")
                    if p1Decision == "Play Again":
                        p2Board.resetGameBoard()
                        continue
                    elif p1Decision == "Fun Times":
                        p2Board.printStats()
                        exit()
                if(p2Board.isWinner() == "f" and p2Board.boardIsFull() == True): 
                    p2Board.numTie += 1
                    p2Board.updateGamesPlayed()
                    p1DecisionData = p1ClientSocket.recv(1024)
                    p1Decision = p1DecisionData.decode("ascii")
                    if p1Decision == "Play Again":
                        p2Board.resetGameBoard()
                        continue
                    elif p1Decision == "Fun Times":
                        p2Board.printStats()
                        exit()
                
            break
                            
       
       
    
   
    
    
