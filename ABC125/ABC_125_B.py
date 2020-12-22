N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
num=0
for i in range(N):

    sum=V[i]-C[i]
    if sum>0:
        num+=sum


print(num)
