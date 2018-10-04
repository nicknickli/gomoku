#handles all menu interactions
from Tkinter import *
import ttk
from singleplayer import singlePlayer
from twoplayer import twoPlayers
from gameboard import startGame
from windowhelper import center

#runs the main menu
class mainMenu():

    def __init__(self):
        self.menuWindow = Tk()
        self.menuWindow.title("Gomoku")
        pixels = 500
        x, y = center(pixels, self.menuWindow)
        self.menuWindow.geometry("%dx%d+%d+%d" % (pixels, pixels, x, y))
        self.boardFrame = Frame(self.menuWindow)
        self.setup()

    def setup(self):
        self.boardFrame.pack_forget()

        #setting up menu
        self.menuFrame = Frame(self.menuWindow, width = 100, height = 100)

        #title
        titleText = StringVar()
        Label(self.menuFrame, textvariable = titleText).pack()
        titleText.set("Gomoku")

        #buttons inside menu
        Button(self.menuFrame, text = "Single Player", command = lambda: self.boardSizeMenu(1)).pack()
        Button(self.menuFrame, text = "Two Players", command = lambda: self.boardSizeMenu(2)).pack()
        Button(self.menuFrame, text = "Quit", command = lambda: self.quit()).pack()

        #set menu
        self.menuFrame.pack()

        self.menuWindow.mainloop()

    #quits window
    def quit(self):
        self.menuWindow.destroy()

    #runs the board size options
    def boardSizeMenu(self, playerNum):
        self.menuFrame.pack_forget()
        self.boardFrame.pack_forget()

        self.playerNum = playerNum

        #setting up menu
        self.boardFrame = Frame(self.menuWindow, width = 100, height = 100)

        #title
        titleText = StringVar()
        Label(self.boardFrame, textvariable = titleText).pack()
        titleText.set("Select a board size")

        #buttons inside menu
        board = IntVar()
        boardSmall = Radiobutton(self.boardFrame, text = "15 x 15", variable = board, value = 1)
        boardLarge = Radiobutton(self.boardFrame, text = "17 x 17", variable = board, value = 2)
        Button(self.boardFrame, text = "Confirm", command = lambda: self.boardSize(board.get())).pack()
        Button(self.boardFrame, text = "Back", command = lambda: self.setup()).pack()
        #CAUTION: Can possibly overload menu window with lots of frames

        #set menu
        boardSmall.pack()
        boardLarge.pack()
        self.boardFrame.pack()

    #starts the game using board size user selected
    def boardSize(self, value):
        if value == 1:
            startGame(self.playerNum, 15, self.menuWindow)
        elif value == 2:
            startGame(self.playerNum, 17, self.menuWindow)
        else:
            self.boardSizeMenu(self.playerNum)
