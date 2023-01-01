import math
import timeit
from sympy import *
from Algorithms.EquationSolver import EquationSolver


class Fixed_Point_Iteration():
    def __init__(self, fx, gx, x0, es, max_iter, sig):
        self.fx = fx
        self.gx = gx
        self.x = float(x0)
        self.es = float(es)
        self.max_iter = int(max_iter)
        self.sig = int(sig)


    def solve(self):
        x = symbols('x')
        f = self.fx.replace("^", "**")
        g = self.gx.replace("^", "**")
        f = lambdify(x, f)
        g = lambdify(x, g)


        startTime = timeit.default_timer()
        counter = 0
        ea=1
        while ea > self.es and counter < self.max_iter:
            xold = self.round_sig(self.x, self.sig)
            self.x = self.round_sig(g(xold),self.sig)#TODO
            if self.x !=0:
                ea = abs((self.x - xold) / self.x) * 100
            counter += 1
            print('iteration:', counter, '  x =',self.x,'   ea =', ea,'%')
        endTime = timeit.default_timer()
        time = endTime - startTime
        # print("time: ",time)
        return self.x

    def round_sig(self, x, sig=-1):
        if (sig == -1):
            return x
        if x == 0:
            return 0
        return float('%.*g' % (sig, x))
