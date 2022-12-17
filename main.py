# This is a sample Python script.
import numpy as np

from Gauss import Gauss
from GaussJordan import GaussJordan
from Jacobi_Itertaions import Jacobi_Iterations
from Gauss_Seidel import Gauss_Seidel
from Crout_LU import Crout_LU

if __name__ == '__main__':
    a = np.array([[2, 3, 1], [4, 1, 4], [3, 4, 6]], dtype = np.double)
    b = np.array([-4, 9, 0], dtype = np.double)
    # obj = GaussJordan(a, b)
    # sol = obj.gaussJordanElimination()
    # print(sol)
    
    

    
    # A = [[9, 2, 3],[1, 12, 9],[4, 6, 14]]
    # b = [7, 2, 1]
    # X = [0, 0, 0]
    # # Obj = Gauss_Seidel()
    # # print(Obj.Gauss_Seidel_Algorithm(A, X, b, 6))
    # Obj = Jacobi_Iterations()
    # Obj.Jacobi_Iterative_Method(A, X, b, 5)


A = [[1,-1,1,-1],[2,-1,3,1],[1,1,2,2],[1,1,1,1]]
b = [1, 2, 3, 3]
X = [0]*len(A)
Obj = Crout_LU()


Obj.Crout(A, b, X, 0.00001)
print(X)
