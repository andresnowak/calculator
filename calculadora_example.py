#!/usr/bin/env python

from calculadora_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_Form): #Ui_Form name of the class in calculadora_ui.py
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.lcdNumber.display(10)
        self.lcdNumber.repaint() #repaint added for what it seems a problem in MacOs, it seems windows and mac have different solutions

        self.number_1.clicked.connect(self.result)

    def result(self):
        self.lcdNumber.display(1)



if __name__ == "__main__": #you need double down lines __
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
