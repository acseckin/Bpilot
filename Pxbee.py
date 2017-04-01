#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""
import serial
import Adafruit_BBIO.UART as UART
class xbee():
    def __init__(self,port="/dev/ttyO5",baud=115200):
        self.port=port
        self.baud=baud
        self.uname="UART"+str(port[-1])
        self.uart=UART.setup(self.uname)
        self.status=0
    
        self.roll=0
        self.pitch=0
        self.yaw=0
        
        self.pos=[0,0,0]
        self.rcchannels=[0,0,0,0]
        
        self.rollPID=[0,0,0]
        self.pitchPID=[0,0,0]
        self.yawPID=[0,0,0]
        self.heightPID=[0,0,0]
        self.posPID=[0,0,0]
        
        self.PIDCONT="$C"
        self.MWII="$M"
        self.POSITION="$P"
        self.RCCHANNEL="$R"
        self.POSCONT="$A"
        
        try:
            self.ser= serial.Serial(port = self.port, baudrate=self.baud)
            self.ser.close()
            self.ser.open()
            self.ser.flush()
            self.status=1
        except ValueError:
            self.status=0
    def read(self):
        if self.ser.inWaiting():
            xbeein=self.ser.readline()
            self.ser.flush()
            return [1,xbeein]
        else:
            return [0]
    
    def transmit(self,send):
        try:
            self.ser.write(str(send))
            self.ser.flush()
            return [1, send]
        except ValueError:
            return [0, ValueError]
            
    def transmitMWii(self,attitude):
        attitude[0]= int(attitude[0]*10)
        attitude[1]= int(attitude[1]*10)
        attitude[2]= int(attitude[2]*10)
        #attitude[3]= int(attitude[3]*1000)
        att=str(attitude)
        outstr=self.MWII+":"+att+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.transmit(outstr)
    
    def transmitPID(self,PID):
        PID=str(PID)
        outstr=self.PIDCONT+":"+PID+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.transmit(outstr)
        
    def transmitRC(self,rcChannels):
        rcChannels=str(rcChannels)
        outstr=self.RCCHANNEL+":"+rcChannels+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.transmit(outstr)
    
    def transmitGPS(self,latitude,longitute,height):
        longitute=str(round(longitute,3))
        latitude=str(round(latitude,3))
        height=str(int(height))
        outstr=self.POSITION+":"+longitute+":"+latitude+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.transmit(outstr)
    
    def receive(self):
        try:
            rv=self.read()
            if rv[0]==1:
                xbeein=rv[1].split(":")
                if (xbeein[0]==self.PIDCONT) and (len(xbeein)>=10):
                    self.rollPID[0]=int(xbeein[1])
                    self.rollPID[1]=int(xbeein[2])
                    self.rollPID[2]=int(xbeein[3])
                    self.pitchPID[0]=int(xbeein[4])
                    self.pitchPID[1]=int(xbeein[5])
                    self.pitchPID[2]=int(xbeein[6])
                    self.yawPID[0]=int(xbeein[7])
                    self.yawPID[1]=int(xbeein[8])
                    self.yawPID[2]=int(xbeein[9])
                    return self.rollPID,self.pitchPID,self.yawPID
                elif (xbeein[0]==self.RCCHANNEL) and (len(xbeein)>=4):
                    self.rcchannels[0]=int(xbeein[1])
                    self.rcchannels[1]=int(xbeein[2])
                    self.rcchannels[2]=int(xbeein[3])
                    return self.rcchannels
                elif (xbeein[0]==self.POSITION) and (len(xbeein)>=4):
                    self.pos[0]=int(xbeein[1])
                    self.pos[1]=int(xbeein[2])
                    self.pos[2]=int(xbeein[3])
                    return self.pos
                elif (xbeein[0]==self.POSCONT) and (len(xbeein)>=7):
                    self.heightPID[0]=int(xbeein[1])
                    self.heightPID[1]=int(xbeein[2])
                    self.heightPID[2]=int(xbeein[3])
                    self.posPID[0]=int(xbeein[4])
                    self.posPID[1]=int(xbeein[5])
                    self.posPID[2]=int(xbeein[6])
                    return self.heightPID,self.posPID
                else:
                    print (xbeein)
        except ValueError:
            print ValueError
   
  
