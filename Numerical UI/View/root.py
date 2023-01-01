from PyQt5 import QtCore, QtGui, QtWidgets
from View.V2Equation import V2EquationSolver
from Controller.Commands import Commands


class RootFinder(object):
    equationSolver = V2EquationSolver()
    command = Commands()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2042, 1372)
        MainWindow.setStyleSheet("background-color:rgb(255, 238, 241)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.solutionButton = QtWidgets.QPushButton(self.centralwidget)
        self.solutionButton.setGeometry(QtCore.QRect(1190, 340, 181, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.solutionButton.setFont(font)
        self.solutionButton.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                          "color: rgb(72, 73, 75);")
        self.solutionButton.setObjectName("solutionButton")
        self.solutionButton.clicked.connect(self.solve)
        self.titleLable = QtWidgets.QLabel(self.centralwidget)
        self.titleLable.setGeometry(QtCore.QRect(400, 0, 981, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.titleLable.setFont(font)
        self.titleLable.setStyleSheet("border-color:rgb(68, 50, 64);\n"
                                      "border-width:10px;\n"
                                      "border-radius: 5px;\n"
                                      "background-color:rgb(72, 73, 75);\n"
                                      "color:rgb(255, 239, 244)\n"
                                      "")
        self.titleLable.setObjectName("titleLable")

        self.equationArea = QtWidgets.QTextEdit(self.centralwidget)
        self.equationArea.setGeometry(QtCore.QRect(780, 340, 401, 111))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)
        self.equationArea.setFont(font)
        self.equationArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.equationArea.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                        "")
        self.equationArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.equationArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.equationArea.setObjectName("equationArea")

        self.method = QtWidgets.QComboBox(self.centralwidget)
        self.method.setGeometry(QtCore.QRect(440, 340, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.method.setFont(font)
        self.method.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                  "color: rgb(72, 73, 73);\n"
                                  "")
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")

        self.methodLable = QtWidgets.QLabel(self.centralwidget)
        self.methodLable.setGeometry(QtCore.QRect(450, 270, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.methodLable.setFont(font)
        self.methodLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.methodLable.setObjectName("methodLable")
        self.systemOfEquationsButton = QtWidgets.QPushButton(self.centralwidget)
        self.systemOfEquationsButton.setGeometry(QtCore.QRect(910, 130, 471, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.systemOfEquationsButton.setFont(font)
        self.systemOfEquationsButton.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                                   "color: rgb(72, 73, 73);")
        self.systemOfEquationsButton.setObjectName("systemOfEquationsButton")
        self.systemOfEquationsButton.clicked.connect(self.equationSolverWindow)

        self.rootFinderButton = QtWidgets.QPushButton(self.centralwidget)
        self.rootFinderButton.setGeometry(QtCore.QRect(400, 130, 511, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rootFinderButton.setFont(font)
        self.rootFinderButton.setStyleSheet("background-color:rgb(191, 135, 158);\n"
                                            "color: rgb(72, 73, 77);")
        self.rootFinderButton.setObjectName("rootFinderButton")


        self.equationLable = QtWidgets.QLabel(self.centralwidget)
        self.equationLable.setGeometry(QtCore.QRect(840, 250, 311, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setItalic(True)
        self.equationLable.setFont(font)
        self.equationLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.equationLable.setObjectName("equationLable")
        self.stepsButton = QtWidgets.QPushButton(self.centralwidget)
        self.stepsButton.setGeometry(QtCore.QRect(810, 670, 521, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.stepsButton.setFont(font)
        self.stepsButton.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                       "color: rgb(72, 73, 73)\n"
                                       "")
        self.stepsButton.setObjectName("stepsButton")
        self.solutionArea = QtWidgets.QTextBrowser(self.centralwidget)
        self.solutionArea.setGeometry(QtCore.QRect(760, 481, 601, 171))
        self.solutionArea.setStyleSheet("border: 3px solid rgb(72, 73, 73);\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;")
        self.solutionArea.setObjectName("solutionArea")
        self.ruleArea = QtWidgets.QTextBrowser(self.centralwidget)
        self.ruleArea.setGeometry(QtCore.QRect(420, 490, 331, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ruleArea.setFont(font)
        self.ruleArea.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ruleArea.setStyleSheet("border: 3px solid rgb(72, 73, 73);\n"
                                    "border-top-left-radius: 7px;\n"
                                    "border-top-right-radius: 7px;\n"
                                    "border-bottom-left-radius: 7px;\n"
                                    "border-bottom-right-radius: 7px;")
        self.ruleArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ruleArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ruleArea.setObjectName("ruleArea")
        self.solutionLable = QtWidgets.QLabel(self.centralwidget)
        self.solutionLable.setGeometry(QtCore.QRect(790, 491, 151, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.solutionLable.setFont(font)
        self.solutionLable.setStyleSheet("color: rgb(72, 73, 73)")
        self.solutionLable.setObjectName("solutionLable")
        self.xLable = QtWidgets.QLabel(self.centralwidget)
        self.xLable.setGeometry(QtCore.QRect(800, 541, 51, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.xLable.setFont(font)
        self.xLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.xLable.setObjectName("xLable")
        self.solution = QtWidgets.QLabel(self.centralwidget)
        self.solution.setGeometry(QtCore.QRect(860, 550, 491, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.solution.setFont(font)
        self.solution.setStyleSheet("color: rgb(85, 85, 85);")
        self.solution.setText("")
        self.solution.setObjectName("solution")
        self.contentFrame = QtWidgets.QFrame(self.centralwidget)
        self.contentFrame.setGeometry(QtCore.QRect(400, 0, 981, 981))
        self.contentFrame.setStyleSheet("border: 3px solid rgb(72, 73, 73);\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.contentFrame.raise_()
        self.solutionButton.raise_()
        self.titleLable.raise_()
        self.equationArea.raise_()
        self.method.raise_()
        self.methodLable.raise_()
        self.systemOfEquationsButton.raise_()
        self.rootFinderButton.raise_()
        self.equationLable.raise_()
        self.stepsButton.raise_()
        self.solutionArea.raise_()
        self.ruleArea.raise_()
        self.solutionLable.raise_()
        self.xLable.raise_()
        self.solution.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def equationSolverWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.equationSolver.setupUi(self.window)
        self.window.show()

    def solve(self):
        if self.command.validateSyntax(self.equationArea.toPlainText()):
            self.command.setRootFinderMethod(self.method.currentText())
            self.command.setRootEquation(self.equationArea.toPlainText())
            self.command.findRoot()
        else:
            self.solution.setText("Invalid input!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Root finder"))
        self.solutionButton.setText(_translate("MainWindow", "Find Root"))
        self.titleLable.setText(_translate("MainWindow", "                             Root Finder"))
        self.method.setItemText(0, _translate("MainWindow", "Bisection"))
        self.method.setItemText(1, _translate("MainWindow", "False-Position"))
        self.method.setItemText(2, _translate("MainWindow", "Fixed point"))
        self.method.setItemText(3, _translate("MainWindow", "Newton-Raphson"))
        self.method.setItemText(4, _translate("MainWindow", "Secant Method"))
        self.methodLable.setText(_translate("MainWindow", "Choose method "))
        self.systemOfEquationsButton.setText(_translate("MainWindow", "System of equations solver"))
        self.rootFinderButton.setText(_translate("MainWindow", "Root finder"))
        self.equationLable.setText(_translate("MainWindow", "Enter Equation"))
        self.stepsButton.setText(_translate("MainWindow", "Show Solution Steps"))
        self.ruleArea.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Sans Serif\'; "
                                         "font-size:8.25pt; font-weight:600; font-style:normal;\">\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><br /></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                         "font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:400; "
                                         "color:#494848;\">Use variable \'x\'</span></p>\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                         "font-size:24pt; color:#494848;\"><br /></p></body></html>"))
        self.solutionLable.setText(_translate("MainWindow", "Solution:"))
        self.xLable.setText(_translate("MainWindow", "x = "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RootFinder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
