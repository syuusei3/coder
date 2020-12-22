L,R=map(int,input().split())
num=2018
for i in range(L,R):
    for k in range(i+1,R+1):
        #print(k*i)
        if(R<L//2019*2019*2):
            num=L*(L+1)%2019
        if(i*k%2019==0):
            num=0
            break
        num=min(num,i*k%2019)
    #print("##")
print(num)
