import winsound

def klingel():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

def succes():
    #drehe Motor 
    klingel()


