import RPi.GPIO as GPIO
import time

dac=[26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
  return [int(element) for element in bin(value)[2:].zfill(8)]
try:
  while True:
    t=int(input())
    T=t/512
    for dc in range(256):
      GPIO.output(dac, dec2bin(dc))
      time.sleep(T)
    for dc in range(255, -1, -1):
      GPIO.output(dac, dec2bin(dc))
      time.sleep(T)
except KeyboardInterrupt:
  pass
finally:
  GPIO.output(dac, 0)
  GPIO.cleanup()
