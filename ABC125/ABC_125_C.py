#2つの値の最大公約数
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

N=int(input())
A=list(map(int,input().split()))

M=max(A)
num=A[0]
#print(M)
for i  in  range(N-1):
    num=gcd(num,A[i+1])
    if(num==1):
        break

print(num)
