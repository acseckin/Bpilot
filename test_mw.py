# -*- coding: utf-8 -*-
"""
@author: acseckin
"""

from Pmwii import MultiWii
import numpy as np
import time

board = MultiWii("/dev/ttyO1")
while True:
  board.getData(MultiWii.ATTITUDE)
  print board.attitude
