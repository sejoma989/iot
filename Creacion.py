


import socket
import network
import utime
import _thread

def creacion_func():
    #1. Validacion de si el archivo existe, sino, debe mandar a crearlo
    conn_creds = []
    try:
        print("intentando abrir archivo WifiConnect")
        with open('WiFiConnect.txt') as f:
            conn_creds = f.readlines()
    except:
        print("no hay archivo")
    print("Creando la red del ESP")


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
            """
            KeyValue = '?'
            if str(request).find(KeyValue) > 0:
                conectToWifi = open('WiFiConnect.txt', 'w')
                con_req = str(request).split('&')
                networkCom1 = con_req[0].split('?')
                networkCom2 = networkCom1[1].split('=')
                newNet = networkCom2[1]
                networkPass = con_req[1].split('=')
                networkPass1 = networkPass[1].split(' ')
                print('pass: ' + networkPass1[0])
                newPass = networkPass1[0]
                print(newNet)
                print(newPass)
                conectToWifi.write(newNet + '\n' + newPass)
                conectToWifi.close()

                conectToWifi = open('WiFiConnect.txt', 'r')
                mensaje = conectToWifi.read()
                print('este es el archivo guardado:\n' + mensaje)
                conectToWifi.close()
                """

            pagina = open("index_con.html", "r")
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(pagina.read())
            conn.close()
        except OSError:
            print("Error en servidor HTTP")




