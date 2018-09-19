#handles main menu
from Tkinter import *
import ttk
from singleplayer import singlePlayer
from twoplayer import twoPlayers

def menu(menuWindow):
    #setting up menu
    menuWindow.title("Gomoku")
    menuFrame = Frame(menuWindow, width = 100, height = 100)

    #title
    titleText = StringVar()
    Label(menuFrame, textvariable = titleText).pack()
    titleText.set("Gomoku")

    #buttons inside menu
    singlePlayerButton = Button(menuFrame, text = "Single Player")
    singlePlayerButton.bind("<Button-1>", lambda event: singlePlayer(event, menuWindow))
    twoPlayersButton = Button(menuFrame, text = "Two Players")
    twoPlayersButton.bind("<Button-1>", lambda event: twoPlayers(event, menuWindow))
    quitButton = Button(menuFrame, text = "Quit")
    quitButton.bind("<Button-1>", lambda event: quit(event, menuWindow))

    #set menu
    singlePlayerButton.pack()
    twoPlayersButton.pack()
    quitButton.pack()
    menuFrame.pack()

    menuWindow.mainloop()

def quit(event, menuWindow):
    menuWindow.destroy()
