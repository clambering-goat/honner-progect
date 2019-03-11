
import numpy as np
import pickle
import struct
import datetime
import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

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
        lengthbuf = self.recvall(4)
        length, = struct.unpack('!I', lengthbuf)
        return self.recvall( length)

    def recvall(self, count):
        buf = b''
        while count:
            newbuf = self.sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf





    def listenToClient(self, client, address):
        count =0
        print("connection from ", address)
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
                        np.save("G:/python_data/depth_carmea"+address+"_"+ str(count), depth)
                        np.save("G:/python_data/couler_carmea"+address+"_"+ str(count), couler)


                else:
                    raise Exception('Client disconnected/no data has been give in 60 sec')
            except:
                currentDT = datetime.datetime.now()
                currentDT=str(currentDT)
                print("closing thred "+address+" at ",currentDT)
                client.close()
                return()


    def input_control(self):
        while 1:
            print("current mode is ",self.mode)
            chose = input("pick a mode")
            if chose == "save":
                self.mode = "save"
            elif chose == "no save":
                self.mode = "no save"
            elif chose =="close connection":
                self.mode == "close"
            elif chose=="shutdown":
                self.main_loop=False
                self.mode == "close"

            else:
                print("not vaild chose")



if __name__ == "__main__":
    ip="192.168.1.156"
    port=50080
    print("starting server")
    print("ip ",ip)
    print("port ",port)
    ThreadedServer(ip,port).listen()