import math
import timeit

from Algorithms.EquationSolver import EquationSolver


class Fixed_Point_Iteration(EquationSolver):

    def __init__(self, fx, gx, x0, es, max_iter, sig):
        self.fx = fx
        self.gx = gx
        self.x = x0
        self.es = es
        self.max_iter = max_iter
        self.sig = sig


    def solve(self):
        startTime = timeit.default_timer()
        counter =0
        ea=1
        while ea > self.es and counter < self.max_iter:
            xold = self.x
            x = xold
            self.x = eval(self.gx)
            if self.x !=0:
                ea = abs((self.x - xold) / self.x) * 100
                print(ea)
            counter += 1

        endTime = timeit.default_timer()
        time = endTime - startTime
        return self.x



# if __name__ == '__main__':
#     obj = Fixed_Point_Iteration("x**2-2*x-3", "(2*x+3)**0.5", 4, 0.0001, 5, 2)
#     print(obj.solve())