#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:40:54 2017

@author: acseckin
"""

import Pxbee
import time
xb=Pxbee.xbee()
xb.start()

t=time.time()
while True:
    if time.time()-t>2:
        t=time.time()
        xb.transmit("hello !!")