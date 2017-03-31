import Adafruit_BBIO.GPIO as GPIO
import time

class gps():
    def __init__(self,trig ="P8_10", echo="P8_8" ,temperature=28.0):
        self.trig=trig
        self.echo=echo
        GPIO.setup(self.trig, GPIO.OUT) 
        GPIO.setup(self.echo, GPIO.IN) 
        self.temp=temperature
        self.speedSound=33100.0+0.6*temperature
        self.status=0
        self.elapsed=0
        self.distance=0
    def getDistance(self):
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(10/1000000.0)
        GPIO.output(self.trig, GPIO.LOW)
        start=time.time()
        stop=0
        loop=time.time()
        while (GPIO.input(self.echo)!=True):
                start=time.time()
                if start-loop>1:
                        break
        while(GPIO.input(self.echo)==True):
                stop=time.time()
                if stop-start>1:
                        break
        self.elapsed=stop-start
        self.distance=(self.elapsed*self.speedSound)/2.0
        if ((self.distance<2.0)|(self.distance>400.0)):
                self.status=0
        else:
                self.status=1
        return self.status, self.elapsed, self.distance
    def updateTemp(self, temperature):
        self.temp=temperature
        self.speedSound=33100.0+0.6*temperature
