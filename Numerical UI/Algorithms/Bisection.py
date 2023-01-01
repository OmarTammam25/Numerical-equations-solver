import math

from sympy import *

import matplotlib.pyplot as pl
import numpy as np

class Bisection():
    def __init__(self, equation, lower, upper, maxError=0.0001, significantFigures=-1, nIterations=500):
        self.equation = equation
        self.maxError = float(maxError)
        self.lower = float(lower)
        self.upper = float(upper)
        self.significantFigures = int(significantFigures)
        self.nIterations = int(nIterations)

    def solve(self):
        if self.calculate_function(self.lower) * self.calculate_function(self.upper) > 0:
            raise Exception("No unique root in this interval")

        current_iterations = 0
        x_l = self.lower
        x_u = self.upper
        x_r_old = (x_l + x_u)
        currentError = 1
        while current_iterations < self.nIterations and currentError > self.maxError:
            current_iterations += 1
            x_r_new = (x_l + x_u) / 2
            f_x_lower = self.calculate_function(x_l)
            f_x_mid = self.calculate_function(x_r_new)
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
        self.plot()
        return x_r_new

    def calculate_function(self, x_i):
        x = symbols('x')
        f = self.equation.replace("^", "**")
        f = lambdify(x, f)
        return f(x_i)

    def print(self, currentIteration, x_new, currentError):
        print("iteration #" + str(currentIteration) + ": " + "\n" +
              "current root: " + str(x_new) + " current error: ", str(currentError), "%")


    def plot(self):
        x = Symbol('x')
        formula = sympify(self.equation)
        plot(formula, (x, self.lower, self.upper))


    def round_sig(x, sig=-1):
        if sig == -1:
            return x
        if x == 0:
            return 0
        return float('%.*g' % (sig, x))








#
#
# import math
# from sympy import *
#
#
# def round_sig(x, sig=-1):
#     # x=float(x)
#     if (sig == -1):
#         return x
#     if x == 0:
#         return 0
#     return float('%.*g' % (sig, x))
#
# class Bisection():
#     def __init__(self, equation, x_lower, x_upper,  maxError = 0.0001, significantFigures = -1, nIterations = 50) :
#         self.equ = equation
#         self.xl = float(x_lower)
#         self.xu = float(x_upper)
#         self.maxError = float(maxError)
#         self.sig = int(significantFigures)
#         self.nIterations = int(nIterations)
#
#     def solve(self):
#         #intitialize symbols for differntiation
#         x = symbols('x')
#         f = self.equ.replace("^", "**")
#         f = lambdify(x, f)
#         oldx = 0
#         current_iterations: number = 0
#         while current_iterations < self.nIterations:
#             current_iterations += 1
#             mid = round_sig(round_sig(self.xl + self.xu,self.sig) / 2.0,self.sig)
#             f_x_lower = round_sig(f(self.xl),self.sig)
#             f_x_mid = round_sig(f(mid),self.sig)
#             try:
#                 currentError = abs((mid - oldx) / mid) * 100
#             except:
#                 currentError = 10000000
#
#
#             oldx = mid
#             if f_x_lower * f_x_mid < 0:
#                 self.xu = mid
#             else:
#                 self.xl = mid
#             print(current_iterations, mid, currentError)
#         return self.xl
#
#     def print(self, currentIteration, x_new, currentError):
#         print("iteration #" + str(currentIteration) + ": " + "\n" +
#               "current root: "+ str(x_new) + " current error: ", str(currentError))
#
#
#
