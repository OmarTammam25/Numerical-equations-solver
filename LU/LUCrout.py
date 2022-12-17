import numpy as np
import math

class LU_Crout:

    def IsSingular(self, A, s, o, k, tol):
        if ((abs(A[o[k]][k]) / float(s[o[k]])) < tol): return True
        return False

    def Crout(self, A, b, X, tol, er=0):
        n = len(A)
        o = [0] * n
        s = [0] * n

        self.Decompose(A, tol, o, s)
        if er == -1: return
        self.Substitute(A, o, n, b, X)

    def Decompose(self, A, tol, o, s, er=0):

        n = len(A)

        for i in range(0, n):
            o[i] = i
            s[i] = abs(A[i][0])

            for j in range(1, n):
                if abs(A[i][j] > s[i]):
                    s[i] = abs(A[i][j])

        for i in range(0, n):
            self.Pivot(A, o, s, n, i)

            if self.IsSingular(A, s, o, i, tol):
                er = -1
                return

            for j in range(i, n):

                for k in range(0, i): A[o[j]][i] -= A[o[j]][k] * A[o[k]][i]

            for j in range(i, n):

                if i == j: continue

                for k in range(0, i): A[o[i]][j] -= A[o[i]][k] * A[o[k]][j]

                if A[o[i]][i] == 0:
                    er = -1
                    return

                A[o[i]][j] /= float(A[o[i]][i])

    def Pivot(self, a, o, s, n, k):
        p = k
        big = abs(a[o[k]][k]) / s[o[k]]
        for i in range(k + 1, n):
            dummy = abs(a[o[i]][k]) / s[o[i]]
            if dummy > big:
                big = dummy
                p = i
        dummy = o[p]
        o[p] = o[k]
        o[k] = dummy

    def ForwardSubstitution(self, A, o, n, b):
        y = [0] * n
        for i in range(0, n):
            y[o[i]] = b[o[i]]

            for j in range(0, i): y[o[i]] -= A[o[i]][j] * y[o[j]]

            y[o[i]] /= float(A[o[i]][i])
        return y

    def BackwardSubtitution(self, A, X, o, n, y):

        X[n - 1] = y[o[n - 1]]
        for i in range(n - 2, -1, -1):
            X[i] = y[o[i]]

            for j in range(n - 1, i, -1):
                X[i] -= A[o[i]][j] * X[j]

    def Substitute(self, A, o, n, b, X):
        y = self.ForwardSubstitution(A, o, n, b)
        self.BackwardSubtitution(A, X, o, n, y)

    def round_sig(self, x, sig=2):
        if x==0:
            return 0
        if sig==-1:
            return x
        return round(x,sig-int(math.floor(math.log10(abs(x))))-1)