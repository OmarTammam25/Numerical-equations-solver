# This is a sample Python script.
import time
from math import floor, log10
from sympy import *
import numpy as np

from Gauss import Gauss
from GaussJordan import GaussJordan
from GaussJordanWithCoefficients import GaussJordanWithcoefficients
from GaussWithCoefficients import GaussWithCoefficients


def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

if __name__ == '__main__':
    # a = np.array([[8, 4, -1], [-2, 3, 1], [2, -1, 6]], dtype = np.double)
    # b = np.array([11, 4, 7], dtype = np.double)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = symbols('a1 a2 a3 a4 a5 a6 a7 a8 a9 a10')
    b1, b2, b3 = symbols('b1 b2 b3')

    a = np.array([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
    b = np.array([b1, b2, b3])
    start = time.time()
    er = 1e-12
    obj = GaussJordanWithcoefficients(a, b)
    sol = obj.gaussJordanElimination()
    end = time.time()
    #
    print(sol, '\n', end - start, 's')
