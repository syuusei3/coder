import math
N,K=map(int,input().split())
if((N-K)>=K):
    M=N-K
    m=K
else:
    M=K
    m=N-K

num=(math.factorial(M+2))/((math.factorial(m))*(math.factorial(M)))
print(int(num))
