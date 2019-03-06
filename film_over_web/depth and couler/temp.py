

import socket
import pickle
ip="localhost"
port=50080      # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        while True:
            data = b""
            while True:
                receiving_buffer = conn.recv(1024)

                data+=receiving_buffer
                if not receiving_buffer:
                    break
                if b"end" in data:
                    print("end found ")


                    data=pickle.loads(data)
                    print(data[0])
                    print()
                    break
                    #print("types ",type(data))