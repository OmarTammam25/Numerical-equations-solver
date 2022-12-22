import math

import numpy as np


class EquationSolver:
    def __init__(self, a, b, maxError, significantDigits=16):
        self.a = a.copy()
        self.b = b.copy()
        self.numOfEquations = len(b)
        self.numOfVariables = len(a[0])
        # self.s = self.getMaxInEachRow()
        self.tol = maxError
        self.sig = significantDigits

    def solve(self):
        pass
    def getMaxInEachRow(self):
        s = np.array([0] * self.numOfEquations)
        for i in range(0, self.numOfEquations):
            mx = 0
            for j in self.a[i]:
                mx = max(abs(j), mx)
            s[i] = mx
        return s
    # def forwardElimination(self):
    #     a = self.a
    #     b = self.b
    #     for k in range(0, self.numOfVariables):  # loop over pivots
    #         # self.partialPivot(a, b, k)
    #         pivot = a[k][k]
    #         # if abs(pivot) < abs(self.er):
    #         #     raise Exception('Singular matrix detected. has no unique solution')
    #         for i in range(k + 1, self.numOfEquations):  # loop over rows
    #             factor = self.round_sig(a[i][k] / pivot, self.sig)
    #
    #             print('factor after round is: ' , factor)
    #             for j in range(k, self.numOfVariables):  # loop over each coefficient in row
    #                 a[i][j] = self.round_sig(a[i][j] - a[k][j] * factor, self.sig)
    #             b[i] = self.round_sig(b[i] - b[k] * factor, self.sig)
    #     # if abs(a[self.numOfEquations-1][self.numOfEquations-1]) < abs(self.er):
    #     #     raise Exception('Singular matrix detected. has no unique solution')
    #     return a, b
    #
    # def partialPivot(self, a, b, k):
    #     currIndex = k
    #     max = abs(a[k][k])
    #     for i in range(k, self.numOfEquations):
    #         if (max < abs(a[i][k])):
    #             max = abs(a[i][k])
    #             currIndex = i
    #
    #     if k != currIndex:
    #         a[[k, currIndex]] = a[[currIndex, k]]
    #         b[[k, currIndex]] = b[[currIndex, k]]
    #         print('pivoting row ', k, 'with row ', currIndex)
    #
    # def forwardEliminationWithScaling(self):
    #     a = self.a
    #     b = self.b
    #     for k in range(0, self.numOfVariables):  # loop over pivots
    #         self.partialPivotWithScaling(a, b, k)
    #         pivot = a[k][k]
    #         if abs(pivot) < abs(self.er / self.s[k]):
    #             raise Exception('Singular matrix detected. has no unique solution')
    #         for i in range(k + 1, self.numOfEquations):  # loop over rows
    #             factor = self.round_sig(a[i][k] / pivot, self.sig)
    #             for j in range(k, self.numOfVariables):  # loop over each coefficient in row
    #                 a[i][j] = self.round_sig(a[i][j] - a[k][j] * factor, self.sig)
    #             b[i] = self.round_sig(b[i] - b[k] * factor, self.sig)
    #     if abs(a[self.numOfEquations-1][self.numOfEquations-1]) < abs(self.er):
    #         raise Exception('Singular matrix detected. has no unique solution')
    #     return a, b
    # def partialPivotWithScaling(self, a, b, k):
    #     currIndex = k
    #     max = abs(a[k][k]) / self.s[k]
    #     for i in range(k, self.numOfEquations):
    #         if max < abs(a[i][k]) / self.s[i]:
    #             max = abs(a[i][k]) / self.s[i]
    #             currIndex = i
    #
    #     if k != currIndex:
    #         a[[k, currIndex]] = a[[currIndex, k]]
    #         b[[k, currIndex]] = b[[currIndex, k]]
    #         self.s[[k, currIndex]] = self.s[[currIndex, k]]
    #         print('pivoting row ', k, 'with row ', currIndex)

    def round_sig(self, x, sig=-1):
        if x == 0:
            return 0
        if(sig == -1):
            return x
        return float('%.*g' % (sig, x))
