#handles board size
from numpy import zeros
from Tkinter import *
import ttk
import menu

def boardSizeMenu(menuWindow, oldFrame):
    #clearing old menu frame
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
    Button(boardFrame, text = "Confirm", command = lambda: boardSize(board.get(), menuWindow, boardFrame)).pack()
    Button(boardFrame, text = "Back", command = lambda: menu.mainMenu(menuWindow, boardFrame)).pack()
    #CAUTION: Can possibly overload menu window with lots of frames

    #set menu
    boardSmall.pack()
    boardLarge.pack()
    boardFrame.pack()

def boardSize(value, menuWindow, boardFrame):
    if value == 1:
        return numpy.zeros(15, 15) #this doesn't get saved, i need to start the game with another function
    elif value == 2:
        return numpy.zeros(17, 17)
    else:
        boardSizeMenu(menuWindow, boardFrame)
