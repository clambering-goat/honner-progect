




import serial
from serial.tools import list_ports






def list_of_ports(port_to_skip=[],timeout_given=3,bit_rate=115200):
    list_of_ports=list_ports.comports()

    list_of_usible_ports=[]

    for  current_port in list_of_ports:
        current_port=current_port[0]

        if current_port in port_to_skip:
            print("skipping port",data_flow)
            continue
            print("try to open port ",data_flow)

        try:

            print("opening port")
            port=serial.Serial(current_port, bit_rate, timeout=3)

            print("reading line")
            line =port.readline()

            print("decodeing")
            x=line.decode("utf-8")

            print("breacking conection")
            port.close()

            print("data")
            print(x)

            if len(x)<1:
                print("no data was given  on port ",current_port)
            elif len(x)>1:
                list_of_usible_ports.append(current_port)


        except Exception as inst:
            print("1 can't open port ",current_port)
            print ("2 ",type(inst))
            print ("3 ",inst.args)
            print ("4 ",inst)
            print()
    return(list_of_usible_ports)
