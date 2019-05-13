import time


file_to_open=("./teast_5/time_layer_data")


file=open(file_to_open,"r")
data_in=file.readlines()
file.close()


# high_time_list=[]
# for w in data_in:
#     for q in w:
#
#         if "DONE" in q:
#             print("printer done ")
#             print("closing code")
#             exit()
#
#         if q == "Z":
#             # time_stamp = w.split("G")
#             # time_stamp = time_stamp[0]
#             # time_stamp = time_stamp[1:]
#             # time_stamp = time_stamp.split(".")
#             # time_stamp = int(time_stamp[0])
#             #
#             # layer_hight = w.split(" ")
#             # layer_hight = layer_hight[-1]
#             # layer_hight = layer_hight.strip()
#             # layer_hight = layer_hight[1:]
#             # layer_hight = float(layer_hight)
#             # high_time_list[layer_hight]=time_stamp
#
#             high_time_list.append(w)
#             break



file=open("time_layer_data","w")
file.close()

file = open("time_layer_data", "a+")
for data_out in data_in:
    file.write(data_out)
    print("data out",data_out)
    time.sleep(0.1)
file.close()
