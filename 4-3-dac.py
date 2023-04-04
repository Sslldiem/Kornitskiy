import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

try:
  while True:
    dc=int(input())
    p.ChangesDutyCycle(dc)
    print("{:.2f}".format(dc*3.3/100))
except KeyboardInterrupt:
  pass
finally:
  GPIO.output(15, 0)
  GPIO.cleanup()
