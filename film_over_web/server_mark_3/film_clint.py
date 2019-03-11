#!/usr/bin/python

import threading
import time
#import freenect
import pickle
import numpy as np
import socket
import struct
exitFlag = 0









class myThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print ("Starting " + self.name)

      if self.name =="web_server":
          web_server()
      if self.name =="get_data":
          get_data()

      print ("Exiting " + self.name)



ip="localhost"
port=50080
sock = socket.socket()

sock.connect((ip,port))


def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)




def web_server():
    global exitFlag
    global lock
    global data_array


    while exitFlag==0:

        if lock=="data pushed":

            #depth to string
            data_to_send=pickle.dumps(data_array)

            send_one_message(sock,data_to_send)
            # sock.sendall(data_to_send)
            # sock.sendall(b"end")
            print("data sent ")
            lock = "data pulled"


data_array=[0,0]
def get_data():
    global exitFlag
    while exitFlag==0:
        global lock
        global data_array
        if lock =="data pulled":
            print("getting  data")
            #data_array[0],_ = freenect.sync_get_depth()
            #data_array[1], _ = freenect.sync_get_video()
            data_array[0]=np.load("./deepth_0_1.npy")
            data_array[1]=np.load("./image_0_15001.npy")
            lock="data pushed"




threadList = ["web_server", "get_data"]
threads = []
threadID = 1
lock ="data pulled"
# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName)
   thread.start()
   threads.append(thread)
   threadID += 1


data=input(" press a key to close the programs ")
exitFlag = 1
for t in threads:
   t.join()
exit()



print ("Exiting Main Thread")
