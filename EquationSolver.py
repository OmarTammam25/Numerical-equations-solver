import numpy as np


class EquationSolver:
    def __init__(self, a, b, maxError):
        self.a = a
        self.b = b
        self.numOfEquations = len(b)
        self.numOfVariables = len(a[0])
        self.s = self.getMaxInEachRow()
        self.er = maxError

    def getMaxInEachRow(self):
        s = np.array([0] * self.numOfEquations)
        for i in range(0, self.numOfEquations):
            mx = 0
            for j in self.a[i]:
                mx = max(abs(j), mx)
            s[i] = mx
        return s
    def forwardElimination(self):
        a = self.a
        b = self.b
        for k in range(0, self.numOfVariables):  # loop over pivots
            self.partialPivot(a, b, k)
            pivot = a[k][k]
            if pivot < abs(self.er):
                raise Exception('Singular matrix detected. has no unique solution')
            factor = a[i][k] / pivot
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = a[i][j] - a[k][j] * factor
                b[i] = b[i] - b[k] * factor
        if a[self.numOfEquations-1][self.numOfEquations] < abs(self.er):
            raise Exception('Singular matrix detected. has no unique solution')
        return a, b

    def partialPivot(self, a, b, k):
        currIndex = k
        max = abs(a[k][k])
        for i in range(k, self.numOfEquations):
            if (max < abs(a[i][k])):
                max = abs(a[i][k])
                currIndex = i

        if k != currIndex:
            a[[k, currIndex]] = a[[currIndex, k]]
            b[[k, currIndex]] = b[[currIndex, k]]
            print('pivoting row ', k, 'with row ', currIndex)

    def forwardEliminationWithScaling(self):
        a = self.a
        b = self.b
        for k in range(0, self.numOfVariables):  # loop over pivots
            self.partialPivotWithScaling(a, b, k)
            pivot = a[k][k]
            if pivot < abs(self.er / self.s[k]):
                raise Exception('Singular matrix detected. has no unique solution')
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = a[i][k] / pivot
                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = a[i][j] - a[k][j] * factor
                b[i] = b[i] - b[k] * factor
        if a[self.numOfEquations-1][self.numOfEquations] < abs(self.er):
            raise Exception('Singular matrix detected. has no unique solution')
        return a, b
    def partialPivotWithScaling(self, a, b, k):
        currIndex = k
        max = abs(a[k][k]) / self.s[k]
        for i in range(k, self.numOfEquations):
            if max < abs(a[i][k]) / self.s[i]:
                max = abs(a[i][k]) / self.s[i]
                currIndex = i

        if k != currIndex:
            a[[k, currIndex]] = a[[currIndex, k]]
            b[[k, currIndex]] = b[[currIndex, k]]
            self.s[[k, currIndex]] = self.s[[currIndex, k]]
            print('pivoting row ', k, 'with row ', currIndex)