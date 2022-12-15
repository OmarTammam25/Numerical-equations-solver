# This is a sample Python script.
import numpy as np

from Gauss import Gauss
from GaussJordan import GaussJordan

if __name__ == '__main__':
    a = np.array([[2, 3, 1], [4, 1, 4], [3, 4, 6]], dtype = np.double)
    b = np.array([-4, 9, 0], dtype = np.double)
    obj = GaussJordan(a, b)
    sol = obj.gaussJordanElimination()
    print(sol)
