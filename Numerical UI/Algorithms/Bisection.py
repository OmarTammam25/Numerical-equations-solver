import math
from sympy import *


def round_sig(x, sig=-1):
    # x=float(x)
    if (sig == -1):
        return x
    if x == 0:
        return 0
    return float('%.*g' % (sig, x))

class Bisection():
    def __init__(self, equation, x_lower, x_upper,  maxError = 0.0001, significantFigures = -1, nIterations = 50) :
        self.equ = equation
        self.xl = float(x_lower)
        self.xu = float(x_upper)
        self.maxError = float(maxError)
        self.sig = int(significantFigures)
        self.nIterations = int(nIterations)

    def solve(self):
        #intitialize symbols for differntiation
        x = symbols('x')
        f = self.equ.replace("^", "**")
        f = lambdify(x, f)
        oldx = 0
        current_iterations: number = 0
        while current_iterations < self.nIterations:
            current_iterations += 1
            mid = round_sig(round_sig(self.xl + self.xu,self.sig) / 2.0,self.sig)
            f_x_lower = round_sig(f(self.xl),self.sig)
            f_x_mid = round_sig(f(mid),self.sig)
            try:
                currentError = abs((mid - oldx) / mid) * 100
            except:
                currentError = 10000000


            oldx = mid
            if f_x_lower * f_x_mid < 0:
                self.xu = mid
            else:
                self.xl = mid
            print(current_iterations, mid, currentError)
        return self.xl

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: "+ str(x_new) + " current error: ", str(currentError))



