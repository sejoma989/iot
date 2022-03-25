import machine
from machine import Pin
import utime

def reset_btn ():
    reset = machine.Pin(27, Pin.IN)
    previous = reset.value()
    print('RESET: ')
    print(previous)
    while previous != 1:
        previous = reset.value()
        #print('Esperando')
        utime.sleep(2)
    else:
        # Reseteamos el archivo confWiFi.txt
        print('Resetting device ESP232...')
        confWifi = open('WiFiConnect.txt', 'w')
        confWifi.write('EMMANUEL\n1nt3rnE7')
        confWifi.close()
        machine.reset()
        previous = 0
        print(previous)