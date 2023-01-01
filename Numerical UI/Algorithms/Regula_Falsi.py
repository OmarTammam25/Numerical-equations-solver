import math
from sympy import *


def round_sig(x, sig=-1):
    if (sig == -1):
        return x
    if x == 0:
        return 0
    return float('%.*g' % (sig, x))

class Regula_Falsi():
    def __init__(self, equation, x_lower, x_upper,  maxError = 0.0001, significantFigures = -1, nIterations = 50) :
        self.equ = equation
        self.xl = x_lower
        self.xu = x_upper
        self.maxError = maxError
        self.sig = significantFigures
        self.nIterations = nIterations

    def solve(self):
        #intitialize symbols for differntiation
        x = symbols('x')
        f = self.equation.replace("^", "**")
        f = lambdify(x, f)
        oldx = 0
        current_iterations: number = 0
        while current_iterations < self.nIterations:
            current_iterations += 1
            xr = round_sig(round_sig((round_sig(self.xl*self.xu,self.sig) - round_sig(self.xu*self.xl,self.sig),self.sig),self.sig) / round_sig((round_sig(f(self.xu),self.sig) - round_sig(f(self.xl),self.sig),self.sig),self.sig),self.sig)
            f_x_lower = round_sig(f(self.xl),self.sig)
            f_x_mid = round_sig(f(mid),self.sig)
            currentError = abs((mid - oldx) / mid) * 100
            if f_x_lower * f_x_mid < 0:
                self.xu = mid
            else:
                self.xl = mid
            print(current_iterations, mid, currentError)
        return self.xl

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: "+ str(x_new) + " current error: ", str(currentError))



