import math
import timeit

from Algorithms.EquationSolver import EquationSolver


class LUCrout(EquationSolver):
    def __init__(self, a, b, maxError, siginficantDigits, x=[]):
        super().__init__(a, b, maxError, siginficantDigits)
        self.o = [0] * self.numOfVariables
        self.s = [0] * self.numOfVariables
        self.x = [0] * self.numOfEquations
        self.er = 0

    def solve(self):
        startTime = timeit.default_timer()
        self.Decompose()

        if (self.er == -1):
            return

        self.Substitute()
        endTime = timeit.default_timer()
        time = endTime - startTime
        return self.x

    def Decompose(self):
        n = self.numOfVariables
        for i in range(0, n):
            self.o[i] = i
            self.s[i] = abs(self.a[i][0])
            for j in range(1, n):
                if abs(self.a[i][j]) > self.s[i]:
                    self.s[i] = abs(self.a[i][j])

        for i in range(0, n):
            self.Pivot(i)
            if self.IsSingular(i):
                self.er = -1
                return

            for j in range(i, n):
                for k in range(0, i):
                    self.a[self.o[j]][i] = self.round_sig(self.round_sig(self.a[self.o[j]][i], self.sig) - self.round_sig(self.a[self.o[j]][k],
                                        self.sig) * self.round_sig(self.a[self.o[k]][i], self.sig), self.sig)

            for j in range(i, n):
                if i == j:
                    continue
                for k in range(0, i):
                    self.a[self.o[i]][j] = self.round_sig(self.round_sig(self.a[self.o[i]][j], self.sig) - self.round_sig(self.a[self.o[i]][k],
                                        self.sig) * self.round_sig(self.a[self.o[k]][j], self.sig), self.sig)
                if self.a[self.o[i]][i] == 0:
                    self.er = -1
                    return
                self.a[self.o[i]][j] = self.round_sig(self.round_sig(self.a[self.o[i]][j], self.sig) / self.round_sig(self.a[self.o[i]][i], self.sig),
                                                self.sig)

    def IsSingular(self, k):
        if (abs(self.a[self.o[k]][k]) / self.s[self.o[k]]) < self.tol:
            return True
        return False

    def Pivot(self, k):
        n = self.numOfVariables
        p = k
        big = abs(self.a[self.o[k]][k]) / self.s[self.o[k]]
        for i in range(k + 1, n):
            dummy = abs(self.a[self.o[i]][k]) / self.s[self.o[i]]
            if (dummy > big):
                big = dummy
                p = i
        dummy = self.o[p]
        self.o[p] = self.o[k]
        self.o[k] = dummy

    def ForwardSubstitution(self):
        n = self.numOfVariables
        y = [0] * n
        for i in range(0, n):
            y[self.o[i]] = self.b[self.o[i]]
            for j in range(0, i):
                y[self.o[i]] = self.round_sig(self.round_sig(y[self.o[i]], self.sig) - self.round_sig(self.a[self.o[i]][j],
                                    self.sig) * self.round_sig(y[self.o[j]], self.sig), self.sig)

            y[self.o[i]] = self.round_sig(self.round_sig(y[self.o[i]], self.sig) / self.round_sig(self.a[self.o[i]][i], self.sig), self.sig)
        return y

    def BackwardSubtitution(self, y):
        n = self.numOfVariables
        self.x[n - 1] = self.round_sig(y[self.o[n - 1]], self.sig)
        for i in range(n - 2, -1, -1):
            self.x[i] = self.round_sig(y[self.o[i]], self.sig)

            for j in range(n - 1, i, -1):
                self.x[i] = self.round_sig(self.round_sig(self.x[i], self.sig) - self.round_sig(self.a[self.o[i]][j],
                                            self.sig) * self.round_sig(self.x[j], self.sig), self.sig)

    def Substitute(self):
        y = self.ForwardSubstitution()
        self.BackwardSubtitution(y)
