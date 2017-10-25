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
        self.Joy = Joy.JoyHandler(sample = 0.3, gui = self.therapy_win)

        #BOOL
        self.ON = True
        #sample time

    def on_start_clicked(self):
        print('started from index')
        self.Joy.launch_thread()


    def on_stop_clicked(self):
        print('stopped from index')
        self.Joy.shutdown()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a =LokomatInterface()
    sys.exit(app.exec_())
