#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:23:31 2017

@author: pi
"""

import threading 
import gui.Interface as interface
import lib.Analog_Joystick_rpi as Joy
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys

class LokomatInterface(object):
    def __init__(self):
        #therapy win interface object
        self.therapy_win = interface.MainTherapyWin()
        #conntecting to interface        
        self.therapy_win.connectStartButton(self.on_start_clicked)
        self.therapy_win.connectStopButton(self.on_stop_clicked)
        #creating Joy object
        self.Joy = Joy.Analog_Joystick()
        #joy capture thread
        self.JoyThread = threading.Thread(target = self.joy_lecture)
        #BOOL
        self.JOY_ON = True
        self.ON = True
        #sample time
        self.joy_ts = 0.3


    def joy_lecture(self):
        
        while self.JOY_ON:
            d =self.Joy.Channel_data()
            print(d)
            self.therapy_win.Borg.j = d['x']
            self.therapy_win.onJoy.emit()
            time.sleep(self.joy_ts)
    
    def on_start_clicked(self):
        print('started from index')
        self.JoyThread.start()
        
    
    def on_stop_clicked(self):
        print('stopped from index')
        self.JOY_ON =False
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a =LokomatInterface()
    sys.exit(app.exec_())
    