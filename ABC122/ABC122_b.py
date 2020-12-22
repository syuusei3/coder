b=input()
num=0
m=0

for i in b:
    if(i=="A"):
        num+=1
    elif(i=="T"):
        num+=1
    elif(i=="G"):
        num+=1
    elif(i=="C"):
        num+=1
    else:
        num=0

    m=max(m,num)


print(m)
