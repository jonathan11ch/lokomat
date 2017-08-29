import serial
import numpy as np
import time
import threading

class ImuSensor(object):
	def __init__(self, port = 'COM4', br = 9600):
		self.port  = port 
		self.baudrate = br 
		self.serial = serial.serial(self.port, self.baudrate)
		self.go_on = False
		self.pause = True
		self.data ={'x': None, 'y': None, 'z': None}

	def process(self):
		
		while self.go_on:
			if not self.pause:
				try:
					#adquire data
					data = self.serial.readline()
					data_split = data.split(',')
					x = data_split[0]
					y = data_split[1]
					z = data_split[2]
					self.data ={'x': x, 'y': y, 'z': z}
					print(self.data)

				except:
					print('no Imu data')
			
			else:
				time.sleep(1)
				
		self.serial.close()

	def get_data():
		return self.data

	def pause(self):
		self.pause = True

	def play(self):
		self.pause = False

	def start(self):
		self.go_on = True

	def shutdown(self):
		self.go_on = False
		

def main():
	imu = ImuSensor()
	imu.start()
	imu.play()
	threading.Thread(target = imu.process).start()
	time.sleep(5)
	d = imu.get_data()
	print(d)
	imu.pause()
	imu.shutdown()


if __name__ == '__main__':
	main()



				
			

