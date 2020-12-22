import numpy as np
H,W=map(int,input().split())

A = []
for i in range(H):
    A.append([0 if i == "#" else 1 for i in list(input())])
A = np.array(A)

#print(A[0][0])
sum1=0
sum2=0

M=0


for i in range(H):
    for k in range(W):
        sum2+=A[i][k]
        if(A[i][k]==0):



        for t in range(H):
            sum1+=A[t][k]
            if(A[t][k]==0):
                M=sum1
