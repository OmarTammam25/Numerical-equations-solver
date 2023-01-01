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

from Algorithms.secant import secant
from Algorithms.NewtonRaphson import NewtonRaphson
from Algorithms.Regula_Falsi import Regula_Falsi
from Algorithms.Bisection import Bisection
from Algorithms.Fixed_Point_Iterations import Fixed_Point_Iteration
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
        self.fx = ''
        self.gx = ''
        self.xl = ''
        self.xu = ''
        self.initialGuessRoot = ''
        self.root = ''
        self.sigFig = '5'

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
        print(method)
        self.rootFinderMethod = method

    def setSigFig(self, sigFig):
        self.sigFig = sigFig

    def setFx(self, fx):
        self.fx = fx
    def setGx(self, gx):
        self.gx = gx
    def setXl(self, xl):
        self.xl = xl

    def setXu(self, xu):
        self.xu = xu

    def setInitialGuessRoot(self, initialGuessRoot):
        self.initialGuessRoot = initialGuessRoot

    def getScalling(self):
        return self.scaling

    def getNEquations(self):
        return self.nEquations

    def getRoot(self):
        return self.root
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

    def validateSyntax(self, expression):
        try:
            eval(expression)
        except (SyntaxError, NameError, ZeroDivisionError):
            return False
        else:
            return True

    def findRoot(self):
        start = time.time()
        if self.rootFinderMethod == "Bisection":
            root = Bisection(self.fx, self.xl, self.xu, self.ARE, self.sigFig, self.nIterations).solve()
        if self.rootFinderMethod == "False-Position":
            root = Regula_Falsi(self.fx,self.xl,self.xu,self.ARE,self.sigFig,self.nIterations).solve()
        if self.rootFinderMethod == "Fixed point":
            root = Fixed_Point_Iteration(self.fx,self.gx,self.initialGuessRoot,self.ARE,self.nIterations,self.sigFig).solve()
        if self.rootFinderMethod == "Newton-Raphson":
            root = NewtonRaphson(self.fx,self.initialGuessRoot,self.ARE,self.sigFig,self.nIterations).solve()
        if self.rootFinderMethod == "Secant Method":
            root = secant(self.fx,self.xl,self.xu,self.ARE,self.sigFig,self.nIterations).solve()

        end = time.time()
        runTime = end - start
        print("time: ", runTime)
        return root

    # Calls the methods
    def calculate(self):
        sol = []
        start = time.time()
        if self.LUForm == "Gauss Elimination":
            if (self.isLetters):
                sol = GaussWithCoefficients(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            else:
                sol = Gauss(self.a, self.b, Decimal(self.ARE), int(self.precision), self.scaling).solve()
        elif self.LUForm == "Gauss-Jordan":
            if (self.isLetters):
                sol = GaussJordanWithcoefficients(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            else:
                sol = GaussJordan(self.a, self.b, Decimal(self.ARE), int(self.precision), self.scaling).solve()
        elif self.LUForm == "Gauss-Seidel":
            sol = GaussSeidel(self.a, self.b, Decimal(self.ARE), int(self.precision), self.initialGuess,
                              self.nIterations).solve()
        elif self.LUForm == "Jacobi-Iteration":
            sol = Jacobi(self.a, self.b, Decimal(self.ARE), int(self.precision), self.initialGuess,
                         self.nIterations).solve()
        elif self.LUForm == "LU Decomposition":
            if self.method == "Doolittle Form":
                sol = LUDoolittle(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            elif self.method == "Crout Form":  # TODO CHECK IF IT WORKS
                sol = LUCrout(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()
            elif self.method == "Cholesky Form":
                sol = LUcholesky(self.a, self.b, Decimal(self.ARE), int(self.precision)).solve()

        end = time.time()
        runTime = end - start
        print(runTime)
        return sol, runTime








