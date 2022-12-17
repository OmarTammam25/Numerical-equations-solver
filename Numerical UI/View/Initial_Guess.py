

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator


class Ui_InitialGuess(object):
    initialGuess = []

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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 160, 2600))
        self.verticalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("horizontalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        InitialGuess.setCentralWidget(self.centralwidget)

        self.validator = QDoubleValidator()
        for i in range(0, 2):
            self.e = QtWidgets.QLineEdit(self.verticalLayoutWidget)
            self.e.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.verticalLayout.addWidget(self.e)
            self.e.setValidator(self.validator)
            self.verticalLayout.addWidget(self.e)
            if i < 2:
                self.e.show()
            else:
                self.e.setStyleSheet("background-color:rgb(255, 253, 184)")
                self.e.setDisabled(True)
            self.initialGuess.append(self.e)

        self.statusbar = QtWidgets.QStatusBar(InitialGuess)
        self.statusbar.setObjectName("statusbar")
        InitialGuess.setStatusBar(self.statusbar)

        self.retranslateUi(InitialGuess)
        QtCore.QMetaObject.connectSlotsByName(InitialGuess)
        self.verticalLayoutWidget.raise_()

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
