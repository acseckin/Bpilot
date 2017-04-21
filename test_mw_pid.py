#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:16:15 2017

@author: acseckin
"""

from Pmwii import MultiWii
import numpy as np
import time
mw = MultiWii("/dev/ttyO1")
i=0
while True:
      pidval=mw.getPID()
      print pidval
      if time.time()%4>2:
          i=i+1
          vals=np.ones(9)*i
          mw.setPID(vals)
          print ">>",vals
          if i>20:
              i=0