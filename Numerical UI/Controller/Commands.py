import time
from decimal import Decimal
import numpy as np
from sympy import *
from math import *

from Algorithms.Gauss import Gauss
from Algorithms.GaussJordan import GaussJordan
from Algorithms.GaussJordanWithCoefficients import GaussJordanWithcoefficients
from Algorithms.GaussWithCoefficients import GaussWithCoefficients
from Algorithms.Gauss_Seidel import GaussSeidel
from Algorithms.Jacobi import Jacobi
from Algorithms.LUCrout import LUCrout
from Algorithms.LUDoolittle import LUDoolittle
from Algorithms.LUcholesky import LUcholesky


class Commands:

    def __init__(self):
        self.nEquations = "2"
        self.method = ""
        self.LUForm = ""
        self.ARE = "0.000001"
        self.precision = "5"
        self.stopCondition = "Number of Iterations"
        self.nIterations = 2
        self.scaling = False
        self.b = []
        self.a = [[]]
        self.initialGuess = []
        self.isLetters = False
        self.initialGuess = np.array([])
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"
        self.rootFinderMethod = 'Bisection'

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
        self.scaling = scale
    def setInitialGuess(self, initialGuess):
        self.initialGuess = np.empty(len(initialGuess))
        for i in range(len(initialGuess)):
            self.initialGuess[i] = initialGuess[i].text()
        self.initialGuess = self.initialGuess.astype(np.double)

    def setRootFinderMethod(self, method):
        self.rootFinderMethod = method


    def getScalling(self):
        return self.scaling

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
        print('yes')
        self.a = np.empty((int(self.nEquations), int(self.nEquations)))
        self.b = np.empty(int(self.nEquations))
        self.initialGuess = np.empty(int(self.nEquations))
        for i in range(0, int(self.nEquations)):
            if b[i].text() == "":
                self.b[i] = "0"
            else:
                self.b[i] = b[i].text()
            if self.LUForm == "Gauss-Seidel" or self.LUForm == "Jacobi-Iteration":
                if initialGuessVector[i].text() == "":
                    self.initialGuess[i] = "0"
                else:
                    self.initialGuess[i] = initialGuessVector[i].text()
            for j in range(0, int(self.nEquations)):
                if a[i][j].text() == "":
                    self.a[i][j] = "0"
                else:
                    self.a[i][j] = a[i][j].text()
        self.a = self.a.astype(np.double)
        self.b = self.b.astype(np.double)
        self.initialGuess = self.initialGuess.astype(np.double)
        print(self.nEquations)
        for i in range(0, int(self.nEquations)):
            print(self.initialGuess[i])

    def validateSyntax(expression):
        try:
            eval(expression)
        except (SyntaxError, NameError, ZeroDivisionError):
            return False
        else:
            return True


    # Calls the methods
    def calculate(self):
        sol = []
        start = time.time()
        if self.LUForm == "Gauss Elimination":
            if(self.isLetters):
                sol =  GaussWithCoefficients(self.a ,self.b, Decimal(self.ARE), int(self.precision)).solve()
            else:
                sol = Gauss(self.a, self.b, Decimal(self.ARE), int(self.precision), self.scaling).solve()
        elif self.LUForm == "Gauss-Jordan":
            if (self.isLetters):
                sol = GaussJordanWithcoefficients(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            else:
                sol = GaussJordan(self.a, self.b, Decimal(self.ARE), int(self.precision), self.scaling).solve()
        elif self.LUForm == "Gauss-Seidel":
            sol = GaussSeidel(self.a, self.b, Decimal(self.ARE), int(self.precision), self.initialGuess, self.nIterations).solve()
        elif self.LUForm == "Jacobi-Iteration":
            sol =  Jacobi(self.a, self.b, Decimal(self.ARE), int(self.precision), self.initialGuess, self.nIterations).solve()
        elif self.LUForm == "LU Decomposition":
            if self.method == "Doolittle Form":
                sol =  LUDoolittle(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            elif self.method == "Crout Form": # TODO CHECK IF IT WORKS
                sol =  LUCrout(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            elif self.method == "Cholesky Form":
                sol = LUcholesky(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()

        end = time.time()
        runTime = end - start
        print (runTime)
        return sol, runTime





