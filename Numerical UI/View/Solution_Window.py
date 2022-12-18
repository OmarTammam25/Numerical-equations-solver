
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultsWindow(object):
    def setupUi(self, resultsWindow):
        resultsWindow.setObjectName("resultsWindow")
        resultsWindow.resize(1450, 927)
        self.centralwidget = QtWidgets.QWidget(resultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_4 = QtWidgets.QListView(self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(-10, -10, 2500, 2600))
        self.listView_4.setMinimumSize(QtCore.QSize(800, 800))
        self.listView_4.setStyleSheet("background-color:rgb(255, 253, 184)")
        self.listView_4.setObjectName("listView_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(290, 0, 1000, 850))
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 200))
        self.scrollArea.setStyleSheet("background-color:rgb(255, 253, 184);\n"
" border-style: outset;\n"
" border-width: 2px;\n"
"border-color: rgb(97, 48, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 996, 846))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(80, 70, 711, 461))
        self.tableWidget.setMinimumSize(QtCore.QSize(2, 0))
        self.tableWidget.setStyleSheet("border-radius: 10px")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(80, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color:rgb(255, 253, 184)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(450, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color:rgb(255, 253, 184)")
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setGeometry(QtCore.QRect(750, 10, 181, 41))
        self.groupBox.setStyleSheet("border-radius: 5px")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
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
        self.listView_4.setToolTip(_translate("resultsWindow", "<html><head/><body><p>Equations Solver Program</p><p><br/></p></body></html>"))
        self.label.setText(_translate("resultsWindow", "Solution "))
        self.label_2.setText(_translate("resultsWindow", "Calculation time: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultsWindow = QtWidgets.QMainWindow()
    ui = Ui_resultsWindow()
    ui.setupUi(resultsWindow)
    resultsWindow.show()
    sys.exit(app.exec_())
