#from statistics import median
n=int(input())
p=list(map(int,input().split()))
cnt=0
p.sort()

if n%2==0:
    mid1=n/2
    mid2=n/2
    mid1=int(mid1-1)
    mid2=int(mid2)
    cnt=p[mid2]-p[mid1]
else:
    cnt=0

print(cnt)
