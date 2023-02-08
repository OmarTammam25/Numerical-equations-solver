from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_resultsWindow(object):
    # def __init__(self):
    #     # self.sol = solutionVector
    #     self.sol = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    sol = []
    def setupUi(self, resultsWindow, runTime):
        resultsWindow.setObjectName("resultsWindow")
        resultsWindow.resize(1450, 927)
        self.centralwidget = QtWidgets.QWidget(resultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_4 = QtWidgets.QListView(self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(-10, -10, 2500, 1100))
        self.listView_4.setMinimumSize(QtCore.QSize(800, 800))
        self.listView_4.setStyleSheet("background-color:rgb(227, 199, 240)")
        self.listView_4.setObjectName("listView_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(290, 0, 1000, 995))
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 200))
        self.scrollArea.setStyleSheet("background-color:rgb(227, 199, 240);\n"
                                      " border-style: outset;\n"
                                      " border-width: 2px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 996, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(1000, 2900))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(80, 70, 711, 2800))
        self.tableWidget.setMinimumSize(QtCore.QSize(2, 0))
        self.tableWidget.setStyleSheet("border-radius: 10px")
        self.tableWidget.setObjectName("tableWidget")

        self.sol = np.array(self.sol)
        if(self.sol.size == 0):
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('No unique solution found.'))
            self.tableWidget.item(0, 0).setBackground(QtGui.QColor(255, 255, 255))
            self.tableWidget.item(0, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.item(0, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        else:
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(self.sol.size)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            row = 0
            for i in self.sol:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('x' + str(row)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i)))
                self.tableWidget.item(row, 0).setBackground(QtGui.QColor(255, 255, 255))
                self.tableWidget.item(row, 1).setBackground(QtGui.QColor(255, 255, 255))
                self.tableWidget.item(row, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.item(row, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.item(row, 0).setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.item(row, 1).setFlags(QtCore.Qt.ItemIsEnabled)
                row += 1

        self.solutionLable = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.solutionLable.setGeometry(QtCore.QRect(80, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        self.solutionLable.setFont(font)
        self.solutionLable.setStyleSheet("border-color:rgb(227, 199, 240)")
        self.solutionLable.setObjectName("label")

        self.timeLable = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.timeLable.setGeometry(QtCore.QRect(450, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timeLable.setFont(font)
        self.timeLable.setStyleSheet("border-color:rgb(227, 199, 240)")
        self.timeLable.setObjectName("label_2")

        self.time = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.time.setGeometry(760, 15, 180, 50)
        self.time.setStyleSheet("color: rgb(121, 104, 62);\n"
                                   "font: 11pt \"Century Gothic\";\n"
                                   "font-weight: bold")
        runTime = runTime * 10**3
        runTime = round(runTime, 10)
        self.time.setText(str(runTime) + 'ms')

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        resultsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(resultsWindow)
        self.statusbar.setObjectName("statusbar")
        resultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultsWindow)
        QtCore.QMetaObject.connectSlotsByName(resultsWindow)

    def retranslateUi(self, resultsWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsWindow.setWindowTitle(_translate("resultsWindow", "Solution"))
        self.listView_4.setToolTip(
            _translate("resultsWindow", "<html><head/><body><p>Equations Solver Program</p><p><br/></p></body></html>"))
        self.solutionLable.setText(_translate("resultsWindow", "Solution "))
        self.timeLable.setText(_translate("resultsWindow", "Calculation time: "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    resultsWindow = QtWidgets.QMainWindow()
    ui = Ui_resultsWindow()
    ui.setupUi(resultsWindow)
    resultsWindow.show()
    sys.exit(app.exec_())