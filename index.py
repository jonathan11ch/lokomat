#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:23:31 2017

@author: pi
"""

import threading
import gui.Interface as interface
import lib.Analog_Joystick_rpi as Joy
import lib.manager as man
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys

class LokomatInterface(object):
    def __init__(self, settings = {
                                    'UseSensors': True,
                                    'UseRobot'  : False
                                  }
        ):
        #load settings
        self.settings = settings
        #therapy win interface object
        self.therapy_win = interface.MainTherapyWin()
        #conntecting to interface
        self.therapy_win.connectStartButton(self.on_start_clicked)
        self.therapy_win.connectStopButton(self.on_stop_clicked)
        #creating Joy object
        self.Joy = Joy.JoyHandler(sample = 0.3, gui = self.therapy_win)

        if self.settings['UseSensors']:
            #create sensor Manager
            self.manager  = man.Manager(
        					  imu1_settings = {'port': 0x28, 'sample': 1, 'bus': 1},
        					  imu2_settings = {'port': 0x29, 'sample': 1, 'bus': 1},
        					  ecg_settings = {'port': 'COM3', 'sample': 1}
        					  )
            #set sensors
            self.manager.set_sensors(ecg = False, imu1 = True, imu2 = True )

            #threads
            self.SensorUpdateThread = SensorUpdateThread(f = self.sensor_update, sample = 1)


        #BOOL
        self.ON = True
        #sample time

    def on_start_clicked(self):
        print('started from index')
        self.Joy.launch_thread()
        if self.settings['UseSensors']:
            self.manager.launch_sensors()
            self.manager.play_sensors()
            self.SensorUpdateThread.start()


    def on_stop_clicked(self):
        print('stopped from index')
        self.Joy.shutdown()
        if self.settings['UseSensors']:
            self.manager.shutdown()
            self.SensorUpdateThread.shutdown()

    def sensor_update(self):

        if self.settings['UseSensors']:
            self.manager.update_data()
            data = self.manager.get_data()
            print(data)
            self.therapy_win.update_display_data(d = {
                                                        'hr' : data['ecg']['hr'],
                                                        'yaw_t' : data['imu1']['yaw'],
                                                        'pitch_t' : data['imu1']['pitch'],
                                                        'roll_t' : data['imu1']['roll'],
                                                        'yaw_c' : data['imu2']['yaw'],
                                                        'pitch_c' : data['imu2']['pitch'],
                                                        'roll_c' : data['imu2']['roll']
                                                      }
                                    )
        else:
            print('no sensors')

class SensorUpdateThread(QtCore.QThread):

     def __init__(self, parent = None, f = None, sample = 1):
        super(SensorUpdateThread,self).__init__()
        self.f = f
        self.Ts = sample
        self.ON = True
        
     def run(self):

        if self.f:
            while self.ON:
                self.f()
                time.sleep(self.Ts)

     def shutdown(self):
        self.ON = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a =LokomatInterface()
    sys.exit(app.exec_())
