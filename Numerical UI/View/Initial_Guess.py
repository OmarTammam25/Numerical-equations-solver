from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator

from Controller.Commands import Commands


class Ui_InitialGuess(object):
    initialGuessVector = []
    nEquations = 2
    command = Commands()

    def setupUi(self, InitialGuess):
        InitialGuess.setObjectName("InitialGuess")
        InitialGuess.resize(1156, 814)
        self.centralwidget = QtWidgets.QWidget(InitialGuess)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1920, 991))
        self.scrollArea.setStyleSheet("background-color:rgb(255, 253, 184)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 9000, 2900))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(4000, 4000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.programTitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.programTitle.setGeometry(QtCore.QRect(-140, 1140, 50000, 6000))
        self.programTitle.setMinimumSize(QtCore.QSize(10000, 6000))
        self.programTitle.setStyleSheet("color: rgb(121, 104, 62);\n"
                                        "font: 25pt \"Century Gothic\";\n"
                                        "font-weight: bold")
        self.programTitle.setText("")
        self.programTitle.setObjectName("programTitle")
        self.initialGeussLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.initialGeussLable.setGeometry(QtCore.QRect(50, 30, 141, 16))
        self.initialGeussLable.setStyleSheet("color: rgb(121, 104, 62);\n"
                                             "font: 14pt \"Century Gothic\";\n"
                                             "font-weight: bold")
        self.initialGeussLable.setObjectName("initialGuessLabel")

        ################################################################################################################

        # Grid
        self.intialGuess = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.intialGuess.setGeometry(QtCore.QRect(70, 60, 120, int(self.command.nEquations) * 25))
        self.intialGuess.setObjectName("intialGuessLabels")
        self.intialGuessLayout = QtWidgets.QGridLayout(self.intialGuess)
        self.intialGuessLayout.setContentsMargins(10, 0, 10, 0)
        self.intialGuessLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        InitialGuess.setCentralWidget(self.centralwidget)

        ################################################################################################################

        # initial guess submit
        self.validator = QDoubleValidator()
        self.btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn.setGeometry(QtCore.QRect(225, 60, 70, 20))
        self.btn.setStyleSheet("background-color:rgb(200, 176, 127);\n"
                               "color:12px rgb(106, 98, 71);\n"
                               "font-weight: bold;\n"
                               "border-radius: 5px")
        self.btn.setText("Submit!")
        self.btn.setEnabled(True)
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn.clicked.connect(self.setInitialGuess)

        ################################################################################################################

        if self.command.isLetters:
            self.validator = QRegExpValidator()
        else:
            self.validator = QDoubleValidator()

        for i in range(0, int(self.command.nEquations)):
            self.e = QtWidgets.QLineEdit(self.intialGuess)
            self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.e.setValidator(self.validator)
            self.intialGuessLayout.addWidget(self.e, i, 1)
            self.e.show()
            self.initialGuessVector.append(self.e)
            self.label = QtWidgets.QLabel(self.initialGeussLable)
            self.label.setText(f"X{i + 1}")
            self.label.setStyleSheet("color:12px rgb(106, 98, 71);\n"
                                     "font-weight: italic;")
            self.intialGuessLayout.addWidget(self.label, i, 0)
            self.label.show()

        self.statusbar = QtWidgets.QStatusBar(InitialGuess)
        self.statusbar.setObjectName("statusbar")
        InitialGuess.setStatusBar(self.statusbar)

        self.retranslateUi(InitialGuess)
        QtCore.QMetaObject.connectSlotsByName(InitialGuess)
        self.intialGuess.raise_()

    def retranslateUi(self, InitialGuess):
        _translate = QtCore.QCoreApplication.translate
        InitialGuess.setWindowTitle(_translate("InitialGuess", "Initial_Guess"))
        self.initialGeussLable.setText(_translate("InitialGuess", "Iintial Guess"))

    def fill(self):
        print(self.initialGuessVector)
        for i in range(0, self.nEquations):
            if self.initialGuessVector[i].text() == "":
                self.initialGuessVector[i].setText("0")

    def setInitialGuess(self):
        self.fill()
        self.command.initialGuess = self.initialGuessVector
    def getInitialGuess(self):
        return self.initialGuessVector

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    InitialGuess = QtWidgets.QMainWindow()
    ui = Ui_InitialGuess()
    ui.setupUi(InitialGuess)
    InitialGuess.show()
    sys.exit(app.exec_())
