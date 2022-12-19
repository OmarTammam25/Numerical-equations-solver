import time
from math import floor, log10
from sympy import *
import numpy as np

from GaussJordanWithCoefficients import GaussJordanWithcoefficients

if __name__ == '__main__':
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = symbols('a1 a2 a3 a4 a5 a6 a7 a8 a9 a10')
    b1, b2, b3 = symbols('b1 b2 b3')

    a = [[5 * a1, 2 * a2, 1 * a3],
         [4 * a1, 4 * a2, -4 * a3],
         [-1 * a1, 2 * a2, -6 * a3]]

    b = [8, 16, 9]
    x = [-0.25, -0.5, 2.25]
    # Jacobi(a, b, 0.00000005, -1, x).solve()
    print("\n\n\n")
    print(GaussJordanWithcoefficients(a, b, 0.000005, -1, x).solve())
