import RPi.GPIO as GPIO
import time

dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        d2ac=dec2bin(i)
        GPIO.output(dac,d2ac)
        time.sleep(0.0001)
        cmp=GPIO.input(comp)
        if cmp==0:
            return i
try:
    while True:
        i=adc()
        if i!=0:
            print(i, "{:.2f}".format(i*3.3/256))
except KeyboardInterrupt:
    pass
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()