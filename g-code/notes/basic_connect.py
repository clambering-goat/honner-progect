import serial





with serial.Serial('COM4', 9600, timeout=5) as ser:

    line =ser.readline()

    x=line.decode("utf-8")
    print(x)
    print(type(x))
    print("sent"in x )
    print(x[0:-2]=="sent")
    #number= int(x[0])
    #print(number+5)
