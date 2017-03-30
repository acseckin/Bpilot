import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_10", GPIO.IN)

temperature=28.0
speedSound=33100.0+0.6*temperature
loop=0
while (True):
        GPIO.output("P8_8", GPIO.LOW)
        time.sleep(0.1)
        GPIO.output("P8_8", GPIO.HIGH)
        time.sleep(10/1000000.0)
        GPIO.output("P8_8", GPIO.LOW)

        start=time.time()
        stop=0
        loop=time.time()
        while (GPIO.input("P8_10")!=True):
                start=time.time()
                if start-loop>1:
                        break
        while(GPIO.input("P8_10")==True):
                stop=time.time()
                if stop-start>1:
                        break
        elapsed=stop-start
        distance=(elapsed*speedSound)/2.0
        if ((distance<2.0)|(distance>400.0)):
                print "Error",
        else:
                print "OK",
        print elapsed, distance
