import time
from math import floor, log10
from sympy import *
import numpy as np

from EquationSolver import EquationSolver
from Gauss import Gauss
from GaussJordan import GaussJordan
from Gauss_Seidel import GaussSeidel
from Jacobi import Jacobi

if __name__ == '__main__':
    a = [[5, 4, -1], [4, 8, -3], [-5, 4, 10]]
    b = [8, 9, 9]
    x = [-0.25, -0.5, 2.25]
    # Gauss(a, b, 0.00000005, 20).solve()
    print("\n\n\n")
    GaussJordan(a, b, 0.00000005, 20).solve()
