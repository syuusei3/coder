N=int(input())

SP=[]
for i in range(N):
    SP.append(input().split())
    SP[i][1] = int(SP[i][1])
    print(SP[i][0])
    SP[i].append(i)
     #print(SP)

SP = sorted(SP, key=lambda x:(x[0],-x[1]))

for j in range(N):
    print(SP[j][2]+1)
