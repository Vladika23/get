import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
tr=13
gpio.setup(dac, gpio.OUT)
gpio.setup(tr, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
def adc():
    for i in range(256):
        temp=dec(i)
        gpio.output(dac, temp)
        value=gpio.input(comp)
        sleep(0.005)
        if value==1:
            return i
try:
    while True:
        i=adc()
        if i!=0:
            if i !=None:
                print(i, '{:.2f}v'.format(3.3*int(i)/256))
            else:
                print(255, 3.28)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
