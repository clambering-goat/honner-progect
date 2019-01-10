import serial





with serial.Serial('COM4', 250000, timeout=5) as ser:

    while 1:
        line =ser.readline()

        x=line.decode("utf-8")
        print(x)
        print(type(x))
