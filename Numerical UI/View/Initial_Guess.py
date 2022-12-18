from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator


class Ui_InitialGuess(object):
    initialGuessVector = []

    def setupUi(self, InitialGuess):
        InitialGuess.setObjectName("InitialGuess")
        InitialGuess.resize(1156, 814)
        self.centralwidget = QtWidgets.QWidget(InitialGuess)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1901, 2800))
        self.scrollArea.setStyleSheet("background-color:rgb(255, 253, 184)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 10000, 3000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(10000, 3000))
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
        self.initialGeussLable.setObjectName("initialGeussLable")
        self.intialGuess = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.intialGuess.setGeometry(QtCore.QRect(100, 100, 100, 5000))
        self.intialGuess.setObjectName("bVector")
        self.intialGuessLayout = QtWidgets.QVBoxLayout(self.intialGuess)
        self.intialGuessLayout.setContentsMargins(10, 0, 10, 0)
        self.intialGuessLayout.setObjectName("bVectorLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        InitialGuess.setCentralWidget(self.centralwidget)

        self.validator = QDoubleValidator()
        for i in range(0, 100):
            self.e = QtWidgets.QLineEdit(self.intialGuess)
            self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.e.setValidator(self.validator)
            self.intialGuessLayout.addWidget(self.e)
            if i < 2:
                self.e.show()
            else:
                self.e.setStyleSheet("background-color:rgb(255, 253, 184)\n"
                                     "border-color: rgb(255, 253, 184)")
                self.e.setDisabled(True)
            self.initialGuessVector.append(self.e)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    InitialGuess = QtWidgets.QMainWindow()
    ui = Ui_InitialGuess()
    ui.setupUi(InitialGuess)
    InitialGuess.show()
    sys.exit(app.exec_())
