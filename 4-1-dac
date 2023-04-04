import RPi.GPIO as GPIO

dac=[26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setuo(dac, GPIO.OUT)

def dec2bin(value):
  return [int(element) for element in bin(value)[2:].zfill(8)]
  
  try:
    while True:
      print('Введите число от 0 до 255:')
      s=input()
      try:
        a=int(float(s))
       except ValueError:
        if s=='q':
          print('Программа остановлена.')
          break
        else:
          print('Введено не числовое значение.')
          continue
      if float(s)!=round(float(s)):
        print('Введено не целое число.')
        continue
      if a<0:
        print('Введено отрицательное значение.'):
        continue
      if a>255:
        print('Введено значение превышающее максимальное допустимое.'):
        continue
      GPIO.output(dac, dec2bin(a))
      print('Предполагаемое напряжение на ЦАП:', ':.f'.format(int(s)/256*3.3))
finally:
  GPIO.output(dac, 0)
  GPIO.cleanup()
