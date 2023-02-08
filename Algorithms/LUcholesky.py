import math
import timeit

from numpy.linalg import linalg

from Algorithms.EquationSolver import EquationSolver


class LUcholesky(EquationSolver):
    def __init__(self, a, b, maxError, siginficantDigits, x = []):
        super().__init__(a, b, maxError, siginficantDigits)
        self.x = [0] * self.numOfVariables
        self.er = 0

    def solve(self):
        self.check_symmetric()
        self.check_eigenValues()
        startTime = timeit.default_timer()
        self.Decompose()
        if self.er != -1:
            self.Substitute()
        endTime = timeit.default_timer()
        time = endTime - startTime
        print("solution: ")
        return self.x
        print(round(time * 10 ** 3, 5), "ms")

    def Decompose(self):
        l = [[0 for x in range(self.numOfVariables)]
             for y in range(self.numOfVariables)]
        for k in range(self.numOfVariables):
            for i in range(k + 1):
                if i != k:
                    sum = 0
                    for j in range(i):
                        sum = self.round_sig(sum + self.round_sig(l[i][j] * l[k][j], self.sig), self.sig)
                    l[k][i] = self.round_sig(self.round_sig(self.a[k][i] - sum, self.sig) / l[i][i], self.sig)
                else:
                    sum = 0
                    for j in range(k):
                        sum = self.round_sig(sum + self.round_sig(pow(l[k][j], 2), self.sig), self.sig)
                    l[k][k] = self.round_sig(math.sqrt(self.round_sig(abs(self.a[k][k] - sum), self.sig)), self.sig)

        for i in range(self.numOfVariables):
            for j in range(i + 1):
                self.a[i][j] = l[i][j]
                self.a[j][i] = l[i][j]

        print(l)

    def Substitute(self):
        n = self.numOfVariables
        sig = self.sig
        y = [0] * n
        y[0] = self.round_sig(self.b[0] / self.a[0][0], sig)
        for i in range(1, n):
            y[i] = self.b[i]
            for j in range(0, i):
                y[i] = self.round_sig(y[i] - self.round_sig(self.a[i][j] * y[j], sig), sig)
            y[i] = self.round_sig(y[i] / self.a[i][i], sig)
        self.x[n - 1] = self.round_sig(y[n - 1] / self.a[n - 1][n - 1], sig)
        for i in range(n - 2, -1, -1):
            self.x[i] = y[i]
            for j in range(n - 1, i, -1):
                self.x[i] = self.round_sig(self.x[i] - self.round_sig(self.a[i][j] * self.x[j], sig), sig)
            self.x[i] = self.round_sig(self.x[i] / self.a[i][i], sig)

    def check_symmetric(self):
        for i in range(self.numOfVariables):
            for j in range(i + 1):
                if self.a[i][j] != self.a[j][i]:
                    self.er = -1
                    raise Exception('not symmetric matrix detected. cholesky can\'t solve')
    def check_eigenValues(self):
        eigenValues = linalg.eigvals(self.a)
        for i in eigenValues:
            if i < 0:
                self.er = -1
                raise Exception('not symmetric matrix detected. cholesky can\'t solve')