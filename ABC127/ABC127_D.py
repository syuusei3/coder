N,M=map(int,input().split())

A=list(map(int,input().split()))
A.sort()
#print(A)
cnt=0
for i in range(M):
    b,c=map(int,input().split())
    for t in range(M):
        if(A[t]<c):
            A[t]=c
            cnt+=1
        if(cnt==b):
            cnt=0
            break


num=sum(A)
print(num)
