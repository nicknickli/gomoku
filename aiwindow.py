from Tkinter import *
import ttk
from windowhelper import offcenter

class AISimulation():

    def __init__(self):
        self.infoWindow = Tk()
        self.infoWindow.title("AI Information")
        pixelsX = 250
        pixelsY = 150
        x, y = offcenter(pixelsX, pixelsY, self.infoWindow)
        self.infoWindow.geometry("%dx%d+%d+%d" % (pixelsX, pixelsY, x, y))
        self.infoFrame = Frame(self.infoWindow)

        #read variables from file
        data = open("AIdata.txt", "r")
        weights = []

        for line in data:
            weights += [line.partition(" ")]

        weights = [x[0] for x in weights]

        print weights


        titleText = StringVar()
        label = Label(self.infoFrame, textvariable = titleText, font = "TKTEXTFONT 20", anchor = CENTER)
        titleText.set("Fitness")



    def update(self):
        return
