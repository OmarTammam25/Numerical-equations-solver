import math
import timeit


class LU_Crout:

    def IsSingular(self, A, s, o, k, tol):
        if ((abs(A[o[k]][k]) / s[o[k]]) < tol): return True
        return False

    def Crout(self, A, b, X, tol, sig=2, er=0):
        startTime = timeit.default_timer()
        n = len(A)
        o = [0] * n
        s = [0] * n

        self.Decompose(A, tol, o, s, sig)
        if (er == -1): return
        self.Substitute(A, o, n, b, X, sig)
        endTime = timeit.default_timer()
        time = endTime - startTime
        print(round(time * 10 ** 3, 5), "ms")

    def Decompose(self, A, tol, o, s, sig, er=0):

        n = len(A)

        for i in range(0, n):
            o[i] = i
            s[i] = abs(A[i][0])

            for j in range(1, n):
                if (abs(A[i][j] > s[i])):
                    s[i] = abs(A[i][j])

        for i in range(0, n):
            self.Pivot(A, o, s, n, i)

            if (self.IsSingular(A, s, o, i, tol)):
                er = -1
                return

            for j in range(i, n):

                for k in range(0, i): A[o[j]][i] = self.round_sig(A[o[j]][i], sig) - self.round_sig(A[o[j]][k],
                                                                                                    sig) * self.round_sig(
                    A[o[k]][i], sig)

            for j in range(i, n):

                if i == j: continue

                for k in range(0, i): A[o[i]][j] = self.round_sig(A[o[i]][j], sig) - self.round_sig(A[o[i]][k],
                                                                                                    sig) * self.round_sig(
                    A[o[k]][j], sig)

                if (A[o[i]][i] == 0):
                    er = -1
                    return

                A[o[i]][j] = self.round_sig(A[o[i]][j], sig) / self.round_sig(A[o[i]][i], sig)

    def Pivot(self, a, o, s, n, k):
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

    def ForwardSubstitution(self, A, o, n, b, sig):
        y = [0] * n
        for i in range(0, n):
            y[o[i]] = b[o[i]]
            for j in range(0, i): y[o[i]] = self.round_sig(y[o[i]], sig) - self.round_sig(A[o[i]][j],
                                                                                          sig) * self.round_sig(y[o[j]],
                                                                                                                sig)

            y[o[i]] = self.round_sig(y[o[i]], sig) / self.round_sig(A[o[i]][i], sig)
        return y

    def BackwardSubtitution(self, A, X, o, n, y, sig):

        X[n - 1] = self.round_sig(y[o[n - 1]], sig)
        for i in range(n - 2, -1, -1):
            X[i] = self.round_sig(y[o[i]], sig)

            for j in range(n - 1, i, -1): X[i] = self.round_sig(X[i], sig) - self.round_sig(A[o[i]][j],
                                                                                            sig) * self.round_sig(X[j],
                                                                                                                  sig)

    def Substitute(self, A, o, n, b, X, sig):
        y = self.ForwardSubstitution(A, o, n, b, sig)
        self.BackwardSubtitution(A, X, o, n, y, sig)

    def round_sig(self, x, sig=2):
        if x == 0:
            return 0
        if sig == -1:
            return x
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

