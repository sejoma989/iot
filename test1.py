import time
import socket
import network
from machine import Pin
import _thread
from umqttsimple import MQTTClient

def Uno():
    pin1 = Pin(34, Pin.IN)
    #pin2 = Pin(32, Pin.OUT)
    while True:
        if pin1.value() == 1:
            time.sleep(1)
            print("Se prendio la lavadora")
        elif pin1.value() == 0:
            print("Se apagó la lavadora")
            time.sleep(1)
        else:
            time.sleep_ms(50)

"""
def Dos():
    if client.check_msg() == b'1':
        Pin(32, Pin.OUT).on()
    elif client.check_msg() == b'0':
        Pin(32, Pin.OUT).off()
"""