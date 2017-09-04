import threading
import lib.manager as man
import time
import gui.index as index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class LokomatInterface(object):

	def __init__(self):
		#create interface object
		self.interface = index.MainInterface()
		#create sensor manager
		self.manager = man.Manager(imu_port = '/dev/tty.usbmodem1411',ecg_port ='/dev/tty.HXM035704-BluetoothSeri')
		self.manager.set_sensors(ecg = False, imu = True)
		#launch capture thread
		self.manager.launch_sensors()
		#connecting to interface
		self.interface.ConnectStartButton(self.on_start_clicked)
		self.interface.ConnectStopButton(self.set_consult_off)

		#boolean
		self.ON = True

	def on_start_clicked(self):
		self.manager.play_sensors()
		time.sleep(3)
		#launch capture thread
		threading.Thread(target = self.consult).start()

	def set_consult_off(self):
		self.ON = False

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
