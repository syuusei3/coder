N=int(input())
dic=[]

for i in range(N-1):
    dic.append(input().split())

c=[]
c=c.append(map(int,input().split()))

c=c.sort()
print(c)

#dup = [x for x in set(c) if c.count(x) > 1]
#print(dup)
"""
num=[]
for i in range(N-1):
    num[dic[i][0]]=c[i]
    num[dic[i][1]]=c[i+1]

print(num)
"""
