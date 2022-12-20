from Algorithms.Gauss import Gauss


class GaussJordan(Gauss):

    def __init__(self, a, b, maxError, siginficantDigits, scaling):
        super().__init__(a, b, maxError, siginficantDigits, scaling)

    def solve(self):
        self.a, self.b = self.forwardEliminationWithScaling() if self.scaling else self.forwardElimination()

        # divide each row by its pivot
        for i in range(0, self.numOfVariables):
            coeff = self.a[i][i]
            for j in range(i, self.numOfEquations):
                self.a[i][j] /= coeff
                self.a[i][j] = self.round_sig(self.a[i][j], self.sig)
            self.b[i] /= coeff
            self.b[i] = self.round_sig(self.b[i], self.sig)

        self.backwardElimination(self.a, self.b)
        print(self.b)
        return self.b

    def backwardElimination(self, a, b):
        for k in range(self.numOfVariables - 1, -1, -1):
            pivot = a[k][k]
            for i in range(k - 1, -1, -1):
                factor = self.round_sig(a[i][k] / pivot, self.sig)
                a[i][k] -= factor * pivot
                a[i][k] = self.round_sig(a[i][k], self.sig)
                b[i] -= factor * b[k]
                b[i] = self.round_sig(b[i], self.sig)
