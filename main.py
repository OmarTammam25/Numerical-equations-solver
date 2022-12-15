# This is a sample Python script.
import numpy as np

from Gauss import Gauss

if __name__ == '__main__':
    a = np.array([[2, 3, 1], [4, 1, 4], [3, 4, 6]], dtype = np.double)
    b = np.array([-4, 9, 0], dtype = np.double)
    obj = GaussJordan(a, b)
    sol = obj.gaussJordanElimination()
    print(sol)
    
    
    # A = [[9, 2, 3],[1, 12, 9],[4, 6, 14]]
    # b = [7, 2, 1]
    # X = [0, 0, 0]
    # # Obj = Gauss_Seidel()
    # # print(Obj.Gauss_Seidel_Algorithm(A, X, b, 6))
    # Obj = Jacobi_Iterations()
    # Obj.Jacobi_Iterative_Method(A, X, b, 5)
