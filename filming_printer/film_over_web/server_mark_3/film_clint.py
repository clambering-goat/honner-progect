#!/usr/bin/python
import freenect
import pickle
import numpy as np
import socket
import struct
exitFlag = 0


def recv_one_message(self, sock):
    lengthbuf = self.recvall(4, sock)
    length, = struct.unpack('!I', lengthbuf)
    return self.recvall(length, sock)


def recvall(self, count, client):
    buf = b''
    while count:
        newbuf = client.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)


def get_data(dev, data, timestamp):


    global exitFlag
    global lock
    global data_array_depth

    if lock ==1:
        data_array_depth= data
        lock=2


def get_data_couler(dev, data, timestamp):
    global exitFlag


    global lock
    global data_array_couler

    if lock ==2:
        data_array_couler = data
        lock=3


def body(sock):
    global lock
    global exitFlag
    global lock
    global data_array_depth
    global data_array_couler



    global lock
    if lock==3:
        data_array = [data_array_depth, data_array_couler]

        #depth to string
        data_to_send=pickle.dumps(data_array)
        try:
            send_one_message(sock,data_to_send)
        except:
            print("lost conect to host shuting down ")
            raise freenect.Kill
        # sock.sendall(data_to_send)
        # sock.sendall(b"end")
        print("data sent ")
        lock = 1














data_array_depth=[]
data_array_couler=[]

lock =1



restset=False

def set_up():
    global restset

    if restset == True:
        print(" resting and try to reconnet to sever ")
        send_one_message("reconnting")

    ip = "192.168.1.156"
    port = 50080

    print("connecting to ")
    print("ip ",ip)
    print("host ",port)

    sock = socket.socket()
    sock.connect((ip, port))

    if restset==False:
        restset=True

    return(sock)


while 1:
    sock=set_up()
    freenect.runloop(depth=get_data,video=get_data_couler,body=body(sock))







