

import serial



class g_code_send:
    """docstring for g_code_send."""
    def __init__(self,g_code_file="not_given"):

        self.bit_rate=250000

        if g_code_file=="not_given":
            print("need g code to file to use ")
            exit()
        self.g_code_file=g_code_file




        import scaning_for_ports
        ports_to_use=scaning_for_ports.list_of_ports(bit_rate= self.bit_rate)
        ports_to_use=ports_to_use[0]
        print("using_port", ports_to_use,"\n")
        self.print_usb_port=ports_to_use



    def file_open_and_possing(self):
        self.g_code_commands=[]

        file=open(self.g_code_file)
        file_lines=file.readlines()
        file.close()

        for lines in file_lines:
            out=""
            for chars in lines:
                if chars==";":
                    break

                out=out+chars


            if not out=="":


                #SPLEIALC CHAR DONE COUNT AS ARRAY POSTIONS

                if out[-1]==" ":
                    out=out[0:-1]
                if not "\n" in out:
                     out=out+"\n"

                self.g_code_commands.append(out)



    def connect(self):

        try:
            connecton_objet=serial.Serial(self.print_usb_port,self.bit_rate,timeout=5)
        except:
            print("failed to connect to printer")
        while 1:
            line = connecton_objet.readline()

            x = line.decode("utf-8")



            print(x)
            print(type(x))




temp=g_code_send("bar teast.gcode")
temp.file_open_and_possing()
