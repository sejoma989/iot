import time
import utime
from machine import Pin
import machine
from umqttsimple import MQTTClient
import ubinascii
import _thread
from EjemploWeb import creacion
from WifiEscaneo import escaneo
from test1 import Uno
from reset_btn import reset_btn

escaneo()
print("Escaneo finished running")
def connect_and_subscribe(broker, topic_sub):
    client = MQTTClient(ubinascii.hexlify(machine.unique_id()), broker)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Conectado a %s MQTT , suscrito al tópico %s' % (broker, topic_sub))
    return client

def publish_on(broker):
    cliente = MQTTClient(ubinascii.hexlify(machine.unique_id()), broker)
    cliente.connect()
    topico = "Topicool"
    while True:
        cliente.publish(topico, b'1')
        utime.sleep(5)

def publish_off(broker):
    cliente = MQTTClient(ubinascii.hexlify(machine.unique_id()), broker)
    cliente.connect()
    topico = "Topicool"
    while True:
        cliente.publish(topico, b'0')
        utime.sleep(5)

def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b'1':
        Pin(32, Pin.OUT).on()
    elif msg == b'0':
        Pin(32, Pin.OUT).off()

def restart_and_reconnect():
    print('Fallo de conexión al broker. Reconnecting...')
    utime.sleep(10)
    machine.reset()

print("after scan and after defining functions")
_thread.start_new_thread(creacion,())
print("Conexion establecida, suscribiendo a topico")

try:
    client = connect_and_subscribe("broker.hivemq.com","Topicool")
    print("Conectado y suscrito a Topicool")
except OSError as e:
    restart_and_reconnect()

#Suscribe
def checkTopic():
    while True:
        try:
            client.check_msg()

        except OSError as e:
            restart_and_reconnect()

#_thread.start_new_thread(checkTopic,())

_thread.start_new_thread(checkTopic,())
_thread.start_new_thread(reset_btn,())

#Publish
publ = Pin(34, Pin.IN)
#pin2 = Pin(32, Pin.OUT)
topic = "esp_lectures"
prev = publ.value()
print(prev)

while True:
    if prev != publ.value():
        if publ.value() == 1:
            client.publish(topic, b'1')
            print("se prendio la lavadora")
            prev = 1
            #if client.publish(topic, b'0'):
             #   client.publish(topic, b'0')
              #  print("se apago la lavadora")
               # prev = 0
        else:
            client.publish(topic, b'0')
            #print("se apago la lavadora")
            prev = 0
    time.sleep(1)