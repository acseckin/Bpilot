#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 00:04:29 2017

@author: acseckin
"""

class control:
    def __init__(self,P=0.1,I=0.01,D=0.01,limits=10.0):
        self.kp=P
        self.kd=D
        self.ki=I
        self.limits=limits
        self.desired=0.0
        self.error=0.0
        self.elast=0.0
        self.esum=0.0
        self.eder=0.0
    def update(self,current):
        self.error=self.desired-current
        self.eder=self.error-self.elast
        self.elast=self.error
        self.esum=self.esum+self.error
        if self.esum>self.limits:
            self.esum=self.limits
        elif abs(self.esum)>self.limits:
            self.esum=-1*self.limits

        self.P=self.kp*self.error
        self.D=self.kd*self.eder
        self.I=self.ki*self.esum
        pid=self.P+self.I+self.D
        return pid
    def setDesired(self,d):
        self.desired=d
    def setGains(self,P,I,D):
        self.kp=P
        self.kd=D
        self.ki=I
    def setLimits(self,pmax,pmin):
        self.pidmax=pmax
        self.pidmin=pmin