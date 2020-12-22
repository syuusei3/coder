N,M=map(int,input().split())

max=100000
min=1
for i in range(M):
    a,b=map(int,input().split())
    if(max>=b):
        max=b
    if(a>min):
        min=a
if(num>=N):
    print(N)
    num=max-min+1
