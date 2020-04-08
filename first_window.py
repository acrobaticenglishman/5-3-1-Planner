# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/nathanprice/Documents/GitHub/5-3-1-Planner/first_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math

class Ui_First_Window(object):
    # SetUp UI Function
    def setupUi(self, First_Window):
        First_Window.setObjectName("First_Window")
        First_Window.setGeometry(50, 300, 0, 0)
        First_Window.resize(855, 604)
        self.centralwidget = QtWidgets.QWidget(First_Window)
        self.centralwidget.setObjectName("centralwidget")
        # SQUAT INFORMATION
        # Squat Reps Box
        self.squat_reps_box = QtWidgets.QSpinBox(self.centralwidget)
        self.squat_reps_box.setGeometry(QtCore.QRect(60, 220, 51, 31))
        self.squat_reps_box.setObjectName("squat_reps_box")
        self.squat_reps_box.setAlignment(Qt.AlignCenter)
        self.squat_reps_box.setButtonSymbols(self.squat_reps_box.NoButtons)
        # Squat Reps Label
        self.squat_reps_label = QtWidgets.QLabel(self.centralwidget)
        self.squat_reps_label.setObjectName('squat_reps_label')
        self.squat_reps_label.setGeometry(QtCore.QRect(69, 195, 51, 31))
        self.squat_reps_label.setText('Reps')
        # Squat Weight Box
        self.squat_weight_box = QtWidgets.QSpinBox(self.centralwidget)
        self.squat_weight_box.setGeometry(QtCore.QRect(140, 220, 51, 31))
        self.squat_weight_box.setObjectName("squat_weight_box")
        self.squat_weight_box.setMaximum(2000)
        self.squat_weight_box.setAlignment(Qt.AlignCenter)
        self.squat_weight_box.setButtonSymbols(self.squat_weight_box.NoButtons)
        # Squat Weight Label
        self.squat_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.squat_weight_label.setObjectName('squat_weight_label')
        self.squat_weight_label.setGeometry(QtCore.QRect(145, 195, 51, 31))
        self.squat_weight_label.setText('Weight')
        # Squat X Label
        self.squat_x_label = QtWidgets.QLabel(self.centralwidget)
        self.squat_x_label.setGeometry(QtCore.QRect(120, 220, 101, 31))
        self.squat_x_label.setText("X")
        self.squat_x_label.setObjectName("squat_label")
        # Squat Label
        self.squat_label = QtWidgets.QLabel(self.centralwidget)
        self.squat_label.setGeometry(QtCore.QRect(75, 260, 101, 31))
        self.squat_label.setText("")
        self.squat_label.setObjectName("squat_label")
        self.squat_label.setAlignment(Qt.AlignCenter)
        # Squat Image
        self.squat_img = QtWidgets.QLabel(self.centralwidget)
        self.squat_img.setGeometry(QtCore.QRect(70, 70, 111, 121))
        self.squat_img.setText("")
        self.squat_img.setPixmap(QtGui.QPixmap("/Users/nathanprice/Documents/GitHub/5-3-1-Planner/Imgs/Back_Squat.jpg"))
        self.squat_img.setScaledContents(True)
        self.squat_img.setObjectName("squat_img")

        # DEADLIFT INFORMATION
        # Deadlift Reps Box
        self.deadlift_reps_box = QtWidgets.QSpinBox(self.centralwidget)
        self.deadlift_reps_box.setGeometry(QtCore.QRect(270, 220, 51, 31))
        self.deadlift_reps_box.setObjectName("deadlift_reps_box")
        self.deadlift_reps_box.setAlignment(Qt.AlignCenter)
        self.deadlift_reps_box.setButtonSymbols(self.deadlift_reps_box.NoButtons)
        # Deadlift Reps Label
        self.deadlift_reps_label = QtWidgets.QLabel(self.centralwidget)
        self.deadlift_reps_label.setObjectName('deadlift_reps_label')
        self.deadlift_reps_label.setGeometry(QtCore.QRect(279, 195, 51, 31))
        self.deadlift_reps_label.setText('Reps')
        # Deadlift Weight Box
        self.deadlift_weight_box = QtWidgets.QSpinBox(self.centralwidget)
        self.deadlift_weight_box.setGeometry(QtCore.QRect(350, 220, 51, 31))
        self.deadlift_weight_box.setObjectName("deadlift_weight_box")
        self.deadlift_weight_box.setMaximum(2000)
        self.deadlift_weight_box.setAlignment(Qt.AlignCenter)
        # Deadlift Weight Label
        self.deadlift_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.deadlift_weight_label.setObjectName('deadlift_weight_label')
        self.deadlift_weight_label.setGeometry(QtCore.QRect(355, 195, 51, 31))
        self.deadlift_weight_label.setText('Weight')
        # Deadlift X Label
        self.deadlift_x_label = QtWidgets.QLabel(self.centralwidget)
        self.deadlift_x_label.setGeometry(QtCore.QRect(330, 220, 101, 31))
        self.deadlift_x_label.setText("X")
        self.deadlift_x_label.setObjectName("deadlift_label")
        # Deadlift One Rep Max Label
        self.deadlift_label = QtWidgets.QLabel(self.centralwidget)
        self.deadlift_label.setGeometry(QtCore.QRect(285, 260, 101, 31))
        self.deadlift_label.setText('')
        self.deadlift_label.setObjectName("deadlift_label")
        self.deadlift_label.setAlignment(Qt.AlignCenter)
        # Deadlift Image
        self.deadlift_img = QtWidgets.QLabel(self.centralwidget)
        self.deadlift_img.setGeometry(QtCore.QRect(280, 70, 111, 121))
        self.deadlift_img.setText("")
        self.deadlift_img.setPixmap(QtGui.QPixmap("/Users/nathanprice/Documents/GitHub/5-3-1-Planner/Imgs/Deadlift.jpg"))
        self.deadlift_img.setScaledContents(True)
        self.deadlift_img.setObjectName("deadlift_img")

        # BENCH PRESS INFORMATION
        # Bench Reps Box
        self.bench_reps_box = QtWidgets.QSpinBox(self.centralwidget)
        self.bench_reps_box.setGeometry(QtCore.QRect(470, 220, 51, 31))
        self.bench_reps_box.setObjectName("bench_reps_box")
        self.bench_reps_box.setAlignment(Qt.AlignCenter)
        self.bench_reps_box.setButtonSymbols(self.bench_reps_box.NoButtons)
        # Bench Reps Label
        self.bench_reps_label = QtWidgets.QLabel(self.centralwidget)
        self.bench_reps_label.setGeometry(QtCore.QRect(479, 195, 51, 31))
        self.bench_reps_label.setText('Reps')
        self.bench_reps_label.setObjectName('bench_reps_label')
        # Bench Weight Box
        self.bench_weight_box = QtWidgets.QSpinBox(self.centralwidget)
        self.bench_weight_box.setGeometry(QtCore.QRect(550, 220, 51, 31))
        self.bench_weight_box.setObjectName("bench_weight_box")
        self.bench_weight_box.setMaximum(2000)
        self.bench_weight_box.setAlignment(Qt.AlignCenter)
        self.bench_weight_box.setButtonSymbols(self.bench_weight_box.NoButtons)
        # Bench Weight Label
        self.bench_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.bench_weight_label.setObjectName('bench_weight_label')
        self.bench_weight_label.setGeometry(QtCore.QRect(555, 195, 51, 31))
        self.bench_weight_label.setText('Weight')
        # Bench X Label
        self.bench_x_label = QtWidgets.QLabel(self.centralwidget)
        self.bench_x_label.setGeometry(QtCore.QRect(530, 220, 101, 31))
        self.bench_x_label.setText("X")
        self.bench_x_label.setObjectName("bench_label")
        # Bench Label
        self.bench_label = QtWidgets.QLabel(self.centralwidget)
        self.bench_label.setGeometry(QtCore.QRect(480, 260, 101, 31))
        self.bench_label.setText("")
        self.bench_label.setObjectName("bench_label")
        self.bench_label.setAlignment(Qt.AlignCenter)
        # Bench Image
        self.bench_img = QtWidgets.QLabel(self.centralwidget)
        self.bench_img.setGeometry(QtCore.QRect(480, 70, 111, 121))
        self.bench_img.setText("")
        self.bench_img.setPixmap(QtGui.QPixmap("/Users/nathanprice/Documents/GitHub/5-3-1-Planner/Imgs/Bench.jpg"))
        self.bench_img.setScaledContents(True)
        self.bench_img.setObjectName("bench_img")

        # OVERHEAD PRESS INFORMATION
        # Overhead Press Reps Box
        self.ohp_reps_box = QtWidgets.QSpinBox(self.centralwidget)
        self.ohp_reps_box.setGeometry(QtCore.QRect(670, 220, 51, 31))
        self.ohp_reps_box.setObjectName("ohp_reps_box")
        self.ohp_reps_box.setAlignment(Qt.AlignCenter)
        self.ohp_reps_box.setButtonSymbols(self.ohp_reps_box.NoButtons)
        # Overhead Press Reps Label
        self.ohp_reps_label = QtWidgets.QLabel(self.centralwidget)
        self.ohp_reps_label.setObjectName('ohp_reps_label')
        self.ohp_reps_label.setGeometry(QtCore.QRect(679, 195, 51, 31))
        self.ohp_reps_label.setText('Reps')
        # Overhead Press Weight Box
        self.ohp_weight_box = QtWidgets.QSpinBox(self.centralwidget)
        self.ohp_weight_box.setGeometry(QtCore.QRect(750, 220, 51, 31))
        self.ohp_weight_box.setObjectName("ohp_weight_box")
        self.ohp_weight_box.setMaximum(2000)
        self.ohp_weight_box.setAlignment(Qt.AlignCenter)
        self.ohp_weight_box.setButtonSymbols(self.ohp_weight_box.NoButtons)
        # Overhead Weight Label
        self.ohp_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.ohp_weight_label.setObjectName('ohp_weight_label')
        self.ohp_weight_label.setGeometry(QtCore.QRect(755, 195, 51, 31))
        self.ohp_weight_label.setText('Weight')
        # Overhead Press X Label
        self.ohp_x_label = QtWidgets.QLabel(self.centralwidget)
        self.ohp_x_label.setGeometry(QtCore.QRect(730, 220, 101, 31))
        self.ohp_x_label.setText("X")
        self.ohp_x_label.setObjectName("ohp_label")
        # Overhead Press Label
        self.ohp_label = QtWidgets.QLabel(self.centralwidget)
        self.ohp_label.setGeometry(QtCore.QRect(685, 260, 101, 31))
        self.ohp_label.setText("")
        self.ohp_label.setObjectName("ohp_label")
        self.ohp_label.setAlignment(Qt.AlignCenter)
        # Overhead Press Image
        self.ohp_img = QtWidgets.QLabel(self.centralwidget)
        self.ohp_img.setGeometry(QtCore.QRect(681, 70, 111, 121))
        self.ohp_img.setText("")
        self.ohp_img.setPixmap(QtGui.QPixmap("/Users/nathanprice/Documents/GitHub/5-3-1-Planner/Imgs/OHP.jpg"))
        self.ohp_img.setScaledContents(True)
        self.ohp_img.setObjectName("ohp_img")

        # One Rep Calc Button
        self.one_rep_calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_rep_calc_button.setGeometry(QtCore.QRect(280, 370, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.one_rep_calc_button.setFont(font)
        self.one_rep_calc_button.setObjectName("one_rep_calc_button")
        self.one_rep_calc_button.clicked.connect(self.click_one_rep_calc_button)

        # First Window - Main
        First_Window.setCentralWidget(self.centralwidget)
        # First Window - Menu Bar
        self.menubar = QtWidgets.QMenuBar(First_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 22))
        self.menubar.setObjectName("menubar")

        self.retranslateUi(First_Window)
        QtCore.QMetaObject.connectSlotsByName(First_Window)

    def retranslateUi(self, First_Window):
        _translate = QtCore.QCoreApplication.translate
        First_Window.setWindowTitle(_translate("First_Window", "One Rep Max Calculator"))
        self.one_rep_calc_button.setText(_translate("First_Window", "Calculate One Rep Max"))

    def click_one_rep_calc_button(self):
        # Squat
        squat_reps = int(self.squat_reps_box.cleanText())
        squat_weight = int (self.squat_weight_box.cleanText())
        squat_one_rep_max = math.floor(squat_weight * (1 + (squat_reps / 30)))
        squat_training_max = math.floor(squat_one_rep_max * .90)
        squat_output = f'One Rep Max: {squat_one_rep_max}\nTraining Max: {squat_training_max}'
        self.squat_label.setText(squat_output)
        self.squat_label.adjustSize()
        self.squat_label.repaint()

        # Deadlift
        deadlift_reps = int(self.deadlift_reps_box.cleanText())
        deadlift_weight = int(self.deadlift_weight_box.cleanText())
        deadlift_one_rep_max = math.floor(deadlift_weight * (1 + (deadlift_reps / 30)))
        deadlift_training_max = math.floor(deadlift_one_rep_max * .90)
        deadlift_output = f'One Rep Max: {deadlift_one_rep_max}\nTraining Max: {deadlift_training_max}'
        self.deadlift_label.setText(deadlift_output)
        self.deadlift_label.adjustSize()
        self.deadlift_label.repaint()

        # Bench Press
        bench_reps = int (self.bench_reps_box.cleanText())
        bench_weight = int (self.bench_weight_box.cleanText())
        bench_one_rep_max = math.floor(bench_weight * (1 + (bench_reps / 30)))
        bench_training_max = math.floor(bench_one_rep_max * .90)
        bench_output = f'One Rep Max: {bench_one_rep_max}\nTraining Max: {bench_training_max}'
        self.bench_label.setText(bench_output)
        self.bench_label.adjustSize()
        self.bench_label.repaint()

        # Overhead Press
        ohp_reps = int (self.ohp_reps_box.cleanText())
        ohp_weight = int (self.ohp_weight_box.cleanText())
        ohp_one_rep_max = math.floor(ohp_weight * (1 + (ohp_reps / 30)))
        ohp_training_max = math.floor(ohp_one_rep_max * .90)
        ohp_output = f'One Rep Max: {ohp_one_rep_max}\nTraining Max: {ohp_training_max}'
        self.ohp_label.setText(ohp_output)
        self.ohp_label.adjustSize()
        self.ohp_label.repaint()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    First_Window = QtWidgets.QMainWindow()
    ui = Ui_First_Window()
    ui.setupUi(First_Window)
    First_Window.show()
    sys.exit(app.exec_())
