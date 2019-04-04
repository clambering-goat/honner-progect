#!/usr/bin/python
import freenect
import pickle
import numpy as np
import socket
import struct
exitFlag = 0








ip="192.168.1.118"
port=50080

sock = socket.socket()
sock.connect((ip,port))







data_array_depth=[]
data_array_couler=[]

lock =1
keep_running = True

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


def body(*args):
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

        send_one_message(sock,data_to_send)
        # sock.sendall(data_to_send)
        # sock.sendall(b"end")
        print("data sent ")
        lock = 1


    if not keep_running:
        raise freenect.Kill

print("in  loop ")


freenect.runloop(depth=get_data,video=get_data_couler,body=body)
print("out loop")
