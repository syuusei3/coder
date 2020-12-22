N=int(input())
h=list(map(int,input().split()))

num=0
for i in range(N-1):
        tmp=h[i+1:]
        #print(min(tmp))
        if(h[i]>min(tmp)+1):
            num=1
            break


if(num==1):
    print("No")
else:
    print("Yes")
