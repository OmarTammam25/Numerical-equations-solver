from secant import  secant
if __name__ == '__main__':
    # Input Section
    equ = input('enter the equ: ')
    x0 = input('Enter First Guess: ')
    x1 = input('Enter Second Guess: ')
    e = input('Tolerable Error: ')
    sig = int(input('sig: '))
    N = input('Maximum Step: ')

    # Converting x0 and e to float
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    # Converting N to integer
    N = int(N)
    s = secant(equ,x0,x1,e,sig,N)
    s.solve()
