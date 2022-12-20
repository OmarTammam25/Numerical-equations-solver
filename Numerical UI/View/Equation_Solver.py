from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator
from Controller.Commands import Commands
from View.Solution_Window import Ui_resultsWindow


class Ui_MainWindow(object):
    coef = [[0 for x in range(100)] for y in range(100)]  # Coefficient matrix
    b = []  # results
    initialGuessVector = []
    command = Commands()
    solutionWindow = Ui_resultsWindow()
    prev = 3

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
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1901, 975))
        self.scrollArea.setStyleSheet("background-color:rgb(227, 199, 240)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2000, 2900))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(9000, 3400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        ################################################################################################################

        # Grid Layout
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 190, 8500, 2600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")

        ################################################################################################################

        # Grid Formation
        self.doubleValidator = QDoubleValidator()
        self.strValidator = QRegExpValidator()
        for i in range(0, 101):
            for j in range(0, 101):
                if i == 0:
                    self.e = QtWidgets.QLabel(self.gridLayoutWidget)
                    if j == 0:
                        self.e.setStyleSheet("color:rgb(121, 104, 62)\n"
                                             "font: 20pt italic \"Segue script\";\n"
                                             "font-weight: bold")
                        self.e.setText("B Vector")
                        self.gridLayout.addWidget(self.e, i + 4, j)
                        continue
                    self.e.setStyleSheet("color:rgb(121, 104, 62)\n"
                                         "font: 20pt bold italic \"Segue script\";\n"
                                         "font-weight: bold")
                    self.e.setText(f"X{j}")
                    self.gridLayout.addWidget(self.e, i + 4, j)
                    continue
                self.e = QtWidgets.QLineEdit(self.gridLayoutWidget)
                self.e.setStyleSheet("background-color:rgb(255, 255, 255)\n")
                self.e.setValidator(self.doubleValidator)
                self.gridLayout.addWidget(self.e, i + 4, j)
                if i < 4 and j < 4:
                    self.e.show()
                    if j == 0:
                        self.b.append(self.e)
                        continue
                else:
                    self.e.setStyleSheet("background-color:rgb(255, 253, 184)\n"
                                         "border-color: rgb(255, 253, 184)")
                    self.e.setDisabled(True)
                if j == 0:
                    self.b.append(self.e)
                else:
                    self.coef[i - 1][j - 1] = self.e

        ################################################################################################################

        # Tools Layout
        self.columnView = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setGeometry(QtCore.QRect(20, 140, 191, 680))
        self.columnView.setStyleSheet("background-color:rgb(227, 199, 240);\n"
                                      "border-color: rgb(0, 0, 100);\n"
                                      "border-radius: 2px;")
        self.columnView.setObjectName("columnView")

        ################################################################################################################

        # All Labels
        self.nEquationDisplayed = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed.setGeometry(QtCore.QRect(220, 120, 620, 40))
        self.nEquationDisplayed.setStyleSheet("font: 25pt \"Segoe script\";\n"
                                              "font-weight: bold")
        self.nEquationDisplayed.setObjectName("nEquationDisplayed")

        self.methodLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.methodLable.setGeometry(QtCore.QRect(40, 150, 151, 20))
        self.methodLable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                       "font-weight: bold;\n"
                                       "background-color:rgb(227, 199, 240)")
        self.methodLable.setObjectName("methodLabel")

        self.variablesForm = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.variablesForm.setGeometry(QtCore.QRect(30, 290, 151, 20))
        self.variablesForm.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                         "font-weight: bold;\n"
                                         "background-color:rgb(227, 199, 240)")
        self.variablesForm.setObjectName("methodLabel")

        self.nEquationsLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationsLable.setGeometry(QtCore.QRect(30, 220, 151, 20))
        self.nEquationsLable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                           "font-weight: bold;\n"
                                           "background-color:rgb(227, 199, 240)")
        self.nEquationsLable.setObjectName("nEquationsLable")

        self.LULable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LULable.setGeometry(QtCore.QRect(30, 370, 111, 16))
        self.LULable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                   "font-weight: bold;\n"
                                   "background-color:rgb(227, 199, 240)")
        self.LULable.setObjectName("LULable")

        self.ARELable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ARELable.setGeometry(QtCore.QRect(30, 440, 171, 16))
        self.ARELable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                    "font-weight: bold;\n"
                                    "background-color:rgb(227, 199, 240)")
        self.ARELable.setObjectName("ARELable")

        self.precisionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.precisionLable.setGeometry(QtCore.QRect(30, 510, 121, 16))
        self.precisionLable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                          "font-weight: bold;\n"
                                          "background-color:rgb(227, 199, 240)")
        self.precisionLable.setObjectName("precisionLable")

        self.stopConditionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.stopConditionLable.setGeometry(QtCore.QRect(30, 570, 161, 20))
        self.stopConditionLable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                              "font-weight: bold;\n"
                                              "background-color:rgb(227, 199, 240)")
        self.stopConditionLable.setObjectName("stopConditionLable")

        self.nIterationLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nIterationLable.setGeometry(QtCore.QRect(30, 640, 151, 21))
        self.nIterationLable.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                           "font-weight: bold;\n"
                                           "background-color:rgb(227, 199, 240)")
        self.nIterationLable.setObjectName("nIterationLable")

        self.nEquationDisplayed_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed_2.setGeometry(QtCore.QRect(30, 30, 581, 61))
        self.nEquationDisplayed_2.setStyleSheet("font: 25pt \"Segoe script\";\n"
                                                "font-weight: bold")
        self.nEquationDisplayed_2.setObjectName("nEquationDisplayed_2")

        self.programTitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.programTitle.setGeometry(QtCore.QRect(-140, 1140, 50000, 6000))
        self.programTitle.setMinimumSize(QtCore.QSize(10000, 6000))
        self.programTitle.setStyleSheet("font: 25pt \"Century Gothic\";\n"
                                        "font-weight: bold")

        self.line = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.line.setGeometry(30, 800, 151, 61)
        self.line.setStyleSheet("font: 25pt \"Segoe script\";\n"
                                "font-weight: bold")

        self.initialGeussLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.initialGeussLable.setGeometry(QtCore.QRect(30, 870, 141, 16))
        self.initialGeussLable.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                             "font-weight: bold;\n"
                                             "background-color:rgb(227, 199, 240)")
        self.initialGeussLable.setObjectName("initialGuessLabel")
        self.initialGeussLable.setVisible(False)

        ################################################################################################################

        # LU Drop-Down List
        self.method = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.method.setEnabled(False)
        self.method.setGeometry(QtCore.QRect(30, 400, 151, 21))
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
        self.nEquations.setValue(3)
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

        # Equations format
        self.format = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.format.setGeometry(QtCore.QRect(30, 325, 151, 22))
        self.format.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.format.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.format.setObjectName("equationsFormate")
        self.format.addItem("")
        self.format.addItem("")
        # self.format.currentTextChanged.connect(self.changeFormat)

        ################################################################################################################

        # Precision
        self.precision = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.precision.setGeometry(QtCore.QRect(30, 530, 151, 22))
        self.precision.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.precision.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.precision.setMinimum(2)
        self.precision.setMaximum(50)
        self.precision.setProperty("value", 50)
        self.precision.setObjectName("precision")

        ################################################################################################################

        # Absolute Relative Error
        self.ARE = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.ARE.setEnabled(False)
        self.ARE.setGeometry(QtCore.QRect(30, 470, 151, 22))
        self.ARE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ARE.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.ARE.setDecimals(6)
        self.ARE.setMinimum(0.000001)
        self.ARE.setSingleStep(1e-06)
        self.ARE.setProperty("value", 1e-06)
        self.ARE.setObjectName("doubleSpinBox")

        ################################################################################################################

        # Stop Condition
        self.stopContition = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.stopContition.setEnabled(False)
        self.stopContition.setGeometry(QtCore.QRect(30, 610, 151, 22))
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
        self.nIteration.setGeometry(QtCore.QRect(30, 670, 151, 22))
        self.nIteration.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nIteration.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.nIteration.setMinimum(2)
        self.nIteration.setMaximum(500)
        self.nIteration.setValue(500)
        self.nIteration.setObjectName("nIteration")

        ################################################################################################################

        # scaling
        self.scaling = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.scaling.setGeometry(QtCore.QRect(30, 710, 151, 22))
        self.scaling.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scaling.setObjectName("scaling")

        # scaling label
        self.scalingLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scalingLabel.setGeometry(QtCore.QRect(50, 710, 151, 22))
        self.scalingLabel.setStyleSheet("font: 11pt \"Century Gothic\";\n"
                                        "font-weight: bold;\n"
                                        "background-color:rgb(227, 199, 240)")
        self.scalingLabel.setObjectName("scaling")

        ################################################################################################################

        # Calculate Button
        self.calcutateButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calcutateButton.setGeometry(QtCore.QRect(30, 750, 151, 61))
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
                                           "font-weight: bold;\n"
                                           "border-radius: 5px")
        self.calcutateButton.setObjectName("calcutateButton")
        self.calcutateButton.clicked.connect(self.start)

        ################################################################################################################

        # Initial guess grid
        self.intialGuess = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.intialGuess.setGeometry(QtCore.QRect(30, 900, 120, 100 * 25))
        self.intialGuess.setObjectName("intialGuessLabels")
        self.intialGuessLayout = QtWidgets.QGridLayout(self.intialGuess)
        self.intialGuessLayout.setContentsMargins(10, 0, 10, 0)
        self.intialGuessLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.intialGuess.setVisible(False)

        ################################################################################################################

        if self.command.isLetters:
            self.validate = self.strValidator
        else:
            self.validate = self.doubleValidator

        for i in range(0, 100):
            self.label = QtWidgets.QLabel(self.initialGeussLable)
            self.label.setText(f"X{i + 1}")
            self.label.setStyleSheet("color:12px rgb(106, 98, 71);\n"
                                     "font-weight: italic;")
            self.intialGuessLayout.addWidget(self.label, i, 0)
            self.label.show()

            self.e = QtWidgets.QLineEdit(self.intialGuess)
            self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.e.setValidator(self.validate)
            if i >= int(self.nEquations.text()):
                self.e.setEnabled(False)
                self.e.setStyleSheet("background-color: rgb(227, 199, 240)")
            self.e.show()
            self.initialGuessVector.append(self.e)
            self.intialGuessLayout.addWidget(self.e, i, 1)

        ################################################################################################################

        self.programTitle.setText("")
        self.programTitle.setObjectName("programTitle")
        self.programTitle.raise_()
        self.gridLayoutWidget.raise_()
        self.columnView.raise_()
        self.nEquationDisplayed.raise_()
        self.methodLable.raise_()
        self.variablesForm.raise_()
        self.method.raise_()
        self.nEquationsLable.raise_()
        self.nEquations.raise_()
        self.LULable.raise_()
        self.LU.raise_()
        self.line.raise_()
        self.format.raise_()
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
        self.scaling.raise_()
        self.scalingLabel.raise_()
        self.intialGuess.raise_()
        self.initialGeussLable.raise_()
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
            self.initialGeussLable.setVisible(False)
            self.intialGuess.setVisible(False)
        elif method == "Gauss-Seidel" or method == "Jacobi-Iteration":
            self.method.setEnabled(False)
            self.stopContition.setEnabled(True)
            self.initialGeussLable.setVisible(True)
            self.intialGuess.setVisible(True)
        else:
            self.method.setEnabled(False)
            self.stopContition.setEnabled(False)
            self.nIteration.setEnabled(False)
            self.ARE.setEnabled(False)
            self.initialGeussLable.setVisible(False)
            self.intialGuess.setVisible(False)

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

        # decrease number of equations
        if self.prev > int(self.nEquations.text()):
            for i in range(1, self.prev + 1):
                for j in range(int(self.nEquations.text()) + 1, self.prev + 1):
                    self.gridLayout.itemAt(101 * i + j).widget().setEnabled(False)
                    self.gridLayout.itemAt(101 * i + j).widget().setStyleSheet("background-color: rgb(227, 199, 240)")
            for i in range(int(self.nEquations.text()) + 1, self.prev + 1):
                for j in range(0, int(self.nEquations.text()) + 1):
                    self.gridLayout.itemAt(101 * i + j).widget().setEnabled(False)
                    self.gridLayout.itemAt(101 * i + j).widget().setStyleSheet("background-color: rgb(227, 199, 240)")

        # increase number of equations
        if self.prev < int(self.nEquations.text()):
            for i in range(1, int(self.nEquations.text()) + 1):
                for j in range(self.prev + 1, int(self.nEquations.text()) + 1):
                    self.gridLayout.itemAt(101 * i + j).widget().setEnabled(True)
                    self.gridLayout.itemAt(101 * i + j).widget().setStyleSheet("background-color: rgb(255, 255, 255)")
            for i in range(self.prev + 1, int(self.nEquations.text()) + 1):
                for j in range(0, self.prev + 1):
                    self.gridLayout.itemAt(101 * i + j).widget().setEnabled(True)
                    self.gridLayout.itemAt(101 * i + j).widget().setStyleSheet("background-color: rgb(255, 255, 255)")
        print(self.initialGuessVector[0].text())
        self.initialGuessShow()

    def initialGuessShow(self):

        # increment Initial Guess
        if self.prev > int(self.nEquations.text()):
            for i in range(int(self.nEquations.text()), self.prev):
                self.intialGuessLayout.itemAt(2 * i + 1).widget().setEnabled(False)
                self.intialGuessLayout.itemAt(2 * i + 1).widget().setStyleSheet("background-color: rgb(227, 199, 240)")
        # Decrement Initial Guess
        elif self.prev < int(self.nEquations.text()):
            for i in range(self.prev, int(self.nEquations.text())):
                self.intialGuessLayout.itemAt(2 * i + 1).widget().setEnabled(True)
                self.intialGuessLayout.itemAt(2 * i + 1).widget().setStyleSheet("background-color: rgb(255, 255, 255)")

        self.prev = int(self.nEquations.text())


    def start(self):
        self.command.setMethod(self.method.currentText())
        self.command.setNIterations(self.nIteration.text())
        self.command.setARE(self.ARE.text())
        self.command.setPrecision(self.precision.text())
        self.command.setLUForm(self.LU.currentText())
        self.command.setStopCondition(self.stopContition.currentText())
        self.command.setNEquations(self.nEquations.text())
        self.command.setScalling(self.scaling.isChecked())
        self.command.fill(self.coef, self.b, self.initialGuessVector)
        
        runTime = 0
        if self.LU.currentText == "Jacobi-Iteration" or self.LU.currentText() == "Gauss-Seidel":
            try:
                self.command.setInitialGuess(self.initialGuessWindow.getInitialGuess())
                sol, runTime = self.command.calculate()
                self.solutionWindow.sol = sol
                self.open_solution_window(runTime)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error occured")
                msg.setText("No initial guess set")
                msg.exec_()
        else:
            try:
                sol, runTime = self.command.calculate()
            except:
                sol = []
            self.solutionWindow.sol = sol
            self.open_solution_window(runTime)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equations Solver"))
        self.nEquationDisplayed.setText(_translate("MainWindow", "Solving 3 x 3 System of Equations"))
        self.methodLable.setText(_translate("MainWindow", "Choose Method"))
        self.method.setCurrentText(_translate("MainWindow", "Doolittle Form"))
        self.method.setItemText(0, _translate("MainWindow", "Doolittle Form"))
        self.method.setItemText(1, _translate("MainWindow", "Crout Form" ""))
        self.method.setItemText(2, _translate("MainWindow", "Cholesky Form"))
        self.nEquationsLable.setText(_translate("MainWindow", "Number of Equations"))
        self.LULable.setText(_translate("MainWindow", "LU Format"))
        self.LU.setItemText(0, _translate("MainWindow", "Gauss Elimination"))
        self.LU.setItemText(1, _translate("MainWindow", "Gauss-Jordan"))
        self.LU.setItemText(2, _translate("MainWindow", "LU Decomposition"))
        self.LU.setItemText(3, _translate("MainWindow", "Gauss-Seidel"))
        self.LU.setItemText(4, _translate("MainWindow", "Jacobi-Iteration"))
        self.format.setItemText(0, _translate("MainWindow", "Numbers"))
        self.format.setItemText(1, _translate("MainWindow", "Letters"))
        self.ARELable.setText(_translate("MainWindow", "Absolute Relative  Error"))
        self.precisionLable.setText(_translate("MainWindow", "Precision"))
        self.stopConditionLable.setText(_translate("MainWindow", "Stopping condition"))
        self.stopContition.setItemText(0, _translate("MainWindow", "Number of Iterations"))
        self.stopContition.setItemText(1, _translate("MainWindow", "Absolute Relative Error"))
        self.stopContition.setItemText(2, _translate("MainWindow", "both"))
        self.nIterationLable.setText(_translate("MainWindow", "Number of iterations"))
        self.calcutateButton.setText(_translate("MainWindow", "Calculate"))
        self.nEquationDisplayed_2.setText(_translate("MainWindow", "Equations Solver"))
        self.variablesForm.setText(_translate("MainWindow", "Equations Formate"))
        self.scalingLabel.setText(_translate("MainWindow", "Scaling"))
        self.initialGeussLable.setText(_translate("MainWindow", "Initial Guess"))
        self.line.setText(_translate("MainWindow", "___________________________________________________________"))
        self.stopContition.setCurrentText("both")

    def open_solution_window(self, runTime):
        self.window = QtWidgets.QMainWindow()
        self.solutionWindow.setupUi(self.window, runTime)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
