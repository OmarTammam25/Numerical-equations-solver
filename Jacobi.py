import math

from EquationSolver import EquationSolver

class Jacobi(EquationSolver):
    def __init__(self, a, b, maxError, siginficantDigits, x0):
        super().__init__(a, b, maxError, siginficantDigits)
        self.x0 = x0.copy()

    def solve(self):
        x1 = self.x0.copy()
        e = [100.0] * self.numOfVariables
        max_iterations = 500

        condition = True
        count = 0

        while condition:
            condition = False
            for i in range(self.numOfVariables):
                temp = 0
                for j in range(self.numOfVariables):
                    if i != j:
                        temp += self.x0[j] * self.a[i][j]
                x1[i] = (self.b[i] - temp) / self.a[i][i]
                x1[i] = self.round_sig(x1[i], self.sig)
                e[i] = float(abs(self.x0[i] - x1[i]) / float(abs(x1[i])))
                condition |= (e[i] > self.tol)

            self.x0 = x1.copy()
            count = count + 1
            condition &= count < max_iterations
            self.print(count, e)

    def print(self, count, e):
        print(count, ':\t', self.x0, '\t', e)
