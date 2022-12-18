from EquationSolver import EquationSolver
from GaussJordan import GaussJordan

class GaussJordanWithcoefficients(EquationSolver, GaussJordan):

    def __init__(self, a, b, maxError, significantDigits):
        super().__init__(a, b, maxError, significantDigits)

    def gaussJordanElimination(self):
        a, b = self.forwardElimination()

        # divide each row by its pivot
        for i in range(0, self.numOfVariables):
            coeff = a[i][i]
            for j in range(i, self.numOfEquations):
                a[i][j] /= coeff
                a[i][j] = self.round_sig(a[i][j], self.sig)
            b[i] /= coeff
            b[i] = self.round_sig(b[i], self.sig)

        self.backwardElimination(a, b)
        return b

    def forwardElimination(self):
        a = self.a
        b = self.b
        for k in range(0, self.numOfVariables):  # loop over pivots
            pivot = a[k][k]
            for i in range(k + 1, self.numOfEquations):  # loop over rows
                factor = a[i][k] / pivot
                for j in range(k, self.numOfVariables):  # loop over each coefficient in row
                    a[i][j] = a[i][j] - a[k][j] * factor
                b[i] = b[i] - b[k] * factor
        return a, b

    def backwardElimination(self, a, b):
        for k in range(self.numOfVariables-1, -1, -1):
            pivot = a[k][k]
            for i in range(k-1, -1, -1):
                factor = a[i][k] / pivot
                a[i][k] -= factor * pivot
                b[i] -= factor * b[k]

