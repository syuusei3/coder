def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

N=int(input())
A=list(map(int,input().split()))

for i in A:
    L.append(gcd(L[-1],i))
for i in A[::-1]:
    R.append(gcd(R[-1],i))
max=0
for l,r in zip(L,reversed(R)):
    if(gcd(l,r)>max):
        max=gcd(l,r)
print(max)
