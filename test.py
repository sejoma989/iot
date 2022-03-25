import time
import socket
import network
from machine import Pin

pin1 = Pin(25, Pin.OUT)

def vladdy(request):
    print("entro a vladdy")
    dirPuer = ('', 80)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(dirPuer)
    tcp_socket.listen(3)
    conn, addr = tcp_socket.accept()
    while True:
        #prev = pin1.value()
        #if prev != pin1.value():
            if request.find("led=on?") > 0:
                print("Encontro on")
                Pin(25, Pin.OUT).on()
                #pin1.on()
                time.sleep(2)
            elif request.find("led=off?"):
                Pin(25, Pin.OUT).off()
                pin1.off()
                #print("Encontro off")
                time.sleep(2)
    print("saliendo de vladdy")


#import time
#import socket
#import network
#
# from machine import Pin
#
# pin1 = Pin(33, Pin.OUT)
# pin2 = Pin(32, Pin.OUT)
#
# def Uno():
#     while True:
#         pin1.on()
#         time.sleep_ms(500)
#         pin1.off()
#         time.sleep_ms(500)
#
# _thread.start_new_thread(Uno, ())
#
# while True:
#     pin2.on()
#     time.sleep_ms(1500)
#     pin2.off()
#     time.sleep_ms(1500)

# from machine import Pin
#
# pin1 = Pin(33, Pin.OUT)
# pin2 = Pin(32, Pin.OUT)
#
# def Uno():
#     while True:
#         pin1.on()
#         time.sleep_ms(500)
#         pin1.off()
#         time.sleep_ms(500)
#
# _thread.start_new_thread(Uno, ())
#
# while True:
#     pin2.on()
#     time.sleep_ms(1500)
#     pin2.off()
#     time.sleep_ms(1500)

#import time
import socket
import network
# from machine import Pin
# import _thread
#
#
# pin1 = Pin(34, Pin.IN)
# pin2 = Pin(32, Pin.OUT)
#
# def Uno():
#     while True:
#         if pin1.value() == 1:
#             pin2.on()
#             print("pin 2 is on")
#         else: #pin1.value() == 0:
#             pin2.off()
#             print("pin 2 is off")
#
# _thread.start_new_thread(Uno, ())



