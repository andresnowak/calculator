#!/usr/bin/env python

from math import pow, sqrt

def Calculator():
    while True:
        number1 = float(input("\nnumber1: "))
        number2 = float(input("number2: "))
        operation = input("operation: ")

        if operation == "exit":
                exit()

        chooseOperation(operation, number1, number2)

def chooseOperation(operation, number1, number2):
        if operation == "+":
                result = Add(number1, number2)
                print("Result: {} + {} = {:.6}".format(number1, number2, result))
        elif operation == "-":
                result = Substract(number1, number2)
                print("Result: {} - {} = {:.6}".format(number1, number2, result))
        elif operation == "/":
                result = Divide(number1, number2)
                print("Result: {} / {} = {:.6}".format(number1, number2, result))
        elif operation == "*":
                result = Multiply(number1, number2)
                print("Result: {} * {} = {:.6}".format(number1, number2, result))
        elif operation == "|":
                result = SqrRoot(number1)
                print("Result: |{} = {:.6}".format(number1, result))
        elif operation == "^":
                result = Power(number1, number2)
                print("Result: {} ^ {} = {:.6}".format(number1, number2, result))
        
        continueOp = input("continue: ")
        
        if continueOp == ("y"):
                continueOperation(result)
        elif continueOp == ("n"):
                Calculator()


def continueOperation(result):
        while True:
                print("\nnumber1: {:.6}".format(result))
                operation = input("operation: ")

                if operation == "exit":
                        exit()

                number2 = float(input("number2: "))
                chooseOperation(operation, result, number2)

def Power(number1, number2):
        result = pow(number1,number2)
        return result

def Add(number1, number2):
        result = number1 + number2
        return result

def Substract(number1, number2):
        result = number1 - number2
        return result

def Multiply(number1, number2):
        result = number1 * number2
        return result

def Divide(number1, number2):
        result = number1 / number2
        return result

def SqrRoot(number1):
        result = sqrt(number1)
        return result

Calculator()     