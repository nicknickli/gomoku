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
    Button(menuFrame, text = "Single Player", command = lambda: singlePlayer(menuWindow, menuFrame)).pack()
    twoPlayersButton = Button(menuFrame, text = "Two Players", command = lambda: twoPlayers(menuWindow, menuFrame)).pack()
    quitButton = Button(menuFrame, text = "Quit", command = lambda: quit(menuWindow)).pack()

    #set menu
    menuFrame.pack()

def quit(menuWindow):
    menuWindow.destroy()
