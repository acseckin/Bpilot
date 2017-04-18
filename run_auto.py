#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: acseckin
"""

import Pgps
import Phcsr04
import Pmwii
import Pxbee

mw=Pmwii.MultiWii()

xb=Pxbee.xbee()
xb.start()
hc=Phcsr04.ultrasonic()
hc.start()
gps=Pgps.gps()
gps.start()

def getInfo():
    attitu=mw.getAttitude()
    rcchan=mw.getRC()
    pidval=mw.getPID()
    height=hc.distance
    gpslong=gps.longitude
    gpslatt=gps.latitude
    gpsval=[gpslong,gpslatt]
    return attitu,rcchan,pidval,height,gpsval
def reportInfo(attitu,rcchan,pidval,height,gpsval):
    xb.transmitMWii(attitu)
    xb.transmitRC(rcchan)
    xb.transmitPID(pidval)
    xb.transmitGPS(gpsval[0],gpsval[1],height)
    xb.saveOutputs()
while True:
    ainfo=getInfo()
    reportInfo(ainfo)
    
    
    
    
    
    
    
    