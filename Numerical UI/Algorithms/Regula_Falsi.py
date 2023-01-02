import math

from sympy import *
import matplotlib.pyplot as pl
import numpy as np


class Regula_Falsi():
    def __init__(self, equation, lower, upper, maxError=0.0001,
                 significantFigures=-1, nIterations=500):
        self.equation = equation
        self.maxError = float(maxError)
        self.lower = float(lower)
        self.upper = float(upper)
        self.significantFigures = int(significantFigures)
        self.nIterations = int(nIterations)

    def solve(self):
        self.plot()
        if self.calculate_function(self.lower) * self.calculate_function(self.upper) > 0:
            raise Exception("No unique root in this interval")


        current_iterations = 0
        x_l = self.lower
        x_u = self.upper
        x_r_old = (x_l + x_u)
        currentError = 1
        while current_iterations < self.nIterations and currentError > self.maxError:
            current_iterations += 1
            f_x_lower = self.calculate_function(x_l)
            f_x_upper = self.calculate_function(x_u)
            if(f_x_upper == f_x_lower):
                return x_r_new
            x_r_new = self.round_sig(self.round_sig(self.round_sig(x_l * f_x_upper,self.significantFigures)
                    - self.round_sig(x_u * f_x_lower,self.significantFigures))
            / self.round_sig((f_x_upper - f_x_lower),self.significantFigures),self.significantFigures)
            f_x_mid = self.round_sig(self.calculate_function(x_r_new),self.significantFigures)
            try:
                currentError = abs((x_r_new - x_r_old) / x_r_new) * 100
            except:
                currentError = 100000000
            x_r_old = x_r_new
            self.print(current_iterations, x_r_new, currentError)

            if f_x_lower * f_x_mid < 0:
                x_u = x_r_new
            else:
                x_l = x_r_new
        return x_r_new

    def calculate_function(self, x_i):
        x = symbols('x')
        f = self.equation.replace("^", "**")
        f = lambdify(x, f)
        return f(x_i)

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: " + str(x_new) + " current error: ", str(currentError), "%")

    def round_sig(self,x, sig=-1):
        if sig == -1:
            return x
        if x == 0:
            return 0
        return float('%.*g' % (sig, x))
    def plot(self):
        x = Symbol('x')
        formula = sympify(self.equation)
        plot(formula, (x, self.lower, self.upper))

