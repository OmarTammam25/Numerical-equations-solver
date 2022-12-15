import numpy as np

class Gauss_Seidel:
    
    def Gauss_Seidel_Algorithm(self, A, X, b, MaxIterations):
        
        n = len(X)
        
        for k in range(0, MaxIterations):
            
            for i in range(0, n):
                X[i] = b[i]
                
                for j in range(0, n):
                    if(i == j):
                        continue
                    X[i] -= A[i][j] * X[j]
                
                X[i] /= float(A[i][i])
                
            print(X)

        return X