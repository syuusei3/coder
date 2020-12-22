A,B=map(int,input().split())
a=A
b=B
if(A>B):
    a=b
    b=A

num=a+b
if(num%2==0):
    k=num//2
    print(k)
else:
    print("IMPOSSIBLE")
