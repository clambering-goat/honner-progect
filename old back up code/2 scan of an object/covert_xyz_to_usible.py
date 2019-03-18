



file=open("63_final_weraid.xyz","r")
data=file.readlines()
file.close()

file_out=open("63_final_fix.xyz","w")


for q in data:
    q=q.split(" ")
    data_to_wite=q[0]+" "+q[1]+" "+q[2]+"\n"
    file_out.write(data_to_wite)

file_out.close()
