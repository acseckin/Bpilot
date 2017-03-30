# -*- coding: utf-8 -*-
"""
@author: acs
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
    def reportMW(self,alttitude,PID,rcChannels):
        alt=str(alttitude)
        pid=str(PID)
        rc=str(rcChannels)
        outstr="MW"+alt+":"+pid+":"+rc+":\n"
        outstr=outstr.replace("[","")
        outstr=outstr.replace("]","")
        outstr=outstr.replace(",",":")
        return self.write(outstr)
    def reportIMU(self,x,y,z,h):
        x=round(float(x),3)
        y=round(float(y),3)
        z=round(float(z),3)
        h=round(float(h),3)
        outstr="$I:"+str(x)+":"+str(y)+":"+str(z)+":"+str(h)+":\n"
        return self.write(outstr)
    def reportTAR(self):
        outstr="$D:"+str(self.dx)+":"+str(self.dy)+":"+str(self.dz)+":"+str(self.dh)+":\n"
        return self.write(outstr)
    def reportALT(self,bp,kbp,hc,dh):
        bp=round(float(bp),2)
        kbp=round(float(kbp),2)
        hc=round(float(hc),2)
        dh=round(float(dh),2)
        outstr="$A:"+str(bp)+":"+str(kbp)+":"+str(hc)+":"+str(dh)+":\n"
        return self.write(outstr)
    def reportPWM(self,p1,p2,p3,p4):
        p1=round(float(p1),2)
        p2=round(float(p2),2)
        p3=round(float(p3),2)
        p4=round(float(p4),2)
        outstr="$M:"+str(p1)+":"+str(p2)+":"+str(p3)+":"+str(p4)+":\n"
        return self.write(outstr)
    def reportPID_x(self):
        outstr="$CX:"+str(self.xkp)+":"+str(self.xki)+":"+str(self.xkd)+":\n"
        return self.write(outstr)
    def reportPID_y(self):
        outstr="$CY:"+str(self.ykp)+":"+str(self.yki)+":"+str(self.ykd)+":\n"
        return self.write(outstr)
    def reportPID_z(self):
        outstr="$CZ:"+str(self.zkp)+":"+str(self.zki)+":"+str(self.zkd)+":\n"
        return self.write(outstr)
    def reportPID_h(self):
        outstr="$CH:"+str(self.hkp)+":"+str(self.hki)+":"+str(self.hkd)+":\n"
        return self.write(outstr)
    def reportPID(self):
        self.reportPID_x()
        self.reportPID_y()
        self.reportPID_z()
        self.reportPID_h()
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
    def setPID_x(self,xkp,xki,xkd):
        self.xkp=xkp
        self.xki=xki
        self.xkd=xkd
    def setPID_y(self,ykp,yki,ykd):
        self.ykp=ykp
        self.yki=yki
        self.ykd=ykd
    def setPID_z(self,zkp,zki,zkd): 
        self.zkp=zkp
        self.zki=zki
        self.zkd=zkd
    def setPID_h(self,hkp,hki,hkd):  
        self.hkp=hkp
        self.hki=hki
        self.hkd=hkd
    def getPID_x(self):
        return [self.xkp,self.xki,self.xkd]
    def getPID_y(self):
        return [self.ykp,self.yki,self.ykd]
    def getPID_z(self):
        return [self.zkp,self.zki,self.zkd]
    def getPID_h(self):
        return [self.hkp,self.hki,self.hkd]
  
