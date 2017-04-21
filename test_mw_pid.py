#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:16:15 2017

@author: acseckin
"""

from Pmwii import MultiWii
import time
vals=[0,0,0,0,0,0,0,0,0]
mw = MultiWii("/dev/ttyO1")
i=0
bt=time.time()
while True:
    pidval=mw.getPID()
    print ">>>>>>>Read:",pidval
    if time.time()-bt>5:
      i=i+1
      vals[:]=[x+i for x in vals]
      mw.setPID(vals)
      print ">>>>>>>Write",vals
      if i>20:
          i=0
      bt=time.time()