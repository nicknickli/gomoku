#handles game mechanics functions
from numpy import full
from Tkinter import *
import ttk

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

    #check win condition each time piece is played
    def checkWin(self, boxX, boxY, player, canvas):
        for dirX in range(-1, 2):
            for dirY in range(-1, 2):
                if dirX == 0 and dirY == 0:
                    continue
                if self.checkAdj(boxX, boxY, dirX, dirY, player, 1):
                    self.winner(player, canvas)

    def checkAdj(self, boxX, boxY, dirX, dirY, player, count):
        newboxX = boxX + dirX
        newboxY = boxY + dirY
        if count == 5:
            return True
        elif self.boardGrid[newboxX][newboxY] == player and self.validIndex(newboxX, newboxY):
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
        canvas.unbind("<Button-1>")
        winDow = Tk()
        winDow.geometry("500x500")
        winDow.title("WINNER!")

        #set frame
        winFrame = Frame(winDow, width = 100, height = 100)

        #declare winner
        Label(winFrame, text = "The winner is player " + str(player + 1) + "!").pack()

        #buttons inside winner menu
        Button(winFrame, text = "Restart", command = lambda: restart).pack()
        Button(winFrame, text = "Main Menu").pack()
        Button(winFrame, text = "Quit").pack()

        winFrame.pack()

        winDow.mainloop()
