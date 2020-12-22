A=list(input())
B=[]
a=A[0]
cnt1=0
cnt2=0
for i in range(4):
    if(a==A[i]):
        cnt1+=1
    else:
        B.append(A[i])

if(cnt1==2):
    b=B[0]
    for i in range(2):
        if(b==B[i]):
            cnt2+=1
    if(cnt2==2):
        print("Yes")
    else:
        print("No")
else:
    print("No")
