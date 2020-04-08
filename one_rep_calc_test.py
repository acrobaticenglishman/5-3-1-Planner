# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/nathanprice/Documents/GitHub/5-3-1-Planner/test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import math
from five_three_one_planner import one_rep_max_calc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.reps_box = QtWidgets.QSpinBox(self.centralwidget)
        self.reps_box.setGeometry(QtCore.QRect(150, 230, 51, 31))
        self.reps_box.setObjectName("reps_box")

        self.one_rep_label = QtWidgets.QLabel(self.centralwidget)
        self.one_rep_label.setGeometry(QtCore.QRect(160, 270, 101, 31))
        self.one_rep_label.setText("")
        self.one_rep_label.setObjectName("one_rep_label")

        self.one_rep_calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_rep_calc_button.setGeometry(QtCore.QRect(120, 320, 191, 32))
        self.one_rep_calc_button.setObjectName("one_rep_calc_button")
        self.one_rep_calc_button.clicked.connect(self.calc_one_rep_max)

        self.weight_box = QtWidgets.QSpinBox(self.centralwidget)
        self.weight_box.setGeometry(QtCore.QRect(230, 230, 51, 31))
        self.weight_box.setObjectName("weight_box")
        self.weight_box.setMaximum(500)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 22))

        self.menubar.setObjectName("menubar")
        self.menuDick = QtWidgets.QMenu(self.menubar)
        self.menuDick.setObjectName("menuDick")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDick.menuAction())
        self.one_rep_calc_button.clicked.connect(self.calc_one_rep_max)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.one_rep_calc_button.setText(_translate("MainWindow", "Calculate One Rep Max"))
        self.menuDick.setTitle(_translate("MainWindow", "File"))

    def calc_one_rep_max(self):

        reps = int (self.reps_box.cleanText())
        weight = int (self.weight_box.cleanText())

        one_rep_max = math.floor(weight * (1 + (reps / 30)))
        training_max = math.floor(one_rep_max * .90)

        print (reps, weight)
        output = f'Your One Rep Max is {one_rep_max}kg\nYour Training Max is {training_max}kg'
        self.one_rep_label.setText(output)
        self.one_rep_label.adjustSize()
        self.one_rep_label.repaint()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
