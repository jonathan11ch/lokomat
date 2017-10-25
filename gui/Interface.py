import PyQt5
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

class MainTherapyWin(QtWidgets.QWidget):
    onData = QtCore.pyqtSignal()
    onJoy = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.dataToDisplay = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0}
        #set signals
        self.set_signals()

        #self.j = None

    def init_ui(self):
        #-----------main config-----------
        #Window title
        self.setWindowTitle("Lokomat therapy")
        #Window size
        self.setGeometry(100,100,1000,600)#Tamaño de la ventana
        #setting backgroung image
        Image=QImage("gui/img/back1.jpg")
        sImage=Image.scaled(QSize(1000,600))
        palette=QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        #----------------------------------
        #-----------Labels config----------
        #Heart rate:
        self.hrDisplay = {}
        #heart_rate label
        self.hrDisplay['name'] = QtWidgets.QLabel(self)
        self.hrDisplay['name'].setText("Heart Rate")
        self.hrDisplay['name'].setStyleSheet("font-size:20px; Arial")
        self.hrDisplay['name'].setGeometry(40,40, 100,100)
        #heart rate units label
        self.hrDisplay['units'] = QtWidgets.QLabel(self)
        self.hrDisplay['units'].setText("Bpm")
        self.hrDisplay['units'].setStyleSheet("font-size:20px; Arial")
        self.hrDisplay['units'].setGeometry(280,40, 100,100)
        #heart rate lcd
        self.hrDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.hrDisplay['lcd'].setGeometry(150,65, 100,50)
        #Yaw angle:
        self.yawDisplay = {}
        #yaw angle label
        self.yawDisplay['name'] = QtWidgets.QLabel(self)
        self.yawDisplay['name'].setText("Yaw")
        self.yawDisplay['name'].setStyleSheet("font-size:20px; Arial")
        self.yawDisplay['name'].setGeometry(50,110, 100,100)
        #yaw angle units label
        self.yawDisplay['units'] = QtWidgets.QLabel(self)
        self.yawDisplay['units'].setText("Deg")
        self.yawDisplay['units'].setStyleSheet("font-size:20px; Arial")
        self.yawDisplay['units'].setGeometry(280,110, 100,100)
        #yaw lcd
        self.yawDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.yawDisplay['lcd'].setGeometry(150,130, 100,50)
        #pitch angle:
        self.pitchDisplay = {}
        #pitch angle label
        self.pitchDisplay['name'] = QtWidgets.QLabel(self)
        self.pitchDisplay['name'].setText("Pitch")
        self.pitchDisplay['name'].setStyleSheet("font-size:20px; Arial")
        self.pitchDisplay['name'].setGeometry(50,180, 100,100)
        #pitch angle units label
        self.pitchDisplay['units'] = QtWidgets.QLabel(self)
        self.pitchDisplay['units'].setText("Deg")
        self.pitchDisplay['units'].setStyleSheet("font-size:20px; Arial")
        self.pitchDisplay['units'].setGeometry(280,180, 100,100)
        #pitch lcd
        self.pitchDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.pitchDisplay['lcd'].setGeometry(150,200, 100,50)
        #roll angle:
        self.rollDisplay = {}
        #roll angle label
        self.rollDisplay['name'] = QtWidgets.QLabel(self)
        self.rollDisplay['name'].setText("Roll")
        self.rollDisplay['name'].setStyleSheet("font-size:20px; Arial")
        self.rollDisplay['name'].setGeometry(50,250, 100,100)
        #roll angle units label
        self.rollDisplay['units'] = QtWidgets.QLabel(self)
        self.rollDisplay['units'].setText("Deg")
        self.rollDisplay['units'].setStyleSheet("font-size:20px; Arial")
        self.rollDisplay['units'].setGeometry(280,250, 100,100)
        #roll lcd
        self.rollDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.rollDisplay['lcd'].setGeometry(150,270, 100,50)
        #----------------------------------

        #----------buttons config----------
        self.controlButtons = {}
        #start button
        self.controlButtons['start'] = QtWidgets.QPushButton(self)
        self.controlButtons['start'].setText("Start")
        self.controlButtons['start'].setGeometry(50,520,120,60)
        self.controlButtons['start'].setStyleSheet("font-size:20px; Arial")
        self.controlButtons['start'].setIcon(QtGui.QIcon('gui/img/play2'))
        self.controlButtons['start'].setIconSize(QSize(40,40))
        #stop button
        self.controlButtons['stop'] = QtWidgets.QPushButton(self)
        self.controlButtons['stop'].setText("Stop")
        self.controlButtons['stop'].setGeometry(180,520,120,60)
        self.controlButtons['stop'].setStyleSheet("font-size:20px; Arial")
        self.controlButtons['stop'].setIcon(QtGui.QIcon('gui/img/stop'))
        self.controlButtons['stop'].setIconSize(QSize(40,40))
        #----------------------------------
        #
        self.LabelPosture=QtWidgets.QLabel(self)
        self.LabelPosture.setGeometry(760,60,220,440)
        self.LabelPosture.setPixmap(QtGui.QPixmap('gui/img/cervical'))
        #
        self.LabelTitle=QtWidgets.QLabel(self)
        self.LabelTitle.setGeometry(788,10,240,30)
        self.LabelTitle.setText("Posture Behavior")
        self.LabelTitle.setStyleSheet("font-size:20px ;Arial")
        #self.Stop.setIconSize(QSize(800,500))
        self.LabelPosture1=QtWidgets.QLabel(self)
        self.LabelPosture1.setGeometry(340,100,400,300)
        self.LabelPosture1.setPixmap(QtGui.QPixmap('gui/img/cervical'))

        #create borgscale button
        self.Borg = BorgButton(self)

        self.show()


    def set_signals(self):
        self.controlButtons['start'].clicked.connect(self.onStartClicked)
        self.controlButtons['stop'].clicked.connect(self.onStopClicked)
        self.onData.connect(self.display_data)
        self.onJoy.connect(self.Borg.move)

    #----------------------------- SIGNAL METHODS ------------------------------
    def connectStartButton(self, f):
        print('connectStartButton')
        self.controlButtons['start'].clicked.connect(f)

    def connectStopButton(self, f):
        self.controlButtons['stop'].clicked.connect(f)
    #---------------------------------------------------------------------------

    def onStartClicked(self):
        #function to modify the interface state and visuals
        print('start clicked')
        self.update_display_data(d = {'hr' : 1, 'yaw' : 2, 'pitch' : 3, 'roll' : 4})
        self.Borg.j = 4
        self.Borg.move()

    def display_data(self):
        self.hrDisplay['lcd'].display(self.dataToDisplay['hr'])
        self.yawDisplay['lcd'].display(self.dataToDisplay['yaw'])
        self.pitchDisplay['lcd'].display(self.dataToDisplay['pitch'])
        self.rollDisplay['lcd'].display(self.dataToDisplay['roll'])

    def update_display_data(self, d = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0}):
        self.dataToDisplay =  d
        self.onData.emit()

    def onStopClicked(self):
        #function to modify the interface state and visuals
        print('stop clicked')
        self.update_display_data(d = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0})
        self.Borg.j = 2
        self.Borg.move()

