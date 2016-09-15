from lib import math_cal
import os
import sys


if __name__ == "__main__":
    calculator = math_cal.MathExpressionsCal()
    print("********************\npyCalculator ver 0.1\n********************")
    while True:
        expressions = input("")
        if expressions == "exit":
            sys.exit(0)
        elif expressions == "clear":
            os.system('cls')
        else:
            calculator.execute_it(expressions)
            print('*'*8)
