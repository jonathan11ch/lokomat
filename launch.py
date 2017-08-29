import threading
import lib.manager as man


def main():
	manager = man.Manager(imu_port = 'COM4')
	
	manager.set_sensors(ecg = False, imu = True)
	manager.launch_sensors()
	manager.play_sensors()
	
	for i in range(10):
		manager.update_data()
		d = manager.get_data()
		print d

	manager.shutdown()

if __name__ == '__main__':
	main()