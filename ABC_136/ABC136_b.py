N=input()
n=len(N)
n=int(n)
num=0
num1=1
num2=1
for i in range(n-1):
    if(i%2==0):
        if(i>1):
            for k in range(i):
                num1=num1*10
                num2=num1
        num1=1
        num+=9*num2

if(int(N)>9):
    if(n%2==1):
        num+=int(N)-num2*100+1
else:
    if(n%2==1):
        num+=int(N)%(num2*100)

print(num)
