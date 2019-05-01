



file=open("time_layer_data","r")

data=file.readlines()
file.close()


for w in data:
    for q in w:

        if q=="Z":

            time_stamp=w.split("G")
            time_stamp=time_stamp[0]
            time_stamp=time_stamp[1:]

            name=w.split(" ")
            name=name[-1]
            name=name.strip()

            print("name",name,"time_stamp",time_stamp)
            break