#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""

import Pgps
import Phcsr04
import Pmwii
import Pxbee

mw=Pmwii.MultiWii()
xb=Pxbee.xbee()
hc=Phcsr04.ultrasonic()
hc.start()
gps=Pgps.gps()
gps.start()
while True:
    attitu=mw.getAttitude()
    print "ATTITUDE:",attitu
    rcchan=mw.getRC()
    print "RC CHANN:",rcchan
    pidval=mw.getPID()
    print "PID COEF:",pidval
    height=hc.distance
    
    gpslong=gps.longitude
    gpslatt=gps.latitude
    gpsval=[gpslong,gpslong]
    print "POSTION:",gpsval,height
    xb.transmitMWii(attitu)
    xb.transmitRC(rcchan)
    xb.transmitPID(pidval)
    xb.transmitGPS(gpsval[0],gpsval[1],height)
    
    