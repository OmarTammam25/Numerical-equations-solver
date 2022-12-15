from LU.LUDoolittle import LU_Doolittle

if __name__ == '__main__':
    lu = LU_Doolittle()
    # a = [[25, 5, 1],
    #      [2.56, -4.8, -1.56],
    #      [5.76, 3.5, 0.7]]
    # x = [0, 0, 0]
    # lu.Substitute(a, [0, 1, 2], 3, [106.8, 177.2, 279.2], x)
    # print(x)
    a = [[25, 5, 1],
         [64, 8, 1],
         [144, 12, 1]]

    b = [106.8, 177.2, 279.2]
    n = 3
    x = [0, 0, 0]
    tol = .00000000000001
    er = 0
    lu.execute(a, b, n, x, tol, er)
    print(x)
