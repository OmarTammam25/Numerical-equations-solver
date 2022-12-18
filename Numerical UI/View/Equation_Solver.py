from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from Controller.Commands import Commands
from View.Initial_Guess import Ui_InitialGuess
from View.Solution_Window import Ui_resultsWindow


class Ui_MainWindow(object):
    coef = [[0 for x in range(100)] for y in range(100)]  # Coefficient matrix
    b = []  # results
    command = Commands()
    solutionWindow = Ui_resultsWindow()
    initialGuessWindow = Ui_InitialGuess()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1986, 1223)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1901, 991))
        self.scrollArea.setStyleSheet("background-color:rgb(255, 253, 184)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 9000, 2900))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(9000, 2900))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.bVector = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.bVector.setGeometry(QtCore.QRect(250, 240, 100, 5000))
        self.bVector.setObjectName("bVector")
        self.bVectorLayout = QtWidgets.QVBoxLayout(self.bVector)
        self.bVectorLayout.setContentsMargins(10, 0, 10, 0)
        self.bVectorLayout.setObjectName("bVectorLayout")

        self.variables = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.variables.setGeometry(QtCore.QRect(275, 190, 8630, 50))
        self.variables.setObjectName("variables")
        self.variablesLayout = QtWidgets.QHBoxLayout(self.variables)
        self.variablesLayout.setContentsMargins(10, 0, 10, 0)

        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(350, 240, 8500, 2600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")

        #########################################################################################################

        # Coefficient matrix formation
        self.validator = QDoubleValidator()
        for i in range(0, 100):
            for j in range(0, 100):
                self.e = QtWidgets.QLineEdit(self.gridLayoutWidget)
                self.e.setStyleSheet("background-color:rgb(255, 255, 255)\n")
                self.e.setValidator(self.validator)
                self.gridLayout.addWidget(self.e, i +10, j)
                if i < 2 and j < 2:
                    self.e.show()
                    print(i)
                else:
                    self.e.setStyleSheet("background-color:rgb(255, 253, 184)\n"
                                         "border-color: rgb(255, 253, 184)")
                    self.e.setDisabled(True)
                self.coef[i][j] = self.e

        ############################################################################################################

        self.columnView = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setGeometry(QtCore.QRect(20, 140, 191, 601))
        self.columnView.setStyleSheet("background-color:rgb(255, 253, 184);\n"
                                      "border-color: rgb(0, 0, 100);")
        self.columnView.setObjectName("columnView")

        self.nEquationDisplayed = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed.setGeometry(QtCore.QRect(220, 120, 700, 61))
        self.nEquationDisplayed.setStyleSheet("color: rgb(121, 104, 62);\n"
                                              "font: 25pt \"Segoe script\";\n"
                                              "font-weight: bold")
        self.nEquationDisplayed.setObjectName("nEquationDisplayed")
        self.methodLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.methodLable.setGeometry(QtCore.QRect(40, 150, 151, 20))
        self.methodLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                       "font: 11pt \"Century Gothic\";\n"
                                       "font-weight: bold")
        self.methodLable.setObjectName("methodLabel")

        ################################################################################################################

        # Labels
        self.nEquationsLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationsLable.setGeometry(QtCore.QRect(30, 220, 151, 20))
        self.nEquationsLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                           "font: 11pt \"Century Gothic\";\n"
                                           "font-weight: bold")
        self.nEquationsLable.setObjectName("nEquationsLable")
        self.LULable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LULable.setGeometry(QtCore.QRect(30, 290, 111, 16))
        self.LULable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                   "font: 11pt \"Century Gothic\";\n"
                                   "font-weight: bold")
        self.LULable.setObjectName("LULable")

        self.ARELable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ARELable.setGeometry(QtCore.QRect(30, 360, 171, 16))
        self.ARELable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                    "font: 11pt \"Century Gothic\";\n"
                                    "font-weight: bold")
        self.ARELable.setObjectName("ARELable")
        self.precisionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.precisionLable.setGeometry(QtCore.QRect(30, 430, 121, 16))
        self.precisionLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                          "font: 11pt \"Century Gothic\";\n"
                                          "font-weight: bold")
        self.precisionLable.setObjectName("precisionLable")
        self.stopConditionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.stopConditionLable.setGeometry(QtCore.QRect(30, 490, 161, 20))
        self.stopConditionLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                              "font: 11pt \"Century Gothic\";\n"
                                              "font-weight: bold")
        self.stopConditionLable.setObjectName("stopConditionLable")

        self.nIterationLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nIterationLable.setGeometry(QtCore.QRect(30, 580, 151, 21))
        self.nIterationLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                           "font: 11pt \"Century Gothic\";\n"
                                           "font-weight: bold")
        self.nIterationLable.setObjectName("nIterationLable")

        self.nEquationDisplayed_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed_2.setGeometry(QtCore.QRect(30, 40, 581, 61))
        self.nEquationDisplayed_2.setStyleSheet("color: rgb(121, 104, 62);\n"
                                                "font: 25pt \"Segoe script\";\n"
                                                "font-weight: bold")
        self.nEquationDisplayed_2.setObjectName("nEquationDisplayed_2")

        ################################################################################################################

        # LU Drop-Down List
        self.method = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.method.setEnabled(False)
        self.method.setGeometry(QtCore.QRect(30, 320, 151, 21))
        self.method.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.method.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.method.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")

        ################################################################################################################

        # Number of Equations
        self.nEquations = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.nEquations.setGeometry(QtCore.QRect(30, 250, 151, 21))
        self.nEquations.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.nEquations.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.nEquations.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nEquations.setMinimum(2)
        self.nEquations.setMaximum(100)
        self.nEquations.setObjectName("nEquations")
        self.nEquations.textChanged.connect(self.showTitleAndChangeCells)

        ################################################################################################################

        # Method to solve the equation
        self.LU = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.LU.setGeometry(QtCore.QRect(30, 180, 151, 22))
        self.LU.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LU.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LU.setObjectName("LU")
        self.LU.addItem("")
        self.LU.addItem("")
        self.LU.addItem("")
        self.LU.addItem("")
        self.LU.addItem("")
        self.LU.currentTextChanged.connect(self.methodCheck)

        ################################################################################################################

        # Precision
        self.precision = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.precision.setGeometry(QtCore.QRect(30, 450, 151, 22))
        self.precision.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.precision.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.precision.setMinimum(2)
        self.precision.setMaximum(20)
        self.precision.setProperty("value", 2)
        self.precision.setObjectName("precision")

        ################################################################################################################

        # Absolute Relative Error
        self.ARE = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.ARE.setEnabled(False)
        self.ARE.setGeometry(QtCore.QRect(30, 390, 151, 22))
        self.ARE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ARE.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.ARE.setDecimals(6)
        self.ARE.setSingleStep(1e-06)
        self.ARE.setProperty("value", 1e-06)
        self.ARE.setObjectName("doubleSpinBox")

        ################################################################################################################

        # Stop Condition
        self.stopContition = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.stopContition.setEnabled(False)
        self.stopContition.setGeometry(QtCore.QRect(30, 530, 151, 22))
        self.stopContition.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.stopContition.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopContition.setObjectName("stopContition")
        self.stopContition.addItem("")
        self.stopContition.addItem("")
        self.stopContition.addItem("")
        self.stopContition.currentTextChanged.connect(self.checkStop)

        ################################################################################################################

        # number of iterations
        self.nIteration = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.nIteration.setEnabled(False)
        self.nIteration.setGeometry(QtCore.QRect(30, 620, 151, 22))
        self.nIteration.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nIteration.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.nIteration.setMinimum(2)
        self.nIteration.setMaximum(150)
        self.nIteration.setObjectName("nIteration")

        ################################################################################################################

        # b cells
        for i in range(0, 200):
            self.e = QtWidgets.QLineEdit(self.bVector)
            self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.e.setValidator(self.validator)
            self.bVectorLayout.addWidget(self.e)
            if i < 2:
                self.e.show()
            else:
                self.e.setStyleSheet("background-color:rgb(255, 253, 184)\n"
                                     "border-color: rgb(255, 253, 184)")
                self.e.setDisabled(True)
            self.b.append(self.e)

        ################################################################################################################

        # Labels
        for i in range(0, 101):
            self.e = QtWidgets.QLabel(self.variables)

            if i == 0:
                self.e.setStyleSheet("color:rgb(121, 104, 62)\n"
                                     "font: 20pt italic \"Segue script\";\n"
                                     "font-weight: bold")
                self.e.setText("B Vector")
                self.variablesLayout.addWidget(self.e)
                continue

            self.e.setStyleSheet("color:rgb(121, 104, 62)\n"
                                 "font: 20pt bold italic \"Segue script\";\n"
                                 "font-weight: bold")
            self.e.setText(f"X{i}")
            self.variablesLayout.addWidget(self.e)

        ################################################################################################################

        # Calculate button
        self.calcutateButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calcutateButton.setGeometry(QtCore.QRect(30, 670, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calcutateButton.setFont(font)
        self.calcutateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcutateButton.setAcceptDrops(True)
        self.calcutateButton.setStyleSheet("background-color:rgb(200, 176, 127);\n"
                                           "color:12px rgb(106, 98, 71);\n"
                                           "font-weight: bold;")
        self.calcutateButton.setObjectName("calcutateButton")
        self.calcutateButton.clicked.connect(self.start)

        ################################################################################################################

        self.programTitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.programTitle.setGeometry(QtCore.QRect(-140, 1140, 50000, 6000))
        self.programTitle.setMinimumSize(QtCore.QSize(10000, 6000))
        self.programTitle.setStyleSheet("color: rgb(121, 104, 62);\n"
                                        "font: 25pt \"Century Gothic\";\n"
                                        "font-weight: bold")
        self.programTitle.setText("")
        self.programTitle.setObjectName("programTitle")
        self.programTitle.raise_()
        self.gridLayoutWidget.raise_()
        self.columnView.raise_()
        self.nEquationDisplayed.raise_()
        self.methodLable.raise_()
        self.method.raise_()
        self.nEquationsLable.raise_()
        self.nEquations.raise_()
        self.LULable.raise_()
        self.LU.raise_()
        self.precision.raise_()
        self.ARELable.raise_()
        self.precisionLable.raise_()
        self.ARE.raise_()
        self.stopConditionLable.raise_()
        self.stopContition.raise_()
        self.nIterationLable.raise_()
        self.nIteration.raise_()
        self.calcutateButton.raise_()
        self.nEquationDisplayed_2.raise_()
        self.variables.raise_()
        self.variables.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.frame)
        self.nEquationDisplayed.setText(self.command.getTitle())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def methodCheck(self):
        method = self.LU.currentText()
        if method == "LU Decomposition":
            self.method.setEnabled(True)
            self.stopContition.setEnabled(False)
        elif method == "Gauss-Seidel" or method == "Jacobi-Iteration":
            self.method.setEnabled(False)
            self.stopContition.setEnabled(True)
            self.initialGuessWindow.nEquations = int(self.nEquations.text())
            self.open_initial_guess_window()
        else:
            self.method.setEnabled(False)
            self.stopContition.setEnabled(False)
            self.nIteration.setEnabled(False)
            self.ARE.setEnabled(False)

    def checkStop(self):
        stop = self.stopContition.currentText()
        if stop == "Number of Iterations":
            self.nIteration.setEnabled(True)
            self.ARE.setEnabled(False)
        elif stop == "Absolute Relative Error":
            self.nIteration.setEnabled(False)
            self.ARE.setEnabled(True)
        else:
            self.nIteration.setEnabled(True)
            self.ARE.setEnabled(True)

    def showTitleAndChangeCells(self):
        n = int(self.nEquations.text())
        self.command.setNEquations(self.nEquations.text())
        self.nEquationDisplayed.setText(self.command.getTitle())

        # only one-step increment is allowed!!
        # increase number of equations
        if not (self.gridLayout.itemAt(n - 1).widget().isEnabled()):
            self.bVectorLayout.itemAt(n - 1).widget().setEnabled(True)
            self.bVectorLayout.itemAt(n - 1).widget().setStyleSheet("background-color:rgb(255, 255, 255)")
            for i in range(0, n):  # Horizontal increment
                self.gridLayout.itemAt(100 * (n - 1) + i).widget().setEnabled(True)
                self.gridLayout.itemAt(100 * (n - 1) + i).widget().setStyleSheet("background-color:rgb(255, 255, 255)")
            for j in range(0, n):  # Vertical increment
                self.gridLayout.itemAt(100 * j + (n - 1)).widget().setEnabled(True)
                self.gridLayout.itemAt(100 * j + (n - 1)).widget().setStyleSheet("background-color:rgb(255, 255, 255)")
        else:
            # decrease number of equations
            self.bVectorLayout.itemAt(n).widget().setEnabled(False)
            self.bVectorLayout.itemAt(n).widget().setStyleSheet("background-color:rgb((255, 253, 184)")
            for i in range(0, n):  # Horizontal decrement
                self.gridLayout.itemAt(100 * n + i).widget().setEnabled(False)
                self.gridLayout.itemAt(100 * n + i).widget().setStyleSheet("background-color:rgb(255, 253, 184)")
            for j in range(0, n + 1):  # Vertical decrement
                self.gridLayout.itemAt(100 * j + n).widget().setEnabled(False)
                self.gridLayout.itemAt(100 * j + n).widget().setStyleSheet("background-color:rgb((255, 253, 184)")

    def start(self):

        if self.command.areFilled(self.coef, self.b):
            self.command.setNIterations(self.nIteration.text())
            self.command.setARE(self.ARE.text())
            self.command.setPrecision(self.precision.text())
            self.command.setLUForm(self.LU.currentText())
            self.command.setStopCondition(self.stopContition.currentText())
            self.command.setNEquations(self.nEquations.text())
            self.command.setMethod(self.method.currentText())
        self.command.calculate()
        self.open_solution_window()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equations Solver"))
        self.nEquationDisplayed.setText(_translate("MainWindow", "Solving 2 x 2 System of Equations"))
        self.methodLable.setText(_translate("MainWindow", "Choose Method"))
        self.method.setCurrentText(_translate("MainWindow", "Downlittle Form"))
        self.method.setItemText(0, _translate("MainWindow", "Downlittle Form"))
        self.method.setItemText(1, _translate("MainWindow", "Crout Form" ""))
        self.method.setItemText(2, _translate("MainWindow", "Cholesky Form"))
        self.nEquationsLable.setText(_translate("MainWindow", "Number of Equations"))
        self.LULable.setText(_translate("MainWindow", "LU Format"))
        self.LU.setItemText(0, _translate("MainWindow", "Gauss Elimination"))
        self.LU.setItemText(1, _translate("MainWindow", "Gauss-Jordan"))
        self.LU.setItemText(2, _translate("MainWindow", "LU Decomposition"))
        self.LU.setItemText(3, _translate("MainWindow", "Gauss-Seidel"))
        self.LU.setItemText(4, _translate("MainWindow", "Jacobi-Iteration"))
        self.ARELable.setText(_translate("MainWindow", "Absolute Relative  Error"))
        self.precisionLable.setText(_translate("MainWindow", "Precision"))
        self.stopConditionLable.setText(_translate("MainWindow", "Stopping condition"))
        self.stopContition.setItemText(0, _translate("MainWindow", "Number of Iterations"))
        self.stopContition.setItemText(1, _translate("MainWindow", "Absolute Relative Error"))
        self.stopContition.setItemText(2, _translate("MainWindow", "both"))
        self.nIterationLable.setText(_translate("MainWindow", "Number of iterations"))
        self.calcutateButton.setText(_translate("MainWindow", "Calculate"))
        self.nEquationDisplayed_2.setText(_translate("MainWindow", "Equations Solver"))

    def open_initial_guess_window(self):
        self.window = QtWidgets.QMainWindow()
        self.initialGuessWindow.setupUi(self.window)
        self.window.show()

    def open_solution_window(self):
        self.window = QtWidgets.QMainWindow()
        self.solutionWindow.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
