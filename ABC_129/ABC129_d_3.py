import numpy as np
H,W=map(int,input().split())
A = []
for i in range(H):
    A.append([0 if i == "#" else 1 for i in list(input())])
A = np.array(A)

def left(k):
    for t in range(H):
        sum1+=A[t][k]
        if(A[t][k]==0):
            M1=sum1
def down(i):
    for j in range(W):
        sum2+=A[i][j]
        if(A[i][j]==0):
            M2=sum2
def up(i):
    
for i in range(H):
    for k in range(W):
        if(A[i][k]==1):
            left(k)
            down(i)

            A[i][k]=M1+M2
            sum1=0
            sum2=0
        else:
            A[i][k]=0
print(A.max())
