A,B,C=map(int,input().split())
A=A-B
C=C-A
if(C<0):
    print(0)
else:
    print(C)
    
