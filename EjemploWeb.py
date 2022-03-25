import socket
import network
from machine import Pin
import time
import _thread
from test import vladdy

def creacion():
    #1. Validacion de si el archivo existe, sino, debe mandar a crearlo
    creds = []
    try:
        with open('conWiFi.txt') as f:
            creds = f.readlines()
    except:
        print("no hay archivo")

    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid="red_dit")
    #ap_if.config(essid=creds[0])
    ap_if.config(authmode=2, password="123456789")
    #ap_if.config(authmode=2, password=creds[1])
    dirPuer = ('', 80)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(dirPuer)
    tcp_socket.listen(3)
    while True:
        try:
            conn, addr = tcp_socket.accept()
            print('Nueva conexion desde:  %s' % str(addr))
            request = (conn.recv(2096).decode("utf-8"))
            #print(request)
            if request.find("led=on?") > 0:
                Pin(25, Pin.OUT).on()
                print("Encontro on")
                time.sleep(1)
            elif request.find("led=off?"):
                Pin(25, Pin.OUT).off()
                time.sleep(1)

                 #print("Encontro off")
                #     print("no encontro nada")

            pagina = open("index.html", "r")
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(pagina.read())
            conn.close()
        except OSError:
            print("Error en servidor HTTP")
        """
        try:
            _thread.start_new_thread(vladdy(request), ())
            print("vladdy thread launched")
        except OSError:
            print("Error en hilo vladdy")
        """

    print("finished creacion")