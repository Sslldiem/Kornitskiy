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
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac,dec2bin(k))
        time.sleep(0.0001)
        if GPIO.input(comp)==0:
            k-=2**i
    return k
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