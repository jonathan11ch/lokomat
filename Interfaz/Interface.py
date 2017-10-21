import PyQt5
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

class Window(QtWidgets.QWidget):
    onData = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.dataToDisplay = {'hr' : 0, 'yaw' : 0, 'pitch' : 0, 'roll' : 0}
        #set signals
        self.set_signals()

    def init_ui(self):
        #-----------main config-----------
        #Window title
        self.setWindowTitle("Lokomat therapy")
        #Window size
        self.setGeometry(100,100,1000,600)#Tamaño de la ventana
        #setting backgroung image
        Image=QImage("back1.jpg")
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
        self.controlButtons['start'].setIcon(QtGui.QIcon('play2'))
        self.controlButtons['start'].setIconSize(QSize(40,40))
        #stop button
        self.controlButtons['stop'] = QtWidgets.QPushButton(self)
        self.controlButtons['stop'].setText("Stop")
        self.controlButtons['stop'].setGeometry(180,520,120,60)
        self.controlButtons['stop'].setStyleSheet("font-size:20px; Arial")
        self.controlButtons['stop'].setIcon(QtGui.QIcon('stop'))
        self.controlButtons['stop'].setIconSize(QSize(40,40))
        #----------------------------------
        #
        self.LabelPosture=QtWidgets.QLabel(self)
        self.LabelPosture.setGeometry(760,60,220,440)
        self.LabelPosture.setPixmap(QtGui.QPixmap('cervical'))
        #
        self.LabelTitle=QtWidgets.QLabel(self)
        self.LabelTitle.setGeometry(788,10,240,30)
        self.LabelTitle.setText("Posture Behavior")
        self.LabelTitle.setStyleSheet("font-size:20px ;Arial")
        #self.Stop.setIconSize(QSize(800,500))
        self.LabelPosture1=QtWidgets.QLabel(self)
        self.LabelPosture1.setGeometry(340,100,400,300)
        self.LabelPosture1.setPixmap(QtGui.QPixmap('cervical'))


    #def create_display_dict(self, name, style,x,y,w,h):

        self.Labelborg=QtWidgets.QLabel(self)
        self.Labelborg.setGeometry(50,430,700,90)
        Icon2=QtGui.QPixmap("borg_act")
        Icon_resize= Icon2.scaled(700,90)
        self.Labelborg.setPixmap(Icon_resize)
        #self.Labelborg.setIconSize(QSize(600,50))

        #self.Labelborg.setPixmap(QtGui.QPixmap('borg_act'))
        #image.scaled(200,200,Qt::IgnoreAspectRatio,Qt::FastTransformation);
        #Botones Escala de Borg
        self.Borg1=QtWidgets.QCommandLinkButton(self)
        self.Borg1.setIconSize(QSize(0, 0))
        self.Borg1.setGeometry(50,435,48,80)
        self.Borg2=QtWidgets.QCommandLinkButton(self)
        self.Borg2.setGeometry(98,435,47,80)
        self.Borg2.setIconSize(QSize(0, 0))
        self.Borg3=QtWidgets.QCommandLinkButton(self)
        self.Borg3.setGeometry(145,435,46,80)
        self.Borg3.setIconSize(QSize(0, 0))
        self.Borg4=QtWidgets.QCommandLinkButton(self)
        self.Borg4.setGeometry(192,435,46,80)
        self.Borg4.setIconSize(QSize(0, 0))
        self.Borg5=QtWidgets.QCommandLinkButton(self)
        self.Borg5.setGeometry(237,435,46,80)
        self.Borg5.setIconSize(QSize(0, 0))
        self.Borg6=QtWidgets.QCommandLinkButton(self)
        self.Borg6.setGeometry(285,435,46,80)
        self.Borg6.setIconSize(QSize(0, 0))
        self.Borg7=QtWidgets.QCommandLinkButton(self)
        self.Borg7.setGeometry(331,435,46,80)
        self.Borg7.setIconSize(QSize(0, 0))
        self.Borg8=QtWidgets.QCommandLinkButton(self)
        self.Borg8.setGeometry(377,435,46,80)
        self.Borg8.setIconSize(QSize(0, 0))
        self.Borg9=QtWidgets.QCommandLinkButton(self)
        self.Borg9.setGeometry(423,435,46,80)
        self.Borg9.setIconSize(QSize(0, 0))
        self.Borg10=QtWidgets.QCommandLinkButton(self)
        self.Borg10.setGeometry(469,435,46,80)
        self.Borg10.setIconSize(QSize(0, 0))
        self.Borg11=QtWidgets.QCommandLinkButton(self)
        self.Borg11.setGeometry(517,435,46,80)
        self.Borg11.setIconSize(QSize(0, 0))
        self.Borg12=QtWidgets.QCommandLinkButton(self)
        self.Borg12.setGeometry(562,435,46,80)
        self.Borg12.setIconSize(QSize(0, 0))
        self.Borg13=QtWidgets.QCommandLinkButton(self)
        self.Borg13.setGeometry(609,435,46,80)
        self.Borg13.setIconSize(QSize(0, 0))
        self.Borg14=QtWidgets.QCommandLinkButton(self)
        self.Borg14.setGeometry(655,435,47,80)
        self.Borg14.setIconSize(QSize(0, 0))
        self.Borg15=QtWidgets.QCommandLinkButton(self)
        self.Borg15.setGeometry(702,435,49,80)
        self.Borg15.setIconSize(QSize(0, 0))


        self.show()

    def set_signals(self):
        self.controlButtons['start'].clicked.connect(self.onStartClicked)
        self.controlButtons['stop'].clicked.connect(self.onStopClicked)
        self.onData.connect(self.display_data)

    #----------------------------- SIGNAL METHODS ------------------------------
    def ConnectStartButton(self, f):
        self.controlButtons['start'].clicked.connect(f)

    def ConnectStopButton(self, f):
        self.controlButtons['stop'].clicked.connect(f)
    #---------------------------------------------------------------------------

    def onStartClicked(self):
        #function to modify the interface state and visuals
        print('start clicked')
        self.update_display_data(d = {'hr' : 1, 'yaw' : 2, 'pitch' : 3, 'roll' : 4})

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



app=QtWidgets.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())

#M=run()
