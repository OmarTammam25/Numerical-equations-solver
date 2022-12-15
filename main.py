# This is a sample Python script.
import numpy as np

from Gauss import Gauss
from Gauss_Seidel import Gauss_Seidel
from Jacobi_Itertaions import Jacobi_Iterations

if __name__ == '__main__':
    a = np.array([[1, 1, -1], [6, 2, 2], [-3, 4, 1]], dtype=np.double)
    b = np.array([-3, 2, 1], dtype=np.double)
    len(b)
    # obj = Gauss(a, b)
    # sol = obj.gaussElimination()
    # print(sol)
    
    
    A = [[9, 2, 3],[1, 12, 9],[4, 6, 14]]
    b = [7, 2, 1]
    X = [0, 0, 0]
    # Obj = Gauss_Seidel()
    # print(Obj.Gauss_Seidel_Algorithm(A, X, b, 6))
    Obj = Jacobi_Iterations()
    Obj.Jacobi_Iterative_Method(A, X, b, 5)
