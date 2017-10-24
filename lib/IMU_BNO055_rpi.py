import sys,getopt
import smbus
import numpy as np
import time
import os

UNIT_SEL=0X3B # Units register
OPR_MODE=0x3D #Operation mode register
CALIB_STAT=0X35 # Calibration register
#Euler angles register
EUL_Pitch_MSB = 0x1F
EUL_Pitch_LSB = 0x1E
EUL_Roll_MSB = 0x1D
EUL_Roll_LSB = 0x1C
EUL_Heading_MSB = 0x1B
EUL_Heading_LSB = 0x1A

class IMU_BNO055(object):
    def __init__(self, device_address,bus):
        self.device_address=device_address
        self.bus=smbus.SMBus(bus) #1
        self.bus.write_byte_data(self.device_address,UNIT_SEL,0b00000010)
        self.bus.write_byte_data(self.device_address, OPR_MODE, 0b00001100) #NDOF mode: all sensors and absolute orientation
        self.acquired_data=0
        
    def read_Euler(self):
        self.acquired_data=self.read_i2c()
        print("Pitch, Roll, Yaw:")
        print(self.acquired_data)

    def read_i2c(self):
        Euler=""
        msb = self.bus.read_byte_data(self.device_address,EUL_Pitch_MSB)
        lsb = self.bus.read_byte_data(self.device_address,EUL_Pitch_LSB)
        data = (msb << 8) + lsb
        if (data & 0x8000)== 0x8000:
            data= data ^ 0xFFFF
            data= data * -1    
            if data < -2880:
                data= data*-1
                data= data ^ 0xFFFF
                data= data & 0x7FFF
        data=data/16.
        Euler= Euler +str(data)
        

        msb = self.bus.read_byte_data(self.device_address,EUL_Roll_MSB)
        lsb = self.bus.read_byte_data(self.device_address,EUL_Roll_LSB)
        data = (msb << 8) + lsb
        if (data & 0x8000)== 0x8000:
            data= data ^ 0xFFFF
            data= data * -1    
            if data < -2880:
                data= data*-1
                data= data ^ 0xFFFF
                data= data & 0x7FFF

        data=data/16.
        Euler= Euler+" , "+str(data)
        

    
        msb = self.bus.read_byte_data(self.device_address,EUL_Heading_MSB)
        lsb = self.bus.read_byte_data(self.device_address,EUL_Heading_LSB)
        data = (msb << 8) + lsb
        if (data & 0x8000)== 0x8000:
            data= data ^ 0xFFFF
            data= data * -1    
            if data < -2880:
                data= data*-1
                data= data ^ 0xFFFF
                data= data & 0x7FFF
        data=data/16.
        Euler= Euler+", "+str(data)
        return(Euler)
        
      

def main():
    bus=1
    device_address=0x28
    imu = IMU_BNO055(device_address, bus)
    for i in range (50):
        imu.read_Euler()

H=main()

    