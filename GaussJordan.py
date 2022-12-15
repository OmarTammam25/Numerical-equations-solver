from EquationSolver import EquationSolver


class GaussJordan(EquationSolver):

    def gaussJordanElimination(self):
        a, b = self.forwardElimination()
        # divide eaceh row by its pivot
        for i in range(0, self.numOfVariables):
            coeff = a[i][i]
            for j in range(i, self.numOfEquations):
                a[i][j] /= coeff
            b[i] /= coeff

        self.backwardElimination(a, b)
        return b

    def backwardElimination(self, a, b):
        for k in range(self.numOfVariables-1, -1, -1):
            pivot = a[k][k]
            for i in range(k-1, -1, -1):
                factor = a[i][k] / pivot
                a[i][k] -= factor *  pivot
                b[i] -= factor * b[k]

