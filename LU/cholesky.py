import math


class LU_cholesky():
    def execute(self, a, b, n, x, tol):
        er = 0
        self.Decompose(a, n, tol, er)
        if er != -1:
            self.Substitute(a, n, b, x)

    def Decompose(self, a, n, tol, er):
        # TODO check if it is symmetric and update the er
        l = [[0 for x in range(n)]
             for y in range(n)]
        for k in range(n):
            for i in range(k + 1):
                if i != k:
                    sum = 0
                    for j in range(i):
                        sum += l[i][j] * l[k][j]
                    l[k][i] = (a[k][i] - sum) / l[i][i]
                else:
                    sum = 0
                    for j in range(k):
                        sum += pow(l[k][j], 2)
                    l[k][k] = math.sqrt(a[k][k] - sum)

        for i in range(n):
            for j in range(i + 1):
                a[i][j] = l[i][j]
                a[j][i] = l[i][j]

    def Substitute(self, a, n, b, x):
        y = [0] * n
        y[0] = b[0] / a[0][0]
        for i in range(1, n):
            y[i] = b[i]
            for j in range(0, i):
                y[i] -= a[i][j] * y[j]
            y[i] /= a[i][i]
        x[n - 1] = y[n - 1] / a[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = y[i]
            for j in range(n - 1, i, -1):
                x[i] -= a[i][j] * x[j]
            x[i] /= a[i][i]
