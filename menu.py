from tkinter import *
from tkinter import ttk

def menu():
    #setting up menu
    menu = Tk()
    menu.title("Gomoku")
    menuFrame = Frame(menu)

    #title
    titleText = StringVar()
    Label(menuFrame, textvariable = titleText).pack()
    titleText.set("Gomoku")

    #buttons inside menu
    singlePlayer = Button(menuFrame, text = "Single Player")
    singlePlayer.bind()
    twoPlayers = Button(menuFrame, text = "Two Players")
    quit = Button(menuFrame, text = "Quit")

    #set menu
    menuFrame.pack()

    menu.mainloop()

def boardSizeMenu():
    #setting up menu
    boardMenu = Tk()
    boardFrame = Frame(boardMenu)

    #title
    titleText = StringVar()
    Label(boardMenu, textvaraible = titleText).pack()
    titleText.set("Board Size")

    #checkboxes inside menu
    Radiobutton(boardMenu, text = "15 x 15", value = 1).pack()
    Radiobutton(boardMenu, text = "17 x 17", value = 2).pack()

    #set menu
    boardFrame.pack()

    boardMenu.mainloop()
