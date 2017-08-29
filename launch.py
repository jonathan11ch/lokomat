import threading
import lib.manager as man
import time


def main():
	manager = man.Manager(imu_port = '/dev/tty.usbmodem1411')
	
	manager.set_sensors(ecg = False, imu = True)
	manager.launch_sensors()
	manager.play_sensors()
	time.sleep(3)
	for i in range(10):
		manager.update_data()
		d = manager.get_data()
		print d
		time.sleep(1)

	manager.shutdown()

if __name__ == '__main__':
	main()