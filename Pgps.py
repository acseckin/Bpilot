#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""
import serial
from math import radians, sin, cos, sqrt, asin,atan2,degrees
import Adafruit_BBIO.UART as UART
import threading

class gps(threading.Thread):
    def __init__(self,port='/dev/ttyO4',baud=9600):
        threading.Thread.__init__(self)
        self.port=port
        self.pname="UART"+port[-1:]
        self.baud=baud
        self.uart=UART.setup(self.pname)
        self.gpsserial=serial.Serial(self.port,self.baud)
        self.active=True
        while (not self.gpsserial.isOpen()):
            print "GPS is not connected"
            self.gpsserial=serial.Serial(self.port,self.baud)
        self.longitude=[0,0,0]
        self.latitude=[0,0,0]
    def read(self):
        gpsinput=self.gpsserial.readline()
        if "$" in gpsinput:
            return gpsinput
        else:
            return ""
    def readGPRMC(self):
        gpsinput=self.read()
        if "GPRMC" in gpsinput:
            rmc=gpsinput.split(',')
            if rmc[2]=='A':
                self.timeUTC=rmc[1][:-8]+":"+rmc[1][-8:-6]+":"+rmc[1][-6:-4]
                self.lat=rmc[3]
                self.long=rmc[5]
            else:
                self.active=False
        self.gpsserial.flushInput()
    def readGPGGA(self):
        gpsinput=self.gpsserial.readline()
        print gpsinput
        if "$GPGGA" in gpsinput:
            gga=gpsinput.split(',')
            print gga
            self.sats=int(gga[7])
            if self.sats>=1:
                self.time=gga[1]
                self.fix=int(gga[6])
                self.altitude=float(gga[9])
                self.latitude=[float(gga[2][:2]),float(gga[2][2:4]),float(gga[2][4:])]
                self.longitude=[float(gga[4][:2]),float(gga[4][2:4]),float(gga[4][4:])]
                self.gpsserial.flushInput()

    def bearing(self, lo1, la1, lo2, la2):
        lat1=la1
        lon1 = lo1
        lat2=la2
        lon2 = lo2
        rlat1 = radians(lat1)
        rlat2 = radians(lat2)
        dlon = radians(lon2-lon1)
        b = atan2(sin(dlon)*cos(rlat2),cos(rlat1)*sin(rlat2)-sin(rlat1)*cos(rlat2)*cos(dlon)) # bearing calc
        bd = degrees(b)
        br,bn = divmod(bd+360,360) # the bearing remainder and final bearing
        return bn
    def haversinedecimal(self, lon1, lat1, lon2, lat2):
        R = 6371.008 # Earth radius in meters
        dLat = radians(lat2 - lat1)
        dLon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))
        return R * c *1000
    def haversinedms(self, lon1, lat1, lon2, lat2):
        dlon1=lon1[0]+(lon1[1]*60.0+lon1[2]+lon1[3])/3600.0
        dlon2=lon2[0]+(lon2[1]*60.0+lon2[2]+lon2[3])/3600.0
        dlat1=lat1[0]+(lat1[1]*60.0+lat1[2]+lat1[3])/3600.0
        dlat2=lat2[0]+(lat2[1]*60.0+lat2[2]+lat2[3])/3600.0
        return self.haversinedecimal(dlon1,dlat1,dlon2,dlat2)
    def deactivate(self):
        self.active=False
        
    def run(self):
        while self.active:
            self.readGPGGA()
            print self.longitude, self.latitude
