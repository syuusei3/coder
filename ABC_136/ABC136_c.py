N=int(input())
h=list(map(int,input().split()))
num=0
for i in range(N-1):
    for k in range(i+1,N):
        #print(h[i],h[k])
        if(h[i]>h[k]+1):
            num=1
            break
if(num==1):
    print("No")
else:
    print("Yes")
