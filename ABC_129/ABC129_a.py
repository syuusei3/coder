p,q,r=map(int,input().split())

m1=p;
m1=min(m1,q)
m1=min(m1,r)
if(m1==p):
        m2=min(q,r)
elif(m1==q):
        m2=min(p,r)
else:
        m2=min(p,q)

print(m1+m2)
