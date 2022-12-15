import numpy as np
from numpy import *

class Jacobi_Iterations:
    
    def Jacobi_Iterative_Method(self, A, X, b, MaxIterations):
        
        
        n = len(X)
        
        
        for k in range(0, MaxIterations):
        
            Xold = array(X)
            
            for i in range(0, n):
                X[i] = b[i]
                
                for j in range(0, n):
                    if(i == j): continue
                    
                    X[i] -= Xold[j] * A[i][j]
                    
                
                X[i] /= float(A[i][i])
                
                
            print(X)

        return X