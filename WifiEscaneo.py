import utime
import network
import time
from machine import Pin

pRE = Pin(33, Pin.OUT)

def escaneo():
    """
    conn_creds = []
    try:
        with open('WiFiConnect.txt') as f:
            conn_creds = f.readlines()
    except:
        print("no hay archivo")
    """
    intento = 0
    WiFi = network.WLAN(network.STA_IF)
    WiFi.active(True)
    utime.sleep(2)
    #WiFi.connect(conn_creds[0],conn_creds[1])
    WiFi.connect("EMMANUEL", "1nt3rnE7")
    while not WiFi.isconnected():
        print("titilante sin conexion")
        pRE.on()
        time.sleep_ms(50)
        pRE.off()
        time.sleep_ms(50)
        intento += 1
        utime.sleep(5)
        if intento > 3:
            break

    if intento <= 3:
        print("Conectado")
        print("prendiendo en conexion")
        pRE.on()

    # else:
    #     red = network.WLAN(network.AP_IF)
    #     red.active(True)
    #     red.config(essid="carenalgasTiO")
    #     red.config(authmode=2, password="caretio2345")
    #     print(red.ifconfig())