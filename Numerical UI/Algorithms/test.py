from secant import  secant
if __name__ == '__main__':
    # Input Section
    x0 = input('Enter First Guess: ')
    x1 = input('Enter Second Guess: ')
    e = input('Tolerable Error: ')
    N = input('Maximum Step: ')

    # Converting x0 and e to float
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    # Converting N to integer
    N = int(N)

    # Note: You can combine above three section like this
    # x0 = float(input('Enter First Guess: '))
    # x1 = float(input('Enter Second Guess: '))
    # e = float(input('Tolerable Error: '))
    # N = int(input('Maximum Step: '))

    # Starting Secant Method
    secant(x0, x1, e, N)
