#handles games graphics, such as board and pieces
from Tkinter import *
from gamemechs import *
from numpy import full
from windowhelper import center

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
        x, y = center(pixels, self.gameWindow)
        self.gameWindow.geometry("%dx%d+%d+%d" % (pixels, pixels, x, y))
        self.canvasWidth = boardSize * self.squareSize
        self.canvasHeight = boardSize * self.squareSize

        #storing game data
        self.boardSize = boardSize
        self.boardGrid = full((self.boardSize, self.boardSize), 2)

        #create canvas
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
        if self.valid(boxX, boxY):
            topX = boxX * self.squareSize
            topY = boxY * self.squareSize
            botX = topX + self.squareSize
            botY = topY + self.squareSize
            if self.player == 0:
                self.canvas.create_oval(topX, topY, botX, botY, fill = "black")
            else:
                self.canvas.create_oval(topX, topY, botX, botY, fill = "white")
            self.boardGrid[boxX][boxY] = self.player
            self.checkWin(boxX, boxY)
            self.player = abs(self.player - 1)

    #see if piece placement is valid
    def valid(self, boxX, boxY):
        if self.boardGrid[boxX][boxY] == 2:
            return True
        else:
            return False

    #check win condition each time piece is played
    def checkWin(self, boxX, boxY):
        for dirX in range(-1, 2):
            for dirY in range(2):
                if dirX == 0 and dirY == 0:
                    continue
                if self.checkAdj(boxX, boxY, dirX, dirY):
                    self.winner()

    def checkAdj(self, boxX, boxY, dirX, dirY):
        while (self.validIndex(boxX, boxY) and self.boardGrid[boxX][boxY] == self.player):
            boxX += dirX
            boxY += dirY
        count = 0
        boxX -= dirX
        boxY -= dirY
        while (self.validIndex(boxX, boxY) and self.boardGrid[boxX][boxY] == self.player):
            count += 1
            boxX -= dirX
            boxY -= dirY
        if count >= 5:
            return True
        else:
            return False

    def validIndex(self, boxX, boxY):
        if boxX < self.boardSize and boxX >= 0 and boxY < self.boardSize and boxY >= 0:
            return True
        else:
            return False

    #declares winner and prompts user to restart, return to menu, or quit
    def winner(self):
        self.canvas.unbind("<Button-1>")
        self.winDow = Tk()
        pixels = 500
        x, y = center(pixels, self.winDow)
        self.winDow.geometry("%dx%d+%d+%d" % (pixels, pixels, x, y))
        self.winDow.title("WINNER!")

        #set frame
        winFrame = Frame(self.winDow, width = 100, height = 100)

        #declare winner
        Label(winFrame, text = "The winner is player " + str(self.player + 1) + "!").pack()

        #buttons inside winner menu
        Button(winFrame, text = "Restart", command = lambda: self.restart()).pack()
        Button(winFrame, text = "Main Menu", command = lambda: self.returnMain()).pack()
        Button(winFrame, text = "Quit").pack()

        winFrame.pack()

        self.winDow.mainloop()

    def restart(self):
        self.gameWindow.destroy()
        self.winDow.destroy()
        Board(self.boardSize)

    def returnMain(self):
        self.gameWindow.destroy()
        self.winDow.destroy()
