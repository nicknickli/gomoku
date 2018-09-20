#handles games graphics, such as board and pieces
from Tkinter import *
from gamemechs import *

class Board():
    player = 0
    squareSize = 32
    canvasWidth = 480
    canvasHeight = 480

    def __init__(self, boardSize):
        #creating new game window
        self.gameWindow = Tk()
        self.gameWindow.title("Gomoku")
        if boardSize == 15:
            pixels = 480
        else:
            pixels = 544
        self.gameWindow.geometry(str(pixels) + "x" + str(pixels))
        self.canvasWidth = boardSize * self.squareSize
        self.canvasHeight = boardSize * self.squareSize
        self.data = GameMechs(boardSize)

        self.canvas = Canvas(self.gameWindow, width = self.canvasWidth, height = self.canvasHeight, bg = "PeachPuff2")
        for i in range(boardSize + 1):
            #have to make sure lines are halves so that each intersection is within box
            self.canvas.create_line(i * self.squareSize - self.squareSize / 2, self.squareSize / 2, i * self.squareSize - self.squareSize / 2, self.canvasHeight - self.squareSize / 2)
            self.canvas.create_line(self.squareSize / 2, i * self.squareSize - self.squareSize / 2, self.canvasWidth - self.squareSize / 2, i * self.squareSize - self.squareSize / 2)

        self.canvas.bind("<Button-1>", lambda event: self.click(event))

        self.canvas.pack(side = "top", fill = "both", expand = True)

        self.gameWindow.mainloop()

    def click(self, event):
        boxX = self.pixelsToBoxes(event.x)
        boxY = self.pixelsToBoxes(event.y)
        self.placePiece(boxX, boxY)

    def pixelsToBoxes(self, pixel):
        return pixel // self.squareSize

    def placePiece(self, boxX, boxY):
        if self.data.valid(boxX, boxY):
            topX = boxX * self.squareSize
            topY = boxY * self.squareSize
            botX = topX + self.squareSize
            botY = topY + self.squareSize
            if self.player == 0:
                self.canvas.create_oval(topX, topY, botX, botY, fill = "black")
            else:
                self.canvas.create_oval(topX, topY, botX, botY, fill = "white")
            self.data.boardGrid[boxX][boxY] = self.player
            self.data.checkWin(boxX, boxY, self.player)
            self.player = abs(self.player - 1)
