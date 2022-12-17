
class Commands:

    def __init__(self):
        self.nEquations = 2
        self.method = ""
        self.LUForm = ""
        self.ARE = 0.000001
        self.precision = 5
        self.stopCondition = "Number of Iterations"
        self.nIterations = 2
#       self.a 2d array
        self.b = []
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

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def getTitle(self):
        self.title = f"Solving {self.nEquations} x {self.nEquations} System of Equations"
        return self.title

#    def calculate(self, coef):



