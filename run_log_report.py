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
gps=Pgps.gps()
while True:
    attitu=mw.getAttitude()
    rcchan=mw.getRC()
    pidval=mw.getPID()
    height=hc.getDistance()
    gpsval=gps.readGPGGA()
    xb.sendMWii(attitu,height)
    xb.sendRC(rcchan)
    xb.sendPID(pidval)
    xb.sendGPS(gpsval[0],gpsval[1])