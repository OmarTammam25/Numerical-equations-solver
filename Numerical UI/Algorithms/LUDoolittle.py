import timeit

from Algorithms.EquationSolver import EquationSolver


class LUDoolittle(EquationSolver):
    def __init__(self, a, b, maxError, siginficantDigits, x=[]):
        super().__init__(a, b, maxError, siginficantDigits)
        self.o = [0] * self.numOfVariables
        self.s = [0] * self.numOfVariables
        self.x = [0] * self.numOfEquations
        self.er = 0

    def solve(self):
        startTime = timeit.default_timer()

        self.Decompose()
        if self.er != -1:
            self.Substitute()
        endTime = timeit.default_timer()
        time = endTime - startTime
        return self.x
        # print(round(time * 10 ** 3, 5), "ms")

    def Decompose(self):
        n = self.numOfVariables
        for i in range(n):
            self.o[i] = i
            self.s[i] = abs(self.a[i][0])
            for j in range(1, n):
                if abs(self.a[i][j]) > self.s[i]:
                    self.s[i] = abs(self.a[i][j])
        for k in range(0, n - 1):
            self.pivot(k)
            if (abs(self.a[self.o[k]][k]) / self.s[self.o[k]]) < self.tol:
                self.er = -1
                return
            for i in range(k + 1, n):
                factor = self.a[self.o[i]][k] / self.a[self.o[k]][k]
                factor = self.round_sig(factor, self.sig)
                self.a[self.o[i]][k] = factor
                for j in range(k + 1, n):
                    self.a[self.o[i]][j] = self.round_sig(self.a[self.o[i]][j] - factor * self.a[self.o[k]][j], self.sig)
        if (abs(self.a[self.o[n - 1]][n - 1])) < self.tol:
            self.er = -1
        print(self.a, self.b)
        print(self.s, self.o)

    def pivot(self, k):
        p = k
        n = self.numOfVariables
        big = abs(self.a[self.o[k]][k]) / self.s[self.o[k]]
        for i in range(k + 1, n):
            dummy = abs(self.a[self.o[i]][k]) / self.s[self.o[i]]
            if (dummy > big):
                big = dummy
                p = i
        dummy = self.o[p]
        self.o[p] = self.o[k]
        self.o[k] = dummy

    def Substitute(self):
        n = self.numOfVariables
        y = [0] * n
        y[self.o[0]] = self.b[self.o[0]]
        for i in range(1, n):
            sum = self.b[self.o[i]]
            for j in range(0, i):
                sum = self.round_sig(sum - self.round_sig(self.a[self.o[i]][j] * y[self.o[j]], self.sig), self.sig)
            y[self.o[i]] = sum
        self.x[n - 1] = self.round_sig(y[self.o[n - 1]] / self.a[self.o[n - 1]][n - 1], self.sig)
        for i in range(n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, n):
                sum = self.round_sig(sum + self.round_sig(self.a[self.o[i]][j] * self.x[j], self.sig), self.sig)
            self.x[i] = self.round_sig(self.round_sig(y[self.o[i]] - sum, self.sig) / self.a[self.o[i]][i], self.sig)
