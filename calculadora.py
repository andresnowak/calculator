#!/usr/bin/env python

from math import pow, sqrt
from calculadora_ui import *

# Ui_Form name of the class in calculadora_ui.py
class MainWindow(QtWidgets.QMainWindow, Ui_Form):
        def __init__ (self, *args, **kwargs):
                QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
                self.setupUi(self)

                self.label.setText("0")

                self.number = 0

                self.operation = ""

                self.number_0.clicked.connect(self.digit_pressed)
                self.number_1.clicked.connect(self.digit_pressed)
                self.number_2.clicked.connect(self.digit_pressed)
                self.number_3.clicked.connect(self.digit_pressed)
                self.number_4.clicked.connect(self.digit_pressed)
                self.number_5.clicked.connect(self.digit_pressed)
                self.number_6.clicked.connect(self.digit_pressed)
                self.number_7.clicked.connect(self.digit_pressed)
                self.number_8.clicked.connect(self.digit_pressed)
                self.number_9.clicked.connect(self.digit_pressed)

                self.decimal.clicked.connect(self.decimal_pressed)

                self.C.clicked.connect(self.erase)

                self.sum.clicked.connect(self.chooseOperation)
                self.minus.clicked.connect(self.chooseOperation)
                self.multiplication.clicked.connect(self.chooseOperation)
                self.division.clicked.connect(self.chooseOperation)
                self.power.clicked.connect(self.chooseOperation)
                self.squareRoot.clicked.connect(self.SqrRoot)
                self.equal.clicked.connect(self.chooseOperation)

        def digit_pressed(self):
                button = self.sender()

                newLabel = format(float(self.label.text() + button.text()), ".15g")

                self.label.setText(newLabel)

        def decimal_pressed(self):
                newLabel = self.label.text()
                if newLabel.find(".") == True:
                        pass
                else:
                        self.label.setText(self.label.text() + ".")

        def erase(self):
                self.label.setText("0")
                self.number = 0
                self.operation = ""

        def chooseOperation(self):
                button = self.sender()
                labelNumber = float(self.label.text())
                #how to do the operations
                if self.operation == "+":
                        self.number = self.Add(self.number, labelNumber)
                        self.operation = button.text()
                        self.label.setText(format(self.number, ".15g"))
                elif self.operation == "-":
                        self.number = self.Substract(self.number, labelNumber)
                        self.operation = button.text()
                        self.label.setText(format(self.number, ".15g"))
                elif self.operation == "÷":
                        self.label.setText("0")
                        self.number = self.Divide(self.number, labelNumber)
                        self.operation = button.text()
                        self.label.setText(format(self.number, ".15g"))
                elif self.operation == "X":
                        self.number = self.Multiply(self.number, labelNumber)
                        self.operation = button.text()
                        self.label.setText(format(self.number, ".15g"))
                elif self.operation == "^":
                        self.number = self.Power(self.number, labelNumber)
                        self.operation = button.text()
                        self.label.setText(format(self.number, ".15g"))                   
                else:
                        self.operation = button.text()
                        self.number = labelNumber
                        self.label.setText("0")
                
        def evaluate(self):
                self.operation = ""
                self.label.setText(format(self.number, ".15g"))           
        
        def Power(self, number1, number2):
                result = pow(number1,number2)
                return result
        
        def Add(self, number1, number2):
                result = number1 + number2
                return result
        
        def Substract(self, number1, number2):
                result = number1 - number2
                return result
        
        def Multiply(self, number1, number2):
                result = number1 * number2
                return result
        
        def Divide(self, number1, number2):
                result = number1 / number2
                return result
        
        def SqrRoot(self):
                self.number = sqrt(self.number)
                self.label.setText(format(self.number, ".15g"))

if __name__ == "__main__":  # you need double down lines __
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec()
