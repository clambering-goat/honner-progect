#!/usr/bin/python

import threading
import time
#import freenect
import numpy as np
import socket
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


def web_server():
    global exitFlag
    global lock
    global data_array


    while exitFlag==0:
        count=0
        data=""
        if lock=="data pushed":
            for x in data_array:

                for y in x :

                    count+=1
                    #print(count)
                    out=str(y)
                    data = data +out
                    data = data + " "
                data = data + "\n"
            sock.sendall(bytes(data, 'ascii'))
            sock.sendall(bytes("end of data ", 'ascii'))
            print("data sent ")
            lock = "data pulled"


def get_data():
    global exitFlag
    while exitFlag==0:
        global lock
        global data_array
        if lock =="data pulled":
            print("getting  data")
            #data_array,_ = freenect.sync_get_depth()
            data_array=np.load("./deepth_0_1.npy")
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
