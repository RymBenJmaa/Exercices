from PyQt5.QtCore import Qt
class MyView():
    def __init__(self, windowTitle, posX, posY, sizeX, sizeY):
        print("MyView::__init__(windowTitle, posX, posY, sizeX, sizeY)")
        self.printWindowTitle(windowTitle)

    def printWindowTitle(self, title):
        nb = 20
        print("#" * nb)
        print("#", "\033[1m", title, "\033[0;0m", "#")
        print("#" * nb)

    def getChar(self):
      import sys, tty, termios
      old_settings = termios.tcgetattr(0)
      new_settings = old_settings[:]
      new_settings[3] &= ~termios.ICANON
      try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
      finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
      return ch
    def getVal(self,val):
        print("shell click")
        print(val)
    def keyPressEvent(self, e):
        e = self.getChar()
        print(e)
        print("key")
    def buttonClicked(self):
        print("Button +1")
        return True
    def run(self):
        while(1):
            e = self.getChar()
