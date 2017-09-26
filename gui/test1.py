# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 433)
        MainWindow.setStyleSheet("background-image: url(background.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(110, 330, 101, 51))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.lcdHeartrate = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdHeartrate.setGeometry(QtCore.QRect(170, 70, 101, 41))
        self.lcdHeartrate.setObjectName("lcdHeartrate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 117, 29))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 90, 41, 21))
        self.label_2.setObjectName("label_2")
        self.pushButtonFinish = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFinish.setGeometry(QtCore.QRect(210, 330, 101, 51))
        self.pushButtonFinish.setObjectName("pushButtonFinish")
        self.lcdYaw = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdYaw.setGeometry(QtCore.QRect(170, 130, 101, 41))
        self.lcdYaw.setObjectName("lcdYaw")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 117, 29))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 150, 41, 21))
        self.label_4.setObjectName("label_4")
        self.lcdPitch = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdPitch.setGeometry(QtCore.QRect(170, 180, 101, 41))
        self.lcdPitch.setObjectName("lcdPitch")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 117, 29))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 200, 41, 21))
        self.label_6.setObjectName("label_6")
        self.lcdRoll = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdRoll.setGeometry(QtCore.QRect(170, 230, 101, 41))
        self.lcdRoll.setObjectName("lcdRoll")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 240, 117, 29))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 250, 41, 21))
        self.label_8.setObjectName("label_8")
        self.postureImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.postureImageLabel.setGeometry(QtCore.QRect(430, 50, 191, 251))
        self.postureImageLabel.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.postureImageLabel.setObjectName("postureImageLabel")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 10, 117, 29))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 370, 61, 16))
        self.label_11.setStyleSheet("font: 11pt ;")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; font-weight:600;\">Heartrate:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "BPM"))
        self.pushButtonFinish.setText(_translate("MainWindow", "Finish"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; font-weight:600;\">Yaw:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Deg"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; font-weight:600;\">Pitch:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Deg"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; font-weight:600;\">Roll:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Deg"))
        self.postureImageLabel.setText(_translate("MainWindow", "<html><head/><body><p>posture_image</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Posture</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-style:italic;\">stopped</span></p></body></html>"))