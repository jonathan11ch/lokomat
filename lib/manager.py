
import imu_sensor as IMU
import ecg_sensor as ECG

import threading

class Manager(object):
	def __init__(self, imu_port = 'COM4', ecg_port = 'COM3'):
		
		self.ECG_ON = False
		self.IMU_ON = False
		self.data = {'ecg': None, 'hr': None}
		self.imu_port = imu_port
		self.ecg_sensor = ecg_port


	def set_sensors(self, ecg = True, imu = True):

		self.ECG_ON = ecg
		self.IMU_ON = imu
		
		if self.IMU_ON:
			self.imu = IMU.ImuSensor(port = self.imu_port, br = 9600)
		if self.ECG_ON:
			self.ecg = ECG.EcgSensor(port = self.ecg_port)


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
		else:
			ecg = None

		if self.IMU_ON:
			imu = self.imu.get_data()
		else:
			ecg = None

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
		








