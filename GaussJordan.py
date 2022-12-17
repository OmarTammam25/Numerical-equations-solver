from EquationSolver import EquationSolver


class GaussJordan(EquationSolver):

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

    def backwardElimination(self, a, b):
        for k in range(self.numOfVariables-1, -1, -1):
            pivot = a[k][k]
            for i in range(k-1, -1, -1):
                factor = self.round_sig(a[i][k] / pivot, self.sig)
                a[i][k] -= factor * pivot
                a[i][k] = self.round_sig(a[i][k], self.sig)
                b[i] -= factor * b[k]
                b[i] = self.round_sig(b[i], self.sig)

