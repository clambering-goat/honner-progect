

import socket
import threading
import time
import numpy as np
import cv2
import pickle
import struct



class ThreadedServer(object):
    def __init__(self, host, port):
        pass


    def listen(self):
        data=np.zeros((6000,600))


        teast_size=100
        for q in range(teast_size):
            threading.Thread(target = self.save,args=(data,q)).start()
            #threading.Thread(target = self.listenToClient,args = (client,address)).start()


        for q in range(teast_size):
            data=np.load("./data_dump/"+str(q)+".npy")
            for m in data:
                for n in m:
                    if n !=0:
                        print("error in ",q)

    def save(self,data,vaule):
        np.save("./data_dump/"+str(vaule),data)



ip="192.168.1.156"
port=50080
ThreadedServer(ip,port).listen()

