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
        self.dx=0
        self.dy=0
        self.dz=0
        self.dh=0
        self.xkp=0
        self.xki=0
        self.xkd=0
        self.ykp=0
        self.yki=0
        self.ykd=0
        self.zkp=0
        self.zki=0
        self.zkd=0
        self.hkp=0
        self.hki=0
        self.hkd=0
        self.th=0
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
    def write(self,send):
        try:
                self.ser.write(str(send))
                self.ser.flush()
                return [1, send]
        except ValueError:
                return [0, ValueError]
    def sendMWii(self,attitude,height):
        attitude[0]= int(attitude[0]*10)
        attitude[1]= int(attitude[1]*10)
        attitude[2]= int(attitude[2]*10)
        attitude[3]= int(attitude[3]*1000)
        att=str(attitude)
        height=str(int(height))
        outstr="$MW:"+att+":"+height+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.write(outstr)

    def sendPID(self,PID):
        PID=str(PID)
        outstr="$RC:"+PID+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.write(outstr)
        
    
    def sendRC(self,rcChannels):
        rcChannels=str(rcChannels)
        outstr="$RC:"+rcChannels+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.write(outstr)
    
    def sendGPS(self,latitude,longitute):
        longitute=str(round(longitute,3))
        latitude=str(round(latitude,3))
        outstr="$RC:"+longitute+":"+latitude+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.write(outstr)
    
  
   
    def readDesired(self):
        try:
            rv=self.read()
            if rv[0]==1:
                xbeein=rv[1].split(":")
                if xbeein[0]=="$I":
                    self.x=float(xbeein[1])
                    self.y=float(xbeein[2])
                    self.z=float(xbeein[3])
                    self.h=float(xbeein[4])
                elif xbeein[0]=="$D":
                    self.dx=float(xbeein[1])
                    self.dy=float(xbeein[2])
                    self.dz=float(xbeein[3])
                    self.dh=float(xbeein[4])
                    print ("Desired Angles:",self.dx,self.dy,self.dz)
                    self.reportTAR()
                elif xbeein[0]=="$CX":
                    self.xkp=float(xbeein[1])
                    self.xki=float(xbeein[2])
                    self.xkd=float(xbeein[3])
                    print ("X PID:",self.xkp,self.xki,self.xkd)
                    self.reportPID()
                elif xbeein[0]=="$CY":
                    self.ykp=float(xbeein[1])
                    self.yki=float(xbeein[2])
                    self.ykd=float(xbeein[3])
                    print ("Y PID:",self.ykp,self.yki,self.ykd)
                    self.reportPID()
                elif xbeein[0]=="$CZ":
                    self.zkp=float(xbeein[1])
                    self.zki=float(xbeein[2])
                    self.zkd=float(xbeein[3])
                    print ("Z PID:",self.zkp,self.zki,self.zkd)
                    self.reportPID()
                elif xbeein[0]=="$CH":
                    self.hkp=float(xbeein[1])
                    self.hki=float(xbeein[2])
                    self.hkd=float(xbeein[3])
                    print ("H PID:",self.hkp,self.hki,self.hkd)
                elif xbeein[0]=="$TH":
                    self.th=float(xbeein[1])
                    print ("Throttle",self.th)
                    self.reportPID()
                else:
                    print (xbeein)
        except ValueError:
            print ValueError
   
  
