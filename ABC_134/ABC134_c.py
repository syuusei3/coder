N=int(input())
l=list()
for i in range(N):
    l.append(int(input()))
a=sorted(l)
m1=a[-1]
m2=a[-2]
for k in range(N):
    if(m1==l[k]):
        print(m2)
    else:
        print(m1)


"""
N=int(input())
l=list()
for i in range(N):
    l.append(int(input()))

num=list()
M=max(l)
for k in range(N):
    if(l[k]==M):
        num=l[:k]+l[k+1:]
        print(max(num))
    else:
        print(M)
"""

"""
for k in range(N):
    num=l[:k]+l[k+1:]
    print(max(num))
"""
"""
for k in range(N-1):
    print(l[:k]+l[k+1:])
"""
