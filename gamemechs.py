#handles game mechanics functions
from numpy import full

class GameMechs():

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.boardGrid = full((self.boardSize, self.boardSize), 2)

    #see if piece placement is valid
    def valid(self, boxX, boxY):
        if self.boardGrid[boxX][boxY] == 2:
            return True
        else:
            return False

    #take in a player input and places the piece on the board accordingly
    def takeTurn(player, input, board):
        #auto switch player by returning player? or returning input
        return 0

    #places piece according to player input
    def placePiece(player, input, board):
        return 0

    #check win condition each time piece is played
    def checkWin(self, boxX, boxY, player):
        for dirX in range(-1, 2):
            for dirY in range(-1, 2):
                if dirX == 0 and dirY == 0:
                    continue
                if self.checkAdj(boxX, boxY, dirX, dirY, player, 1):
                    self.winner(player)

    def checkAdj(self, boxX, boxY, dirX, dirY, player, count):
        newboxX = boxX + dirX
        newboxY = boxY + dirY
        if count == 5:
            return True
        elif self.boardGrid[newboxX][newboxY] == player and self.validIndex(newboxX, newboxY):
            print(count)
            return self.checkAdj(newboxX, newboxY, dirX, dirY, player, count + 1)
        else:
            return False

    def validIndex(self, boxX, boxY):
        if boxX < self.boardSize and boxX >= 0 and boxY < self.boardSize and boxY >= 0:
            return True
        else:
            return False

    #declares winner and prompts user to restart, return to menu, or quit
    def winner(self, player):
        return player
