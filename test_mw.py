#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:31:33 2017

@author: acseckin
"""

from mw import MultiWii
import numpy as np
import time

board = MultiWii("/dev/ttyO1")
while True:
  board.getData(MultiWii.ATITUDE)
            he[0]=float(board.altitude['EstAlt'])
            he=np.roll(he, 1)
            base=np.mean(he)
            bvar=np.var(be)
        he=np.zeros(500)
        print base
        time.sleep(5)
        while True:
            board.getData(MultiWii.ATTITUDE)
            print board.attitude 
