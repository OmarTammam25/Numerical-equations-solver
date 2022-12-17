import math


class LU_cholesky():
    def execute(self, a, b, n, x, tol,seg,er=0):
        self.check_syemetric(a, n, er)
        self.Decompose(a, n, tol, seg,er)
        if er != -1:
            self.Substitute(a, n, b, x,seg)

    def Decompose(self, a, n, tol,seg, er):
        # TODO check if it is symmetric and update the er
        l = [[0 for x in range(n)]
             for y in range(n)]
        for k in range(n):
            for i in range(k + 1):
                if i != k:
                    sum = 0
                    for j in range(i):
                        sum = self.round_sig(sum+self.round_sig(l[i][j] * l[k][j],seg),seg)
                    l[k][i] = self.round_sig(self.round_sig(a[k][i] - sum,seg) / l[i][i],seg)
                else:
                    sum = 0
                    for j in range(k):
                        sum = self.round_sig(sum+self.round_sig(pow(l[k][j], 2),seg),seg)
                    l[k][k] = self.round_sig(math.sqrt(self.round_sig(a[k][k] - sum,seg)),seg)

        for i in range(n):
            for j in range(i + 1):
                a[i][j] = l[i][j]
                a[j][i] = l[i][j]

    def Substitute(self, a, n, b, x,seg):
        y = [0] * n
        y[0] = self.round_sig(b[0] / a[0][0],seg)
        for i in range(1, n):
            y[i] = b[i]
            for j in range(0, i):
                y[i] = self.round_sig(y[i]-self.round_sig(a[i][j] * y[j],seg),seg)
            y[i] = self.round_sig(y[i]/a[i][i],seg)
        x[n - 1] = self.round_sig(y[n - 1] / a[n - 1][n - 1],seg)
        for i in range(n - 2, -1, -1):
            x[i] = y[i]
            for j in range(n - 1, i, -1):
                x[i] = self.round_sig(x[i]-self.round_sig(a[i][j] * x[j],seg),seg)
            x[i] = self.round_sig(x[i]/a[i][i])

    def check_syemetric(self, a, n, er):
        for i in range(n):
            for j in range(i + 1):
                if a[i][j] != a[j][i]:
                    er = -1

    def round_sig(self, x, sig=2):
        if x==0:
            return 0
        if sig==-1:
            return x
        return round(x,sig-int(math.floor(math.log10(abs(x))))-1)