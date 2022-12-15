# This is a sample Python script.
import numpy as np

from Gauss import Gauss

if __name__ == '__main__':
    a = np.array([[1, 1, -1], [6, 2, 2], [-3, 4, 1]], dtype=np.double)
    b = np.array([-3, 2, 1], dtype=np.double)
    len(b)
    obj = Gauss(a, b)
    sol = obj.gaussElimination()
    print(sol)
