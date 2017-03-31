#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""

import Phcsr04

ultra=Phcsr04.ultrasonic()

while (True):
    print ultra.getDistance()
    