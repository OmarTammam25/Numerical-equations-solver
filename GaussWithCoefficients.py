class GaussWithCoefficients:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.numOfEquations = len(b)
        self.numOfVariables = len(a[0])

    def gaussElimination(self):
        a, b = self.forwardElimination()
        x = self.backwardSubstitution(a, b)
        return x

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

    def backwardSubstitution(self, a, b):
        solution = [0] * self.numOfEquations
        for i in range(self.numOfEquations-1, -1, -1):
            sum = 0
            for j in range(i+1, self.numOfVariables):
                sum += a[i][j] * solution[j]
            solution[i] = (b[i] - sum) / a[i][i]
        return solution