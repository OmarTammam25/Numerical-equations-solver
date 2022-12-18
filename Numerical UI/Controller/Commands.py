import numpy as np


class Commands:
    def __init__(self):
        self.nEquations = 2
        self.method = ""
        self.LUForm = ""
        self.ARE = 0.000001
        self.precision = 5
        self.stopCondition = "Number of Iterations"
        self.nIterations = 2
        self.b = []
        self.a = [[]]
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

    def getTitle(self):
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"
        return self.title

    # Check validity and form arrays
    def areFilled(self, a, b):
        self.a = np.empty((self.nEquations, self.nEquations), np.double)
        self.b = np.empty(self.nEquations, np.double)
        for i in range(0, self.nEquations):
            if b[i].text() == "":
                return False
            self.b[i] = b[i].text()
            for j in range(0, self.nEquations):
                if a[i][j].text() == "":
                    return False
                self.a[i][j] = a[i][j].text()
            print(self.nEquations)
        return True

    #Calls the methods
    def calculate(self):
        print(self)
        if self.LUForm == "Gauss Elimination":
            print("Gauss")






