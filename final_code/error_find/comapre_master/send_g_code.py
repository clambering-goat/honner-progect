
import struct

import serial
import time
import argparse
import sys
import socket


class motor_(object):
    def __init__(self, ip, networking_port, usb_port, file_name):
        self.ip = str(ip)
        self.network_port = int(networking_port)
        self.usb_port = usb_port
        self.file_name = file_name

    def make_network_connection(self):
        sock = socket.socket()
        print("ip",self.ip)
        #when ip give from self.ip code not work ??
        sock.connect(("192.168.1.156", self.network_port))
        return  sock


    def make_usb_connection(self):
        print('Opening Serial Port')
        self.ser_connertion = serial.Serial(self.usb_port, 250000)

        data = "\r\n\r\n"
        data = data.encode()
        self.ser_connertion.write(data)  # Hit enter a few times to wake the Printrbot
        time.sleep(2)  # Wait for Printrbot to initialize
        self.ser_connertion.flushInput()  # Flush startup text in serial input
        print("printer connection up ")

    def send_one_message(self,sock, data):
        length = len(data)
        sock.sendall(struct.pack('!I', length))
        sock.sendall(data)

    def send_g_code(self):

        def removeComment(string):
            if (string.find(';') == -1):
                return string
            else:
                return string[:string.index(';')]

        time_to_send_network_data = False
        print('Opening gcode file')
        f = open(self.file_name, 'r')


        # Stream g-code
        for line in f:
            l = removeComment(line)
            l = l.strip()  # Strip all EOL characters for streaming
            if (l.isspace() == False and len(l) > 0):

                if "M117 Printing..." == l and time_to_send_network_data == False:
                    sock=self.make_network_connection()
                    time_to_send_network_data = True

                print('Sending: ' + l)
                data = (l + '\n')
                data = data.encode()
                self.ser_connertion.write(data)  # Send g-code block

                if time_to_send_network_data == True:
                    print("sending data")
                    self.send_one_message(sock, data)

                while True:
                    grbl_out =  self.ser_connertion.readline()  # Wait for response with carriage return
                    grbl_out = grbl_out.decode()
                    print(' : ' + grbl_out.strip())
                    if "ok" in grbl_out:
                        break
        print("done")
        data="DONE"
        data=data.encode()
        self.send_one_message(sock, data)


if len(sys.argv) < 4:
    print("missing argument")
    print("need ")
    print("usb port ")
    print("file name ")
    print("ip ")
    print("netwokring port ")
    exit()

port_usb = sys.argv[1]
file_name = sys.argv[2]
ip = sys.argv[3]
port_network = sys.argv[4]
for q in sys.argv:
    print(q)
temp = motor_(ip, port_network, port_usb, file_name)

temp.make_usb_connection()
temp.send_g_code()
