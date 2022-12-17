from LU.LUDoolittle import LU_Doolittle
from LU.cholesky import LU_cholesky

if __name__ == '__main__':
    # lu = LU_Doolittle()
    # a = [[25, 5, 1],
    #      [2.56, -4.8, -1.56],
    #      [5.76, 3.5, 0.7]]
    # x = [0, 0, 0]
    # lu.Substitute(a, [0, 1, 2], 3, [106.8, 177.2, 279.2], x)
    # print(x)
    ##to test the whole code
    # lu = LU_Doolittle()
    # a = [[25, 5, 1],
    #      [64, 8, 1],
    #      [144, 12, 1]]
    #
    # b = [106.8, 177.2, 279.2]
    # n = 3
    # x = [0, 0, 0]
    # tol = .00000000000001
    # er = 0
    # lu.execute(a, b, n, x, tol, er)
    # print(x)
    ##to test the decomposition of cholesky
    lu = LU_cholesky()
    a = [[6, 15, 55],
         [15, 55, 225],
         [55, 225, 979]]
    b = [76,295,1259]
    x=[0,0,0]
    lu.execute(a,b,3,x,0.0111)
    print(x)