#Borg Button object
class BorgButton(object):
    def __init__(self, window):
        self.window = window
        self.cursorStatus = 0
        self.j = None
        #setting background Label Borgº
        self.Labelborg=QtWidgets.QLabel(self.window)
        self.Labelborg.setGeometry(50,430,718,90)
        Icon2=QtGui.QPixmap("gui/img/borg_act")
        Icon_resize= Icon2.scaled(700,90)
        self.Labelborg.setPixmap(Icon_resize)

        #get borg scale buttons
        self.create_borg_button()

    def create_borg_button(self, ep = 48,xp = 50, yp = 430, hp = 48,wp = 90):
        self.Borg = []
        offset = 1
        x = xp
        e = ep
        y = yp
        h = hp
        w = wp
        for i in range(15):
            #print ('button created')
            #self.Borg.append(QtWidgets.QCommandLinkButton(self.window))
            self.Borg.append(QtWidgets.QLabel(self.window))
            #self.Borg[-1].setIconSize(QSize(0, 0))
            Icon2=QtGui.QPixmap("gui/img/l" + str(i))
            Icon_resize= Icon2.scaled(h,w)
            self.Borg[-1].setPixmap(Icon_resize)
            self.Borg[-1].setGeometry(x,y,h,w)
            x = x + e
            '''
            if i < 2:
                self.Borg.append(QtWidgets.QCommandLinkButton(self.window))
                self.Borg[-1].setIconSize(QSize(0, 0))
                self.Borg[-1].setGeometry(x,y,h,w)
                x = x + e

            else:
                self.Borg.append(QtWidgets.QCommandLinkButton(self.window))
                self.Borg[-1].setIconSize(QSize(0, 0))
                self.Borg[-1].setGeometry(x,y,h-1,w)
                x = x + e
            '''

        self.set_cursor(0)

    def set_cursor(self, p):
        self.Borg[self.cursorStatus].setStyleSheet("border-style: outset")
        self.Borg[p].setStyleSheet("border:3px solid rgb(0,0,0);")
        self.cursorStatus = p

    def move(self):

        if self.j == 4:
            if self.cursorStatus < 14:
                self.set_cursor(self.cursorStatus + 1)
        elif self.j ==2:
            if self.cursorStatus > 0:
                self.set_cursor(self.cursorStatus -1)

    #def

    #TODO: to implement these functions
    def lock_buttons(self):
        print('lock borg buttons')

    def unlock_buttons(self):
        print('unlock borg buttons')


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    GUI=MainTherapyWin()
    sys.exit(app.exec_())

#M=run()
