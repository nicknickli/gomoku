#handles board size
from numpy import zeros
from Tkinter import *
import ttk

def boardSizeMenu(menuWindow):
    #setting up menu
    boardFrame = Frame(menuWindow, width = 100, height = 100)
    boardFrame.tkraise()

    #title
    titleText = StringVar()
    Label(boardFrame, textvariable = titleText).pack()
    titleText.set("Board Size")

    #buttons inside menu
    board = StringVar()
    boardSmall = Radiobutton(boardFrame, text = "15 x 15", value = 1, variable = board)
    boardLarge = Radiobutton(boardFrame, text = "17 x 17", value = 2, variable = board)
    confirmButton = Button(boardFrame, text = "Confirm")
    confirmButton.bind("<Button-1>", lambda x: boardSize(event, board.get()))
    backButton = Button(boardFrame, text = "Back")
    #CAUTION: Can possibly overload menu window with lots of frames
    backButton.bind("<Button-1>", lambda x: menu(menuWindow))

    #set menu
    boardSmall.pack()
    boardLarge.pack()
    boardFrame.pack()

def boardSize(event, value):
    if value == 1:
        return numpy.zeros(15, 15)
    elif value == 2:
        return numpy.zeros(17, 17)
    else:
        print("Please select a board size")
        boardSizeMenu()
