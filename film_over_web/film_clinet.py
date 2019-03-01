import socket

import threading
import numpy as np
import time
import cv2


# import freenect
#
# class kinect_data_get():
#     def __init__(self):
#         ints=freenect.init()
#
#         self.mdev = freenect.open_device(ints, 1)
#         freenect.set_depth_mode(self.mdev, freenect.RESOLUTION_MEDIUM, freenect.DEPTH_REGISTERED)
#         freenect.runloop(dev=self.mdev, depth=self.get_depth)
#     def get_depth(dev,depth,time_stamp):
#         array=depth
#         global lock
#
#         if lock=="data pulled":
#             data_array = array.astype(np.uint8)
#             lock = "data pushed"
#




class web_server():


    def __init__(self,ip,port,threadID):

        data=[]
        self.sock = socket.socket()
        try:
            self.sock.connect((ip,port))
        except:
            print("could not connect")
            exit()


        threading.Thread.__init__(self)
        self.threadID = threadID


    def run(self):
        print("Starting " + self.threadID)
        self.data_send()
        print("Exiting " + self.threadID)


    def data_send(self):
        while 1:
            global lock
            global data_array
            if lock=="data pushed":
                print("getting data")
                for x in data_array:
                    self.sock.send(bytes("new line", 'ascii'))
                    for y in x :
                        out=str(y)
                        self.sock.send(bytes(out, 'ascii'))
                        self.sock.send(bytes(" ", 'ascii'))
                lock = "data pulled"

    def close(self):
        self.sock.close()




class teast_main():
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("Starting " + self.threadID)
        self.load()
        print("Exiting " + self.threadID)
    def load(self):
        while 1:
            global lock
            global data_array
            if lock =="data pulled":
                print("getting  data")
                data_array=np.load("./deepth_0_1.npy")
                lock="data pushed"



data_array="data pushed",np.zeros((480,640))


thread1 = teast_main(2)
thread2 = web_server(ip="localhost",port=50008,threadID=2)


thread1.start()
thread2.start()

print("Exiting Main Thread")
