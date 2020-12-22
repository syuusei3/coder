N=int(input())
dic=[]

for i in range(N):
    dic.append(input().split())
    dic[i][0] = int(dic[i][0])
    dic[i][1] = int(dic[i][1])
dic=sorted(dic, key=lambda x:(x[0],-x[1]))


min=N-1
cnt=0

for i in range(N-1):
    p=dic[i+1][0]-dic[i][0]
    q=dic[i+1][1]-dic[i][1]
    if p==0 and q==0:
        cnt=0
    else:
            for k in range(N-1):
                if(dic[k+1][0]-dic[k][0]==p)and(dic[k+1][1]-dic[k][1]==q):
                    cnt+=0
                else:
                    cnt+=1
    cnt=0

print(min+1)
