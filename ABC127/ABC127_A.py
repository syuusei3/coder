A,B=map(int,input().split())
num=0
if A>=13:
    num=B
elif 6<=A<=12:
    num=B//2
else:
    num=0
print(num)
