#import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(19,GPIO.OUT)
#GPIO.setup(24,GPIO.IN)
#while True:
#    GPIO.output(19,GPIO.input(24))
import matplotlib.pyplot as plt
x = [0, 2, 4, 5,32,64,127,255]
y = [0, 12, 26, 64, 410,822,1630, 3270]
plt.plot(x, y, marker='o')
plt.show()