N=int(input())
l=list(map(int,input().split()))

S1=sum(l)
S2=0
diff=0
m=S1

for i in range(N-1):
    S1=S1-l[i]
    #print(S1)
    S2+=l[i]
    #print(S2)
    diff=abs(S1-S2)
    #print(diff)
    if(m>=diff):
        m=diff

print(m)
