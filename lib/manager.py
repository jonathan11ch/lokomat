
import imu_sensor as IMU
import ecg_sensor as ECG

import threading

class Manager(object):
	def __init__(self):
		self.imu = IMU.ImuSensor(port = 'COM4', br = 9600)
		self.ecg = ECG.EcgSensor(port = 'COM3')
		self.ECG_ON = False
		self.IMU_ON = False
		self.data = {'ecg': None, 'hr': None}


	def set_sensors(self, ecg = True, imu = True):
		self.ECG_ON = ecg
		self.IMU_ON = imu

	def launch_sensors(self):
		#launch imu thread
		if self.IMU_ON:
			self.imu.start()
			threading.Thread(target = self.imu.process).start()
		#launch ecg thread
		if self.ECG_ON:
			self.ecg.start()
			threading.Thread(target = self.ecg.process).start()

	def play_sensors(self):
		#start acquiring data
		if self.ECG_ON:
			self.ecg.play()
		
		if self.IMU_ON:
			self.imu.play()


	def update_data(self):
		if self.ECG_ON:
			ecg = self.ecg.get_data()
		if self.IMU_ON:
			imu = self.imu.get_data()

		self.data = {'ecg': ecg, 'imu': imu }


	def get_data(self):
		return self.data


	def shutdown(self):
		#shutdown Imu
		if self.IMU_ON:
			self.imu.shutdown()
		#shutdown Ecg
		if self.ECG_ON:
			self.ecg.shutdown()
		








