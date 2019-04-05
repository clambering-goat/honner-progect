
import numpy as np
import pickle
import struct
import datetime
import socket
import threading
import os
import cv2
import traceback

class ThreadedServer(object):
    def __init__(self, host, port,floder_name):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.floder_name=floder_name
        self.mode="no save"
        self.main_loop=True



    def listen(self):

        threading.Thread(target=self.input_control).start()

        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            if self.main_loop==False:
                break
            threading.Thread(target = self.listenToClient,args = (client,address)).start()


    def recv_one_message(self,sock):
        lengthbuf = self.recvall(4,sock)
        length, = struct.unpack('!I', lengthbuf)
        return self.recvall(length,sock)

    def recvall(self, count,client):
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




    def listenToClient(self, client, address):
        count =0

        print("connection from ", address)
        #set up portaion



        while True:
            try:
                if self.mode == "close":
                    raise Exception('user total server to stop')
                data = self.recv_one_message(client)
                if data !=None:
                    if self.mode=="save":
                        data = pickle.loads(data)
                        count+=1
                        depth = data[0]
                        couler = data[1]
                        np.save(self.floder_name+"/depth_carmea"+str(address)+"_"+ str(count), depth)
                        np.save(self.floder_name+"/couler_carmea"+str(address)+"_"+ str(count), couler)

                    if self.mode=="display":
                        data = pickle.loads(data)
                        count += 1
                        depth = data[0]
                        couler = data[1]

                        name="depth_carmea"+str(address)+"_"+ str(count)+".png"
                        depth = depth.astype(np.uint8)
                        cv2.imwrite(name, depth)

                        name="couler_carmea"+str(address)+"_"+ str(count)+".png"

                        cv2.imwrite(name, couler)

                else:
                    raise Exception('Client disconnected/no data has been give in 60 sec')
            except Exception as inst:
                print(traceback.format_exc())
                # print(type(inst))
                # print(type(inst.args))
                # print(inst)


                currentDT = datetime.datetime.now()
                currentDT=str(currentDT)
                print("closing thred "+str(address)+" at "+currentDT)
                client.close()
                return()


    def input_control(self):
        while 1:
            print("current mode is ",self.mode)
            chose = input("pick a mode \n")
            if chose == "save":
                self.mode = "save"
            elif chose == "no save":
                self.mode = "no save"
            elif chose=="shutdown":
                self.main_loop=False
            elif chose=="display":
                self.mode="display"


            else:
                print("not vaild chose for serveer modes")



if __name__ == "__main__":

    floader_name=input("select the anme of foulder ")
    #newpath = "G:/python_data/"+floader_name
    newpath="D:/scan_notes/"+floader_name
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    ip="192.168.1.156"
    port=50080
    print("starting server")
    print("ip ",ip)
    print("port ",port)
    ThreadedServer(ip,port,newpath).listen()