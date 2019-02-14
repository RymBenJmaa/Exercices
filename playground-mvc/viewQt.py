import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLCDNumber, QPushButton)
from PyQt5.QtWidgets import QApplication


class MyView(QWidget):
    def __init__(self, windowTitle, posX, posY, sizeX, sizeY):
        self.app = QApplication(sys.argv)
        super().__init__()
        print("MyView::__init__(windowTitle, posX, posY, sizeX, sizeY)")
        self.setGeometry(posX, posY, sizeX, sizeY)
        self.setWindowTitle(windowTitle)
	#setting up the Vertical Layout
        self.control_layout = QVBoxLayout()
        self.setLayout(self.control_layout)
	#setting up the button widget
        self.button = QPushButton()
        self.button.setFixedSize(40, 40)
        self.button.setText("+")
        self.button.clicked.connect(self.buttonClicked)
	#setting up the Counter widget 
        self.timer = QLCDNumber()
        self.timer.setNumDigits(4)
        self.timer.setStyleSheet("QLCDNumber {color: pink;}")
        self.timer.setFixedWidth(400)
        #self.timer.display(self.getVal())
        self.control_layout.addWidget(self.timer)
        self.control_layout.addWidget(self.button)
        self.show()
    def getVal(self,val):
        self.timer.display(val)
    def keyPressEvent(self, e):
        if e.key():
            print("Key +1")
            return "a"
    def buttonClicked(self):
        print("Button +1")
        return True
    def run(self):
        sys.exit(self.app.exec_())

