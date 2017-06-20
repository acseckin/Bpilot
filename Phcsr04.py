#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:07:35 2017

@author: acseckin
"""
import Adafruit_BBIO.GPIO as GPIO
import time
import threading

class ultrasonic(threading.Thread):
    def __init__(self,trig ="P8_10", echo="P8_8" ,temperature=28.0):
        threading.Thread.__init__(self)
        self.trig=trig
        self.echo=echo
        GPIO.setup(self.trig, GPIO.OUT) 
        GPIO.setup(self.echo, GPIO.IN) 
        self.temp=temperature
        self.speedSound=33100.0+0.6*temperature
        self.status=0
        self.elapsed=0
        self.distance=0
        self.active=False
        self.trigtime=10/1000000.0
        GPIO.output(self.trig, GPIO.LOW)
    def getDistance(self):
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(self.trigtime)
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(self.trigtime)
        GPIO.output(self.trig, GPIO.LOW)
        start=time.time()
        stop=0
        loop=time.time()
        while (GPIO.input(self.echo)!=True):
                start=time.time()
                if start-loop>0.001:
                        break
        while(GPIO.input(self.echo)==True):
                stop=time.time()
                if stop-start>0.001:
                        break
        self.elapsed=stop-start
        self.distance=(self.elapsed*self.speedSound)/2.0
        if ((self.distance<2.0)|(self.distance>400.0)):
                self.status=0
                self.distance=0
        else:
                self.status=1
        return self.status, self.elapsed, self.distance
    def updateTemp(self, temperature):
        self.temp=temperature
        self.speedSound=33100.0+0.6*temperature
    def deactivate(self):
        self.active=False
    def run(self):
        self.active=True
        while self.active:
            self.getDistance()
