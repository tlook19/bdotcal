import numpy as np
import matplotlib.pyplot as plt
from gpiozero import LED

bxrelay = LED(22) # pin 15
byrelay = LED(27) # pin 13
bzrelay = LED(17) # pin 11

def all_off():
    bxrelay.off()
    byrelay.off()
    bzrelay.off()


def activate_coil(coil):
    all_off()
    if coil == 'x':
        bxrelay.on()
        print('Bx relay on')
    elif coil == 'y':
        byrelay.on()
        print('By relay on')
    elif coil == 'z':
        bzrelay.on()
        print('Bz relay on')
    elif coil == 'all':
        bxrelay.on()
        byrelay.on()
        bzrelay.on()
        print('All relays on')
    elif coil == 'off':
        print('All relays off')
    else:
        print('Invalid coil, all relays off')
        print('Valid coils are x, y, z, all, off')
        return
    

while True:
    coil = input('Enter coil to activate: ')
    activate_coil(coil)
    if coil == 'off':
        break