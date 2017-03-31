#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""
from Pmwii import MultiWii
import numpy as np
import time

board = MultiWii("/dev/ttyO1")
while True:
  board.getData(MultiWii.ATTITUDE)
  print board.attitude
