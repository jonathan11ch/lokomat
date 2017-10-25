import threading
import lib.manager as man
import lib.Analog_Joystick_rpi as Joy
import gui.Interface as interface
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class LokomatInterface(object):

	def __init__(self):
		#create interface object
                print('ak')
                self.therapy_win = interface.MainTherapyWin()
		#create sensor manager
		#print('ak')
		self.manager = man.Manager(imu_port = '/dev/tty.usbmodem1411',ecg_port ='/dev/tty.HXM035704-BluetoothSeri')
		#print('ak')
		self.manager.set_sensors(ecg = False, imu = False)
		#launch capture thread
		#print('ak')
		self.manager.launch_sensors()
		#connecting to interface
		
		self.therapy_win.ConnectStartButton(self.on_start_clicked)
		self.therapy_win.ConnectStopButton(self.set_consult_off)
		#Joystick object
		self.Joy = Joy.Analog_Joystick()
		self.JoyThread = threading.Thread(target = self.joy_lecture)
		#boolean
		self.ON = True
		self.JOY_ON =True
		self.joy_ts = 0.5

	def on_start_clicked(self):
                print('started from launch')
                self.manager.play_sensors()
                time.sleep(3)
		#launch capture thread
                threading.Thread(target = self.consult).start()
                self.JoyThread.start()

	def set_consult_off(self):
		self.ON = False
		self.JOY_ON = False
           

	def joy_lecture(self):
          time.sleep(5)
          print("joy lecture thread started")
          
          while self.JOY_ON:
              d = self.Joy.Channel_data()
              self.therapy_win.Borg.j = d['x']
              self.therapy_win.onJoy.emit()
              print(d)    
              (self.joy_ts)


	def consult(self):
		cont = 0
		while self.ON:
			self.manager.update_data()
			d = self.manager.get_data()
			print(d)
			imu = d['imu']
			ecg = {'hr': 5}

			if not imu == None:
				d = {'hr' : ecg['hr'], 'yaw' :imu['x'], 'pitch' : imu['y'], 'roll' : imu['z']}
			else:
				d = {'hr' : ecg['hr'], 'yaw' :cont, 'pitch' : cont, 'roll' :cont}
			self.interface.update_display_data(d)
			if cont < 50:
				cont +=1
			else:
				cont = 0
			time.sleep(1)

		print('going.. out')
		self.manager.shutdown()





def main():
	manager = man.Manager(imu_port = '/dev/tty.usbmodem1411')

	manager.set_sensors(ecg = False, imu = True)
	manager.launch_sensors()
	manager.play_sensors()
	time.sleep(3)
	for i in range(10):
		manager.update_data()
		d = manager.get_data()
		print (d)
		time.sleep(1)

	manager.shutdown()

def main2():
	app = QtWidgets.QApplication(sys.argv)
	a = LokomatInterface()
	

	sys.exit(app.exec_())


if __name__ == '__main__':
	main2()
