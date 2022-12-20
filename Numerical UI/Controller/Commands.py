from unicodedata import decimal
import numpy as np

from Controller.Gauss import Gauss


class Commands:
    initialGuess = []
    def __init__(self):
        self.nEquations = "2"
        self.method = ""
        self.LUForm = ""
        self.ARE = "0.000001"
        self.precision = "5"
        self.stopCondition = "Number of Iterations"
        self.nIterations = 2
        self.scalling = False
        self.b = []
        self.a = [[]]
        self.isLetters = False
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"

    def setNEquations(self, n):
        self.nEquations = n

    def setMethod(self, method):
        self.method = method

    def setARE(self, ARE):
        self.ARE = ARE

    def setLUForm(self, LUForm):
        self.LUForm = LUForm

    def setPrecision(self, precision):
        self.precision = precision

    def setStopCondition(self, stopCondition):
        self.stopCondition = stopCondition

    def setNIterations(self, n):
        self.nIterations = n

    def setLetters(self, formate):
        self.isLetters = formate

    def setScalling(self, scale):
        self.scalling = scale

    def getScalling(self):
        return self.scalling

    def getNEquations(self):
        return self.nEquations

    def getMethod(self):
        return self.method

    def getARE(self):
        return self.ARE

    def getLUForm(self):
        return self.LUForm

    def getPrecision(self):
        return self.precision

    def getStopCondition(self):
        return self.stopCondition

    def getNIterations(self):
        return self.nIterations

    def getTitle(self):
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"
        return self.title

    # Check validity and form arrays
    def fill(self, a, b, initialGuessVector):
        self.a = np.empty((int(self.nEquations), int(self.nEquations)))
        self.b = np.empty(int(self.nEquations))
        self.initialGuess = np.empty(int(self.nEquations))
        for i in range(0, int(self.nEquations)):
            if b[i].text() == "":
                self.b[i] = "0"
            else:
                self.b[i] = b[i].text()
            if self.method == "Gauss-Siedel" or self.method == "Jacobi-Iterations":
                if initialGuessVector[i] == "":
                    self.initialGuess[i] = "0"
                else:
                    self.initialGuess = initialGuessVector[i]
            for j in range(0, int(self.nEquations)):
                if a[i][j].text() == "":
                    self.a[i][j] = "0"
                else:
                    self.a[i][j] = a[i][j].text()
        self.a = self.a.astype(np.double)
        self.b = self.b.astype(np.double)
        self.initialGuess = self.initialGuess.astype(np.double)

    #Calls the methods
    def calculate(self):
        sol = 0.0
        try:
            if self.LUForm == "Gauss Elimination":
                mySol =  Gauss(self.a, self.b, 0.00000005, 20, False).solve()
            return mySol
        except:
            print('error')
            return [-1] * int(self.nEquations)

        #     if(isLetterCoefficients):
        #         sol = GaussWithCoefficients(a,b, self.ARE, self.precision)
        #     else:
        #         sol = Gauss.solve(a, b, self.ARE, self.precision)
        # elif self.LUForm == "Gauss-Jordan":
        #     if (isLetterCoefficients):
        #         sol = GaussJordanWithCofficients(a, b, self.ARE, self.precision)
        #     else:
        #         sol = GaussJordan(a, b, self.ARE, self.precision)
        # elif self.LUForm == "Gauss-Seidel":
        #     sol = GaussSeidel(a, b, self.ARE, self.precision)
        # elif self.LUForm == "Jacobi-Iteration":
        #     sol = Jacobi(a, b, self.ARE, self.precision)

        #solution is stored in sol




