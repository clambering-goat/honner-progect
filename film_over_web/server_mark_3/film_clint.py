#!/usr/bin/python
import freenect
import pickle
import numpy as np
import socket
import struct
exitFlag = 0











ip="192.168.1.156"
port=50080
sock = socket.socket(

sock.connect((ip,port))


def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)







data_array_depth=[]
data_array_couler=[]
def get_data(dev, data, timestamp):
    print("depth" )
    global exitFlag
    global lock
    global data_array_depth
    if lock ==1:
        print("getting data")
        data_array_depth= data
        print("got data")
        lock=2


def get_data_couler(dev, data, timestamp):
    global exitFlag
    print("coluer")

    global lock
    global data_array_couler
    if lock ==2:
        print("getting  data 2")
        data_array_couler = data
        print("got couler")
        lock=3





lock =1


keep_running = True

def body(*args):
    global lock

    global exitFlag
    global lock
    global data_array_depth
    global data_array_couler

    data_array=[data_array_depth,data_array_couler]

    global lock
    if lock==3:

        #depth to string
        data_to_send=pickle.dumps(data_array)

        send_one_message(sock,data_to_send)
        # sock.sendall(data_to_send)
        # sock.sendall(b"end")
        print("data sent ")
        lock = 1


    if not keep_running:
        raise freenect.Kill


print('Press ESC in window to stop')
freenect.runloop(depth=get_data,video=get_data_couler,body=body)


exitFlag = 1




print ("Exiting Main Thread")
