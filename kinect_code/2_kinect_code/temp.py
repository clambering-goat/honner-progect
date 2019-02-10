





def big_swap(v1,v2):
    if v2 < v1:
        temp=v1
        v1=v2
        v2=temp
    return(v1,v2)


v1,v2=big_swap(600,500)

for q in range (v1,v2):
    print(q)