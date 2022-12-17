import time

import numpy as np

from EquationSolver import EquationSolver


class Gauss(EquationSolver):
    def __init__(self, a, b, maxError, siginficantDigits):
        super().__init__(a, b, maxError, siginficantDigits)
    # a is the coefficient matrix
    # b is the values
    #

    def gaussElimination(self):

        a, b = self.forwardElimination()

        x = self.backwardSubstitution(a, b)

        return x


    def backwardSubstitution(self, a, b):
        solution = [0] * self.numOfEquations
        for i in range(self.numOfEquations-1, -1, -1):
            sum = 0
            for j in range(i+1, self.numOfVariables):
                sum += a[i][j] * solution[j]
                sum = self.round_sig(sum, self.sig)
            solution[i] = self.round_sig((b[i] - sum) / a[i][i], self.sig)
        return solution


