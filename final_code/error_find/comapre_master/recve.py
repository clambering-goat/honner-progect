



import struct

import serial
import time
import argparse
import sys
import socket

class receve():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.client, address = self.sock.accept()
        print(self.client)
    def recv_one_message(self):
        lengthbuf = self.recvall(4)
        length, = struct.unpack('!I', lengthbuf)
        return self.recvall(length)

    def recvall(self, count):
        buf = b''
        while count:
            newbuf = self.client.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf


ip = "192.168.1.156"
port = 50050

temp=receve(ip,port)
file=open("time_layer_data","w")

while True:

    data=(temp.recv_one_message())
    data=data.decode()
    data=data+" "+str(time.time())
    file.write(data)