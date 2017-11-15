#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:23:31 2017

@author: pi
"""

import threading
import gui.Interface as interface
#import lib.Analog_Joystick_rpi as Joy
#import lib.manager as man
import lib.ManagerTx as ManagerTx       
import robotController.controller as controller
from PyQt4 import QtCore, QtGui
import time
import sys

class LokomatInterface(object):

    def __init__(self, settings = {
                                    'UseSensors': True,
                                    'UseRobot'  : False,
                                    'RobotIp'   : "10.30.0.191",
                                    'RobotPort' : 9559
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
        #self.Joy = Joy.JoyHandler(sample = 0.3, gui = self.therapy_win)
        #create robot controller
        '''self.RobotController = controller.RobotController(ip = self.settings['UseRobot'], useSpanish = True)
        self.RobotController.set_sentences()
        self.RobotController.set_limits()
        self.NaoThread = RobotCaptureThread(self)
        '''
        if self.settings['UseSensors']:
            #create sensor Manager
            self.ManagerRx  = ManagerTx.ManagerRx(settings = {
                                'joy_port'  : 'COM9',
                                'imu_port'  : 'COM4',
                                'ecg_port'  : 'COM6',
                                'joy_sample': 0.2,
                                'imu_sample': 1,
                                'joy_baud'  : 9600,
                                'imu_baud'  : 9600,
                                'ecg_sample': 1
                              })
            # set sensors
            self.ManagerRx.set_sensors(ecg = False, imu = True, joy= True )
            # threads
            # display data update data 
            self.SensorUpdateThread = SensorUpdateThread(f = self.sensor_update, sample = 1)
            #sensor update processes
            self.ImuCaptureThread   = ImuCaptureThread(interface = self)
            self.JoyCaptureThread   = JoyCaptureThread(interface = self)
            #binding functions
            self.ManagerRx.joy_gui_bind(self.joy_handler)
            self.ManagerRx.imu_gui_bind(self.imu_handler)  
            #


        #BOOL
        self.ON = True
        #sample time

    def on_start_clicked(self):
        print('started from index')
        self.JoyCaptureThread.start()
        #self.Joy.launch_thread()
        if self.settings['UseSensors']:
            print('sensors')
            self.ImuCaptureThread.start()
            self.SensorUpdateThread.start()
            #self.manager.launch_sensors()
            #self.manager.play_sensors()
            #self.SensorUpdateThread.start()
            #self.NaoThread.start()

    def on_stop_clicked(self):
        print('stopped from index')
        self.JoyCaptureThread.shutdown()
        if self.settings['UseSensors']:
            print('sensors')
            self.ManagerRx.shutdown()

        self.shutdown()
            #self.manager.shutdown()
            #self.SensorUpdateThread.shutdown()
            #self.NaoThread.stop()

    #bind functions to the sensor data manager

    def imu_handler(self, data):
        print('Getting IMU data ')



    def joy_handler(self, data):
        print('MOVING CURSOR')
        self.therapy_win.Borg.j  = data['joy']
        print(self.therapy_win.Borg.j)
        self.therapy_win.onJoy.emit()

    def sensor_update(self):

        if self.settings['UseSensors']:
            #self.ManagerRx  .update_data()
            data = self.ManagerRx.get_data()
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



    def shutdown(self):
        if self.settings['UseSensors']:
            self.SensorUpdateThread.shutdown()
            #sensor update processes
            self.ImuCaptureThread.shutdown()
            self.JoyCaptureThread.shutdown()



class ImuCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 1, interface = None):
        super(ImuCaptureThread,self).__init__()
        self.on = False 
        self.interface = interface

    def run(self):
        self.interface.ManagerRx.imu_thread()

    def shutdown(self):
        self.on = False 
        self.interface.ManagerRx.imu_shutdown()      

class JoyCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 1, interface = None):
        super(JoyCaptureThread,self).__init__()
        self.on  = True
        self.interface   = interface    
    def run(self):
        self.interface.ManagerRx.joy_thread()
            
    def shutdown(self):
        self.on = False 
        self.interface.ManagerRx.joy_shutdown()    



class RobotCatureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 1, interface = None):
        super(RobotCaptureThread,self).__init__()
        self.Ts = sample
        self.ON = True
        self.interface = interface
        
        
    def run(self):
        
        while self.ON:
            d = self.interface.manager.get_data()
            self.interface.RobotController.get_data(d)
            time.sleep(self.Ts)
            
                
    def shutdown(self):
        self.ON = False

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
    app = QtGui.QApplication(sys.argv)
    a =LokomatInterface()
    sys.exit(app.exec_())
