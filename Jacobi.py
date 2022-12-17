import math


class Jacobi:
    def __init__(self, a, b, x0, sig):
        self.a = a.copy()
        self.b = b.copy()
        self.seg = sig
        self.x0 = x0.copy()

    def solve(self):
        n = len(self.b)
        x1 = self.x0.copy()
        e = [100.0] * n

        Etol = 0.000000005
        max_iterations = 500

        condition = True
        count = 0

        while condition:
            condition = False
            for i in range(n):
                temp = 0
                for j in range(n):
                    if i != j:
                        temp += self.x0[j] * self.a[i][j]
                x1[i] = (self.b[i] - temp) / self.a[i][i]
                x1[i] = self.round_sig(x1[i], self.sig)
                e[i] = (abs(self.x0[i] - x1[i]) / float(abs(x1[i])))
                condition |= (e[i] > Etol)

            self.x0 = x1.copy()
            count = count + 1
            condition &= count < max_iterations
            self.print(count, e)

    def round_sig(self, x, sig=-1):
        if x == 0:
            return 0
        if (sig == -1):
            return x
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

    def print(self, count, e):
        print(count, ':\t', self.x0, '\t', e, '\n')
