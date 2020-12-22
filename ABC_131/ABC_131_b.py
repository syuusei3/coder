N,L=map(int,input().split())
sum=L
m=abs(L)
b=L
for i in range(1,N):
    a=L+i
    sum+=L+i
    if(abs(a)<=m):
        m=abs(a)
        b=a
print(sum-b)
