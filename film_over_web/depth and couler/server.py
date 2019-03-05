

import socket
import threading
import time
import numpy as np
import cv2
import pickle
import struct

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      if "nump_handel"==self.name:
        data_to_nump()
      if "get_input"==self.name:
          change_mode()
      print ("Exiting " + self.name)




mode="no_save"

def change_mode():
    while 1:
        global mode
        chose=input("pick a mode")
        if chose =="save":
            mode="save"
        elif chose =="no save":
            mode="no save"
        else:
            print("not vaild chose")

loack="off"
shared_data=[0,0]
def data_to_nump():
    global loack
    global shared_data
    global mode
    count_np = 0
    while 1:
        if loack == "on":
            count_np+=1
            depth=shared_data[0]

            couler=shared_data[1]


            depth_show=depth.astype(np.uint8)
            #print("data got ")
            cv2.imshow("depth",depth_show)
            cv2.imshow("couler", couler)

            if mode =="save":
                np.save("G:/python_data/depth"+str(count_np),depth)
                np.save("G:/python_data/couler"+str(count_np),couler)

            cv2.waitKey(200)
            #print("lock off")
            loack="off"

        #cv2.destroyAllWindows()



thread1 = myThread(1, "nump_handel", 1)
thread2 = myThread(1, "get_input", 1)

thread1.start()
thread2.start()
def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('!I', lengthbuf)
    return recvall(sock, length)

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf





ip="192.168.1.156"
port=50080      # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #print('Connected by', addr)
        while True:

            data=recv_one_message(conn)
            if loack == "off":
                data = pickle.loads(data)
                shared_data = data
                loack = "on"
            # data = b""
            # while True:
            #
            #     receiving_buffer = conn.recv(1024)
            #     data += receiving_buffer
            #     if not receiving_buffer: break
            #
            #     if b"end" in receiving_buffer:
            #         if loack=="off":
            #             print(" revecedf the data")
            #             try:
            #                 data = pickle.loads(data)
            #                 shared_data=data
            #                 loack = "on"
            #                 print("lock on")
            #             finally:
            #                 data = b""
            #                 break

