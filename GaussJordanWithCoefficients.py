from EquationSolver import EquationSolver
from GaussJordan import GaussJordan

class GaussJordanWithcoefficients(GaussJordan):

    def __init__(self, a, b, maxError, significantDigits, scaling=False):
        super().__init__(a, b, maxError, significantDigits, scaling)

    def solve(self):
        self.a, self.b = self.forwardElimination()

        # divide each row by its pivot
        for i in range(0, self.numOfVariables):
            coeff = self.a[i][i]
            for j in range(i, self.numOfEquations):
                self.a[i][j] /= coeff
                self.a[i][j] = self.round_sig(self.a[i][j], self.sig)
            self.b[i] /= coeff
            self.b[i] = self.round_sig(self.b[i], self.sig)

        self.backwardElimination(self.a, self.b)
        return self.b

    def forwardElimination(self):
        for k in range(0, self.numOfVariables):  # loop over pivots
            pivot = self.a[k][k]
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = self.a[i][k] / pivot
                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    self.a[i][j] = self.a[i][j] - self.a[k][j] * factor
                self.b[i] = self.b[i] - self.b[k] * factor
        return self.a, self.b

    def backwardElimination(self, a, b):
        for k in range(self.numOfVariables-1, -1, -1):
            pivot = a[k][k]
            for i in range(k-1, -1, -1):
                factor = a[i][k] / pivot
                a[i][k] -= factor * pivot
                b[i] -= factor * b[k]

