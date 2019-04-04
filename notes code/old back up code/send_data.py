

import serial
with serial.Serial('COM10', 250000, timeout=5) as ser:


#ser = serial.Serial('/dev/ttyUSB0')  # open serial port
#print(ser.name)         # check which port was really used
    while 1:
        line =ser.readline()

        x=line.decode("utf-8")
        print(x)
        if "ok" in x:
            break
    ser.write(b'M105\n')    # write a string
    while 1:

        line =ser.readline()

        x=line.decode("utf-8")
        print(x)
    ser.close()
