W,H,x,y=map(int,input().split())

S1=(H-y)*W
S2=y*W

S3=x*H
S4=(W-x)*H

m1=min(S1,S2)
m2=min(S3,S4)

if(m1==m2):
    #print(float(m1),end=' ')
    print('{:.6f}'.format(m1),end=' ')
    print(1)
else:
    M=max(m1,m2)
    #print(float(M),end=' ')
    print('{:.6f}'.format(M),end=' ')
    print(0)
