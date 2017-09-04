import os
import sys
import gui.test1 as test1
from PyQt5 import QtCore, QtGui, QtWidgets

import time



class MainInterface(QtCore.QObject):
    #create custom signals
    onData = QtCore.pyqtSignal()
    def __init__(self):
        super(MainInterface, self).__init__()
        self.m = QtWidgets.QMainWindow()
        self.a = test1.Ui_MainWindow()
        self.a.setupUi(self.m)

        #init data to display
        self.dataToDisplay = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0}

        #set signals
        self.a.pushButtonStart.clicked.connect(self.onStartClicked)
        self.a.pushButtonFinish.clicked.connect(self.onStopClicked)
        self.onData.connect(self.display_data)

        #show interface
        self.m.show()

        #self.a.pushButtonStart.clicked.connect(lambda: self.setValue(hr = 4, yaw = 10))

    ################################# SIGNAL METHODS #################################
    def ConnectStartButton(self, f):
        self.a.pushButtonStart.clicked.connect(f)

    def ConnectStopButton(self, f):
        self.a.pushButtonFinish.clicked.connect(f)


    ################################# BUTTONS METHODS #################################
    def onStartClicked(self):
        self.a.label_11.setStyleSheet("font: 11pt;")
        self.a.label_11.setText('capturing...')
        self.dataToDisplay = {'hr' : 10, 'yaw' : 20, 'pitch' : 30, 'roll' : 0}
        self.onData.emit()


    def onStopClicked(self):
        self.a.label_11.setStyleSheet("font-style: italic; font: 11pt;")
        self.a.label_11.setText('stop...')
        self.clearDisplays()

    ################################# LCD METHODS #################################
    def display_data(self):
        self.a.lcdHeartrate.display(self.dataToDisplay['hr'])
        self.a.lcdYaw.display(self.dataToDisplay['yaw'])
        self.a.lcdPitch.display(self.dataToDisplay['pitch'])
        self.a.lcdRoll.display(self.dataToDisplay['roll'])


    def clearDisplays(self):
        self.update_display_data()
        self.onData.emit()

    def update_display_data(self, d = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0}):
        self.dataToDisplay =  d
        self.onData.emit()

    def setValue(self, hr = None, yaw = None, pitch = None, roll = None):
        if not hr == None:
            self.a.lcdHeartrate.display(hr)
        if not yaw == None:
            self.a.lcdYaw.display(yaw)
        if not pitch == None:
            self.a.lcdPitch.display(pitch)
        if not roll == None:
            self.a.lcdRoll.display(roll)


        #time.sleep(5)
        #self.a.change_image()





def main():
    app = QtWidgets.QApplication(sys.argv)
    a = MainInterface()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()
    '''
    app = QtWidgets.QApplication(sys.argv)
    m = QtWidgets.QMainWindow()
    a = test.Ui_MainWindow()
    a.setupUi(m)
    m.show()
    sys.exit(app.exec_())
    '''
