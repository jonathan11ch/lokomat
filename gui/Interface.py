import PyQt5
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #-----------main config-----------
        #Window title
        self.setWindowTitle("Lokomat therapy")
        #Window size
        self.setGeometry(100,100,1000,600)
        #setting backgroung image
        Image=QImage("back1.jpg")
        sImage=Image.scaled(QSize(1000,600))
        palette=QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        #----------------------------------
        #-----------Labels config----------
        #Heart rate:
        #label name
        self.hrDisplay = {}
        self.hrDisplay['name'] = QtWidgets.QLabel(self)
        self.hrDisplay['name'].setText("Heart Rate")
        self.hrDisplay['name'].setStyleSheet("font-size:20px; Arial")
        self.hrDisplay['name'].setGeometry(40,40, 100,100)

        self.label2=QtWidgets.QLabel(self)
        self.label2.setText("Yaw")
        self.label2.setStyleSheet("font-size:20px; Arial")
        self.label2.setGeometry(50,110, 100,100)

        self.label3=QtWidgets.QLabel(self)
        self.label3.setText("Pitch")
        self.label3.setStyleSheet("font-size:20px; Arial")
        self.label3.setGeometry(50,180, 100,100)

        self.label4=QtWidgets.QLabel(self)
        self.label4.setText("Roll")
        self.label4.setStyleSheet("font-size:20px; Arial")
        self.label4.setGeometry(50,250, 100,100)

        self.textbox=QtWidgets.QLineEdit(self)
        self.textbox.setGeometry(150,65, 100,50)
        self.textbox.setStyleSheet("font-size:20px; Arial")
        self.textbox1=QtWidgets.QLineEdit(self)
        self.textbox1.setGeometry(150,130, 100,50)
        self.textbox1.setStyleSheet("font-size:20px; Arial")
        self.textbox1=QtWidgets.QLineEdit(self)
        self.textbox1.setGeometry(150,130, 100,50)
        self.textbox1.setStyleSheet("font-size:20px; Arial")
        self.textbox2=QtWidgets.QLineEdit(self)
        self.textbox2.setGeometry(150,200, 100,50)
        self.textbox2.setStyleSheet("font-size:20px; Arial")
        self.textbox3=QtWidgets.QLineEdit(self)
        self.textbox3.setGeometry(150,270, 100,50)
        self.textbox3.setStyleSheet("font-size:20px; Arial")
        self.label11=QtWidgets.QLabel(self)
        self.label11.setText("Bpm")
        self.label11.setStyleSheet("font-size:20px; Arial")
        self.label11.setGeometry(280,40, 100,100)
        self.label21=QtWidgets.QLabel(self)
        self.label21.setText("°")
        self.label21.setStyleSheet("font-size:20px; Arial")
        self.label21.setGeometry(280,110, 100,100)
        self.label31=QtWidgets.QLabel(self)
        self.label31.setText("°")
        self.label31.setStyleSheet("font-size:20px; Arial")
        self.label31.setGeometry(280,180, 100,100)
        self.label41=QtWidgets.QLabel(self)
        self.label41.setText("°")
        self.label41.setStyleSheet("font-size:20px; Arial")
        self.label41.setGeometry(280,250, 100,100)
        self.Start=QtWidgets.QPushButton(self)
        self.Start.setText("Start")
        self.Start.setGeometry(440,535,100,50)
        self.Start.setStyleSheet("font-size:15px; Arial")
        self.Start.setIcon(QtGui.QIcon('play2'))
        self.Start.setIconSize(QSize(30,30))
        self.Stop=QtWidgets.QPushButton(self)
        self.Stop.setText("Stop")
        self.Stop.setGeometry(560,535,100,50)
        self.Stop.setStyleSheet("font-size:15px; Arial")
        self.Stop.setIcon(QtGui.QIcon('stop'))
        self.Stop.setIconSize(QSize(30,30))
        self.LabelPosture=QtWidgets.QLabel(self)
        self.LabelPosture.setGeometry(760,60,220,440)
        self.LabelPosture.setPixmap(QtGui.QPixmap('cervical'))
        self.LabelTitle=QtWidgets.QLabel(self)
        self.LabelTitle.setGeometry(788,10,240,30)
        self.LabelTitle.setText("Posture Behavior")
        self.LabelTitle.setStyleSheet("font-size:20px ;Arial")
        self.LabelPosture1=QtWidgets.QLabel(self)
        self.LabelPosture1.setGeometry(340,100,400,300)
        self.LabelPosture1.setPixmap(QtGui.QPixmap('cervical'))
        #
        self.Labelborg=QtWidgets.QLabel(self)
        self.Labelborg.setGeometry(50,430,700,90)
        Icon2=QtGui.QPixmap("borg_act")
        Icon_resize= Icon2.scaled(700,80)
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














        #self.Label1=QtWidgets.QLabel(self)
        #self.Label1.setText("Hello World")
        #self.Label2=QtWidgets.QLabel(self)
        #self.Label2.setPixmap(QtGui.QPixmap('Imagen'))
        #self.btn=QtWidgets.QPushButton(self)
        #self.btn.setText("Start")
        #self.btn.move(100,50)

        #self.Label1.move(130,20)#mover el label
        #self.Label2.move(120,90)
        self.show()


app=QtWidgets.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())

#M=run()
