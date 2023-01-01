import math
from sympy import *


def round_sig(x, sig=-1):
    if (sig == -1):
        return x
    if x == 0:
        return 0
    return float('%.*g' % (sig, x))

class secant():
    def __init__(self, equation, firstInitialGuess, secondInitialGuess, maxError = 0.0001, significantFigures = -1, nIterations = 50):
        self.equation = equation
        self.maxError = maxError
        self.firstInitialGuess = firstInitialGuess
        self.secondInitialGuess = secondInitialGuess
        self.significantFigures = significantFigures
        self.nIterations = nIterations

    def solve(self):
        #intitialize symbols for differntiation
        x = symbols('x')
        f = self.equation.replace("^", "**")
        f = lambdify(x, f)
        step = 1
        condition = True
        while condition:
            if f(self.firstInitialGuess) == f(self.secondInitialGuess):
                print('Divide by zero error!')
                break

            x2 = round_sig(self.firstInitialGuess - round_sig(round_sig(round_sig((self.secondInitialGuess - self.firstInitialGuess),self.significantFigures) * round_sig(f(self.firstInitialGuess),self.significantFigures),self.significantFigures) / round_sig(round_sig(f(self.secondInitialGuess),self.significantFigures) - round_sig(f(self.firstInitialGuess),self.significantFigures),self.significantFigures),self.significantFigures),self.significantFigures)
            print('Iteration-%d, x2 = %f and f(x2) = %f' % (step, x2, f(x2)))
            self.firstInitialGuess = self.secondInitialGuess
            self.secondInitialGuess = x2
            step = step + 1

            if step > self.nIterations:
                print('Not Convergent!')
                break

            condition = abs(f(x2)) > self.maxError
        print('\n Required root is: %f' % x2)

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: "+ str(x_new) + " current error: ", str(currentError))



