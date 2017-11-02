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

        self.dataToDisplay = {'hr' : 0,
                              'yaw_t' : 0,
                              'pitch_t:' : 0,
                              'roll_t' : 0,
                              'yaw_c' : 0,
                              'pitch_c:' : 0,
                              'roll_c' : 0
                              }
        #set signals
        self.set_signals()

        #self.j = None

    def init_ui(self):
        #-----------main config-----------
        #Window title
        self.setWindowTitle("Lokomat therapy")
        #Window size
        self.setGeometry(100,100,1000,580)#Tamaño de la ventana
        #setting backgroung image
        Image=QImage("gui/img/Int.jpg")
        sImage=Image.scaled(1000,700,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        palette=QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        #----------------------------------
        #-----------Labels config----------
        #Heart rate:
        self.hrDisplay = {}
        #heart rate lcd
        self.hrDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.hrDisplay['lcd'].setGeometry(120,95, 120,30)
        #Yaw angle:
        self.yawDisplay = {}
        #yaw angle label
        self.yawDisplay['name'] = QtWidgets.QLabel(self)
        self.yawDisplay['name'].setText("Yaw")
        self.yawDisplay['name'].setStyleSheet("font-size:15px; Arial")
        self.yawDisplay['name'].setGeometry(120,125, 100,50)
        #yaw lcd
        self.yawDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.yawDisplay['lcd'].setGeometry(100,165, 50,30)
        #pitch angle:
        self.pitchDisplay = {}
        #pitch angle label
        self.pitchDisplay['name'] = QtWidgets.QLabel(self)
        self.pitchDisplay['name'].setText("Pitch")
        self.pitchDisplay['name'].setStyleSheet("font-size:15px; Arial")
        self.pitchDisplay['name'].setGeometry(175,125, 100,50)
        #pitch lcd
        self.pitchDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.pitchDisplay['lcd'].setGeometry(160,165, 50,30)
        #roll angle:
        self.rollDisplay = {}
        #roll angle label
        self.rollDisplay['name'] = QtWidgets.QLabel(self)
        self.rollDisplay['name'].setText("Roll")
        self.rollDisplay['name'].setStyleSheet("font-size:15px; Arial")
        self.rollDisplay['name'].setGeometry(230,125, 100,50)
        #roll lcd
        self.rollDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.rollDisplay['lcd'].setGeometry(220,165, 50,30)
        #Therapy time lcd
        self.TtimeDisplay = {}
        self.TtimeDisplay['lcd'] = QtWidgets.QLCDNumber(self)
        self.TtimeDisplay['lcd'].setGeometry(865,45, 100,50)


        #a =300
        #Yaw angle:
        self.yawDisplay1 = {}

        #yaw lcd
        self.yawDisplay1['lcd'] = QtWidgets.QLCDNumber(self)
        self.yawDisplay1['lcd'].setGeometry(100,235, 50,30)
        #pitch angle:
        self.pitchDisplay1 = {}
        #pitch lcd
        self.pitchDisplay1['lcd'] = QtWidgets.QLCDNumber(self)
        self.pitchDisplay1['lcd'].setGeometry(160, 235, 50, 30)
        #roll angle:
        self.rollDisplay1 = {}

        #roll lcd
        self.rollDisplay1['lcd'] = QtWidgets.QLCDNumber(self)
        self.rollDisplay1['lcd'].setGeometry(220,235, 50,30)



        #----------------------------------

        #----------buttons config----------
        #setting background start image
        
        self.start=QtWidgets.QLabel(self)
        self.start.setGeometry(885,165,55,55)
        Icon3=QtGui.QPixmap("gui/img/play.png")
        Icon_resize3= Icon3.scaled(55,55,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.start.setPixmap(Icon_resize3)
        
        #setting background start image
        
        self.stop=QtWidgets.QLabel(self)
        self.stop.setGeometry(885,235,55,55)
        Icon4=QtGui.QPixmap("gui/img/stop.png")
        Icon_resize5= Icon4.scaled(55,55,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.stop.setPixmap(Icon_resize5)
        
        self.controlButtons = {}
        #start button
        self.controlButtons['start'] = QtWidgets.QCommandLinkButton(self)
        self.controlButtons['start'].setIconSize(QSize(0,0))
        #self.controlButtons['start'].setText("Start")
        self.controlButtons['start'].setGeometry(885,165,55,55)
        
        
        self.controlButtons['stop'] = QtWidgets.QCommandLinkButton(self)
        self.controlButtons['stop'].setText("Stop")
        self.controlButtons['stop'].setGeometry(885,235,55,55)
        #self.controlButtons['stop'].setIcon(QtGui.QIcon('gui/img/stop'))
        self.controlButtons['stop'].setIconSize(QSize(0,0))
        self.controlButtons['stop'].setEnabled(False)
        #----------------------------------
        #
        #self.LabelPosture=QtWidgets.QLabel(self)
        #self.LabelPosture.setGeometry(760,60,220,440)
        #self.LabelPosture.setPixmap(QtGui.QPixmap('gui/img/cervical'))
        #
    
        #self.Stop.setIconSize(QSize(800,500))
        #self.LabelPosture1=QtWidgets.QLabel(self)
        #self.LabelPosture1.setGeometry(340,100,400,300)
        #self.LabelPosture1.setPixmap(QtGui.QPixmap('gui/img/cervical'))

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
        #lock start button
        self.controlButtons['start'].setEnabled(False)
        self.controlButtons['stop'].setEnabled(True)
        self.update_display_data(d = {
                                        'hr' : 1,
                                        'yaw_t' : 2,
                                        'pitch_t' : 3,
                                        'roll_t' : 4,
                                        'yaw_c' : 5,
                                        'pitch_c' : 6,
                                        'roll_c' : 7
                                        }
                                )
        self.Borg.j = 4
        self.Borg.move()

    def display_data(self):

        self.hrDisplay['lcd'].display(self.dataToDisplay['hr'])
        self.yawDisplay['lcd'].display(self.dataToDisplay['yaw_t'])
        self.pitchDisplay['lcd'].display(self.dataToDisplay['pitch_t'])
        self.rollDisplay['lcd'].display(self.dataToDisplay['roll_t'])
        self.yawDisplay1['lcd'].display(self.dataToDisplay['yaw_c'])
        self.pitchDisplay1['lcd'].display(self.dataToDisplay['pitch_c'])
        self.rollDisplay1['lcd'].display(self.dataToDisplay['roll_c'])

    def update_display_data(self,
                            d = {
                                'hr' : 0,
                                'yaw_t' : 0,
                                'pitch_t' : 0,
                                'roll_t' : 0,
                                'yaw_c' : 0,
                                'pitch_c:' : 0,
                                'roll_c' : 0
                                }
                            ):
        self.dataToDisplay =  d
        self.onData.emit()

    def onStopClicked(self):
        #function to modify the interface state and visuals
        self.controlButtons['start'].setEnabled(True)
        self.controlButtons['stop'].setEnabled(False)
        print('stop clicked')
        self.update_display_data(d = {
                                        'hr' : 0,
                                        'yaw_t' : 0,
                                        'pitch_t' : 0,
                                        'roll_t' : 0,
                                        'yaw_c' : 0,
                                        'pitch_c' : 0,
                                        'roll_c' : 0
                                        }
                                        )
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
        self.Labelborg.setGeometry(25,465,730,55)
        Icon2=QtGui.QPixmap("gui/img/borgh")
        Icon_resize= Icon2.scaled(730,55)
        self.Labelborg.setPixmap(Icon_resize)

        #get borg scale buttons
        self.create_borg_button()

    def create_borg_button(self, ep = 48,xp = 30, yp = 473, hp = 39,wp = 39):
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
        self.Borg[p].setStyleSheet("border:2.5px solid rgb(50,50,50); border-radius:10px;")
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
