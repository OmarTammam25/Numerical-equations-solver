class Commands:
    a = [[0 for x in range(100)] for y in range(100)]
    b = []
    initialGuess = []
    def __init__(self):
        self.nEquations = "2"
        self.method = ""
        self.LUForm = ""
        self.ARE = "0.000001"
        self.precision = "5"
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

    ####################################################################################################################

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
                self.a[i][j] = decimal(a[i][j].text())
            print(self.nEquations)
        return True

    def isInitialGuessValid(self, initialGuess):
        for i in range(0, int(self.nEquations)):
            if initialGuess[i].text() == "":
                return False
        return True

    #Calls the methods
    def calculate(self):
        print(self)
        if self.LUForm == "Gauss Elimination":
            print("Gauss")






