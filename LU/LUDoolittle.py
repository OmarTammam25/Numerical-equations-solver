import math
class LU_Doolittle():
    def execute(self, a, b, n, x, tol, seg, er=0):
        s = [0] * n
        o = [0] * n
        er = 0
        self.Decompose(a, n, tol, o, s, seg, er)
        if er != -1:
            self.Substitute(a, o, n, b, x,seg)

    def Decompose(self, a, n, tol, o, s, seg, er):
        for i in range(0, n):
            o[i] = i
            s[i] = abs(a[i][0])
            for j in range(1, n):
                if (abs(a[i][j]) > s[i]):
                    s[i] = abs(a[i][j])
        for k in range(0, n - 1):
            self.pivot(a, o, s, n, k)
            if (abs(a[o[k]][k]) / s[o[k]]) < tol:
                er = -1
                return
            for i in range(k + 1, n):
                factor = a[o[i]][k] / a[o[k]][k]
                factor = self.round_sig(factor, seg)
                a[o[i]][k] = factor
                for j in range(k + 1, n):
                    a[o[i]][j] = self.round_sig(a[o[i]][j] - factor * a[o[k]][j],seg)
        if (abs(a[o[n - 1]][n - 1])) < tol:
            er = -1

    def pivot(self, a, o, s, n, k):
        p = k
        big = abs(a[o[k]][k]) / s[o[k]]
        for i in range(k + 1, n):
            dummy = abs(a[o[i]][k]) / s[o[i]]
            if (dummy > big):
                big = dummy
                p = i
        dummy = o[p]
        o[p] = o[k]
        o[k] = dummy

    def Substitute(self, a, o, n, b, x, seg):
        y = [0] * n
        y[o[0]] = b[o[0]]
        for i in range(1, n):
            sum = b[o[i]]
            for j in range(0, i):
                sum = self.round_sig(sum - self.round_sig(a[o[i]][j] * y[o[j]],seg),seg)
            y[o[i]] = sum
        x[n - 1] = self.round_sig(y[o[n - 1]] / a[o[n - 1]][n - 1],seg)
        for i in range(n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, n):
                sum = self.round_sig(sum + self.round_sig(a[o[i]][j] * x[j],seg),seg)
            x[i] = self.round_sig(self.round_sig(y[o[i]] - sum,seg) / a[o[i]][i],seg)

    def round_sig(self, x, sig=2):
        if x==0:
            return 0
        if sig==-1:
            return x
        return round(x,sig-int(math.floor(math.log10(abs(x))))-1)