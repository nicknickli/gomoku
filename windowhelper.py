def center(pixelsX, pixelsY, window):
    screenWidth, screenHeight = getscreen(pixelsX, pixelsY, window)
    x = (screenWidth / 2) - (pixelsX / 2)
    y = (screenHeight / 2) - (pixelsY / 2)
    return x, y

def offcenter(pixelsX, pixelsY, window):
    screenWidth, screenHeight = getscreen(pixelsX, pixelsY, window)
    x = (screenWidth / 2) - (pixelsX / 2) - pixelsX
    y = (screenHeight /2) - (pixelsY / 2)
    return x, y

def getscreen(pixelsX, pixelsY, window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    return screenWidth, screenHeight
