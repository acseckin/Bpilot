#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: acseckin
"""

import Phcsr04

ultra=Phcsr04.ultrasonic()

while (True):
    print ultra.getDistance()
    