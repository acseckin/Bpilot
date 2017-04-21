#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: acseckin
"""
import time
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
    rv= attitu,rcchan,pidval,height,gpsval
    return rv
def reportInfo(inval):
    attitu,rcchan,pidval,height,gpsval=inval
    xb.transmitMWii(attitu)
    xb.transmitRC(rcchan)
    xb.transmitPID(pidval)
    xb.transmitGPS(gpsval[0],gpsval[1],height)
    xb.saveOutputs()
def getUpdates():
    if xb.isNewUpdate==1:
        vals=xb.readUpdates()
        print "PID:",vals[0]
        mw.setPID(vals[0])
        time.sleep(1)
    elif xb.isNewUpdate==2:
        vals=xb.readUpdates()
        print "RC:",vals
        time.sleep(1)
    
while True:
    ainfo=getInfo()
    reportInfo(ainfo)
    getUpdates()