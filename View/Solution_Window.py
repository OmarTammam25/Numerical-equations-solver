from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_resultsWindow(object):
    sol = []

    def setupUi(self, resultsWindow, runTime):
        resultsWindow.setObjectName("resultsWindow")
        resultsWindow.resize(1450, 927)
        self.centralwidget = QtWidgets.QWidget(resultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1901, 975))
        self.scrollArea.setStyleSheet("background-color:rgb(255, 238, 241)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2000, 3100))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(9000, 3400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(280, 70, 711, 2800))
        self.tableWidget.setMinimumSize(QtCore.QSize(2, 0))
        self.tableWidget.setObjectName("tableWidget")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setWeight(50)
        self.sol = np.array(self.sol)
        if (self.sol.size == 0):
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('No unique solution found.'))
            self.tableWidget.item(0, 0).setBackground(QtGui.QColor(255, 246, 247))
            self.tableWidget.item(0, 0).setFont(font)
            self.tableWidget.item(0, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.item(0, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        else:
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(self.sol.size)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setFont(font)
            header.setStyleSheet("background-color: rgb(73, 73, 73)")
            row = 0
            for i in self.sol:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('x' + str(row)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i)))
                self.tableWidget.item(row, 0).setBackground(QtGui.QColor(255, 246, 247))
                self.tableWidget.item(row, 1).setBackground(QtGui.QColor(255, 246, 247))
                self.tableWidget.item(row, 0).setFont(font)
                self.tableWidget.item(row, 1).setFont(font)
                self.tableWidget.item(row, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.item(row, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.item(row, 0).setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.item(row, 1).setFlags(QtCore.Qt.ItemIsEnabled)
                row += 1

        self.solutionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.solutionLable.setGeometry(QtCore.QRect(280, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setWeight(100)
        self.solutionLable.setFont(font)
        self.solutionLable.setStyleSheet("border-color:rgb(227, 199, 240)")
        self.solutionLable.setObjectName("label")

        self.timeLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.timeLable.setGeometry(QtCore.QRect(560, 14, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timeLable.setFont(font)
        self.timeLable.setStyleSheet("border-color:rgb(72, 73, 73)")
        self.timeLable.setObjectName("label_2")

        self.time = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.time.setGeometry(830, 12, 180, 50)
        self.time.setStyleSheet("border-color:rgb(227, 199, 240);\n"
                                "font: 15pt \"Century Gothic\";\n"
                                "color: rgb(73, 73, 73);\n"
                                "font-weight: bold")
        runTime = runTime * 10 ** 3
        runTime = round(runTime, 10)
        self.time.setText(str(runTime) + 'ms')

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        resultsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(resultsWindow)
        self.statusbar.setObjectName("statusbar")
        resultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultsWindow)
        QtCore.QMetaObject.connectSlotsByName(resultsWindow)

    def retranslateUi(self, resultsWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsWindow.setWindowTitle(_translate("resultsWindow", "Solution"))
        self.solutionLable.setText(_translate("resultsWindow", "Solution "))
        self.timeLable.setText(_translate("resultsWindow", "Calculation time: "))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultsWindow = QtWidgets.QMainWindow()
    ui = Ui_resultsWindow()
    ui.setupUi(resultsWindow)
    resultsWindow.show()
    sys.exit(app.exec_())