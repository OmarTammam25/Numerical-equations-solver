import time

import numpy as np

from Algorithms.EquationSolver import EquationSolver


class Gauss(EquationSolver):
    # a is the coefficient matrix
    # b is the values

    def __init__(self, a, b, maxError, siginficantDigits, scaling):
        super().__init__(a, b, maxError, siginficantDigits)
        self.scaling = scaling

    def solve(self):
        # f = open("solution.txt", "w")
        # f.close()
        a, b = self.forwardEliminationWithScaling() if self.scaling else self.forwardElimination()
        x = self.backwardSubstitution(a, b)
        print(x)
        return x

    # def getMaxInEachRow(self):
    #     s = np.array([0] * self.numOfEquations)
    #     for i in range(0, self.numOfEquations):
    #         mx = 0
    #         for j in self.a[i]:
    #             mx = max(abs(j), mx)
    #         s[i] = mx
    #     return s

    def forwardElimination(self):
        f = open("solution.txt", "a")
        a = np.array(self.a.copy())
        b = np.array(self.b.copy())
        f.write(str(a)+'\n')
        f.write(str(b)+'\n')
        for k in range(0, self.numOfVariables):  # loop over pivots
            self.partialPivot(a, b, k)
            pivot = a[k][k]
            f.write(str(a) + '\n')
            f.write(str(b) + '\n')
            f.write("new pivot is: " + str(pivot) + '\n')
            if abs(pivot) < abs(self.tol):
                f.write("Singular Matrix detected\n")
                raise Exception('Singular matrix detected. has no unique solution')
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = self.round_sig(a[i][k] / pivot, self.sig)
                f.write("multiplier" + str(i) + str(k) + '\n')
                print('factor after round is: ', factor)

                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = self.round_sig(a[i][j] - a[k][j] * factor, self.sig)
                f.write(str(a) + '\n')
                b[i] = self.round_sig(b[i] - b[k] * factor, self.sig)
                f.write(str(b) + '\n')
        if abs(a[self.numOfEquations-1][self.numOfEquations-1]) < abs(self.tol):
            f.write("Singular Matrix detected.\n")
            raise Exception('Singular matrix detected. has no unique solution')
        f.write(str(a) + '\n')
        f.write(str(b) + '\n')
        f.close()
        return a, b

    def partialPivot(self, a, b, k):
        f = open("solution.txt", "a")
        currIndex = k
        max = abs(a[k][k])
        for i in range(k, self.numOfEquations):
            if (max < abs(a[i][k])):
                max = abs(a[i][k])
                currIndex = i

        if k != currIndex:
            f.write("Pivoting\n")
            f.write("interchanging row " + str(k) + " with row " + str(currIndex) + '\n')
            a[[k, currIndex]] = a[[currIndex, k]]
            b[[k, currIndex]] = b[[currIndex, k]]
            print('pivoting row ', k, 'with row ', currIndex)
        f.close()

    def forwardEliminationWithScaling(self):
        a = self.a.copy()
        b = self.b.copy()
        for k in range(0, self.numOfVariables):  # loop over pivots
            self.partialPivotWithScaling(a, b, k)
            pivot = a[k][k]
            if abs(pivot) < abs(self.tol / self.s[k]):
                raise Exception('Singular matrix detected. has no unique solution')
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = self.round_sig(a[i][k] / pivot, self.sig)
                print('factor after round is: ', factor)

                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = self.round_sig(a[i][j] - a[k][j] * factor, self.sig)
                b[i] = self.round_sig(b[i] - b[k] * factor, self.sig)
                print(a, b)
        if abs(a[self.numOfEquations - 1][self.numOfEquations - 1]) < abs(self.tol):
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

    def backwardSubstitution(self, a, b):
        solution = [0] * self.numOfEquations
        for i in range(self.numOfEquations - 1, -1, -1):
            sum = 0
            for j in range(i + 1, self.numOfVariables):
                sum += a[i][j] * solution[j]
                sum = self.round_sig(sum, self.sig)
            solution[i] = self.round_sig((b[i] - sum) / a[i][i], self.sig)
        return solution
