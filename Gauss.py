import numpy as np

from EquationSolver import EquationSolver


class Gauss(EquationSolver):
    def __init__(self, a, b):
        super().__init__(a, b)
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
            solution[i] = (b[i] - sum) / a[i][i]
        return solution


