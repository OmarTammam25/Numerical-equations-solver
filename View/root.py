from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Commands import Commands


class RootFinder(object):
    command = Commands()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2042, 1372)
        MainWindow.setStyleSheet("background-color:rgb(255, 238, 241)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ################################################################################################################
        # Buttons

        # Solution button
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

        # System Of Equations Button
        self.systemOfEquationsButton = QtWidgets.QPushButton(self.centralwidget)
        self.systemOfEquationsButton.setGeometry(QtCore.QRect(910, 130, 471, 81))
        self.systemOfEquationsButton.setFont(font)
        self.systemOfEquationsButton.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                                   "color: rgb(72, 73, 73);")
        self.systemOfEquationsButton.setObjectName("systemOfEquationsButton")

        # Root Finder Button
        self.rootFinderButton = QtWidgets.QPushButton(self.centralwidget)
        self.rootFinderButton.setGeometry(QtCore.QRect(400, 130, 511, 81))
        self.rootFinderButton.setFont(font)
        self.rootFinderButton.setStyleSheet("background-color:rgb(191, 135, 158);\n"
                                            "color: rgb(72, 73, 77);")
        self.rootFinderButton.setObjectName("rootFinderButton")

        # Steps Button
        self.stepsButton = QtWidgets.QPushButton(self.centralwidget)
        self.stepsButton.setGeometry(QtCore.QRect(800, 700, 521, 101))
        self.stepsButton.setFont(font)
        self.stepsButton.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                       "color: rgb(72, 73, 73)\n"
                                       "")
        self.stepsButton.setObjectName("stepsButton")

        ################################################################################################################

        # Side Bar

        # Method Dropdown list
        self.method = QtWidgets.QComboBox(self.centralwidget)
        self.method.setGeometry(QtCore.QRect(420, 330, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.method.setFont(font)
        self.method.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                  "color: rgb(72, 73, 73);\n"
                                  "")
        self.method.setObjectName("method_2")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.currentTextChanged.connect(self.changeView)

        # Number of iterations dropdown list
        self.numberOfIterations = QtWidgets.QSpinBox(self.centralwidget)
        self.numberOfIterations.setGeometry(QtCore.QRect(420, 580, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.numberOfIterations.setFont(font)
        self.numberOfIterations.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                              "color: rgb(72, 73, 73);\n"
                                              "\n"
                                              "")
        self.numberOfIterations.setMinimum(2)
        self.numberOfIterations.setMaximum(100)
        self.numberOfIterations.setProperty("value", 50)
        self.numberOfIterations.setObjectName("numberOfIterations")

        # Significant Figures
        self.sigFig = QtWidgets.QSpinBox(self.centralwidget)
        self.sigFig.setGeometry(QtCore.QRect(420, 720, 151, 71))
        self.sigFig.setFont(font)
        self.sigFig.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                  "color: rgb(72, 73, 73);\n"
                                  "\n"
                                  "")
        self.sigFig.setMinimum(2)
        self.sigFig.setMaximum(25)
        self.sigFig.setProperty("value", 5)
        self.sigFig.setObjectName("sigFig")

        # Absolute Relative Error
        self.error = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(600, 580, 141, 71))
        self.error.setFont(font)
        self.error.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                 "color: rgb(72, 73, 73);\n"
                                 "")
        self.error.setDecimals(6)
        self.error.setMinimum(1e-06)
        self.error.setSingleStep(1e-06)
        self.error.setObjectName("error")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 430, 331, 71))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                    "color: rgb(72, 73, 73);\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")

        ################################################################################################################

        # Labels
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
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)

        self.equationLable = QtWidgets.QLabel(self.centralwidget)
        self.equationLable.setGeometry(QtCore.QRect(840, 220, 311, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setItalic(True)
        self.equationLable.setFont(font)
        self.equationLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.equationLable.setObjectName("equationLable")

        self.gxLable = QtWidgets.QLabel(self.centralwidget)
        self.gxLable.setGeometry(QtCore.QRect(765, 300, 60, 80))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setItalic(True)
        self.gxLable.setFont(font)
        self.gxLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.gxLable.setObjectName("equationLable")

        self.fxLable = QtWidgets.QLabel(self.centralwidget)
        self.fxLable.setGeometry(QtCore.QRect(765, 400, 60, 71))
        self.fxLable.setFont(font)
        self.fxLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.fxLable.setObjectName("equationLable")

        self.solutionLable = QtWidgets.QLabel(self.centralwidget)
        self.solutionLable.setGeometry(QtCore.QRect(790, 500, 151, 61))
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
        self.xLable.setGeometry(QtCore.QRect(800, 550, 51, 61))
        self.xLable.setFont(font)
        self.xLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.xLable.setObjectName("xLable")

        self.timeLable = QtWidgets.QLabel(self.centralwidget)
        self.timeLable.setGeometry(QtCore.QRect(800, 600, 100, 40))
        self.timeLable.setFont(font)
        self.timeLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.timeLable.setObjectName("xLable")

        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(910, 600, 370, 41))
        self.time.setFont(font)
        self.time.setStyleSheet("color: rgb(85, 85, 85);")
        self.time.setText("")
        self.time.setObjectName("solution")

        self.solution = QtWidgets.QLabel(self.centralwidget)
        self.solution.setGeometry(QtCore.QRect(860, 560, 491, 41))
        self.solution.setFont(font)
        self.solution.setStyleSheet("color: rgb(85, 85, 85);")
        self.solution.setText("")
        self.solution.setObjectName("solution")

        self.methodLable = QtWidgets.QLabel(self.centralwidget)
        self.methodLable.setGeometry(QtCore.QRect(420, 260, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.methodLable.setFont(font)
        self.methodLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.methodLable.setObjectName("methodLable")

        self.noIterationsLable = QtWidgets.QLabel(self.centralwidget)
        self.noIterationsLable.setGeometry(QtCore.QRect(420, 510, 161, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.noIterationsLable.setFont(font)
        self.noIterationsLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.noIterationsLable.setObjectName("noIterationsLable")

        self.Xl = QtWidgets.QLabel(self.centralwidget)
        self.Xl.setGeometry(QtCore.QRect(420, 390, 41, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Xl.setFont(font)
        self.Xl.setStyleSheet("color: rgb(72, 73, 73);")
        self.Xl.setObjectName("Xl")

        self.sigFigLable = QtWidgets.QLabel(self.centralwidget)
        self.sigFigLable.setGeometry(QtCore.QRect(420, 670, 300, 50))
        self.sigFigLable.setFont(font)
        self.sigFigLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.sigFigLable.setObjectName("noIterationsLable")

        self.initialGuessLable = QtWidgets.QLabel(self.centralwidget)
        self.initialGuessLable.setGeometry(QtCore.QRect(420, 390, 311, 41))
        self.initialGuessLable.setFont(font)
        self.initialGuessLable.setStyleSheet("color: rgb(72, 73, 73);")
        self.initialGuessLable.setObjectName("initialGuessLable")

        self.XU = QtWidgets.QLabel(self.centralwidget)
        self.XU.setGeometry(QtCore.QRect(590, 390, 41, 41))
        self.XU.setFont(font)
        self.XU.setStyleSheet("color: rgb(72, 73, 73);")
        self.XU.setObjectName("XU")

        ################################################################################################################

        # fx and gx fields
        self.gx = QtWidgets.QTextEdit(self.centralwidget)
        self.gx.setGeometry(QtCore.QRect(830, 300, 350, 80))
        self.gx.setFont(font)
        self.gx.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.gx.setStyleSheet("background-color:rgb(255, 246, 247);\n")
        self.gx.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.gx.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.gx.setObjectName("equationArea")

        self.fx = QtWidgets.QTextEdit(self.centralwidget)
        self.fx.setGeometry(QtCore.QRect(830, 400, 350, 80))
        self.fx.setFont(font)
        self.fx.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.fx.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                              "")
        self.fx.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.fx.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.fx.setObjectName("equationArea")

        ################################################################################################################

        # Solution Area
        self.solutionArea = QtWidgets.QTextBrowser(self.centralwidget)
        self.solutionArea.setGeometry(QtCore.QRect(760, 490, 601, 171))
        self.solutionArea.setStyleSheet("border: 3px solid rgb(72, 73, 73);\n"
                                        "border-top-left-radius: 7px;\n"
                                        "border-top-right-radius: 7px;\n"
                                        "border-bottom-left-radius: 7px;\n"
                                        "border-bottom-right-radius: 7px;")
        self.solutionArea.setObjectName("solutionArea")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(600, 485, 140, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        ################################################################################################################

        # Equation Constraints
        self.ruleArea = QtWidgets.QTextBrowser(self.centralwidget)
        self.ruleArea.setGeometry(QtCore.QRect(420, 830, 331, 120))
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

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 430, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                      "color: rgb(72, 73, 73);\n"
                                      "")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 430, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 246, 247);\n"
                                      "color: rgb(72, 73, 73);\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")

        ################################################################################################################

        self.textBrowser.raise_()
        self.contentFrame.raise_()
        self.solutionButton.raise_()
        self.titleLable.raise_()
        self.fx.raise_()
        self.gx.raise_()
        self.methodLable.raise_()
        self.systemOfEquationsButton.raise_()
        self.rootFinderButton.raise_()
        self.ruleArea.raise_()
        self.method.raise_()
        self.numberOfIterations.raise_()
        self.solutionArea.raise_()
        self.solutionArea.raise_()
        self.textBrowser.raise_()
        self.xLable.raise_()
        self.solution.raise_()
        self.error.raise_()
        self.solutionLable.raise_()
        self.lineEdit.raise_()
        self.initialGuessLable.raise_()
        self.noIterationsLable.raise_()
        self.Xl.raise_()
        self.XU.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.stepsButton.raise_()
        self.equationLable.raise_()
        self.fxLable.raise_()
        self.gxLable.raise_()
        self.sigFig.raise_()
        self.sigFigLable.raise_()
        self.timeLable.raise_()
        self.time.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def solve(self):
        self.command.setGx(self.gx.toPlainText())
        self.command.setRootFinderMethod(self.method.currentText())
        self.command.setFx(self.fx.toPlainText())
        self.command.setXl(self.lineEdit_3.text())
        self.command.setXu(self.lineEdit_2.text())
        self.command.setInitialGuessRoot(self.lineEdit.text())
        self.command.setSigFig(self.sigFig.text())
        self.command.setNIterations(self.numberOfIterations.text())
        self.command.setARE(self.error.text())
        try:
            self.time.setText(str(self.command.getTime()))
            self.solution.setText(str(self.command.findRoot()))
        except:
            self.solution.setText("can't find a solution")

    def changeView(self):
        if self.method.currentText() == "Bisection" or self.method.currentText() == "False-Position" or self.method.currentText() == "Secant Method":
            self.Xl.setVisible(True)
            self.XU.setVisible(True)
            self.lineEdit_3.setVisible(True)
            self.lineEdit_2.setVisible(True)
            self.initialGuessLable.setVisible(False)
            self.lineEdit.setVisible(False)
            self.gx.setDisabled(True)
            self.gx.setText("")
        else:
            self.Xl.setVisible(False)
            self.XU.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.initialGuessLable.setVisible(True)
            self.lineEdit.setVisible(True)
            self.gx.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Root finder"))
        self.solutionButton.setText(_translate("MainWindow", "Find Root"))
        self.titleLable.setText(_translate("MainWindow", "                             Root Finder"))
        self.methodLable.setText(_translate("MainWindow", "Choose method "))
        self.systemOfEquationsButton.setText(_translate("MainWindow", "System of equations solver"))
        self.rootFinderButton.setText(_translate("MainWindow", "Root finder"))
        self.ruleArea.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Sans Serif\'; "
                                         "font-size:8.25pt; font-weight:600; font-style:normal;\">\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; text-indent:0px;\"><br /></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg "
                                         "2\'; font-size:24pt; font-weight:400; color:#494848;\">Use "
                                         "variable \'x\'</span></p>\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                         "font-size:24pt; color:#494848;\"><br /></p></body></html>"))
        self.solutionLable.setText(_translate("MainWindow", "Solution:"))
        self.xLable.setText(_translate("MainWindow", "x = "))
        self.stepsButton.setText(_translate("MainWindow", "Show Solution Steps"))
        self.method.setItemText(0, _translate("MainWindow", "Bisection"))
        self.method.setItemText(1, _translate("MainWindow", "False-Position"))
        self.method.setItemText(2, _translate("MainWindow", "Fixed point"))
        self.method.setItemText(3, _translate("MainWindow", "Newton-Raphson"))
        self.method.setItemText(4, _translate("MainWindow", "Secant Method"))
        self.initialGuessLable.setText(_translate("MainWindow", "Initial guess"))
        self.noIterationsLable.setText(_translate("MainWindow", "Iterations"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Sans Serif\'; "
                                            "font-size:8pt; font-weight:400; font-style:normal;\">\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:24pt; "
                                            "color:#494848;\">Relative Error</span></p>\n "
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                            "font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#494848;\"><br "
                                            "/></p></body></html>"))
        self.Xl.setText(_translate("MainWindow", "Xl"))
        self.XU.setText(_translate("MainWindow", "Xu"))
        self.equationLable.setText(_translate("MainWindow", "Enter Equation"))
        self.fxLable.setText(_translate("MainWindow", "F(x)"))
        self.gxLable.setText(_translate("MainWindow", "G(x)"))
        self.sigFigLable.setText(_translate("MainWindow", "Significant Figures"))
        self.timeLable.setText(_translate("MainWindow", "Time = "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RootFinder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())