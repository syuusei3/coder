N,K=(int(i) for i in input().split())
s=input()
S=list(s)

if(S[K-1]=='A'):
    S[K-1]='a'
elif(S[K-1]=='B'):
    S[K-1]='b'
elif(S[K-1]=='C'):
    S[K-1]='c'

A=''.join(S)
print(A)
