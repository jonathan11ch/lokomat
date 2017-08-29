import threading
import lib.manager as manager


def main():
	manager = manager.Manager()
	
	manager.set_sensors(ecg = False, imu = True)
	manager.launch_sensors()
	manager.play_sensors()
	
	for i in range(10):
		d = manager.get_data()
		print d

	manager.shutdown()

if __name__ == '__main__':
	main()