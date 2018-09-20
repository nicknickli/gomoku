#handles main menu
from Tkinter import *
import ttk
from singleplayer import singlePlayer
from twoplayer import twoPlayers

def mainMenu(menuWindow, oldFrame = 0):
    #clear old frame
    if oldFrame != 0:
        oldFrame.pack_forget()

    #setting up menu
    menuFrame = Frame(menuWindow, width = 100, height = 100)

    #title
    titleText = StringVar()
    Label(menuFrame, textvariable = titleText).pack()
    titleText.set("Gomoku")

    #buttons inside menu
    Button(menuFrame, text = "Single Player", command = lambda: boardSizeMenu(menuWindow, menuFrame, 1)).pack()
    twoPlayersButton = Button(menuFrame, text = "Two Players", command = lambda: boardSizeMenu(menuWindow, menuFrame, 2)).pack()
    quitButton = Button(menuFrame, text = "Quit", command = lambda: quit(menuWindow)).pack()

    #set menu
    menuFrame.pack()

def quit(menuWindow):
    menuWindow.destroy()

def boardSizeMenu(menuWindow, oldFrame, playerNum):
    #clearing old menu frame
    if oldFrame != 0:
        oldFrame.pack_forget()

    #setting up menu
    boardFrame = Frame(menuWindow, width = 100, height = 100)

    #title
    titleText = StringVar()
    Label(boardFrame, textvariable = titleText).pack()
    titleText.set("Select a board size")

    #buttons inside menu
    board = IntVar()
    boardSmall = Radiobutton(boardFrame, text = "15 x 15", variable = board, value = 1)
    boardLarge = Radiobutton(boardFrame, text = "17 x 17", variable = board, value = 2)
    Button(boardFrame, text = "Confirm", command = lambda: boardSize(board.get(), menuWindow, boardFrame, playerNum)).pack()
    Button(boardFrame, text = "Back", command = lambda: mainMenu(menuWindow, boardFrame)).pack()
    #CAUTION: Can possibly overload menu window with lots of frames

    #set menu
    boardSmall.pack()
    boardLarge.pack()
    boardFrame.pack()

def boardSize(value, menuWindow, boardFrame, playerNum):
    if value == 1:
        startGame(playerNum, 15)
    elif value == 2:
        startGame(playerNum, 17)
    else:
        boardSizeMenu(menuWindow, boardFrame)
