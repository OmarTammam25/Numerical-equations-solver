from LU.LUCrout import LU_Crout
from LU.LUDoolittle import LU_Doolittle
from LU.cholesky import LU_cholesky

if __name__ == '__main__':
    doo = LU_Doolittle()
    crout = LU_Crout()
    cho = LU_cholesky()
    a = [[6, 15, 55],
         [15, 55, 225],
         [55, 225, 979]]
    b = [76, 295, 1259]
    x = [0, 0, 0]
    er=1
    doo.execute(a,b,3,x,0.000001, 9, er)
    print("doo" , x)
    a = [[6, 15, 55],
         [15, 55, 225],
         [55, 225, 979]]
    b = [76, 295, 1259]
    x = [0, 0, 0]
    crout.Crout(a,b,x,0.00001,9,er)
    print("crout",x)
    a = [[6, 15, 55],
         [15, 55, 225],
         [55, 225, 979]]
    b = [76, 295, 1259]
    x = [0, 0, 0]
    cho.execute(a,b,3,x,0.00001,9,er)
    print("cho" , x)


    # # lu = LU_Doolittle()
    # # a = [[25, 5, 1],
    # #      [2.56, -4.8, -1.56],
    # #      [5.76, 3.5, 0.7]]
    # # x = [0, 0, 0]
    # # lu.Substitute(a, [0, 1, 2], 3, [106.8, 177.2, 279.2], x)
    # # print(x)
    # ##to test the whole code
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
    # ##to test the decomposition of cholesky
    # # lu = LU_cholesky()
    # # a = [[6, 15, 55],
    # #      [15, 55, 225],
    # #      [55, 225, 979]]
    # # b = [76,295,1259]
    # # x=[0,0,0]
    # # lu.execute(a,b,3,x,0.0111)
    # # print(x)
    # ##to test the crout
    # # A = [[1, -1, 1, -1],
    # #      [2, -1, 3, 1],
    # #      [1, 1, 2, 2],
    # #      [1, 1, 1, 1]]
    # # b = [1, 2, 3, 3]
    # # X = [0] * len(A)
    # # a = [[25, 5, 1],
    # #      [2.56, -4.8, -1.56],
    # #      [5.76, 3.5, 0.7]]
    # # x = [0, 0, 0]
    # Obj = LU_Crout()
    #
    # Obj.Crout(a, [106.8, 177.2, 279.2], x, 0.00001)
    # print(x)
