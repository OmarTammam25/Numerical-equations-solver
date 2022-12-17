from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from Controller.Commands import Commands


class Ui_MainWindow(object):
    coef = [[0 for x in range(101)] for y in range(101)]  # Coefficient matrix
    b = []  # results
    LUEnabled = False
    nIterationsEnabled = False
    stopConditionEnabled = True
    command = Commands()


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
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 240, 8500, 2600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")

        #########################################################################################################

        # Coefficient matrix formation
        self.validator = QDoubleValidator()
        for i in range(0, 101):
            for j in range(0, 101):
                self.e = QtWidgets.QLineEdit(self.gridLayoutWidget)
                self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.e.setValidator(self.validator)
                self.gridLayout.addWidget(self.e, i + 4, j)
                if i < 2 and j < 2:
                    self.e.show()
                else:
                    self.e.setStyleSheet("background-color:rgb(255, 253, 184)")
                    self.e.setDisabled(True)
                self.coef[i][j] = self.e

        ############################################################################################################

        self.columnView = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setGeometry(QtCore.QRect(20, 140, 191, 601))
        self.columnView.setStyleSheet("background-color:rgb(255, 253, 184);\n"
                                      "border-color: rgb(0, 0, 100);")
        self.columnView.setObjectName("columnView")

        self.nEquationDisplayed = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed.setGeometry(QtCore.QRect(220, 120, 581, 61))
        self.nEquationDisplayed.setStyleSheet(
            "color: rgb(121, 104, 62);\n"
            "font: 25pt \"Century Gothic\";\n"
            "font-weight: bold")
        self.nEquationDisplayed.setObjectName("nEquationDisplayed")
        self.methodLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.methodLable.setGeometry(QtCore.QRect(40, 150, 151, 20))
        self.methodLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                       "font: 11pt \"Century Gothic\";\n"
                                       "font-weight: bold")
        self.methodLable.setObjectName("methodLabel")

        ################################################################################################################

        # LU Drop-Down List
        self.method = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.method.setEnabled(self.LUEnabled)
        self.method.setGeometry(QtCore.QRect(30, 320, 151, 21))
        self.method.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.method.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.method.setAcceptDrops(True)
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
        self.nEquations.setMinimum(2)
        self.nEquations.setMaximum(100)
        self.nEquations.setObjectName("nEquations")

        ################################################################################################################

        # Choose method
        self.LU = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.LU.setGeometry(QtCore.QRect(30, 180, 151, 22))
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
        self.precision.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.precision.setMinimum(1)
        self.precision.setMaximum(30)
        self.precision.setProperty("value", 5)
        self.precision.setObjectName("precision")

        ################################################################################################################

        # Absolute Relative Error
        self.ARE = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.ARE.setGeometry(QtCore.QRect(30, 390, 151, 22))
        self.ARE.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.ARE.setDecimals(6)
        self.ARE.setSingleStep(1e-06)
        self.ARE.setProperty("value", 1e-06)
        self.ARE.setObjectName("doubleSpinBox")

        ################################################################################################################

        # Stop Condition
        self.stopContition = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.stopContition.setEnabled(self.stopConditionEnabled)
        self.stopContition.setGeometry(QtCore.QRect(30, 530, 151, 22))
        self.stopContition.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.stopContition.setObjectName("stopContition")
        self.stopContition.addItem("")
        self.stopContition.addItem("")
        self.stopContition.addItem("")

        ################################################################################################################

        # number of iterations
        self.nIteration = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.nIteration.setEnabled(self.nIterationsEnabled)
        self.nIteration.setGeometry(QtCore.QRect(30, 620, 151, 22))
        self.nIteration.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.nIteration.setMinimum(2)
        self.nIteration.setMaximum(150)
        self.nIteration.setObjectName("nIteration")

        ################################################################################################################

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
        self.precisionLable.setStyleSheet(
            "color: rgb(121, 104, 62);\n"
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

        ################################################################################################################

        self.calcutateButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calcutateButton.clicked.connect(self.calculate)
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

        # self.calcutateButton.clicked.connect(Commands().calculate(self))

        self.nEquationDisplayed_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nEquationDisplayed_2.setGeometry(QtCore.QRect(30, 40, 581, 61))
        self.nEquationDisplayed_2.setStyleSheet("color: rgb(121, 104, 62);\n"
                                                "font: 25pt \"Century Gothic\";\n"
                                                "font-weight: bold")
        self.nEquationDisplayed_2.setObjectName("nEquationDisplayed_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 180, 231, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        for i in range(0, 101):
            self.res = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
            self.horizontalLayout.addWidget(self.res)
            if i < 2:
                self.res.show()
            else:
                self.res.setStyleSheet("background-color:rgb(255, 255, 255)")
                self.res.setDisabled(True)
                self.b.append(self.res)
            print(i)

        # self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.label_2.setStyleSheet("background-color: none;\n"
        #                            "color: rgb(121, 104, 62);\n"
        #                            "font: 11pt \"Century Gothic\";\n"
        #                            "font-weight: bold")
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout.addWidget(self.label_2)
        # self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.label.setStyleSheet("background-color: none;\n"
        #                          "color: rgb(121, 104, 62);\n"
        #                          "font: 11pt \"Century Gothic\";\n"
        #                          "font-weight: bold\n"
        #                          "")
        # self.label.setObjectName("label")
        # self.horizontalLayout.addWidget(self.label)

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
        self.horizontalLayoutWidget.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.frame)
        self.nEquationDisplayed.setText(f"Solving {self.nEquations.text()} x {self.nEquations.text()} System of Equations")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def methodCheck(self):
        method = self.method.currentText()
        if method == "LU Decomposition":
            self.LUEnabled = True
            self.stopConditionEnabled = False
        elif method == "Gauss-Seidel" or method == "Jacobi-Iteration":
            self.stopConditionEnabled = True
            self.LUEnabled = False
        else:
            self.stopConditionEnabled = False
            self.LUEnabled = False

    def start(self):
        if self.command.areFilled(self.coef, self.b):
            self.command.setNIterations(self.nIteration.text())
            self.command.setARE(self.ARE.text())
            self.command.setPrecision(self.precision)
            self.command.setLUForm(self.LU.currentText())
            self.command.setStopCondition(self.stopContition.currentText())
            self.command.setNEquations(self.nEquations.text())
            self.command.setMethod(self.method.currentText())
            self.command.setA(self.coef)
            self.command.setB(self.b)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equations Solver"))
        self.frame.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.nEquationDisplayed.setText(_translate("MainWindow", "Solving 2 x 2 System of Equations"))
        self.methodLable.setText(_translate("MainWindow", "Choose Method"))
        self.method.setCurrentText(_translate("MainWindow", "Downlittle Form"))
        self.method.setItemText(0, _translate("MainWindow", "Downlittle Form"))
        self.method.setItemText(1, _translate("MainWindow", "Crout Form\n" ""))
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
        # self.label_2.setText(_translate("MainWindow", "X1"))
        # self.label.setText(_translate("MainWindow", "X2"))

    def calculate(self):
        print(self.coef[0][0].text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
