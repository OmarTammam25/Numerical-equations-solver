import numpy as np

from EquationSolver import EquationSolver


class Gauss(EquationSolver):
    def __init__(self, a, b):
        super().__init__(a, b)
    # a is the coefficient matrix
    # b is the values
    #

    def gaussElimination(self):
        a, b = self.forwardEliminationWithScaling()
        x = self.backwardSubstitution(a, b)

        return x
    def forwardEliminationWithScaling(self):
        a = self.a
        b = self.b
        for k in range(0, self.numOfVariables):  # loop over pivots
            self.partialPivotWithScaling(a, b, k)
            pivot = a[k][k]
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = a[i][k] / pivot
                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = a[i][j] - a[k][j] * factor
                b[i] = b[i] - b[k] * factor
        return a, b

    def backwardSubstitution(self, a, b):
        solution = [0] * self.numOfEquations
        for i in range(self.numOfEquations-1, -1, -1):
            sum = 0
            for j in range(i+1, self.numOfVariables):
                sum += a[i][j] * solution[j]
            solution[i] = (b[i] - sum) / a[i][i]
        return solution

    def partialPivotWithScaling(self, a, b, k):
        currIndex = k
        max = abs(a[k][k]) / self.s[k]
        for i in range(k, self.numOfEquations):
            if (max < abs(a[i][k]) / self.s[k]):
                max = abs(a[i][k]) / self.s[k]
                currIndex = i

        if k != currIndex:
            a[[k, currIndex]] = a[[currIndex, k]]
            b[[k, currIndex]] = b[[currIndex, k]]
            self.s[[k, currIndex]] = self.s[[currIndex, k]]
            print('pivoting row ', k, 'with row ', currIndex)
