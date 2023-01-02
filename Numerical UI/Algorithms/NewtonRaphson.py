import math

from sympy import *


def round_sig(x, sig=-1):
    if (sig == -1):
        return x
    if x == 0:
        return 0
    return float('%.*g' % (sig, x))


class NewtonRaphson():
    def __init__(self, equation, initialGuess, maxError = 0.0001, significantFigures = -1, nIterations = 50):
        self.equation = equation
        self.maxError = float(maxError)
        self.initialGuess = float(initialGuess)
        self.significantFigures = int(significantFigures)
        self.nIterations = int(nIterations)

    def solve(self):
        #intitialize symbols for differntiation
        x = symbols('x')
        f = self.equation.replace("^", "**")
        #TODO plot this
        f_prime = diff(f, x)
        self.f_prime = f_prime
        f = lambdify(x, f)
        f_prime = lambdify(x, f_prime)

        currentIteration = 1
        currentError = 1
        x_new = 1
        x_old = self.initialGuess
        while(currentIteration < self.nIterations and currentError > self.maxError):
            x_new = x_old - f(x_old) / f_prime(x_old)
            # for rounding
            x_new = round_sig(x_new, self.significantFigures)
            try:
                currentError = abs((x_new - x_old)/x_new) * 100
            except: currentError = 100000000
            self.print(currentIteration, x_new, currentError)
            currentIteration = currentIteration + 1
            x_old = x_new

        if(f(x_new) > 1e-3):
            raise Exception("couldn't find root accurately enough with " + str(self.nIterations) + " iterations")
        self.x_new = x_new
        self.plot()
        return x_new

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: "+ str(x_new) + " current error: ", str(currentError))

    def plot(self):
        x = Symbol('x')
        formula = sympify(self.f_prime)
        plot(formula, (x, self.x_new-10,self.x_new+10 ))