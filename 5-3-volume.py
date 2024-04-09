import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
tr=13
leds=[9,10,22,27,17,4,3,2]
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(tr, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
def dec(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, dec(k))
        sleep(0.005)
        if gpio.input(comp) == gpio.HIGH:
            k-=2**i
    return k


def volume(n):
    n=int(round(n/32,0))
    arr=[0]*8
    for i in range(n):
        arr[i]=1
    return arr
try:
    while True:
        i=adc()
        if i!=0:
            gpio.output(leds, volume(i))
            print(int(i)/256*10)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()

