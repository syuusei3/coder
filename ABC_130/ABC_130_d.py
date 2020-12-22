N,K=map(int,input().split())
a=input().split()

cnt=0
sum=0
for i in range(N):
    sum=0
    for k in range(i,N):
        sum+=int(a[k])
        if(sum>=K):
            cnt+=1

print(cnt)
